import config

def build_machinery(ox, oy, oz):
    cmds = []
    h_deck = oy + config.Y_DECK

    def create_crane(cx, cz, is_starboard):
        cmds.append(f"setblock {cx} {h_deck} {cz} {config.BLOCK_STRUCTURE}")
        for y_off in range(1, 3):
            cmds.append(f"setblock {cx} {h_deck + y_off} {cz} {config.BLOCK_CRANE_PEDESTAL}")

        cab_y = h_deck + 3
        for y_cab in range(cab_y, cab_y + 3):
            cmds.append(f"fill {cx - 1} {y_cab} {cz - 1} {cx + 1} {y_cab} {cz + 1} {config.BLOCK_CRANE_CAB}")
        cmds.append(f"fill {cx} {cab_y} {cz} {cx} {cab_y + 1} {cz} {config.BLOCK_AIR}")

        if is_starboard:
            cmds.append(f"fill {cx + 1} {cab_y + 1} {cz - 1} {cx + 1} {cab_y + 1} {cz + 1} {config.BLOCK_GLASS}")
            cmds.append(f"setblock {cx - 1} {cab_y} {cz} {config.BLOCK_ANVIL}")
            cmds.append(f"setblock {cx - 1} {cab_y + 1} {cz} {config.BLOCK_ANVIL}")
            for i in range(config.CRANE_BOOM_LENGTH):
                by = cab_y + 1 + i
                bx = cx + 1 + i
                cmds.append(f"setblock {bx} {by} {cz} {config.BLOCK_TRUSS}")
                if i == config.CRANE_BOOM_LENGTH - 1:
                    cmds.append(f"setblock {bx} {by} {cz} {config.BLOCK_GLOW}")
            cmds.append(f"fill {cx + config.CRANE_BOOM_LENGTH} {cab_y + config.CRANE_BOOM_LENGTH} {cz} {cx + config.CRANE_BOOM_LENGTH} {cab_y} {cz} {config.BLOCK_TRUSS}")
            cmds.append(f"setblock {cx + config.CRANE_BOOM_LENGTH} {cab_y - 1} {cz} {config.BLOCK_CRANE_PEDESTAL}")
        else:
            cmds.append(f"fill {cx - 1} {cab_y + 1} {cz - 1} {cx - 1} {cab_y + 1} {cz + 1} {config.BLOCK_GLASS}")
            cmds.append(f"setblock {cx + 1} {cab_y} {cz} {config.BLOCK_ANVIL}")
            cmds.append(f"setblock {cx + 1} {cab_y + 1} {cz} {config.BLOCK_ANVIL}")
            for i in range(config.CRANE_BOOM_LENGTH):
                by = cab_y + 1 + i
                bx = cx - 1 - i
                cmds.append(f"setblock {bx} {by} {cz} {config.BLOCK_TRUSS}")
                if i == config.CRANE_BOOM_LENGTH - 1:
                    cmds.append(f"setblock {bx} {by} {cz} {config.BLOCK_GLOW}")
            cmds.append(f"fill {cx - config.CRANE_BOOM_LENGTH} {cab_y + config.CRANE_BOOM_LENGTH} {cz} {cx - config.CRANE_BOOM_LENGTH} {cab_y} {cz} {config.BLOCK_TRUSS}")
            cmds.append(f"setblock {cx - config.CRANE_BOOM_LENGTH} {cab_y - 1} {cz} {config.BLOCK_CRANE_PEDESTAL}")

        cmds.append(f"setblock {cx + (2 if not is_starboard else -2)} {h_deck} {cz} {config.BLOCK_LADDER} 3")
        for ly in range(h_deck, cab_y + 2):
            cmds.append(f"setblock {cx + (2 if not is_starboard else -2)} {ly} {cz} {config.BLOCK_LADDER} 3")

    create_crane(ox - 9, oz + 22, False)
    create_crane(ox + 9, oz + 22, True)
    create_crane(ox - 9, oz - 38, False)
    create_crane(ox + 9, oz - 38, True)

    kx, kz = ox, oz + 40
    cmds.append(f"setblock {kx} {h_deck} {kz} {config.BLOCK_STRUCTURE}")
    cmds.append(f"setblock {kx} {h_deck + 1} {kz} {config.BLOCK_PISTON}")
    for i in range(6):
        cmds.append(f"setblock {kx} {h_deck + 2 + i} {kz} {config.BLOCK_TRUSS}")
    cmds.append(f"setblock {kx + 1} {h_deck + 6} {kz} {config.BLOCK_STRUCTURE}")
    for i in range(7):
        cmds.append(f"setblock {kx + 2 + i} {h_deck + 6 - i // 2} {kz} {config.BLOCK_TRUSS}")
    cmds.append(f"fill {kx + 8} {h_deck + 1} {kz} {kx + 8} {h_deck + 4} {kz} {config.BLOCK_CABLE}")
    cmds.append(f"setblock {kx + 8} {h_deck} {kz} {config.BLOCK_CRANE_PEDESTAL}")

    for bz in range(oz + 12, oz + 28, 4):
        cmds.append(f"fill {ox - 10} {h_deck} {bz} {ox - 3} {h_deck} {bz} {config.BLOCK_STRUCTURE}")
        cmds.append(f"fill {ox + 3} {h_deck} {bz} {ox + 10} {h_deck} {bz} {config.BLOCK_STRUCTURE}")
        for side_off in [-10, -3, 3, 10]:
            cmds.append(f"fill {ox + side_off} {h_deck + 1} {bz} {ox + side_off} {h_deck + 5} {bz} {config.BLOCK_TRUSS}")

    for z in range(oz + 12, oz + 28):
        for x in [ox - 6, ox + 6]:
            cmds.append(f"setblock {x} {h_deck} {z} {config.BLOCK_DECK_GRATING}")
        cmds.append(f"setblock {ox} {h_deck} {z} {config.BLOCK_DECK_PLATE}")

    for z in range(oz + 12, oz + 28):
        cmds.append(f"setblock {ox - 2} {h_deck + 1} {z} {config.BLOCK_TRUSS}")
        cmds.append(f"setblock {ox + 2} {h_deck + 1} {z} {config.BLOCK_TRUSS}")

    for tier, (x_range, y_off) in enumerate([
        (range(ox - 9, ox - 3), 1),
        (range(ox - 8, ox - 4), 2),
        ([-5], 3),
        (range(ox + 4, ox + 10), 1),
        (range(ox + 5, ox + 9), 2),
        ([6], 3),
    ]):
        for x in x_range:
            cmds.append(f"fill {x} {h_deck + y_off} {oz + 14} {x} {h_deck + y_off} {oz + 26} {config.BLOCK_RISER}")

    cmds.append(f"fill {ox - 4} {h_deck} {oz - 48} {ox + 4} {h_deck + 1} {oz - 44} {config.BLOCK_STRUCTURE}")
    cmds.append(f"fill {ox - 4} {h_deck + 1} {oz - 48} {ox + 4} {h_deck + 1} {oz - 44} {config.BLOCK_TRUSS}")
    for wx, wz in [(-4, -48), (-4, -44), (4, -48), (4, -44)]:
        cmds.append(f"setblock {ox + wx} {h_deck} {oz + wz} {config.BLOCK_PISTON}")
    cmds.append(f"fill {ox - 4} {h_deck} {oz - 48} {ox - 4} {h_deck} {oz - 20} {config.BLOCK_STRUCTURE}")
    cmds.append(f"fill {ox + 4} {h_deck} {oz - 48} {ox + 4} {h_deck} {oz - 20} {config.BLOCK_STRUCTURE}")
    for z in range(oz - 48, oz - 20):
        cmds.append(f"setblock {ox + 6} {h_deck} {z} {config.BLOCK_DECK_PLATE}")
        cmds.append(f"setblock {ox + 5} {h_deck + 1} {z} {config.BLOCK_TRUSS}")

    for wz in [30, -52]:
        for wx in [-10, 10]:
            cmds.append(f"fill {ox + wx - 1} {h_deck} {oz + wz} {ox + wx + 1} {h_deck + 2} {oz + wz} {config.BLOCK_STRUCTURE}")
            cmds.append(f"setblock {ox + wx} {h_deck + 1} {oz + wz} {config.BLOCK_PISTON}")
            cmds.append(f"fill {ox + wx} {h_deck} {oz + wz + (1 if wx < 0 else -1)} {ox + wx} {h_deck} {oz + wz + (3 if wx < 0 else -3)} {config.BLOCK_CABLE}")

    for wz, label in [(32, "Fwd"), (-25, "Aft")]:
        for wx, side in [(-14, "Port"), (14, "Starboard")]:
            for y_off in range(h_deck, h_deck + 6):
                cmds.append(f"setblock {wx + ox} {y_off} {wz + oz} {config.BLOCK_STRUCTURE}")
            cmds.append(f"fill {wx + ox - 1} {h_deck} {wz + oz - 2} {wx + ox + 1} {h_deck + 2} {wz + oz + 2} {config.BLOCK_ORANGE}")
            cmds.append(f"fill {wx + ox - 1} {h_deck + 3} {wz + oz - 2} {wx + ox + 1} {h_deck + 3} {wz + oz + 2} {config.BLOCK_WHITE}")
            cmds.append(f"setblock {wx + ox} {h_deck + 1} {wz + oz + 2} {config.BLOCK_GLASS}")
            cmds.append(f"setblock {wx + ox} {h_deck + 2} {wz + oz + 2} {config.BLOCK_GLASS}")
            plat_x = ox + wx + (1 if wx > 0 else -1)
            cmds.append(f"fill {plat_x} {h_deck} {wz + oz - 1} {plat_x + (1 if wx > 0 else -1)} {h_deck} {wz + oz + 1} {config.BLOCK_DECK_PLATE}")
            cmds.append(f"fill {plat_x} {h_deck + 1} {wz + oz - 1} {plat_x + (1 if wx > 0 else -1)} {h_deck + 1} {wz + oz + 1} {config.BLOCK_TRUSS}")
            cmds.append(f"setblock {plat_x} {h_deck} {wz + oz} {config.BLOCK_LADDER} 3")
            for ly in range(h_deck, h_deck + 6):
                cmds.append(f"setblock {plat_x} {ly} {wz + oz} {config.BLOCK_LADDER} 3")

    for z in range(oz - 30, oz + 30, 3):
        cmds.append(f"setblock {ox} {h_deck} {z} {config.BLOCK_STRUCTURE}")
    cmds.append(f"fill {ox} {h_deck + 1} {oz - 30} {ox} {h_deck + 1} {oz + 28} {config.BLOCK_TRUSS}")
    for z in range(oz - 30, oz + 29):
        cmds.append(f"setblock {ox - 1} {h_deck + 2} {z} {config.BLOCK_TRUSS}")
        cmds.append(f"setblock {ox + 1} {h_deck + 2} {z} {config.BLOCK_TRUSS}")

    cmds.append(f"fill {ox - 1} {h_deck} {oz - 55} {ox - 1} {h_deck} {oz - 13} {config.BLOCK_SAFETY_YELLOW}")
    cmds.append(f"fill {ox + 1} {h_deck} {oz - 55} {ox + 1} {h_deck} {oz - 13} {config.BLOCK_SAFETY_YELLOW}")

    for cx, cz in [(ox-9, oz+22), (ox+9, oz+22), (ox-9, oz-38), (ox+9, oz-38)]:
        cmds.append(f"fill {cx - 2} {h_deck} {cz - 2} {cx + 2} {h_deck} {cz - 2} {config.BLOCK_SAFETY_YELLOW}")
        cmds.append(f"fill {cx - 2} {h_deck} {cz + 2} {cx + 2} {h_deck} {cz + 2} {config.BLOCK_SAFETY_YELLOW}")
        cmds.append(f"fill {cx - 2} {h_deck} {cz - 1} {cx - 2} {h_deck} {cz + 1} {config.BLOCK_SAFETY_YELLOW}")
        cmds.append(f"fill {cx + 2} {h_deck} {cz - 1} {cx + 2} {h_deck} {cz + 1} {config.BLOCK_SAFETY_YELLOW}")

    return cmds
