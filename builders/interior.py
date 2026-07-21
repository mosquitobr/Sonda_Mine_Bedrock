import config

def build_interior(ox, oy, oz):
    cmds = []
    y_floor = oy + config.Y_INTERIOR_FLOOR
    y_ceil = oy + config.Y_INTERIOR_CEIL
    h_deck = oy + config.Y_DECK

    bh_z = [-53, -33, -22, -14, -5, 7, 15]
    for bz_rel in bh_z:
        bz = oz + bz_rel
        cmds.append(f"fill {ox - 10} {y_floor} {bz} {ox + 10} {y_ceil} {bz} {config.BLOCK_WALL_FIREPROOF}")
        cmds.append(f"fill {ox} {y_floor} {bz} {ox} {y_floor + 2} {bz} {config.BLOCK_AIR}")
        cmds.append(f"setblock {ox} {y_floor} {bz} {config.BLOCK_DOOR_IRON}")
        for side_x in [-8, 8]:
            cmds.append(f"fill {ox + side_x} {y_floor} {bz} {ox + side_x} {y_floor + 2} {bz} {config.BLOCK_AIR}")
            cmds.append(f"setblock {ox + side_x} {y_floor} {bz} {config.BLOCK_DOOR_IRON}")

    for z in range(oz - 65, oz + 16):
        cmds.append(f"setblock {ox} {y_floor} {z} {config.BLOCK_DECK_PLATE}")
    for z in range(oz - 65, oz + 16):
        cmds.append(f"fill {ox - 1} {y_floor} {z} {ox - 1} {y_ceil} {z} {config.BLOCK_WALL_CORRIDOR}")
        cmds.append(f"fill {ox + 1} {y_floor} {z} {ox + 1} {y_ceil} {z} {config.BLOCK_WALL_CORRIDOR}")
    for z in range(oz - 65, oz + 16, 4):
        cmds.append(f"setblock {ox} {y_ceil} {z} {config.BLOCK_GLOW_CEILING}")

    for z in range(oz - 65, oz + 16):
        cmds.append(f"setblock {ox - 6} {y_floor} {z} {config.BLOCK_DECK_PLATE}")
        cmds.append(f"setblock {ox + 6} {y_floor} {z} {config.BLOCK_DECK_PLATE}")
    for tz in [oz - 55, oz - 40, oz - 28, oz - 18, oz - 10, oz, oz + 10]:
        cmds.append(f"fill {ox - 6} {y_floor} {tz} {ox + 6} {y_floor} {tz} {config.BLOCK_DECK_PLATE}")

    pump_z = oz - 59
    cmds.append(f"fill {ox - 8} {y_floor} {oz - 63} {ox - 5} {y_floor + 2} {oz - 56} {config.BLOCK_STRUCTURE}")
    cmds.append(f"setblock {ox - 6} {y_floor + 2} {oz - 59} {config.BLOCK_PISTON}")
    cmds.append(f"fill {ox + 5} {y_floor} {oz - 63} {ox + 8} {y_floor + 2} {oz - 56} {config.BLOCK_STRUCTURE}")
    cmds.append(f"setblock {ox + 6} {y_floor + 2} {oz - 59} {config.BLOCK_PISTON}")

    cmds.append(f"setblock {ox} {y_floor} {oz - 61} {config.BLOCK_STRUCTURE}")
    cmds.append(f"setblock {ox} {y_floor + 1} {oz - 61} {config.BLOCK_HOPPER}")
    cmds.append(f"setblock {ox} {y_floor + 2} {oz - 61} {config.BLOCK_CAULDRON}")

    cmds.append(f"fill {ox - 4} {y_floor} {oz - 55} {ox + 4} {y_floor} {oz - 55} {config.BLOCK_SAFETY_YELLOW}")
    for x in range(ox - 3, ox + 4):
        cmds.append(f"setblock {x} {y_floor} {oz - 55} {config.BLOCK_CAULDRON}")

    for side_x in [-8, 8]:
        cmds.append(f"setblock {ox + side_x} {y_floor + 1} {oz - 54} {config.BLOCK_GLOW_RED}")
        cmds.append(f"setblock {ox + side_x} {y_floor + 1} {oz - 55} {config.BLOCK_BUTTON}")

    cmds.append(f"fill {ox - 10} {y_floor} {oz - 64} {ox - 9} {y_floor + 5} {oz - 54} {config.BLOCK_HULL_ABOVEWATER}")
    cmds.append(f"fill {ox + 9} {y_floor} {oz - 64} {ox + 10} {y_floor + 5} {oz - 54} {config.BLOCK_HULL_ABOVEWATER}")
    cmds.append(f"fill {ox - 10} {y_floor} {oz - 63} {ox - 10} {y_floor + 1} {oz - 62} {config.BLOCK_HOPPER}")
    cmds.append(f"fill {ox + 10} {y_floor} {oz - 63} {ox + 10} {y_floor + 1} {oz - 62} {config.BLOCK_HOPPER}")

    tank_configs = [
        (ox - 8, ox - 4, oz - 49, oz - 44),
        (ox + 4, ox + 8, oz - 49, oz - 44),
        (ox - 8, ox - 4, oz - 38, oz - 34),
        (ox + 4, ox + 8, oz - 38, oz - 34),
    ]
    for x1, x2, z1, z2 in tank_configs:
        cmds.append(f"fill {x1} {y_floor} {z1} {x2} {y_floor + 4} {z2} {config.BLOCK_GREEN}")
        for glass_x in [x1 - 1, x2 + 1]:
            cmds.append(f"fill {glass_x} {y_floor} {z1} {glass_x} {y_floor + 5} {z2} {config.BLOCK_GLASS_REINFORCED}")
        for glass_z in [z1 - 1, z2 + 1]:
            cmds.append(f"fill {x1} {y_floor} {glass_z} {x2} {y_floor + 5} {glass_z} {config.BLOCK_GLASS_REINFORCED}")

    for sx in [ox - 6, ox, ox + 6]:
        cmds.append(f"setblock {sx} {y_floor} {oz - 27} {config.BLOCK_STRUCTURE}")
        cmds.append(f"setblock {sx} {y_floor + 1} {oz - 27} {config.BLOCK_HOPPER}")
        cmds.append(f"setblock {sx} {y_floor + 2} {oz - 27} {config.BLOCK_TRUSS}")
        cmds.append(f"setblock {sx + (-1 if sx <= ox else 1)} {y_floor + 1} {oz - 27} {config.BLOCK_PISTON}")

    cmds.append(f"fill {ox - 2} {y_floor} {oz - 24} {ox + 2} {y_floor + 2} {oz - 24} {config.BLOCK_STRUCTURE}")
    cmds.append(f"setblock {ox} {y_floor + 1} {oz - 23} {config.BLOCK_HOPPER}")
    cmds.append(f"setblock {ox} {y_floor + 2} {oz - 24} {config.BLOCK_GLOW_RED}")

    cmds.append(f"fill {ox - 3} {y_floor} {oz - 31} {ox + 3} {y_floor + 1} {oz - 30} {config.BLOCK_STRUCTURE}")
    cmds.append(f"setblock {ox - 1} {y_floor + 1} {oz - 31} {config.BLOCK_DISPENSER}")
    cmds.append(f"setblock {ox + 1} {y_floor + 1} {oz - 31} {config.BLOCK_DROPPER}")
    cmds.append(f"setblock {ox} {y_floor + 2} {oz - 31} {config.BLOCK_TRUSS}")
    cmds.append(f"fill {ox - 1} {y_floor + 1} {oz - 30} {ox + 1} {y_floor + 1} {oz - 30} {config.BLOCK_HULL_ABOVEWATER}")

    scr_z = oz - 11
    for sx in [ox - 8, ox + 8]:
        cmds.append(f"fill {sx} {y_floor} {scr_z - 2} {sx} {y_floor + 4} {scr_z + 2} {config.BLOCK_STRUCTURE}")
        cmds.append(f"fill {sx} {y_floor} {scr_z - 1} {sx} {y_floor + 4} {scr_z + 1} {config.BLOCK_GLOW_RED}")
    cmds.append(f"fill {ox - 4} {y_floor} {scr_z - 1} {ox + 4} {y_floor + 3} {scr_z + 1} {config.BLOCK_BLACK}")

    gen_z = oz - 8
    for sx in [ox - 5, ox + 5]:
        cmds.append(f"fill {sx - 1} {y_floor} {gen_z - 2} {sx + 1} {y_floor + 3} {gen_z} {config.BLOCK_STRUCTURE}")
        cmds.append(f"fill {sx - 1} {y_floor + 1} {gen_z - 1} {sx + 1} {y_floor + 1} {gen_z - 1} {config.BLOCK_OBSERVER}")
    cmds.append(f"fill {ox - 3} {y_floor} {gen_z - 2} {ox + 3} {y_floor + 5} {gen_z - 2} {config.BLOCK_STRUCTURE}")
    cmds.append(f"fill {ox - 2} {y_floor + 1} {gen_z - 1} {ox + 2} {y_floor + 4} {gen_z - 1} {config.BLOCK_AIR}")

    cmds.append(f"fill {ox - 4} {y_ceil - 1} {oz - 65} {ox - 4} {y_ceil - 1} {oz + 15} {config.BLOCK_TRUSS}")
    cmds.append(f"fill {ox + 4} {y_ceil - 1} {oz - 65} {ox + 4} {y_ceil - 1} {oz + 15} {config.BLOCK_TRUSS}")
    for bz in [oz - 50, oz - 36, oz - 20, oz]:
        cmds.append(f"fill {ox - 9} {y_ceil - 1} {bz} {ox + 9} {y_ceil - 1} {bz} {config.BLOCK_TRUSS}")
    for dx, dz in [(-6, -59), (6, -59), (-6, -40), (6, -40)]:
        cmds.append(f"fill {ox + dx} {y_floor + 2} {oz + dz} {ox + dx} {y_ceil - 1} {oz + dz} {config.BLOCK_TRUSS}")

    cmds.append(f"fill {ox - 9} {y_ceil} {oz - 65} {ox - 9} {y_ceil} {oz + 15} {config.BLOCK_STRUCTURE}")
    cmds.append(f"fill {ox + 9} {y_ceil} {oz - 65} {ox + 9} {y_ceil} {oz + 15} {config.BLOCK_STRUCTURE}")
    for z in range(oz - 63, oz + 14, 5):
        cmds.append(f"setblock {ox - 4} {y_ceil} {z} {config.BLOCK_GLOW}")
        cmds.append(f"setblock {ox + 4} {y_ceil} {z} {config.BLOCK_GLOW}")

    for gz in range(oz - 65, oz + 3, 2):
        for gx in [ox - 7, ox + 7]:
            cmds.append(f"setblock {gx} {y_floor} {gz} {config.BLOCK_DECK_GRATING}")
    for gz in range(oz - 32, oz - 22, 2):
        for gx in range(ox - 7, ox + 8, 2):
            cmds.append(f"setblock {gx} {y_floor} {gz} {config.BLOCK_DECK_GRATING}")

    emergency_ladders = [
        (ox - 7, oz - 50),
        (ox + 7, oz - 50),
        (ox - 7, oz - 10),
        (ox + 7, oz - 10),
        (ox - 7, oz + 10),
        (ox + 7, oz + 10),
    ]
    for ex, ez in emergency_ladders:
        cmds.append(f"fill {ex} {y_floor} {ez} {ex} {h_deck - 1} {ez} {config.BLOCK_AIR}")
        for ly in range(y_floor, h_deck):
            cmds.append(f"setblock {ex} {ly} {ez} {config.BLOCK_LADDER} 3")
        cmds.append(f"setblock {ex} {h_deck} {ez} {config.BLOCK_DOOR_IRON}")
        cmds.append(f"fill {ex} {h_deck} {ez} {ex} {h_deck + 1} {ez} {config.BLOCK_DOOR_IRON}")

    for sz in [oz - 65, oz - 53, oz - 33, oz - 22, oz - 4, oz + 15]:
        cmds.append(f"fill {ox - 9} {y_floor} {sz} {ox + 9} {y_floor} {sz} {config.BLOCK_SAFETY_YELLOW}")
        cmds.append(f"fill {ox - 9} {y_floor + 1} {sz} {ox - 9} {y_ceil} {sz} {config.BLOCK_SAFETY_YELLOW}")
        cmds.append(f"fill {ox + 9} {y_floor + 1} {sz} {ox + 9} {y_ceil} {sz} {config.BLOCK_SAFETY_YELLOW}")

    for ez in range(oz - 62, oz + 13, 6):
        cmds.append(f"setblock {ox - 1} {y_floor + 1} {ez} {config.BLOCK_FIRE_EXTINGUISHER}")
        cmds.append(f"setblock {ox + 1} {y_floor + 1} {ez} {config.BLOCK_FIRE_EXTINGUISHER}")

    return cmds
