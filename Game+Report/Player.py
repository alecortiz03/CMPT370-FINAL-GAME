from Settings import *
from pygame.math import Vector2 as vec2
import pygame as pg
import math

class Player:
    def __init__(self, engine):
        self.engine = engine
        self.thing = engine.wad_data.things[0]
        self.pos = self.thing.pos
        self.angle = self.thing.angle
        self.DIAG_MOVE_CORR = 1 / math.sqrt(2)  # Correction factor for diagonal movement
        self.height = PLAYER_HEIGHT

    def update(self):
        self.get_height()  # Update player's height
        self.control()  # Handle player controls

    def control(self):
        speed = PLAYER_SPEED * self.engine.dt  # Calculate movement speed
        rot_speed = PLAYER_ROT_SPEED * self.engine.dt  # Calculate rotation speed

        key_state = pg.key.get_pressed()  # Get the current state of all keyboard buttons
        if key_state[pg.K_LEFT]:
            self.angle += rot_speed  # Rotate left
        if key_state[pg.K_RIGHT]:
            self.angle -= rot_speed  # Rotate right

        inc = vec2(0)  # Initialize movement increment vector
        if key_state[pg.K_a]:
            inc += vec2(0, speed)  # Move left
        if key_state[pg.K_d]:
            inc += vec2(0, -speed)  # Move right
        if key_state[pg.K_w]:
            inc += vec2(speed, 0)  # Move forward
        if key_state[pg.K_s]:
            inc += vec2(-speed, 0)  # Move backward

        if inc.x and inc.y:
            inc *= self.DIAG_MOVE_CORR  # Apply diagonal movement correction

        inc.rotate_ip(self.angle)  # Rotate increment vector by player's angle
        new_pos = self.pos + inc  # Calculate new position

        if not self.check_collision(new_pos):  # Check for collisions
            self.pos = new_pos  # Update position if no collision

    def get_height(self):
        self.height = self.engine.bsp.get_subSector_height() + PLAYER_HEIGHT  # Update player's height based on subsector height

    def check_collision(self, new_pos):
        for seg in self.engine.bsp.segs:
            if seg.linedef.flags & self.engine.wad_data.LINEDEF_FLAGS['BLOCKING']:  # Check if the segment is blocking
                v1, v2 = seg.start_vertex, seg.end_vertex
                wall_vector = v2 - v1  # Vector representing the wall
                point_vector = new_pos - v1  # Vector from wall start to new position
                wall_length = wall_vector.length()  # Length of the wall
                projection = wall_vector.dot(point_vector) / wall_length  # Projection of point vector onto wall vector
                if 0 <= projection <= wall_length:
                    perpendicular_distance = abs(wall_vector.cross(point_vector) / wall_length)  # Perpendicular distance from point to wall
                    if perpendicular_distance < PLAYER_RADIUS:  # Check if within collision radius
                        return True
        return False  # No collision detected
