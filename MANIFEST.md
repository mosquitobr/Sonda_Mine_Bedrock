<div align="center">

# 📑 Manifesto de Arquivos e Integridade
### Inventário e Estrutura do Pacote de Comissionamento Público - Navio-Sonda Classe Aq

[![Minecraft Bedrock Edition](https://img.shields.io/badge/Minecraft-Bedrock_Edition-green?style=for-the-badge&logo=minecraft)](https://www.minecraft.net)
[![License MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Integrity Verified](https://img.shields.io/badge/Integrity-100%25_Verified-brightgreen?style=for-the-badge)](#)

---

**Repositório Oficial:** [https://github.com/mosquitobr/Sonda_Mine_Bedrock](https://github.com/mosquitobr/Sonda_Mine_Bedrock)  
**Versão do Manifesto:** `v2.0.0-commissioning` | **Data:** 2026-07-21

</div>

---

## 🌳 1. Árvore de Diretórios Explicativa

Abaixo está representada a estrutura de arquivos e pastas do pacote de comissionamento público:

```text
comissionamento/main/
├── 📄 README.md                 <-- Apresentação visual, especificações técnicas e início rápido
├── 📖 MANUAL.md                 <-- Manual didático para leigos, duplo-clique no mcpack e comandos
├── 📑 MANIFEST.md               <-- Manifesto de integridade, árvore de arquivos e regras de dados
├── ⚖️ LICENSE                   <-- Licença MIT oficial de código aberto
├── 📋 requirements.txt          <-- Dependências Python (websockets>=10.0)
├── ⚙️ config.py                 <-- Configuração geométrica, offsets e paleta de blocos do Bedrock
├── 🚀 main.py                   <-- Servidor WebSocket principal e orquestrador do deploy (8 fases)
├── 🧱 builders/                 <-- Módulos procedurais em Python
│   ├── 🛠️ hull.py               <-- Construtor do casco, proa bulbosa, moonpool e amuradas
│   ├── 🏗️ derrick.py            <-- Construtor da torre de perfuração 55m, top drive e dog house
│   ├── 🏥 accommodation.py      <-- Construtor do alojamento 3 andares, passadiço e heliporto
│   ├── ⚓ subsea.py             <-- Construtor do BOP submarino, LMRP, acumuladores e riser
│   ├── ⚙️ interior.py           <-- Construtor da praça de máquinas, geradores SCR e mud pumps
│   ├── 🏗️ machinery.py          <-- Construtor dos guindastes, pipe racks e baleeiras
│   └── 👷 crew_spawner.py       <-- Evocador dos 15 tripulantes com EPIs e armaduras coloridas
└── 📦 assets/                   <-- Arquivos de Suporte e Recursos do Minecraft Bedrock
    ├── 🎒 sonda_bp.mcpack       <-- Behavior Pack (duplo-clique para instalar no Minecraft)
    ├── 📐 meu_navio_final.json  <-- Estrutura geométrica de backup em formato JSON
    └── 🧩 test.mcstructure      <-- Estrutura de teste em formato NBT Bedrock
```

---

## 📋 2. Inventário Detalhado dos Arquivos da Release

Abaixo encontra-se a relação exata de todos os arquivos componentes do pacote de comissionamento:

| Caminho Relativo | Categoria / Função | Função Técnica | Status / Integridade |
| :--- | :--- | :--- | :--- |
| `README.md` | Documentação | Apresentação executiva, badges, especificação técnica e guia de início rápido. | Validado |
| `MANUAL.md` | Documentação | Guia didático de comissionamento, duplo-clique no mcpack, tickingarea e comandos. | Validado |
| `MANIFEST.md` | Documentação | Manifesto oficial de integridade, árvore de arquivos e conformidade LGPD. | Validado |
| `LICENSE` | Licenciamento | Texto integral da Licença MIT com copyright de mosquitobr. | Validado |
| `requirements.txt` | Dependências | Lista de dependências Python (`websockets>=10.0`). | Validado |
| `main.py` | Código-Fonte | Orquestrador principal do servidor WebSocket e gerenciador do fluxo em 8 etapas. | Validado |
| `config.py` | Configuração | Parâmetros geométricos do navio, cotas de altura e paleta de blocos do Bedrock. | Validado |
| `builders/hull.py` | Módulo Procedural | Construtor do casco, proa bulbosa, bilge keels, moonpool e amuradas. | Validado |
| `builders/derrick.py` | Módulo Procedural | Construtor da torre de perfuração de 55m, drill floor, top drive, drawworks e dog house. | Validado |
| `builders/accommodation.py` | Módulo Procedural | Construtor da superestrutura de 3 andares, cabines, hospital, passadiço e heliporto. | Validado |
| `builders/subsea.py` | Módulo Procedural | Construtor do BOP submarino, LMRP, acumuladores, riser e tensionadores. | Validado |
| `builders/interior.py` | Módulo Procedural | Construtor da praça de máquinas, geradores SCR, mud pumps, tanques e shakers. | Validado |
| `builders/machinery.py` | Módulo Procedural | Construtor dos guindastes pedestais, pipe racks, baleeiras e guinchos. | Validado |
| `builders/crew_spawner.py` | Módulo Procedural | Evocador dos 15 tripulantes caracterizados com profissões e armaduras/EPIs. | Validado |
| `assets/sonda_bp.mcpack` | Recurso Binário | Pacote de Comportamento (Behavior Pack) para Bedrock com comportamentos da tripulação. | Validado |
| `assets/meu_navio_final.json` | Estrutura JSON | Modelo de backup em JSON da geometria da estrutura do navio-sonda. | Validado |
| `assets/test.mcstructure` | Estrutura NBT | Estrutura auxiliar em formato `.mcstructure` para testes de importação direta. | Validado |

---

## 🛠️ 3. Detalhamento Funcional das Subpastas

### 3.1 Subpasta `builders/` (Módulos Procedurais de Engenharia)
Esta pasta agrupa todos os scripts Python responsáveis por calcular dinamicamente a geometria tridimensional do navio e traduzi-la em comandos de blocos do Minecraft Bedrock Edition:
- Cada construtor recebe offsets absolutos (`ox`, `oy`, `oz`) e aplica matemática paramétrica de interpolação (`lerp`) para formar superfícies orgânicas.

### 3.2 Subpasta `assets/` (Recursos e Modelos)
Contém os arquivos binários e estruturais necessários para o suporte in-game:
- `sonda_bp.mcpack`: Pacote oficial de comportamentos (Behavior Pack) importável no Minecraft Bedrock via duplo-clique.
- `meu_navio_final.json` / `test.mcstructure`: Arquivos de dados geométricos para restauração estática se necessário.

---

## 🛡️ 4. Declaração de Integridade & Proteção de Dados

### Conformidade com LGPD / GDPR
- **Sem Rastreamento:** Este software não coleta, armazena nem transmite dados pessoais ou telemétricos dos usuários.
- **Transparência Código-Aberto:** Todo o código-fonte está aberto para auditoria pública no GitHub.
- **Execução Desconectada:** O servidor WebSocket funciona em modo local (`localhost`), dispensando envio de dados para servidores externos.

---

## 📜 5. Histórico de Alterações do Pacote

- **v2.0.0-commissioning:** Lançamento público da release limpa do Navio-Sonda Classe Aq, com documentação didática, árvore visual no manifesto e scripts procedurais de alta precisão.
