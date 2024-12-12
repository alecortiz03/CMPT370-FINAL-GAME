# CMPT 370 - GROUP 2
# DoomEngine: A simple Doom-like game engine using Pygame

# H - uint16, h - int16, I - uint32, i - int32, c - char

class Sector:
    # Represents a sector in the game world
    __slots__ = [
        'floor_height',      # Floor height of the sector
        'ceiling_height',    # Ceiling height of the sector
        'floor_texture',     # Texture used for the floor
        'ceiling_texture',   # Texture used for the ceiling
        'light_level',       # Light level in the sector
        'type',              # Type of the sector
        'tag'                # Tag for identifying the sector
    ]

class Sidedef:
    # Represents a side definition in the game world
    __slots__ = [
        'x_offset',          # X offset for texture alignment
        'y_offset',          # Y offset for texture alignment
        'upper_texture',     # Texture for the upper part
        'lower_texture',     # Texture for the lower part
        'middle_texture',    # Texture for the middle part
        'sector_id'          # ID of the sector this sidedef belongs to
    ]
    __slots__ += ['sector']  # Reference to the sector object

class Thing:
    # Represents an object or entity in the game world
    # 10 bytes
    __slots__ = [
        'pos',               # Position (pos.x, pos.y - 4h)
        'angle',             # Angle (2H)
        'type',              # Type of the thing (2H)
        'flags'              # Flags (2H)
    ]

class Seg:
    # Represents a segment in the game world
    # 12 bytes = 2h x 6
    __slots__ = [
        'start_vertex_id',   # ID of the start vertex
        'end_vertex_id',     # ID of the end vertex
        'angle',             # Angle of the segment
        'linedef_id',        # ID of the linedef
        'direction',         # Direction of the segment
        'offset',            # Offset of the segment
    ]
    __slots__ += ['start_vertex', 'end_vertex', 'linedef', 'front_sector', 'back_sector']  # References to related objects

class SubSector:
    # Represents a subsector in the game world
    # 4 bytes = 2h + 2h
    __slots__ = [
        'seg_count',         # Number of segments in the subsector
        'first_seg_id'       # ID of the first segment
    ]

class Node:
    # Represents a node in the BSP tree
    # 28 bytes = 2h x 12 + 2H x 2

    class BBox:
        # Represents a bounding box
        __slots__ = ['top', 'bottom', 'left', 'right']  # Boundaries of the bounding box

    __slots__ = [
        'x_partition',       # X coordinate of the partition line
        'y_partition',       # Y coordinate of the partition line
        'dx_partition',      # Delta X of the partition line
        'dy_partition',      # Delta Y of the partition line
        'bbox',              # Bounding box (8h)
        'front_child_id',    # ID of the front child node
        'back_child_id',     # ID of the back child node
    ]
    def __init__(self):
        self.bbox = {'front': self.BBox(), 'back': self.BBox()}  # Initialize bounding boxes for front and back

class Lindedef:
    # Represents a linedef in the game world
    # 14 bytes = 2H x 7
    __slots__ = [
        'start_vertex_id',   # ID of the start vertex
        'end_vertex_id',     # ID of the end vertex
        'flags',             # Flags for the linedef
        'line_type',         # Type of the linedef
        'sector_tag',        # Tag for identifying the sector
        'front_sidedef_id',  # ID of the front sidedef
        'back_sidedef_id'    # ID of the back sidedef
    ]
    __slots__ += ['front_sidedef', 'back_sidedef']  # References to the front and back sidedefs