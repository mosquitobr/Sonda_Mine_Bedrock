import config

COLOR_HARD_HAT    = 16776960  # amarelo
COLOR_SAFETY_VEST = 16753920  # laranja
COLOR_COVERALL    = 256       # azul marinho
COLOR_WHITE       = 16777215  # branco
COLOR_KHAKI       = 15127540  # caqui
COLOR_DARK_BLUE   = 170       # azul escuro
COLOR_RED         = 16711680  # vermelho

CREW_MEMBERS = [
    ("Mestre de Obra - Carlos",     "toolsmith",  "EPI", -4, 70, 26,   COLOR_HARD_HAT, COLOR_SAFETY_VEST),
    ("Operador de Guincho - Pedro", "armorer",    "EPI", -9, 70, 22,   COLOR_HARD_HAT, COLOR_SAFETY_VEST),
    ("Operador de Guincho - João",  "armorer",    "EPI",  9, 70, 22,   COLOR_HARD_HAT, COLOR_SAFETY_VEST),
    ("Operador de Guincho - Luiz",  "armorer",    "EPI", -9, 70, -38,  COLOR_HARD_HAT, COLOR_SAFETY_VEST),
    ("Operador de Guincho - Mário", "armorer",    "EPI",  9, 70, -38,  COLOR_HARD_HAT, COLOR_SAFETY_VEST),
    ("Roustabout - Antonio",        "weaponsmith","EPI", -6, 70, 18,   COLOR_HARD_HAT, COLOR_SAFETY_VEST),
    ("Roustabout - Francisco",      "weaponsmith","EPI",  6, 70, 18,   COLOR_HARD_HAT, COLOR_SAFETY_VEST),
    ("Marinheiro - Raimundo",       "fisherman",  "EPI",  5, 70, -50,  COLOR_HARD_HAT, COLOR_SAFETY_VEST),
    ("Bombeiro - Heliporto",        "shepherd",   "EPI",  0, 78, 68,   COLOR_RED,       COLOR_SAFETY_VEST),
    ("Técnico BOP - Cláudio",       "mason",      "EPI",  6, 70, -44,  COLOR_HARD_HAT, COLOR_SAFETY_VEST),

    ("Perfurador - Ricardo",        "cleric",     "UNIF", -7, 73, -8,   COLOR_DARK_BLUE, COLOR_DARK_BLUE),
    ("Aux. Perfurador - Paulo",     "cleric",     "UNIF",  3, 73,  4,   COLOR_DARK_BLUE, COLOR_DARK_BLUE),
    ("Eng. Lama - Roberto",         "butcher",    "UNIF",  0, 56, -55,  COLOR_WHITE,     COLOR_KHAKI),
    ("Eletricista - Sérgio",        "librarian",  "UNIF", -8, 56, -11,  COLOR_DARK_BLUE, COLOR_DARK_BLUE),
    ("Comandante - Almir",          "nitwit",     "UNIF",  0, 79, 48,   COLOR_WHITE,     COLOR_WHITE),
]

PADRAO_ARMADURA = {
    "EPI":  {"helmet": "leather_helmet", "chest": "leather_chestplate", "legs": "leather_leggings", "boots": "leather_boots"},
    "UNIF": {"helmet": "leather_helmet", "chest": "leather_chestplate", "legs": "leather_leggings", "boots": "leather_boots"},
}

def cor_component(cor_decimal: int) -> str:
    return f'[{{"color":{cor_decimal}}}]'

def spawn_crew_commands(cmds, ox, oy, oz):
    for nome, profissao, tipo, x, y, z, cor_cap, cor_vest in CREW_MEMBERS:
        ax = ox + x
        ay = oy + y
        az = oz + z

        cmds.append(f'summon villager "{nome}" {ax} {ay} {az}')
        cmds.append(f'event entity @e[type=villager,name="{nome}",c=1] minecraft:become_{profissao}')

        stand_x = ax + 1.5
        stand_z = az + 0.5
        cmds.append(f'summon armor_stand "{nome}" {stand_x} {ay} {stand_z}')
        selector = f'@e[type=armor_stand,name="{nome}",c=1]'

        armadura = PADRAO_ARMADURA[tipo]
        cor_helmet = cor_cap if tipo == "EPI" else cor_cap
        cor_chest  = cor_vest if tipo == "EPI" else cor_vest
        cor_legs   = int(cor_vest * 0.7)
        cor_boots  = cor_vest

        cmds.append(f'replaceitem entity {selector} slot.armor.head 0 {armadura["helmet"]} 1 {cor_component(cor_helmet)}')
        cmds.append(f'replaceitem entity {selector} slot.armor.chest 0 {armadura["chest"]} 1 {cor_component(cor_chest)}')
        cmds.append(f'replaceitem entity {selector} slot.armor.legs 0 {armadura["legs"]} 1 {cor_component(cor_legs)}')
        cmds.append(f'replaceitem entity {selector} slot.armor.feet 0 {armadura["boots"]} 1 {cor_component(cor_boots)}')

        if tipo == "EPI":
            cmds.append(f'setblock {ax + 1} {ay} {az} {config.BLOCK_SAFETY_YELLOW}')
            cmds.append(f'setblock {ax + 1} {ay + 1} {az} {config.BLOCK_GLOW_RED}')

def build_crew(ox=0, oy=0, oz=0):
    cmds = []
    spawn_crew_commands(cmds, ox, oy, oz)
    return cmds
