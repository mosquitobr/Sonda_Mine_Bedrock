import config

def build_derrick(ox, oy, oz):
    cmds = []
    h_deck = oy + config.Y_DECK

    df_y1 = oy + config.Y_DECK + 1
    df_y3 = oy + config.Y_DECK + 3
    df_x1, df_x2 = ox - config.DRILL_FLOOR_HALF_X, ox + config.DRILL_FLOOR_HALF_X
    df_z1, df_z2 = oz - config.DRILL_FLOOR_HALF_Z, oz + config.DRILL_FLOOR_HALF_Z

    cmds.append(f"fill {df_x1} {df_y1} {df_z1} {df_x2} {df_y3} {df_z2} {config.BLOCK_STRUCTURE}")

    rth = config.ROTARY_TABLE_HALF
    cmds.append(f"fill {ox - rth} {df_y1} {oz - rth - 2} {ox + rth} {df_y3} {oz + rth + 2} {config.BLOCK_AIR}")
    rt_y = df_y3
    cmds.append(f"fill {ox - rth} {rt_y} {oz - rth} {ox + rth} {rt_y} {oz + rth} {config.BLOCK_SAFETY_YELLOW}")
    cmds.append(f"setblock {ox} {rt_y} {oz} {config.BLOCK_AIR}")
    for dx, dz in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        cmds.append(f"setblock {ox + dx} {rt_y + 1} {oz + dz} {config.BLOCK_STRUCTURE}")

    stair_positions = [
        (ox - 8, oz - 9),
        (ox + 8, oz - 9),
        (ox - 8, oz + 9),
        (ox + 8, oz + 9),
    ]
    for sx, sz in stair_positions:
        cmds.append(f"fill {sx} {h_deck} {sz} {sx} {df_y1} {sz} {config.BLOCK_AIR}")
        cmds.append(f"setblock {sx} {h_deck} {sz} {config.BLOCK_LADDER} 3")
        cmds.append(f"setblock {sx} {df_y1} {sz} {config.BLOCK_DECK_PLATE}")
        cmds.append(f"setblock {sx} {df_y1 + 1} {sz} {config.BLOCK_TRUSS}")

    dh_x1, dh_x2 = ox - 9, ox - 5
    dh_z1, dh_z2 = oz - 10, oz - 6
    dh_y1 = df_y1
    dh_y2 = dh_y1 + 4

    for y in range(dh_y1, dh_y2 + 1):
        cmds.append(f"fill {dh_x1} {y} {dh_z1} {dh_x2} {y} {dh_z1} {config.BLOCK_WALL_OUTER}")
        cmds.append(f"fill {dh_x1} {y} {dh_z2} {dh_x2} {y} {dh_z2} {config.BLOCK_WALL_OUTER}")
        cmds.append(f"fill {dh_x1} {y} {dh_z1} {dh_x1} {y} {dh_z2} {config.BLOCK_WALL_OUTER}")
        cmds.append(f"fill {dh_x2} {y} {dh_z1} {dh_x2} {y} {dh_z2} {config.BLOCK_WALL_OUTER}")
    cmds.append(f"fill {dh_x1} {dh_y2} {dh_z1} {dh_x2} {dh_y2} {dh_z2} {config.BLOCK_WALL_OUTER}")
    cmds.append(f"fill {dh_x1 + 1} {dh_y1} {dh_z1 + 1} {dh_x2 - 1} {dh_y1} {dh_z2 - 1} {config.BLOCK_DECK_ANTI_SLIP}")

    for wz in range(dh_z1 + 1, dh_z2):
        for wy in range(dh_y1 + 1, dh_y2):
            cmds.append(f"setblock {dh_x2} {wy} {wz} {config.BLOCK_GLASS}")
    for wx in range(dh_x1 + 2, dh_x2 - 1):
        for wy in range(dh_y1 + 1, dh_y2):
            cmds.append(f"setblock {wx} {wy} {dh_z2} {config.BLOCK_GLASS}")

    cmds.append(f"fill {dh_x1} {dh_y1} {dh_z1 + 2} {dh_x1} {dh_y1 + 2} {dh_z1 + 2} {config.BLOCK_AIR}")
    cmds.append(f"setblock {dh_x1} {dh_y1} {dh_z1 + 2} {config.BLOCK_DOOR_IRON}")
    cmds.append(f"setblock {dh_x1} {dh_y1 + 1} {dh_z1 + 2} {config.BLOCK_DOOR_IRON}")

    cmds.append(f"fill {dh_x2 - 1} {dh_y1 + 1} {dh_z1 + 2} {dh_x2 - 1} {dh_y1 + 2} {dh_z2 - 1} {config.BLOCK_BLACK}")
    for iz in range(dh_z1 + 2, dh_z2):
        cmds.append(f"setblock {dh_x2 - 1} {dh_y1 + 2} {iz} {config.BLOCK_GLOW_RED}")
    cmds.append(f"setblock {dh_x2 - 1} {dh_y1 + 1} {dh_z1 + 2} {config.BLOCK_LEVER}")
    cmds.append(f"setblock {dh_x2 - 1} {dh_y1 + 1} {dh_z1 + 3} {config.BLOCK_BUTTON}")
    cmds.append(f"setblock {dh_x2 - 1} {dh_y1 + 1} {dh_z2 - 1} {config.BLOCK_LEVER}")

    cmds.append(f"setblock {dh_x1 + 2} {dh_y1 + 1} {dh_z1 + 2} {config.BLOCK_FENCE}")
    cmds.append(f"setblock {dh_x1 + 2} {dh_y1 + 2} {dh_z1 + 2} {config.BLOCK_PRESSURE_PLATE}")
    cmds.append(f"setblock {dh_x1 + 1} {dh_y1} {dh_z1 + 3} {config.BLOCK_PRESSURE_PLATE_IRON}")

    cmds.append(f"setblock {dh_x1 + 1} {dh_y2 - 1} {dh_z1 + 1} {config.BLOCK_GLOW}")
    cmds.append(f"setblock {dh_x2 - 2} {dh_y2 - 1} {dh_z2 - 1} {config.BLOCK_GLOW}")
    cmds.append(f"setblock {dh_x1 + 1} {dh_y2 + 1} {dh_z1 + 1} {config.BLOCK_OBSERVER}")

    for z in range(oz - 9, oz + 10):
        cmds.append(f"setblock {df_x1} {df_y3 + 1} {z} {config.BLOCK_TRUSS}")
        cmds.append(f"setblock {df_x2} {df_y3 + 1} {z} {config.BLOCK_TRUSS}")
    for x in range(ox - 8, ox + 9):
        cmds.append(f"setblock {x} {df_y3 + 1} {df_z1} {config.BLOCK_TRUSS}")
        cmds.append(f"setblock {x} {df_y3 + 1} {df_z2} {config.BLOCK_TRUSS}")
    cmds.append(f"fill {ox - 2} {df_y3 + 1} {df_z2} {ox + 2} {df_y3 + 1} {df_z2} {config.BLOCK_AIR}")

    derrick_base_y = df_y3 + 1
    derrick_top_y = derrick_base_y + config.DERRICK_HEIGHT
    bw = config.DERRICK_BASE_HALF_W
    tw = config.DERRICK_TOP_HALF_W

    for y in range(derrick_base_y, derrick_top_y + 1):
        t = (y - derrick_base_y) / config.DERRICK_HEIGHT
        w = int(round(bw - (bw - tw) * t))
        x_min, x_max = ox - w, ox + w
        z_min, z_max = oz - w, oz + w

        cmds.append(f"setblock {x_min} {y} {z_min} {config.BLOCK_STRUCTURE}")
        cmds.append(f"setblock {x_max} {y} {z_min} {config.BLOCK_STRUCTURE}")
        cmds.append(f"setblock {x_min} {y} {z_max} {config.BLOCK_STRUCTURE}")
        cmds.append(f"setblock {x_max} {y} {z_max} {config.BLOCK_STRUCTURE}")

        if (y - derrick_base_y) % config.STRUCTURAL_RING_INTERVAL == 0:
            cmds.append(f"fill {x_min} {y} {z_min} {x_max} {y} {z_min} {config.BLOCK_STRUCTURE}")
            cmds.append(f"fill {x_min} {y} {z_min} {x_min} {y} {z_max} {config.BLOCK_STRUCTURE}")
            cmds.append(f"fill {x_max} {y} {z_min} {x_max} {y} {z_max} {config.BLOCK_STRUCTURE}")
            if y < derrick_base_y + config.V_DOOR_HEIGHT:
                cmds.append(f"fill {x_min} {y} {z_max} {ox - 2} {y} {z_max} {config.BLOCK_STRUCTURE}")
                cmds.append(f"fill {ox + 2} {y} {z_max} {x_max} {y} {z_max} {config.BLOCK_STRUCTURE}")
            else:
                cmds.append(f"fill {x_min} {y} {z_max} {x_max} {y} {z_max} {config.BLOCK_STRUCTURE}")
        else:
            cmds.append(f"fill {x_min + 1} {y} {z_min} {x_max - 1} {y} {z_min} {config.BLOCK_TRUSS}")
            cmds.append(f"fill {x_min} {y} {z_min + 1} {x_min} {y} {z_max - 1} {config.BLOCK_TRUSS}")
            cmds.append(f"fill {x_max} {y} {z_min + 1} {x_max} {y} {z_max - 1} {config.BLOCK_TRUSS}")
            if y < derrick_base_y + config.V_DOOR_HEIGHT:
                cmds.append(f"fill {x_min + 1} {y} {z_max} {ox - 2} {y} {z_max} {config.BLOCK_TRUSS}")
                cmds.append(f"fill {ox + 2} {y} {z_max} {x_max - 1} {y} {z_max} {config.BLOCK_TRUSS}")
            else:
                cmds.append(f"fill {x_min + 1} {y} {z_max} {x_max - 1} {y} {z_max} {config.BLOCK_TRUSS}")

    cmds.append(f"fill {ox - 2} {derrick_top_y} {oz - 2} {ox + 2} {derrick_top_y} {oz + 2} {config.BLOCK_STRUCTURE}")
    for sx, sz in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        cmds.append(f"setblock {ox + sx} {derrick_top_y + 1} {oz + sz} {config.BLOCK_HULL_ABOVEWATER}")
    cmds.append(f"fill {ox - 1} {derrick_top_y + 2} {oz - 1} {ox + 1} {derrick_top_y + 2} {oz + 1} {config.BLOCK_GLOW}")

    rack_y = derrick_base_y + 33
    rw = bw - 2
    cmds.append(f"fill {ox - rw} {rack_y} {oz - rw} {ox + rw} {rack_y} {oz + rw} {config.BLOCK_TRUSS}")
    for side_z in [-rw, rw]:
        cmds.append(f"fill {ox - rw} {rack_y} {oz + side_z} {ox + rw} {rack_y + 3} {oz + side_z} {config.BLOCK_TRUSS}")
    for side_x in [-rw, rw]:
        cmds.append(f"fill {ox + side_x} {rack_y} {oz - rw} {ox + side_x} {rack_y + 3} {oz + rw} {config.BLOCK_TRUSS}")
    for px in range(ox - rw + 1, ox + rw):
        for pz in range(oz - rw + 1, oz + rw):
            if (px + pz) % 4 == 0:
                cmds.append(f"fill {px} {rack_y + 1} {pz} {px} {rack_y + 4} {pz} {config.BLOCK_RISER}")

    for ly in range(derrick_base_y + 5, rack_y + 3):
        if ly % 2 == 0:
            cmds.append(f"setblock {ox + 2} {ly} {oz - 2} {config.BLOCK_LADDER} 3")

    tb_y = derrick_base_y + 23
    cmds.append(f"fill {ox - 1} {tb_y} {oz - 1} {ox + 1} {tb_y + 4} {oz + 1} {config.BLOCK_SAFETY_YELLOW}")
    cmds.append(f"fill {ox} {tb_y} {oz} {ox} {tb_y + 4} {oz} {config.BLOCK_STRUCTURE}")
    cmds.append(f"setblock {ox} {tb_y - 1} {oz} {config.BLOCK_STICKY_PISTON}")

    cmds.append(f"fill {ox - 2} {rt_y + 1} {oz + 5} {ox + 2} {rt_y + 2} {oz + 5} {config.BLOCK_STRUCTURE}")
    cmds.append(f"setblock {ox} {rt_y + 1} {oz + 4} {config.BLOCK_PISTON}")
    cmds.append(f"fill {ox - 1} {rt_y + 2} {oz + 3} {ox + 1} {rt_y + 2} {oz + 3} {config.BLOCK_TRUSS}")

    cmds.append(f"fill {ox + 5} {rt_y - 1} {oz - 1} {ox + 5} {rt_y + 2} {oz + 1} {config.BLOCK_STRUCTURE}")
    cmds.append(f"setblock {ox + 5} {rt_y} {oz} {config.BLOCK_AIR}")
    cmds.append(f"setblock {ox + 5} {rt_y + 1} {oz} {config.BLOCK_AIR}")

    cmds.append(f"fill {ox} {oy + config.Y_SEABED} {oz} {ox} {tb_y - 2} {oz} {config.BLOCK_TRUSS}")

    cmds.append(f"fill {ox - 4} {rt_y} {oz - 7} {ox + 4} {rt_y + 3} {oz - 7} {config.BLOCK_HULL_ABOVEWATER}")
    cmds.append(f"fill {ox - 3} {rt_y + 1} {oz - 6} {ox + 3} {rt_y + 2} {oz - 6} {config.BLOCK_STRUCTURE}")
    cmds.append(f"setblock {ox} {rt_y + 1} {oz - 6} {config.BLOCK_PISTON}")
    cmds.append(f"fill {ox} {rt_y + 3} {oz - 6} {ox} {derrick_top_y} {oz - 6} {config.BLOCK_CABLE}")

    cw_z_start = oz + 11
    cw_z_end = oz + 28
    cmds.append(f"fill {ox - 2} {h_deck} {cw_z_start} {ox + 2} {h_deck} {cw_z_end} {config.BLOCK_STRUCTURE}")
    cmds.append(f"fill {ox - 1} {h_deck + 1} {cw_z_start + 2} {ox - 1} {h_deck + 1} {cw_z_end - 2} {config.BLOCK_STRUCTURE}")
    cmds.append(f"fill {ox + 1} {h_deck + 1} {cw_z_start + 2} {ox + 1} {h_deck + 1} {cw_z_end - 2} {config.BLOCK_STRUCTURE}")
    cmds.append(f"fill {ox} {h_deck + 1} {cw_z_start + 3} {ox} {h_deck + 1} {cw_z_end - 3} {config.BLOCK_TRUSS}")
    for z in range(cw_z_start, cw_z_end + 1):
        cmds.append(f"setblock {ox - 3} {h_deck + 2} {z} {config.BLOCK_TRUSS}")
        cmds.append(f"setblock {ox + 3} {h_deck + 2} {z} {config.BLOCK_TRUSS}")
    cmds.append(f"setblock {ox} {h_deck + 1} {cw_z_start + 1} {config.BLOCK_PISTON}")
    cmds.append(f"fill {ox} {h_deck + 2} {cw_z_start + 1} {ox} {h_deck + 5} {cw_z_start + 1} {config.BLOCK_TRUSS}")

    cmds.append(f"fill {df_x1} {df_y3} {df_z1} {df_x2} {df_y3} {df_z1} {config.BLOCK_SAFETY_YELLOW}")
    cmds.append(f"fill {df_x1} {df_y3} {df_z2} {df_x2} {df_y3} {df_z2} {config.BLOCK_SAFETY_YELLOW}")
    cmds.append(f"fill {df_x1} {df_y3} {df_z1} {df_x1} {df_y3} {df_z2} {config.BLOCK_SAFETY_YELLOW}")
    cmds.append(f"fill {df_x2} {df_y3} {df_z1} {df_x2} {df_y3} {df_z2} {config.BLOCK_SAFETY_YELLOW}")

    return cmds
