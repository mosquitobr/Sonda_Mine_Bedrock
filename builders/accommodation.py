import config
from builders.hull import get_hull_width

def build_accommodation(ox, oy, oz):
    cmds = []
    y_start = oy + config.Y_DECK + 1
    h_deck = oy + config.Y_DECK

    for y in range(y_start, y_start + config.ACCOM_HEIGHT):
        rel_y = y - y_start
        is_floor = rel_y % config.ACCOM_DECK_INTERVAL == 0 or rel_y == config.ACCOM_HEIGHT - 1

        for z in range(oz + config.ACCOM_Z_START, oz + config.ACCOM_Z_END + 1):
            rel_z = z - oz
            w = max(0, get_hull_width(rel_z) - 1)
            if w <= 0:
                continue
            x_min = ox - w
            x_max = ox + w

            if is_floor:
                cmds.append(f"fill {x_min} {y} {z} {x_max} {y} {z} {config.BLOCK_STRUCTURE}")
            else:
                cmds.append(f"setblock {x_min} {y} {z} {config.BLOCK_WALL_OUTER}")
                cmds.append(f"setblock {x_max} {y} {z} {config.BLOCK_WALL_OUTER}")
                if w > 1:
                    cmds.append(f"fill {x_min + 1} {y} {z} {x_max - 1} {y} {z} {config.BLOCK_AIR}")
                if z in [oz + config.ACCOM_Z_START, oz + config.ACCOM_Z_END]:
                    is_bridge = rel_y >= 8
                    if is_bridge and z == oz + config.ACCOM_Z_END:
                        cmds.append(f"fill {x_min} {y} {z} {x_max} {y} {z} {config.BLOCK_GLASS}")
                    else:
                        cmds.append(f"fill {x_min} {y} {z} {x_max} {y} {z} {config.BLOCK_WALL_OUTER}")

        if not is_floor and rel_y < 8:
            for z in range(oz + 28, oz + 48, 4):
                rel_z = z - oz
                w = get_hull_width(rel_z) - 1
                if w > 1:
                    cmds.append(f"setblock {ox - w} {y} {z} {config.BLOCK_GLASS_PANE}")
                    cmds.append(f"setblock {ox + w} {y} {z} {config.BLOCK_GLASS_PANE}")

    corr_z_start = oz + config.ACCOM_Z_START + 2
    corr_z_end = oz + config.ACCOM_Z_END - 1

    for deck_idx in range(3):
        deck_y_base = y_start + deck_idx * config.ACCOM_DECK_INTERVAL
        for z in range(corr_z_start, corr_z_end + 1):
            for cx in range(-1, 2):
                cmds.append(f"setblock {ox + cx} {deck_y_base} {z} {config.BLOCK_WALL_CORRIDOR}")
            cmds.append(f"fill {ox - 2} {deck_y_base} {z} {ox - 2} {deck_y_base + 2} {z} {config.BLOCK_WALL_CORRIDOR}")
            cmds.append(f"fill {ox + 2} {deck_y_base} {z} {ox + 2} {deck_y_base + 2} {z} {config.BLOCK_WALL_CORRIDOR}")
        for z in range(corr_z_start, corr_z_end + 1, 4):
            cmds.append(f"setblock {ox} {deck_y_base + 3} {z} {config.BLOCK_GLOW_CEILING}")

    stair_x, stair_z = ox, oz + 37
    for deck_idx in range(2):
        lower_y = y_start + deck_idx * config.ACCOM_DECK_INTERVAL + 1
        upper_y = lower_y + config.ACCOM_DECK_INTERVAL - 1
        cmds.append(f"fill {stair_x} {lower_y} {stair_z} {stair_x} {upper_y} {stair_z} {config.BLOCK_AIR}")
        for ly in range(lower_y, upper_y + 1):
            cmds.append(f"setblock {stair_x} {ly} {stair_z} {config.BLOCK_LADDER} 3")
        cmds.append(f"fill {stair_x - 1} {lower_y - 1} {stair_z - 1} {stair_x + 1} {lower_y - 1} {stair_z + 1} {config.BLOCK_AIR}")
        cmds.append(f"setblock {stair_x} {lower_y - 1} {stair_z} {config.BLOCK_DOOR_IRON}")
        cmds.append(f"fill {stair_x} {lower_y - 1} {stair_z} {stair_x} {lower_y} {stair_z} {config.BLOCK_DOOR_IRON}")

    for side_x in [-1, 1]:
        cmds.append(f"setblock {ox + side_x} {y_start} {oz + 24} {config.BLOCK_DOOR_IRON}")
        cmds.append(f"fill {ox + side_x} {y_start} {oz + 24} {ox + side_x} {y_start + 1} {oz + 24} {config.BLOCK_DOOR_IRON}")
        cmds.append(f"setblock {ox + side_x * 2} {y_start + 1} {oz + 24} {config.BLOCK_BUTTON}")
    cmds.append(f"fill {ox - 1} {y_start} {oz + 25} {ox + 1} {y_start + 2} {oz + 25} {config.BLOCK_AIR}")

    w_35 = get_hull_width(35) - 1
    for side, mult in [(-1, -1), (1, 1)]:
        col_x = ox + side * (w_35 + 1)
        cmds.append(f"fill {col_x} {h_deck} {oz + 35} {col_x} {y_start + 11} {oz + 35} {config.BLOCK_STRUCTURE}")
        for y in range(h_deck, y_start + 11):
            cmds.append(f"setblock {col_x} {y} {oz + 36} {config.BLOCK_LADDER} 2")
        for plat_y in range(h_deck + 4, y_start + 11, 4):
            cmds.append(f"setblock {col_x} {plat_y} {oz + 34} {config.BLOCK_DECK_PLATE}")
            cmds.append(f"setblock {col_x} {plat_y + 1} {oz + 34} {config.BLOCK_TRUSS}")
            door_z = oz + 34
            cmds.append(f"fill {ox - w_35} {plat_y} {door_z} {ox - w_35} {plat_y + 1} {door_z} {config.BLOCK_AIR}")
            cmds.append(f"setblock {ox - w_35} {plat_y} {door_z} {config.BLOCK_DOOR_IRON}")
            cmds.append(f"setblock {ox - w_35} {plat_y + 1} {door_z} {config.BLOCK_DOOR_IRON}")
            cmds.append(f"fill {ox + w_35} {plat_y} {door_z} {ox + w_35} {plat_y + 1} {door_z} {config.BLOCK_AIR}")
            cmds.append(f"setblock {ox + w_35} {plat_y} {door_z} {config.BLOCK_DOOR_IRON}")
            cmds.append(f"setblock {ox + w_35} {plat_y + 1} {door_z} {config.BLOCK_DOOR_IRON}")

    d1_y = y_start
    cabins = [
        (-5, 29, 2),
        (5, 29, 2),
        (-5, 42, 2),
        (5, 42, 2),
        (-7, 29, 1),
        (7, 29, 1),
        (-7, 42, 1),
        (7, 42, 1),
    ]
    for door_x, door_z, size in cabins:
        wall_x = -2 if door_x < 0 else 2
        cmds.append(f"fill {ox + wall_x} {d1_y} {oz + door_z} {ox + wall_x} {d1_y + 1} {oz + door_z} {config.BLOCK_AIR}")
        cmds.append(f"setblock {ox + wall_x} {d1_y} {oz + door_z} {config.BLOCK_DOOR_WOOD}")
        bed_x = door_x + (-1 if door_x > 0 else 1)
        cmds.append(f"setblock {ox + bed_x} {d1_y} {oz + door_z - 1} {config.BLOCK_WOOL_RED}")
        cmds.append(f"setblock {ox + bed_x} {d1_y} {oz + door_z} {config.BLOCK_WOOL_WHITE}")
        cmds.append(f"setblock {ox + door_x} {d1_y} {oz + door_z + 1} {config.BLOCK_CHEST}")

    d2_y = y_start + 4
    for tz in [30, 36]:
        cmds.append(f"setblock {ox - 4} {d2_y} {oz + tz} {config.BLOCK_FENCE}")
        cmds.append(f"setblock {ox - 4} {d2_y + 1} {oz + tz} {config.BLOCK_PRESSURE_PLATE}")
        cmds.append(f"setblock {ox - 4} {d2_y} {oz + tz - 1} {config.BLOCK_STAIRS} 2")
        cmds.append(f"setblock {ox - 4} {d2_y} {oz + tz + 1} {config.BLOCK_STAIRS} 3")

    cmds.append(f"fill {ox + 3} {d2_y} {oz + 30} {ox + 5} {d2_y} {oz + 30} {config.BLOCK_HULL_ABOVEWATER}")
    cmds.append(f"setblock {ox + 3} {d2_y} {oz + 31} {config.BLOCK_FURNACE}")
    cmds.append(f"setblock {ox + 4} {d2_y} {oz + 31} {config.BLOCK_BLAST_FURNACE}")
    cmds.append(f"setblock {ox + 5} {d2_y} {oz + 31} {config.BLOCK_CAULDRON}")
    cmds.append(f"setblock {ox + 5} {d2_y + 1} {oz + 31} {config.BLOCK_HOPPER}")
    cmds.append(f"fill {ox + 3} {d2_y} {oz + 38} {ox + 5} {d2_y} {oz + 38} {config.BLOCK_CHEST}")

    cmds.append(f"fill {ox - 6} {d2_y} {oz + 40} {ox - 2} {d2_y} {oz + 44} {config.BLOCK_WOOL_BLUE}")
    cmds.append(f"setblock {ox - 3} {d2_y + 1} {oz + 42} {config.BLOCK_GLOW}")
    cmds.append(f"setblock {ox - 5} {d2_y + 1} {oz + 42} {config.BLOCK_GLOW}")

    d3_y = y_start + 8
    br_z = oz + 48

    cmds.append(f"fill {ox - 5} {d3_y} {br_z} {ox + 5} {d3_y} {br_z} {config.BLOCK_HULL_ABOVEWATER}")
    cmds.append(f"setblock {ox - 4} {d3_y + 1} {br_z} {config.BLOCK_BUTTON}")
    cmds.append(f"setblock {ox - 3} {d3_y + 1} {br_z} {config.BLOCK_LEVER}")
    cmds.append(f"setblock {ox - 2} {d3_y + 1} {br_z} {config.BLOCK_REPEATER}")
    cmds.append(f"setblock {ox - 1} {d3_y + 1} {br_z} {config.BLOCK_COMPARATOR}")
    cmds.append(f"setblock {ox} {d3_y + 1} {br_z} {config.BLOCK_FRAME}")
    cmds.append(f"setblock {ox + 1} {d3_y + 1} {br_z} {config.BLOCK_COMPARATOR}")
    cmds.append(f"setblock {ox + 2} {d3_y + 1} {br_z} {config.BLOCK_REPEATER}")
    cmds.append(f"setblock {ox + 3} {d3_y + 1} {br_z} {config.BLOCK_LEVER}")
    cmds.append(f"setblock {ox + 4} {d3_y + 1} {br_z} {config.BLOCK_BUTTON}")

    cmds.append(f"setblock {ox} {d3_y} {br_z - 2} {config.BLOCK_STAIRS} 3")
    cmds.append(f"setblock {ox} {d3_y + 1} {br_z - 4} {config.BLOCK_GLOW}")
    cmds.append(f"setblock {ox} {d3_y + 2} {br_z - 4} {config.BLOCK_TRUSS}")

    for wx in [-7, 7]:
        cmds.append(f"fill {ox + wx} {d3_y} {br_z - 1} {ox + wx} {d3_y + 2} {br_z - 1} {config.BLOCK_WALL_OUTER}")
        cmds.append(f"setblock {ox + wx} {d3_y + 2} {br_z} {config.BLOCK_LEVER}")
        for wz in range(br_z - 2, br_z + 2):
            cmds.append(f"setblock {ox + wx + (1 if wx > 0 else -1)} {d3_y + 1} {wz} {config.BLOCK_TRUSS}")
        cmds.append(f"fill {ox + wx} {d3_y} {br_z - 1} {ox + wx + (1 if wx > 0 else -1)} {d3_y} {br_z + 2} {config.BLOCK_DECK_PLATE}")

    med_y = d3_y - 4
    med_x1, med_x2 = ox + 3, ox + 8
    med_z1, med_z2 = oz + 40, oz + 46
    cmds.append(f"fill {med_x1} {med_y} {med_z1} {med_x2} {med_y + 3} {med_z2} {config.BLOCK_WALL_INNER}")
    cmds.append(f"setblock {ox + 4} {med_y} {oz + 40} {config.BLOCK_DOOR_IRON}")
    cmds.append(f"setblock {ox + 5} {med_y} {oz + 43} {config.BLOCK_BED}")
    cmds.append(f"setblock {ox + 7} {med_y} {oz + 44} {config.BLOCK_CHEST}")
    cmds.append(f"setblock {ox + 7} {med_y + 1} {oz + 44} {config.BLOCK_GLOW}")

    hp_y = y_start + config.HELIPAD_Y_OFFSET
    hp_zc = oz + config.HELIPAD_CENTER_Z
    hp_r = config.HELIPAD_RADIUS

    for dz in range(-hp_r, hp_r + 1):
        z = hp_zc + dz
        w = hp_r if abs(dz) <= 3 else hp_r - (abs(dz) - 3)
        x_min, x_max = ox - w, ox + w
        cmds.append(f"fill {x_min} {hp_y} {z} {x_max} {hp_y} {z} {config.BLOCK_GREEN}")
        cmds.append(f"setblock {x_min} {hp_y} {z} {config.BLOCK_SAFETY_YELLOW}")
        cmds.append(f"setblock {x_max} {hp_y} {z} {config.BLOCK_SAFETY_YELLOW}")
        if dz in [-hp_r, hp_r]:
            cmds.append(f"fill {x_min} {hp_y} {z} {x_max} {hp_y} {z} {config.BLOCK_SAFETY_YELLOW}")

    cmds.append(f"fill {ox - 2} {hp_y} {hp_zc - 2} {ox - 2} {hp_y} {hp_zc + 2} {config.BLOCK_WALL_OUTER}")
    cmds.append(f"fill {ox + 2} {hp_y} {hp_zc - 2} {ox + 2} {hp_y} {hp_zc + 2} {config.BLOCK_WALL_OUTER}")
    cmds.append(f"fill {ox - 1} {hp_y} {hp_zc} {ox + 1} {hp_y} {hp_zc} {config.BLOCK_WALL_OUTER}")

    for dz in range(-hp_r - 1, hp_r + 2):
        z = hp_zc + dz
        w = hp_r + 1 if abs(dz) <= 3 else max(0, hp_r - (abs(dz) - 3) + 1)
        if w > 0:
            cmds.append(f"setblock {ox - w} {hp_y} {z} {config.BLOCK_TRUSS}")
            cmds.append(f"setblock {ox + w} {hp_y} {z} {config.BLOCK_TRUSS}")

    for side, off in [(-1, -5), (1, 5)]:
        cmds.append(f"fill {ox + off} {h_deck} {oz + 46} {ox + off // 2} {hp_y - 1} {hp_zc} {config.BLOCK_STRUCTURE}")
        cmds.append(f"fill {ox + off} {h_deck} {oz + 48} {ox + off // 2} {hp_y - 1} {hp_zc - 2} {config.BLOCK_STRUCTURE}")
        cmds.append(f"fill {ox + off} {h_deck + 1} {oz + 47} {ox + off // 2} {hp_y - 2} {hp_zc - 1} {config.BLOCK_TRUSS}")

    for gx, gz in [(-hp_r, -3), (-hp_r, 3), (hp_r, -3), (hp_r, 3)]:
        cmds.append(f"setblock {ox + gx} {hp_y} {hp_zc + gz} {config.BLOCK_GLOW}")

    cmds.append(f"fill {ox - 1} {hp_y} {hp_zc + hp_r + 2} {ox + 1} {hp_y + 2} {hp_zc + hp_r + 2} {config.BLOCK_DECK_WARNING}")

    for ez in range(oz + 28, oz + 48, 6):
        cmds.append(f"setblock {ox - 2} {y_start + 1} {ez} {config.BLOCK_FIRE_EXTINGUISHER}")
        cmds.append(f"setblock {ox + 2} {y_start + 1} {ez} {config.BLOCK_FIRE_EXTINGUISHER}")

    for ez in range(oz + 28, oz + 48, 4):
        cmds.append(f"setblock {ox} {y_start + 3} {ez} {config.BLOCK_EMERGENCY_SIGN}")

    return cmds
