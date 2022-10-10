WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 128
DIFFICULTY = ['easy','hard']

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'graphics/font/diablo.ttf'
UI_FONT_SIZE = 24

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
UI_SELECTED_BOX_COLOR = '#5c5c3d'
TEXT_COLOR = '#eeeeee'

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': 'graphics/sword/full.png'}
}

magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic': 'graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic': 'graphics/particles/heal/heal.png'}
}

monster_data = {
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder',
               'attack_sound': 'audio/attack/fireball.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 60,
               'notice_radius': 350}
}

WORLD_MAP = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 's', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 's', ' ', 's', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
]
