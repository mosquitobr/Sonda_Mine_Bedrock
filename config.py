import math

# ─── Servidor WebSocket ───
PORT = 19131
HOST = "0.0.0.0"
COMMAND_DELAY = 0.02
BATCH_SIZE = 120

# ─── Referenciais de altura (Y absoluto Minecraft Bedrock) ───
Y_SEABED = 12
Y_SEA_LEVEL = 62
Y_DECK = 70
Y_HULL_BOTTOM = 55
Y_HULL_BILGE = 57
Y_INTERIOR_FLOOR = 56
Y_INTERIOR_CEIL = 69

# ─── Dimensões principais da Sonda (Classe Aq) ───
SHIP_LENGTH = 140  # along Z
SHIP_BEAM = 25
HULL_HEIGHT = 15

# ─── Geometria de proa/popa ───
BOW_START_REL_Z = 25
BOW_END_REL_Z = 70
STERN_TAPER_START = -50
STERN_END = -70
STERN_TRANSOM_WIDTH = 9

# ─── Moonpool ───
MOONPOOL_X_MIN = -3
MOONPOOL_X_MAX = 3
MOONPOOL_Z_MIN = -5
MOONPOOL_Z_MAX = 5

# ─── Drill floor & Derrick (Torre de Perfuração) ───
DRILL_FLOOR_HALF_X = 9
DRILL_FLOOR_HALF_Z = 10
ROTARY_TABLE_HALF = 3
DERRICK_HEIGHT = 55
DERRICK_BASE_HALF_W = 7
DERRICK_TOP_HALF_W = 2
V_DOOR_HEIGHT = 22
STRUCTURAL_RING_INTERVAL = 4

# ─── Subsea / BOP (Blowout Preventer) ───
BOP_BASE_HALF = 4
BOP_STACK_HALF = 1
ACCUMULATOR_HEIGHT = 8
BOP_CENTER_X = 0
BOP_CENTER_Z = 0

# ─── Alojamento & Superestrutura ───
ACCOM_Z_START = 24
ACCOM_Z_END = 50
ACCOM_HEIGHT = 12
ACCOM_DECK_INTERVAL = 4

# ─── Heliporto ───
HELIPAD_CENTER_Z = 60
HELIPAD_RADIUS = 8
HELIPAD_Y_OFFSET = 7

# ─── Máquinas & Guindastes ───
CRANE_BOOM_LENGTH = 12
PIPE_RACK_Z_START = 11
PIPE_RACK_Z_END = 28

# ─── Oceano / Área de Limpeza ───
OCEAN_SIZE = 90

# ─── Larguras de corredores de segurança ───
CORRIDOR_WIDTH = 3
CORRIDOR_HEIGHT = 3
ALLEY_WIDTH = 2

# ═══════════════════════════════════════════════
# PALETA DE BLOCOS MINECRAFT BEDROCK
# ═══════════════════════════════════════════════

BLOCK_WATER = "water"
BLOCK_AIR = "air"
BLOCK_SEABED = "gravel"
BLOCK_DEEP_SEABED = "stone"
BLOCK_CLAY = "clay"

BLOCK_HULL_BULBOUS = "blackstone"
BLOCK_HULL_UNDERWATER = "red_concrete"
BLOCK_HULL_ABOVEWATER = "gray_concrete"
BLOCK_HULL_BILGE_KEEL = "dark_oak_planks"
BLOCK_HULL_STABILIZER = "iron_block"

BLOCK_DECK = "polished_andesite"
BLOCK_DECK_ALT = "stone_bricks"
BLOCK_DECK_GRATING = "iron_bars"
BLOCK_DECK_GRATING_FLOOR = "iron_bars"
BLOCK_DECK_PLATE = "smooth_stone"
BLOCK_DECK_TILE = "white_concrete"
BLOCK_DECK_ANTI_SLIP = "polished_blackstone"

BLOCK_WALL_OUTER = "white_concrete"
BLOCK_WALL_INNER = "smooth_stone"
BLOCK_WALL_FIREPROOF = "nether_brick"
BLOCK_WALL_BULKHEAD = "stone_bricks"
BLOCK_WALL_ACCOM = "quartz_block"
BLOCK_WALL_CORRIDOR = "smooth_quartz"

BLOCK_GLASS = "glass"
BLOCK_GLASS_PANE = "glass_pane"
BLOCK_GLASS_TINTED = "tinted_glass"
BLOCK_GLASS_REINFORCED = "lime_stained_glass"
BLOCK_GLASS_BRIDGE = "blue_stained_glass"

BLOCK_STRUCTURE = "iron_block"
BLOCK_HEAVY_STRUCTURE = "netherite_block"
BLOCK_LIGHT_STRUCTURE = "iron_bars"
BLOCK_TRUSS = "iron_bars"
BLOCK_LATTICE = "chain"
BLOCK_CABLE = "chain"

BLOCK_GLOW = "sea_lantern"
BLOCK_GLOW_RED = "redstone_lamp"
BLOCK_GLOW_LANTERN = "lantern"
BLOCK_GLOW_CEILING = "glowstone"
BLOCK_GLOW_WALL = "redstone_torch"

BLOCK_PISTON = "piston"
BLOCK_STICKY_PISTON = "sticky_piston"
BLOCK_OBSERVER = "observer"
BLOCK_CAULDRON = "cauldron"
BLOCK_HOPPER = "hopper"
BLOCK_DISPENSER = "dispenser"
BLOCK_DROPPER = "dropper"
BLOCK_COMPARATOR = "redstone_comparator"
BLOCK_REPEATER = "redstone_repeater"
BLOCK_LEVER = "lever"
BLOCK_BUTTON = "stone_button"
BLOCK_PRESSURE_PLATE = "wooden_pressure_plate"
BLOCK_PRESSURE_PLATE_IRON = "heavy_weighted_pressure_plate"

BLOCK_YELLOW = "yellow_concrete"
BLOCK_GREEN = "lime_concrete"
BLOCK_BLACK = "black_concrete"
BLOCK_RED = "red_concrete"
BLOCK_ORANGE = "orange_concrete"
BLOCK_BLUE = "blue_concrete"
BLOCK_WHITE = "white_concrete"
BLOCK_LIGHT_GRAY = "light_gray_concrete"

BLOCK_SAFETY_YELLOW = "yellow_concrete"
BLOCK_SAFETY_YELLOW_PANE = "yellow_stained_glass_pane"
BLOCK_SAFETY_RED = "red_concrete"
BLOCK_SAFETY_WHITE = "white_concrete"
BLOCK_SAFETY_BLACK = "black_concrete"
BLOCK_DECK_WARNING = "red_concrete"

BLOCK_BOP_BODY = "netherite_block"
BLOCK_VALVE_RED = "red_concrete"
BLOCK_VALVE_YELLOW = "yellow_concrete"
BLOCK_VALVE_BLUE = "blue_concrete"
BLOCK_RISER = "gray_concrete"
BLOCK_RISER_BUOY = "yellow_wool"

BLOCK_CRANE_PEDESTAL = "stone_brick_wall"
BLOCK_CRANE_CAB = "yellow_concrete"
BLOCK_ANVIL = "anvil"

BLOCK_LADDER = "ladder"
BLOCK_STAIRS = "spruce_stairs"
BLOCK_STAIRS_STONE = "stone_brick_stairs"
BLOCK_STAIRS_IRON = "polished_blackstone_brick_stairs"
BLOCK_SLAB = "spruce_slab"
BLOCK_SLAB_STONE = "stone_brick_slab"
BLOCK_SLAB_IRON = "polished_blackstone_brick_slab"
BLOCK_DOOR_WOOD = "wooden_door"
BLOCK_DOOR_IRON = "iron_door"
BLOCK_DOOR_DARK_OAK = "dark_oak_door"
BLOCK_FENCE_GATE = "fence_gate"
BLOCK_FENCE_GATE_IRON = "iron_bars"
BLOCK_FENCE = "fence"
BLOCK_FENCE_NETHER = "nether_brick_fence"
BLOCK_WOOL_RED = "red_wool"
BLOCK_WOOL_WHITE = "white_wool"
BLOCK_WOOL_BLUE = "blue_wool"
BLOCK_BED = "red_bed"
BLOCK_CHEST = "chest"
BLOCK_FURNACE = "furnace"
BLOCK_BLAST_FURNACE = "blast_furnace"
BLOCK_CAKE = "cake"
BLOCK_FRAME = "frame"
BLOCK_PAINTING = "painting"

BLOCK_WATERLOGGED = "water"
BLOCK_FIRE_EXTINGUISHER = "red_concrete"
BLOCK_EMERGENCY_SIGN = "glowstone"
BLOCK_NOZZLE = "tripwire_hook"

def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t
