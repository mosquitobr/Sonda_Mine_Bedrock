<div align="center">

# 🚢 Navio-Sonda Classe Aq
### Comissionamento Público e Automação de Montagem Paramétrica no Minecraft Bedrock

[![Minecraft Bedrock Edition](https://img.shields.io/badge/Minecraft-Bedrock_Edition-green?style=for-the-badge&logo=minecraft)](https://www.minecraft.net)
[![License MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org)
[![Protocol WebSocket V2](https://img.shields.io/badge/Protocol-WebSocket_V2-purple?style=for-the-badge)](MANUAL.md)
[![Status Stable](https://img.shields.io/badge/Status-Comissionamento_Pronto-brightgreen?style=for-the-badge)](#)
[![Privacy Safe](https://img.shields.io/badge/Privacy-LGPD%2FGDPR_Compliant-success?style=for-the-badge)](#)

---

**Repositório Oficial no GitHub:** [https://github.com/mosquitobr/Sonda_Mine_Bedrock](https://github.com/mosquitobr/Sonda_Mine_Bedrock)  
**Status do Comissionamento:** Aprovado & Operacional

</div>

---

## 📋 Sumário
1. [Visão Geral](#-visão-geral)
2. [Especificações Técnicas da Embarcação](#-especificações-técnicas-da-embarcação)
3. [Requisitos de Sistema](#-requisitos-de-sistema)
4. [Início Rápido (Quick Start)](#-início-rápido-quick-start)
5. [As 8 Fases do Deploy Procedural](#-as-8-fases-do-deploy-procedural)
6. [Segurança e Proteção de Dados](#-segurança-e-proteção-de-dados)
7. [Licença](#-licença)

---

## 🌊 Visão Geral

Este repositório fornece a estrutura completa para o **comissionamento público e deploy automatizado** do **Navio-Sonda Classe Aq** e seu sistema submarino **BOP (Blowout Preventer)** diretamente em qualquer mundo do **Minecraft Bedrock Edition**.

Através de uma arquitetura em Python baseada em conexões **WebSocket**, o sistema efetua o cálculo tridimensional paramétrico de coordenadas e realiza a montagem procedural da estrutura, construindo o leito marinho, casco, moonpool, torre de perfuração de 55 metros, praça de máquinas, alojamentos e convocando 15 tripulantes caracterizados com EPIs de segurança industrial.

```text
       ┌──────────────────────────────────────────────────────────┐
       │                 HELICTOR / PASSADIÇO (Y=79)              │
       │                   ┌───────────────────────┐              │
       │  TORRE DERRICK    │   ALOJAMENTO (Y=71)   │   GUINDASTES │
       │     (55m Y=128)   └───────────┬───────────┘    & PIPE RACK│
  ~~~~~┼─────────■─────────────────────┼────────────────────■─────┼~~~~~ [Nível do Mar Y=62]
       │       MOONPOOL               CASCO                 |     │
       │       │    │               (Y=55 - 70)             |     │
       │       └─||─┘                                       |     │
       │         || RISER DE PERFURAÇÃO                      |     │
  ═════╧═════════||═════════════════════════════════════════╧═════╧═════ [Leito Marinho Y=12]
               ┌────┐
               │BOP │ STACK SUBMARINO
               └────┘
```

---

## 📐 Especificações Técnicas da Embarcação

| Parâmetro / Componente | Valor / Especificação | Descrição |
| :--- | :--- | :--- |
| **Comprimento Total (LOA)** | 140 blocos (eixo Z) | Dimensão longitudinal com proa bulbosa e popa cônica |
| **Boca Moldada (Beam)** | 25 blocos (eixo X) | Largura com amuradas e passarelas laterais |
| **Altura do Casco** | 15 blocos (Y=55 a Y=70) | Casco duplo com amuradas, estabilizadores e bilge keels |
| **Cota d'Água de Referência** | Y = 62 | Alinhamento hidrostático realista do mar |
| **Torre de Perfuração** | 55 metros (até Y=128) | Estrutura treliçada cônica com Top Drive, Drawworks e Monkey Board |
| **Moonpool** | Centralizado (X: -3 a 3, Z: -5 a 5) | Poço de lançamento submarino com paredes reforçadas e passarela |
| **Sistema Submarino (BOP)** | Assoalho marinho (Y=12) | BOP Stack, LMRP, válvulas de contingência, acumuladores e riser |
| **Alojamento & Ponte** | 3 Conveses + Heliporto | Cabines duplas, mess hall, hospital de bordo, passadiço com bridge wings |
| **Tripulação Comissionada** | 15 Integrantes | Aldeões com profissões dedicadas, estantes de armadura com EPIs coloridos |

---

## 💻 Requisitos de Sistema

* **Minecraft Bedrock Edition** (Windows 10/11, Consoles ou Mobile com suporte a comandos e WebSocket).
* **Python 3.10** ou superior instalado no sistema.
* Módulo Python `websockets` (`pip install -r requirements.txt`).
* Mundo do Minecraft com **Opções de Trapaça (Cheats)** ativadas.

---

## 🚀 Início Rápido (Quick Start)

### 1. Obter o Projeto
Baixe o arquivo ZIP do repositório no GitHub ou clone utilizando o Git:
```bash
git clone https://github.com/mosquitobr/Sonda_Mine_Bedrock.git
cd Sonda_Mine_Bedrock/comissionamento/main
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Iniciar o Servidor de Comissionamento
Execute o script informando as coordenadas de ancoragem desejadas (ou use o padrão):
```bash
python main.py --anchor-x -217 --anchor-z 300 --water-y 62
```

### 4. Conectar no Minecraft Bedrock
Abra o chat no Minecraft (com Cheats habilitados) e digite:
```text
/connect localhost:19131
```

---

## 🏗️ As 8 Fases do Deploy Procedural

1. **Ocean & Seabed (Y=12 a 62):** Limpeza tridimensional e assentamento do leito marinho em gravel/stone.
2. **Hull & Bulwarks (Y=55 a 70):** Construção do casco duplo, proa bulbosa, bilge keels, moonpool e amuradas.
3. **Subsea & BOP (Y=12 a 55):** Instalação do BOP submarino, LMRP, acumuladores e riser flutuante.
4. **Derrick & Drill Floor (Y=71 a 128):** Erguimento da torre treliçada, top drive, drawworks e dog house.
5. **Accommodation & Helipad (Y=71 a 85):** Superestrutura de 3 andares, cabines, hospital, passadiço e heliporto.
6. **Interior & Machinery (Y=56 a 69):** Praça de máquinas, geradores SCR, mud pumps, tanques de lama e shakers.
7. **Cargo & Equipment (Y=70):** Guindastes operacionais, pipe racks, baleeiras de emergência e guinchos.
8. **Crew & Safety:** Convocação de 15 tripulantes caracterizados com EPIs em conformidade industrial.

---

## 🛡️ Segurança e Proteção de Dados

Este projeto adota as melhores práticas de **Privacidade por Design (Privacy by Design)**:
- **Zero Dados Pessoais:** Nenhum caminho absoluto local, token, chave de API ou credencial está contido nos arquivos.
- **Operação Local:** Toda a comunicação ocorre via loopback seguro (`localhost` na porta TCP 19131).
- **Conformidade:** Totalmente aderente às diretrizes da LGPD (Lei Geral de Proteção de Dados) e GDPR.

---

## 📄 Licença

Este projeto é distribuído sob a **Licença MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

Copyright (c) 2026 **mosquitobr** ([GitHub](https://github.com/mosquitobr)).
