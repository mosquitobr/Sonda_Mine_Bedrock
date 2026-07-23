<div align="center">

# 📖 Manual de Comissionamento e Implementação Operacional
### Guia Didático de Instalação, Deploy e Operação do Navio-Sonda Classe Aq

[![Minecraft Bedrock Edition](https://img.shields.io/badge/Minecraft-Bedrock_Edition-green?style=for-the-badge&logo=minecraft)](https://www.minecraft.net)
[![License MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org)
[![Protocol WebSocket V2](https://img.shields.io/badge/Protocol-WebSocket_V2-purple?style=for-the-badge)](#)

---

**Repositório Oficial:** [https://github.com/mosquitobr/Sonda_Mine_Bedrock](https://github.com/mosquitobr/Sonda_Mine_Bedrock)

</div>

---

## 📥 1. Como Obter os Arquivos do Repositório (Passo a Passo Didático)

Se você é novo no GitHub ou não possui experiência técnica prévia, siga as etapas simples abaixo para obter todos os arquivos necessários em seu computador:

### Opção A: Download Direto via Arquivo ZIP (Recomendado para Leigos)
1. Acesse a página do repositório no seu navegador: [https://github.com/mosquitobr/Sonda_Mine_Bedrock](https://github.com/mosquitobr/Sonda_Mine_Bedrock).
2. Clique no botão verde rotulado **"Code"** (localizado no canto superior direito da lista de arquivos).
3. No menu suspenso que aparece, clique na opção **"Download ZIP"**.
4. Quando o download for concluído, abra a pasta de Downloads do seu computador, clique com o botão direito sobre o arquivo `Sonda_Mine_Bedrock-main.zip` e escolha **"Extrair Tudo..."**.
5. Abra a pasta extraída **`Sonda_Mine_Bedrock-main`**. O arquivo `main.py` e a pasta `assets/` estarão diretamente na raiz desta pasta.

### Opção B: Clonagem via Git Terminal (Para Desenvolvedores)
Se você já utiliza o Git instalado em seu sistema:
```powershell
git clone https://github.com/mosquitobr/Sonda_Mine_Bedrock.git
cd Sonda_Mine_Bedrock
```
*(Nota: Os arquivos do projeto estarão diretamente na raiz da pasta `Sonda_Mine_Bedrock`)*

---

## 🛠️ 2. Pré-Requisitos e Preparação do Ambiente

### 2.1 Verificar a Instalação do Python
O sistema necessita do Python (versão 3.10 ou superior) para executar o servidor WebSocket:
1. Abra o **Prompt de Comando** (cmd) ou **PowerShell** no seu Windows.
2. Digite o comando:
   ```powershell
   python --version
   ```
   *Se o Python estiver instalado, aparecerá algo como `Python 3.10.x` ou superior. Caso não tenha o Python, baixe a versão oficial gratuita na [Microsoft Store](https://apps.microsoft.com) ou em [python.org](https://www.python.org).*

3. Instale a biblioteca necessária (`websockets`) digitando no terminal (na pasta raiz onde se encontra o arquivo `requirements.txt`):
   ```powershell
   pip install -r requirements.txt
   ```

### 2.2 Configurar o Mundo no Minecraft Bedrock
Antes de importar e construir o navio, certifique-se das seguintes opções no seu mundo e perfil:
* **Permitir Trapaças (Allow Cheats):** Mantenha `ATIVADO` nas Opções do Mundo (necessário para que o script possa enviar comandos e blocos).
* **Modo de Jogo:** `Criativo` (recomendado para voar e explorar a embarcação).
* **Desativar WebSockets Criptografados:** No menu principal de Opções do Minecraft Bedrock, acesse **Opções > Geral > Perfil** (ou **Settings > Profile**) e certifique-se de que a opção **"Exigir WebSockets Criptografados"** (Require Encrypted WebSockets) esteja **DESATIVADA**. Como o servidor WebSocket Python local roda em `ws://` (sem criptografia TLS), o jogo impedirá a conexão silenciosamente se essa opção estiver ativa.

---

## 📦 3. Ativação do Pacote da Tripulação (sonda_bp.mcpack)

O arquivo `sonda_bp.mcpack` contém o pacote de comportamentos que adiciona a tripulação técnica (aldeões caracterizados com capacetes e coletes de proteção industrial EPI).

### Método do Duplo-Clique (Simples e Direto):
1. Abra a pasta `assets/` na raiz do projeto no seu Explorador de Arquivos do Windows.
2. Localize o arquivo **`sonda_bp.mcpack`**.
3. **Dê um DUPLO-CLIQUE diretamente sobre o arquivo `sonda_bp.mcpack`**.
4. O Windows iniciará automaticamente o **Minecraft Bedrock Edition** e exibirá no topo da tela do jogo a mensagem:
   `Importação de "Sonda Behavior Pack" iniciada com sucesso! / Importação concluída.`

### Ativar o Pacote nas Configurações do seu Mundo:
1. No menu principal do Minecraft Bedrock, clique em **Jogar** -> clique no ícone de **Lápis (Editar)** ao lado do seu mundo.
2. No menu lateral esquerdo, role até a seção **"Pacotes de Comportamento" (Behavior Packs)**.
3. Na aba **"Adquiridos" / "Disponíveis"**, clique sobre o pacote **"Sonda Behavior Pack"** e clique no botão **"Ativar"**.
4. Confirme a ativação quando o jogo solicitar.

---

## 📍 4. Configuração da Área de Carregamento (Tickingarea)

O Navio-Sonda Classe Aq é uma estrutura monumental de 140 blocos de comprimento e 55m de altura. Para impedir que partes do navio falhem devido ao descarregamento de chunks distantes no Minecraft:

### Como Aplicar o Comando no Chat In-Game:
Com o mundo aberto no Minecraft Bedrock, abra o chat (pressione a tecla `T` ou `Enter`) e execute:
```text
/tickingarea add -247 0 209 -187 128 391 sonda_area
```
*Este comando garante que toda a área da água e leito marinho onde o navio será montado permanecerá carregada na memória do jogo.*

---

## ⚙️ 5. Execução do Servidor e Deploy Automatizado

### 5.1 Iniciar o Servidor Python
No seu PowerShell / Prompt de Comando, posicionado na raiz da pasta do projeto (onde está o arquivo `main.py`), execute:
```powershell
python main.py
```
O servidor exibirá a mensagem:
`[SERVIDOR ATIVO] Servidor pronto. Aguardando conexão do Minecraft na porta 19131...`

### 5.2 Conectar no Minecraft e Iniciar a Montagem
1. Volte para a tela do **Minecraft Bedrock** no seu mundo.
2. Abra o chat in-game (tecla `T`) e digite o comando de conexão:
   ```text
   /connect localhost:19131
   ```
3. Pressione `Enter`. O script começará instantaneamente a enviar e construir as 8 fases da embarcação em tempo real!
4. Para se teleportar direto para o convés do navio:
   ```text
   /tp @s -217 75 300
   ```

---

## 🔄 6. Reconstrução Rápida (Rebuild)

Se você fizer modificações ou quiser restaurar o navio ao estado original sem fechar nada:
1. Abra o chat do Minecraft.
2. Digite apenas a palavra:
   ```text
   rebuild
   ```
3. O script reiniciará o ciclo de montagem procedural automaticamente!

---

## 🔍 7. Solução de Problemas (FAQ para Leigos)

* **Problema: Dobrei o clique no `sonda_bp.mcpack` mas o Minecraft não abriu.**
  * *Solução:* Certifique-se de que o Minecraft Bedrock Edition está instalado no Windows. Se necessário, abra o Minecraft primeiro, vá em Opções -> Armazenamento e importe o pacote.
* **Problema: Apareceu "Conexão Recusada" ao digitar `/connect localhost:19131`.**
  * *Solução:* Verifique se a janela do terminal com o `python main.py` ainda está aberta. Se a porta estiver presa, feche o terminal e abra novamente.
* **Problema: Os blocos pararam de aparecer na metade da construção.**
  * *Solução:* Lembre-se de rodar o comando de `/tickingarea` do Passo 4 para manter a área do oceano carregada.
