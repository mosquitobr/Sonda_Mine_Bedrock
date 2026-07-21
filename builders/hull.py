import config

def get_hull_width(rel_z):
    if rel_z > config.BOW_START_REL_Z:
        if rel_z >= config.BOW_END_REL_Z:
            return 0
        return int(round((config.SHIP_BEAM//2) * (config.BOW_END_REL_Z - rel_z) / (config.BOW_END_REL_Z - config.BOW_START_REL_Z)))
    elif rel_z < config.STERN_TAPER_START:
        if rel_z <= config.STERN_END:
            return config.STERN_TRANSOM_WIDTH
        return int(round(config.STERN_TRANSOM_WIDTH + (config.SHIP_BEAM//2 - config.STERN_TRANSOM_WIDTH) * (rel_z - config.STERN_END) / (config.STERN_TAPER_START - config.STERN_END)))
    else:
        return config.SHIP_BEAM // 2

def build_ocean_and_seabed(ox, oy, oz):
    cmds = []
    sb_y = oy + config.Y_SEABED - 1
    cl_y = oy + config.Y_SEABED - 2
    ds_y = oy + config.Y_SEABED - 4
    x1, x2 = ox - config.OCEAN_SIZE, ox + config.OCEAN_SIZE
    z1, z2 = oz - config.OCEAN_SIZE, oz + config.OCEAN_SIZE

    cmds.append(f"fill {x1} {ds_y} {z1} {x2} {ds_y} {z2} {config.BLOCK_DEEP_SEABED}")
    cmds.append(f"fill {x1} {cl_y} {z1} {x2} {cl_y} {z2} {config.BLOCK_CLAY}")
    cmds.append(f"fill {x1} {sb_y} {z1} {x2} {sb_y} {z2} {config.BLOCK_SEABED}")

    w_start = oy + config.Y_SEABED
    w_end = oy + config.Y_SEA_LEVEL
    chunk = 16
    for cx in range(x1, x2 + 1, chunk):
        cxe = min(cx + chunk - 1, x2)
        for cz in range(z1, z2 + 1, chunk):
            cze = min(cz + chunk - 1, z2)
            cmds.append(f"fill {cx} {w_start} {cz} {cxe} {w_end} {cze} {config.BLOCK_WATER}")
    return cmds

def build_hull(ox, oy, oz):
    cmds = []

    box_x1 = ox - (config.SHIP_BEAM // 2 + 3)
    box_x2 = ox + (config.SHIP_BEAM // 2 + 3)
    box_y1 = oy + config.Y_HULL_BOTTOM - 2
    box_y2 = oy + config.Y_DECK + 25
    box_z1 = oz - (config.SHIP_LENGTH // 2 + 5)
    box_z2 = oz + (config.SHIP_LENGTH // 2 + 5)

    chunk = 16
    for cx in range(box_x1, box_x2 + 1, chunk):
        cxe = min(cx + chunk - 1, box_x2)
        for cz in range(box_z1, box_z2 + 1, chunk):
            cze = min(cz + chunk - 1, box_z2)
            cmds.append(f"fill {cx} {box_y1} {cz} {cxe} {box_y2} {cze} {config.BLOCK_AIR}")

    z_min = oz - config.SHIP_LENGTH // 2
    z_max = oz + config.SHIP_LENGTH // 2
    h_bot = oy + config.Y_HULL_BOTTOM
    h_bilge = oy + config.Y_HULL_BILGE
    h_sea = oy + config.Y_SEA_LEVEL
    h_deck = oy + config.Y_DECK

    for z in range(z_min, z_max + 1):
        rel_z = z - oz
        w = get_hull_width(rel_z)
        if w == 0:
            continue
        x_min = ox - w
        x_max = ox + w
        cmds.append(f"fill {x_min} {h_bot} {z} {x_max} {h_sea} {z} {config.BLOCK_HULL_UNDERWATER}")
        cmds.append(f"fill {x_min} {h_sea + 1} {z} {x_max} {h_deck} {z} {config.BLOCK_HULL_ABOVEWATER}")

    for z in range(oz + config.BOW_START_REL_Z - 5, oz + config.BOW_START_REL_Z):
        rel_z = z - oz
        w_b = max(1, get_hull_width(rel_z) - 1)
        for y_off in range(0, 5):
            yb = h_bot + y_off
            cmds.append(f"fill {ox - w_b} {yb} {z} {ox + w_b} {yb} {z} {config.BLOCK_HULL_BULBOUS}")
        if rel_z >= config.BOW_START_REL_Z - 2:
            bt = max(1, w_b // 2)
            for y_off in range(1, 4):
                yb = h_bot + y_off
                cmds.append(f"fill {ox - bt} {yb} {z} {ox + bt} {yb} {z} {config.BLOCK_HULL_BULBOUS}")

    for z in range(z_min + 8, z_max - 8):
        rel_z = z - oz
        w = get_hull_width(rel_z)
        if w < 4:
            continue
        bk_off = w + 1
        cmds.append(f"fill {ox - bk_off} {h_bilge} {z} {ox - bk_off} {h_bilge} {z} {config.BLOCK_HULL_BILGE_KEEL}")
        cmds.append(f"fill {ox + bk_off} {h_bilge} {z} {ox + bk_off} {h_bilge} {z} {config.BLOCK_HULL_BILGE_KEEL}")

    for side in [-1, 1]:
        fx = ox + side * (config.SHIP_BEAM // 2 + 1)
        for dz in range(-4, 5):
            fz = oz + dz
            for dy in range(4):
                fy = h_bilge + dy
                cmds.append(f"setblock {fx} {fy} {fz} {config.BLOCK_HULL_STABILIZER}")
        ftx = ox + side * (config.SHIP_BEAM // 2 + 2)
        for dz in range(-3, 4):
            fz = oz + dz
            cmds.append(f"fill {ftx} {h_bilge} {fz} {ftx} {h_bilge + 2} {fz} {config.BLOCK_HULL_STABILIZER}")

    for z in range(z_min, z_max + 1):
        rel_z = z - oz
        w = get_hull_width(rel_z)
        if w == 0:
            continue
        x_min = ox - w
        x_max = ox + w
        cmds.append(f"fill {x_min} {h_deck} {z} {x_max} {h_deck} {z} {config.BLOCK_DECK}")

    for z in range(z_min, z_max + 1):
        rel_z = z - oz
        w = get_hull_width(rel_z)
        if w < 2:
            continue
        cmds.append(f"fill {ox - w} {h_deck + 1} {z} {ox - w} {h_deck + 1} {z} {config.BLOCK_HULL_ABOVEWATER}")
        cmds.append(f"fill {ox + w} {h_deck + 1} {z} {ox + w} {h_deck + 1} {z} {config.BLOCK_HULL_ABOVEWATER}")

    alley_z_start = oz + config.ACCOM_Z_START - 2
    alley_z_end = oz + config.ACCOM_Z_END + 2
    for z in range(alley_z_start, alley_z_end + 1):
        rel_z = z - oz
        w = get_hull_width(rel_z)
        if w < 4:
            continue
        for deck_x in [-1, 1]:
            ax = ox + deck_x * (w - 2)
            cmds.append(f"fill {ax} {h_deck} {z} {ax} {h_deck} {z} {config.BLOCK_DECK_PLATE}")

    for z in range(z_min + 1, z_max):
        rel_z = z - oz
        w = get_hull_width(rel_z)
        if w < 2:
            continue
        cmds.append(f"setblock {ox - w} {h_deck + 2} {z} {config.BLOCK_TRUSS}")
        cmds.append(f"setblock {ox + w} {h_deck + 2} {z} {config.BLOCK_TRUSS}")

    for z in range(z_min, z_max + 1):
        rel_z = z - oz
        w = get_hull_width(rel_z)
        if w < 2:
            continue
        cmds.append(f"setblock {ox - w} {h_deck} {z} {config.BLOCK_SAFETY_YELLOW}")
        cmds.append(f"setblock {ox + w} {h_deck} {z} {config.BLOCK_SAFETY_YELLOW}")
        if abs(rel_z) % 5 == 0 and w > 4:
            cmds.append(f"setblock {ox - w + 1} {h_deck} {z} {config.BLOCK_SAFETY_YELLOW}")
            cmds.append(f"setblock {ox + w - 1} {h_deck} {z} {config.BLOCK_SAFETY_YELLOW}")

    for z in range(z_min + 1, z_max - 1):
        rel_z = z - oz
        w = get_hull_width(rel_z)
        w_in = w - 2
        if w_in < 2:
            continue
        x_in_min = ox - w_in
        x_in_max = ox + w_in
        cmds.append(f"fill {x_in_min} {h_bot + 1} {z} {x_in_max} {h_deck - 1} {z} {config.BLOCK_AIR}")

    mp_x_min = ox + config.MOONPOOL_X_MIN
    mp_x_max = ox + config.MOONPOOL_X_MAX
    mp_z_min = oz + config.MOONPOOL_Z_MIN
    mp_z_max = oz + config.MOONPOOL_Z_MAX

    for layer in range(2):
        l = layer
        cmds.append(f"fill {mp_x_min - 1 - l} {h_bot} {mp_z_min - 1 - l} {mp_x_min - 1 - l} {h_deck} {mp_z_max + 1 + l} {config.BLOCK_STRUCTURE}")
        cmds.append(f"fill {mp_x_max + 1 + l} {h_bot} {mp_z_min - 1 - l} {mp_x_max + 1 + l} {h_deck} {mp_z_max + 1 + l} {config.BLOCK_STRUCTURE}")
        cmds.append(f"fill {mp_x_min - 1 - l} {h_bot} {mp_z_min - 1 - l} {mp_x_max + 1 + l} {h_bot} {mp_z_min - 1 - l} {config.BLOCK_STRUCTURE}")
        cmds.append(f"fill {mp_x_min - 1 - l} {h_bot} {mp_z_max + 1 + l} {mp_x_max + 1 + l} {h_bot} {mp_z_max + 1 + l} {config.BLOCK_STRUCTURE}")

    for y in range(h_bot, h_deck + 1, 3):
        cmds.append(f"fill {mp_x_min - 2} {y} {mp_z_min - 1} {mp_x_min - 2} {y} {mp_z_max + 1} {config.BLOCK_TRUSS}")
        cmds.append(f"fill {mp_x_max + 2} {y} {mp_z_min - 1} {mp_x_max + 2} {y} {mp_z_max + 1} {config.BLOCK_TRUSS}")
        cmds.append(f"fill {mp_x_min - 1} {y} {mp_z_min - 2} {mp_x_max + 1} {y} {mp_z_min - 2} {config.BLOCK_TRUSS}")
        cmds.append(f"fill {mp_x_min - 1} {y} {mp_z_max + 2} {mp_x_max + 1} {y} {mp_z_max + 2} {config.BLOCK_TRUSS}")

    for gz in range(mp_z_min - 1, mp_z_max + 2):
        cmds.append(f"setblock {mp_x_min - 2} {h_deck - 1} {gz} {config.BLOCK_DECK_GRATING}")
        cmds.append(f"setblock {mp_x_max + 2} {h_deck - 1} {gz} {config.BLOCK_DECK_GRATING}")
    for gx in range(mp_x_min - 1, mp_x_max + 2):
        cmds.append(f"setblock {gx} {h_deck - 1} {mp_z_min - 2} {config.BLOCK_DECK_GRATING}")
        cmds.append(f"setblock {gx} {h_deck - 1} {mp_z_max + 2} {config.BLOCK_DECK_GRATING}")
    for gz in range(mp_z_min - 1, mp_z_max + 2):
        cmds.append(f"setblock {mp_x_min - 2} {h_deck} {gz} {config.BLOCK_TRUSS}")
        cmds.append(f"setblock {mp_x_max + 2} {h_deck} {gz} {config.BLOCK_TRUSS}")

    cmds.append(f"fill {mp_x_min} {h_bot} {mp_z_min} {mp_x_max} {h_deck} {mp_z_max} {config.BLOCK_AIR}")
    cmds.append(f"fill {mp_x_min} {h_bot} {mp_z_min} {mp_x_max} {h_sea} {mp_z_max} {config.BLOCK_WATER}")

    for gx in [mp_x_min, mp_x_max]:
        for gz in [mp_z_min, mp_z_max]:
            cmds.append(f"setblock {gx} {h_deck} {gz} {config.BLOCK_GLOW}")

    cmds.append(f"fill {mp_x_min - 1} {h_deck} {mp_z_min - 1} {mp_x_max + 1} {h_deck} {mp_z_min - 1} {config.BLOCK_SAFETY_YELLOW}")
    cmds.append(f"fill {mp_x_min - 1} {h_deck} {mp_z_max + 1} {mp_x_max + 1} {h_deck} {mp_z_max + 1} {config.BLOCK_SAFETY_YELLOW}")
    cmds.append(f"fill {mp_x_min - 1} {h_deck} {mp_z_min} {mp_x_min - 1} {h_deck} {mp_z_max} {config.BLOCK_SAFETY_YELLOW}")
    cmds.append(f"fill {mp_x_max + 1} {h_deck} {mp_z_min} {mp_x_max + 1} {h_deck} {mp_z_max} {config.BLOCK_SAFETY_YELLOW}")

    stair_positions = [
        (ox - 4, oz - 10),
        (ox + 4, oz - 10),
        (ox - 4, oz + 10),
        (ox + 4, oz + 10),
    ]
    for sx, sz in stair_positions:
        cmds.append(f"fill {sx} {h_bot + 1} {sz} {sx} {h_deck} {sz} {config.BLOCK_AIR}")
        cmds.append(f"fill {sx - 1} {h_bot + 1} {sz - 1} {sx + 1} {h_bot + 1} {sz + 1} {config.BLOCK_STRUCTURE}")
        for ly in range(h_bot + 1, h_deck):
            cmds.append(f"setblock {sx} {ly} {sz} {config.BLOCK_LADDER} 3")
        cmds.append(f"setblock {sx} {h_deck} {sz} {config.BLOCK_DOOR_IRON}")
        cmds.append(f"fill {sx} {h_deck} {sz} {sx} {h_deck + 1} {sz} {config.BLOCK_DOOR_IRON}")

    for z_lit in range(z_min + 10, z_max - 10, 8):
        for side in [-1, 1]:
            lx = ox + side * (config.SHIP_BEAM // 2 - 1)
            cmds.append(f"setblock {lx} {h_deck + 2} {z_lit} {config.BLOCK_GLOW_LANTERN}")

    return cmds
