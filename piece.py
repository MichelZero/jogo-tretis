import pygame
from config import *

class Piece:
    # Formas das peças (cada peça tem 4 rotações possíveis)
    SHAPES = [
        # I - Linha
        [
            ['.....',
             '..#..',
             '..#..',
             '..#..',
             '..#..'],
            ['.....',
             '.....',
             '####.',
             '.....',
             '.....'],
        ],
        # J
        [
            ['.....',
             '.#...',
             '.###.',
             '.....',
             '.....'],
            ['.....',
             '..##.',
             '..#..',
             '..#..',
             '.....'],
            ['.....',
             '.....',
             '.###.',
             '...#.',
             '.....'],
            ['.....',
             '..#..',
             '..#..',
             '.##..',
             '.....'],
        ],
        # L
        [
            ['.....',
             '...#.',
             '.###.',
             '.....',
             '.....'],
            ['.....',
             '..#..',
             '..#..',
             '..##.',
             '.....'],
            ['.....',
             '.....',
             '.###.',
             '.#...',
             '.....'],
            ['.....',
             '.##..',
             '..#..',
             '..#..',
             '.....'],
        ],
        # O - Quadrado
        [
            ['.....',
             '.....',
             '.##..',
             '.##..',
             '.....'],
        ],
        # S
        [
            ['.....',
             '.....',
             '.##..',
             '##...',
             '.....'],
            ['.....',
             '.#...',
             '.##..',
             '..#..',
             '.....'],
        ],
        # T
        [
            ['.....',
             '.....',
             '.#...',
             '###..',
             '.....'],
            ['.....',
             '.....',
             '.#...',
             '.##..',
             '.#...'],
            ['.....',
             '.....',
             '.....',
             '###..',
             '.#...'],
            ['.....',
             '.....',
             '.#...',
             '##...',
             '.#...'],
        ],
        # Z
        [
            ['.....',
             '.....',
             '##...',
             '.##..',
             '.....'],
            ['.....',
             '..#..',
             '.##..',
             '.#...',
             '.....'],
        ],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = 0  # Índice da forma
        self.rotation = 0
        self.color = PIECE_COLORS[self.shape]

    def get_rotated_shape(self):
        """Retorna a forma atual com a rotação atual"""
        return self.SHAPES[self.shape][self.rotation % len(self.SHAPES[self.shape])]

    def rotate(self):
        """Rotaciona a peça"""
        self.rotation = (self.rotation + 1) % len(self.SHAPES[self.shape])

    def get_blocks(self):
        """Retorna as posições dos blocos da peça"""
        blocks = []
        shape = self.get_rotated_shape()
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell == '#':
                    blocks.append((self.x + j, self.y + i))
        return blocks

    def copy(self):
        """Cria uma cópia da peça"""
        new_piece = Piece(self.x, self.y)
        new_piece.shape = self.shape
        new_piece.rotation = self.rotation
        new_piece.color = self.color
        return new_piece
