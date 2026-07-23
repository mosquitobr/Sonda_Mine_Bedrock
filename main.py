import asyncio
import json
import uuid
import time
import argparse
import websockets

import config
from builders.hull import build_ocean_and_seabed, build_hull
from builders.derrick import build_derrick
from builders.accommodation import build_accommodation
from builders.subsea import build_subsea
from builders.interior import build_interior
from builders.machinery import build_machinery
from builders.crew_spawner import build_crew


class BuildState:
    def __init__(self):
        self.completed_steps = set()
        self.total_commands = 0
        self.sent_commands = 0
        self.start_time = 0.0

    def reset(self):
        self.completed_steps.clear()
        self.total_commands = 0
        self.sent_commands = 0
        self.start_time = 0.0

    def checkpoint(self, step_name: str):
        self.completed_steps.add(step_name)

    def was_step_completed(self, step_name: str) -> bool:
        return step_name in self.completed_steps

    def progress_pct(self) -> float:
        if self.total_commands == 0:
            return 0.0
        return (self.sent_commands / self.total_commands) * 100.0


build_state = BuildState()


async def send_command(websocket, cmd: str):
    packet = {
        "header": {
            "version": 1,
            "requestId": str(uuid.uuid4()),
            "messagePurpose": "commandRequest",
            "messageType": "commandRequest"
        },
        "body": {
            "version": 1,
            "commandLine": cmd,
            "origin": {"type": "player"}
        }
    }
    await websocket.send(json.dumps(packet))
    await asyncio.sleep(config.COMMAND_DELAY)


def get_terminal_progress_bar(pct: float, length: int = 30) -> str:
    filled = int(round(pct / 100.0 * length))
    bar = "█" * filled + "░" * (length - filled)
    return f"[{bar}] {pct:5.1f}%"


def get_minecraft_progress_bar(pct: float, length: int = 10) -> str:
    filled = int(round(pct / 100.0 * length))
    bar = "■" * filled + "□" * (length - filled)
    return f"[{bar}] {pct:.0f}%"


async def send_batch(websocket, cmds, batch_name: str, batch_size: int = None):
    if batch_size is None:
        batch_size = config.BATCH_SIZE
    total = len(cmds)

    for i in range(0, total, batch_size):
        chunk = cmds[i:i + batch_size]
        for cmd in chunk:
            await send_command(websocket, cmd)
            build_state.sent_commands += 1

        pct = build_state.progress_pct()
        elapsed = time.time() - build_state.start_time
        bar = get_terminal_progress_bar(pct)
        print(f"\r  {bar} - {batch_name} - {build_state.sent_commands}/{build_state.total_commands} comandos (Tempo: {elapsed:.1f}s)", end="", flush=True)

    build_state.checkpoint(batch_name)
    
    # Envia barra de progresso do Minecraft ao final de cada etapa
    pct = build_state.progress_pct()
    mc_bar = get_minecraft_progress_bar(pct)
    try:
        await send_command(websocket, f'tellraw @a {{"rawtext":[{{"text":"§a{mc_bar} - Etapa \'{batch_name}\' concluída!"}}]}}')
    except Exception:
        pass


async def run_deployment(websocket, anchor_x: int, anchor_z: int, water_y: int):
    ox = anchor_x
    oz = anchor_z
    oy = water_y - 62  # Offset em relação ao nível de água padrão Y=62

    print(f"\n" + "═" * 60)
    print(f"🚀 INICIANDO DEPLOY DA SONDA DE PERFURAÇÃO CLASSE AQ")
    print(f"📍 Coordenadas de Ancoragem: X={ox}, Z={oz}, Nível da Água Y={water_y} (Offset OY={oy})")
    print(f"═" * 60)

    build_state.reset()
    build_state.start_time = time.time()

    # Gerando os conjuntos de comandos procedurais
    print("⏳ Gerando geometria procedural e calculando blocos...")
    step1 = build_ocean_and_seabed(ox, oy, oz)
    step2 = build_hull(ox, oy, oz)
    step3 = build_subsea(ox, oy, oz)
    step4 = build_derrick(ox, oy, oz)
    step5 = build_accommodation(ox, oy, oz)
    step6 = build_interior(ox, oy, oz)
    step7 = build_machinery(ox, oy, oz)
    step8 = build_crew(ox, oy, oz)

    all_steps = [
        ("1. Oceano & Leito Marinho", step1),
        ("2. Casco, Amuradas & Moonpool", step2),
        ("3. Subsea & BOP", step3),
        ("4. Torre de Perfuração (Derrick)", step4),
        ("5. Alojamento, Passadiço & Heliporto", step5),
        ("6. Praça de Máquinas & Interiores", step6),
        ("7. Guindastes, Pipe Racks & Bote", step7),
        ("8. Convocação da Tripulação & EPIs", step8),
    ]

    build_state.total_commands = sum(len(cmds) for _, cmds in all_steps)
    print(f"📊 Total de comandos computados: {build_state.total_commands}")
    print(f"  {get_terminal_progress_bar(0.0)} - Aguardando início...", end="", flush=True)

    # Notificar jogador in-game
    await send_command(websocket, f'tellraw @a {{"rawtext":[{{"text":"§a[Sonda-Deploy] Conexão WebSocket estabelecida! Iniciando montagem do Navio-Sonda..."}}]}}')

    # Execução sequencial de cada etapa
    for step_name, cmds in all_steps:
        await send_batch(websocket, cmds, step_name)

    elapsed_total = time.time() - build_state.start_time
    print(f"\n" + "═" * 60)
    print(f"🎉 COMISSIONAMENTO E DEPLOY CONCLUÍDOS EM {elapsed_total:.2f} SEGUNDOS!")
    print(f"⚓ Navio-Sonda ancorado nas coordenadas X={ox}, Z={oz}, Y={water_y}")
    print(f"═" * 60)

    # Teleportar e exibir mensagem de conclusão
    await send_command(websocket, f'tellraw @a {{"rawtext":[{{"text":"§6[Sonda-Deploy] Deploy concluído com sucesso! Navio-Sonda Classe Aq pronto para operação."}}]}}')
    await send_command(websocket, f'tp @s {ox} 75 {oz}')


async def handler(websocket):
    print(f"\n[CLIENTE CONECTADO] Minecraft Bedrock conectado com sucesso!")
    
    # Executar deploy principal
    await run_deployment(websocket, G_ARGS.anchor_x, G_ARGS.anchor_z, G_ARGS.water_y)

    # Notificar fechamento
    try:
        await send_command(websocket, 'tellraw @a {{"rawtext":[{{"text":"§e[Sonda-Deploy] Deploy finalizado. Encerrando servidor e liberando o terminal..."}}]}}')
    except Exception:
        pass

    # Aguardar um momento para garantir o envio das mensagens finais
    await asyncio.sleep(3)

    print("\n[ENCERRANDO] Conexão finalizada. Servidor desligado com sucesso.")
    exit_event.set()


async def main():
    parser = argparse.ArgumentParser(description="Servidor de Deploy da Sonda de Perfuração (Minecraft Bedrock)")
    parser.add_argument("--anchor-x", type=int, default=-217, help="Coordenada X de ancoragem (Padrão: -217)")
    parser.add_argument("--anchor-z", type=int, default=300, help="Coordenada Z de ancoragem (Padrão: 300)")
    parser.add_argument("--water-y", type=int, default=62, help="Cota do nível da água Y (Padrão: 62)")
    parser.add_argument("--port", type=int, default=config.PORT, help=f"Porta do servidor WebSocket (Padrão: {config.PORT})")
    
    global G_ARGS
    G_ARGS = parser.parse_args()

    print("=" * 70)
    print("      NAVIO-SONDA CLASSE AQ - SERVIDOR DE COMISSIONAMENTO")
    print("                      MINECRAFT BEDROCK EDITION")
    print("=" * 70)
    print(f"📡 Escutando na porta: {G_ARGS.port}")
    print(f"⚓ Parâmetros de Ancoragem -> X: {G_ARGS.anchor_x} | Z: {G_ARGS.anchor_z} | Nível d'água Y: {G_ARGS.water_y}")
    print(f"💡 No Minecraft Bedrock, execute o comando: /connect localhost:{G_ARGS.port}")
    print("=" * 70)

    global exit_event
    exit_event = asyncio.Event()

    async with websockets.serve(
        handler,
        config.HOST,
        G_ARGS.port,
        ping_interval=None,
        ping_timeout=None
    ):
        await exit_event.wait()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[ENCERRADO] Servidor WebSocket finalizado pelo usuário.")

