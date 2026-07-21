import config

def build_subsea(ox, oy, oz):
    cmds = []
    bx = ox + config.BOP_CENTER_X
    bz = oz + config.BOP_CENTER_Z
    y_sb = oy + config.Y_SEABED
    y_bot = oy + config.Y_HULL_BOTTOM

    cmds.append(f"fill {bx - 4} {y_sb} {bz - 4} {bx + 4} {y_sb} {bz + 4} {config.BLOCK_BOP_BODY}")
    for dx, dz in [(-4, -4), (-4, 4), (4, -4), (4, 4)]:
        cmds.append(f"fill {bx + dx} {y_sb + 1} {bz + dz} {bx + dx} {y_sb + 4} {bz + dz} {config.BLOCK_STRUCTURE}")

    cmds.append(f"fill {bx - 1} {y_sb + 1} {bz - 1} {bx + 1} {y_sb + 3} {bz + 1} {config.BLOCK_BOP_BODY}")
    for dx, dz in [(-3, 0), (3, 0), (0, -3), (0, 3)]:
        cmds.append(f"setblock {bx + dx} {y_sb + 2} {bz + dz} {config.BLOCK_PISTON}")
        cmds.append(f"setblock {bx + dx} {y_sb + 3} {bz + dz} {config.BLOCK_VALVE_RED}")

    for dx, dz in [(-3, -3), (-3, 3), (3, -3), (3, 3)]:
        cmds.append(f"fill {bx + dx} {y_sb + 1} {bz + dz} {bx + dx} {y_sb + config.ACCUMULATOR_HEIGHT} {bz + dz} {config.BLOCK_VALVE_YELLOW}")
        cmds.append(f"setblock {bx + dx} {y_sb + config.ACCUMULATOR_HEIGHT + 1} {bz + dz} {config.BLOCK_TRUSS}")

    cmds.append(f"fill {bx - 1} {y_sb + 4} {bz - 1} {bx + 1} {y_sb + 6} {bz + 1} {config.BLOCK_STRUCTURE}")
    for dy in range(4, 7):
        for dx, dz in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            cmds.append(f"setblock {bx + dx} {y_sb + dy} {bz + dz} {config.BLOCK_AIR}")
    cmds.append(f"fill {bx - 1} {y_sb + 7} {bz - 1} {bx + 1} {y_sb + 7} {bz + 1} {config.BLOCK_HULL_ABOVEWATER}")

    cmds.append(f"fill {bx - 1} {y_sb + 8} {bz - 1} {bx + 1} {y_sb + 10} {bz + 1} {config.BLOCK_BOP_BODY}")
    for dx, dz in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cmds.append(f"setblock {bx + dx} {y_sb + 9} {bz + dz} {config.BLOCK_VALVE_YELLOW}")

    cmds.append(f"fill {bx - 4} {y_sb + 8} {bz - 2} {bx - 4} {y_sb + 10} {bz + 2} {config.BLOCK_VALVE_BLUE}")
    cmds.append(f"fill {bx + 4} {y_sb + 8} {bz - 2} {bx + 4} {y_sb + 10} {bz + 2} {config.BLOCK_VALVE_YELLOW}")
    for sx in [-4, 4]:
        cmds.append(f"fill {bx + sx} {y_sb + 11} {bz - 1} {bx + sx} {y_sb + 11} {bz + 1} {config.BLOCK_STRUCTURE}")

    r_start = y_sb + 11
    r_end = y_bot

    cmds.append(f"fill {bx} {r_start} {bz} {bx} {r_end} {bz} {config.BLOCK_RISER}")
    for dx, dz in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cmds.append(f"fill {bx + dx} {r_start} {bz + dz} {bx + dx} {r_end} {bz + dz} {config.BLOCK_TRUSS}")

    for ry in range(r_start, r_end, 8):
        for dx, dz in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
            cmds.append(f"setblock {bx + dx} {ry} {bz + dz} {config.BLOCK_RISER_BUOY}")

    cmds.append(f"setblock {bx} {r_start} {bz} {config.BLOCK_GLOW}")

    for dx, dz in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
        cmds.append(f"fill {bx + dx} {r_end} {bz + dz} {bx + dx} {r_end + 5} {bz + dz} {config.BLOCK_PISTON}")
        cmds.append(f"fill {bx + dx} {r_end + 6} {bz + dz} {bx + dx} {r_end + 8} {bz + dz} {config.BLOCK_STRUCTURE}")
        cmds.append(f"fill {bx + dx // 2} {r_end + 5} {bz + dx // 2} {bx + dx // 2} {r_end + 8} {bz + dz // 2} {config.BLOCK_CABLE}")

    mp_h = oy + config.Y_HULL_BOTTOM
    for sx in range(bx - 4, bx + 5):
        for sz in range(bz - 4, bz + 5):
            if abs(sx - bx) > 3 or abs(sz - bz) > 3:
                cmds.append(f"setblock {sx} {mp_h + 8} {sz} {config.BLOCK_DECK_GRATING}")
    for sx in [bx - 4, bx + 4]:
        for sz in range(bz - 4, bz + 5):
            cmds.append(f"setblock {sx} {mp_h + 9} {sz} {config.BLOCK_TRUSS}")
    for sz in [bz - 4, bz + 4]:
        for sx in range(bx - 3, bx + 4):
            cmds.append(f"setblock {sx} {mp_h + 9} {sz} {config.BLOCK_TRUSS}")

    return cmds
