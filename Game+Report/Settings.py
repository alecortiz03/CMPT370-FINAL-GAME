import math

# Doom resolution settings
DOOM_RES = DOOM_W, DOOM_H = 1280, 720

# Scale factor for the window resolution
SCALE = 1.0
# Window resolution settings
WIN_RES = WIDTH, HEIGHT = int(DOOM_W * SCALE), int(DOOM_H * SCALE)
# Half-width and half-height of the window
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2

# Field of view settings
FOV = 90.0
# Half of the field of view
H_FOV = FOV / 2

# Player movement speed
PLAYER_SPEED = 0.3
# Player rotation speed
PLAYER_ROT_SPEED = 0.12
# Player height
PLAYER_HEIGHT = 41
# Player radius
PLAYER_RADIUS = 10

# Distance from the screen to the player
SCREEN_DIST = H_WIDTH / math.tan(math.radians(H_FOV))