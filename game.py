# para gerar os caracteres corretamente, use utf-8
# -*- coding: utf-8 -*-

import pygame
import random
from config import *
from piece import Piece

class Game:
    def __init__(self):
        # Inicializar pygame
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        
        # Grid do jogo
        self.grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        
        # Peça atual e próxima
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        
        # Tempo e pontuação
        self.fall_time = 0
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        
        # Estado do jogo
        self.game_over = False
        self.paused = False
        
        # Font para texto
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

    def new_piece(self):
        """Cria uma nova peça aleatória"""
        piece = Piece(GRID_WIDTH // 2 - 2, 0)
        piece.shape = random.randint(0, len(Piece.SHAPES) - 1)
        piece.color = PIECE_COLORS[piece.shape]
        return piece

    def is_valid_position(self, piece, dx=0, dy=0, rotation=None):
        """Verifica se a posição da peça é válida"""
        test_piece = piece.copy()
        test_piece.x += dx
        test_piece.y += dy
        
        if rotation is not None:
            test_piece.rotation = rotation
        
        blocks = test_piece.get_blocks()
        
        for x, y in blocks:
            # Verifica limites
            if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT:
                return False
            
            # Verifica colisão com blocos existentes
            if y >= 0 and self.grid[y][x] != BLACK:
                return False
        
        return True

    def place_piece(self, piece):
        """Coloca a peça no grid"""
        blocks = piece.get_blocks()
        for x, y in blocks:
            if y >= 0:
                self.grid[y][x] = piece.color

    def clear_lines(self):
        """Remove linhas completas e retorna o número de linhas removidas"""
        lines_to_clear = []
        
        for y in range(GRID_HEIGHT):
            if all(self.grid[y][x] != BLACK for x in range(GRID_WIDTH)):
                lines_to_clear.append(y)
        
        for y in lines_to_clear:
            del self.grid[y]
            self.grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])
        
        lines_cleared = len(lines_to_clear)
        if lines_cleared > 0:
            # Atualizar pontuação
            points = [0, 100, 300, 500, 800][lines_cleared]
            self.score += points * self.level
            self.lines_cleared += lines_cleared
            
            # Aumentar nível a cada 10 linhas
            self.level = self.lines_cleared // 10 + 1
        
        return lines_cleared

    def check_game_over(self):
        """Verifica se o jogo acabou"""
        return not self.is_valid_position(self.current_piece)

    def move_piece(self, dx, dy):
        """Move a peça se possível"""
        if self.is_valid_position(self.current_piece, dx, dy):
            self.current_piece.x += dx
            self.current_piece.y += dy
            return True
        return False

    def rotate_piece(self):
        """Rotaciona a peça se possível"""
        new_rotation = (self.current_piece.rotation + 1) % len(Piece.SHAPES[self.current_piece.shape])
        if self.is_valid_position(self.current_piece, rotation=new_rotation):
            self.current_piece.rotation = new_rotation
            return True
        return False

    def drop_piece(self):
        """Faz a peça cair uma posição"""
        if not self.move_piece(0, 1):
            # Peça não pode mais cair
            self.place_piece(self.current_piece)
            self.clear_lines()
            
            # Nova peça
            self.current_piece = self.next_piece
            self.next_piece = self.new_piece()
            
            # Verificar game over
            if self.check_game_over():
                self.game_over = True

    def hard_drop(self):
        """Faz a peça cair instantaneamente"""
        while self.move_piece(0, 1):
            pass
        self.drop_piece()

    def update(self, dt):
        """Atualiza o estado do jogo"""
        if self.game_over or self.paused:
            return
        
        self.fall_time += dt
        fall_speed = max(50, FALL_TIME - (self.level - 1) * 50)
        
        if self.fall_time >= fall_speed:
            self.drop_piece()
            self.fall_time = 0

    def draw_grid(self):
        """Desenha o grid do jogo"""
        grid_x = 50
        grid_y = 50
        
        # Desenhar blocos do grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(
                    grid_x + x * BLOCK_SIZE,
                    grid_y + y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE
                )
                pygame.draw.rect(self.screen, self.grid[y][x], rect)
                pygame.draw.rect(self.screen, WHITE, rect, 1)
        
        # Desenhar peça atual
        if not self.game_over:
            blocks = self.current_piece.get_blocks()
            for x, y in blocks:
                if 0 <= x < GRID_WIDTH and y >= 0:
                    rect = pygame.Rect(
                        grid_x + x * BLOCK_SIZE,
                        grid_y + y * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE
                    )
                    pygame.draw.rect(self.screen, self.current_piece.color, rect)
                    pygame.draw.rect(self.screen, WHITE, rect, 1)

    def draw_next_piece(self):
        """Desenha a próxima peça"""
        next_x = 400
        next_y = 100
        
        # Título
        text = self.font.render("Proxima:", True, WHITE)
        self.screen.blit(text, (next_x, next_y - 30))
        
        # Desenhar próxima peça
        shape = self.next_piece.get_rotated_shape()
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell == '#':
                    rect = pygame.Rect(
                        next_x + j * 20,
                        next_y + i * 20,
                        20,
                        20
                    )
                    pygame.draw.rect(self.screen, self.next_piece.color, rect)
                    pygame.draw.rect(self.screen, WHITE, rect, 1)

    def draw_info(self):
        """Desenha informações do jogo"""
        info_x = 400
        info_y = 250
        
        # Pontuação
        score_text = self.font.render(f"Pontos: {self.score}", True, WHITE)
        self.screen.blit(score_text, (info_x, info_y))
        
        # Linhas
        lines_text = self.font.render(f"Linhas: {self.lines_cleared}", True, WHITE)
        self.screen.blit(lines_text, (info_x, info_y + 40))
        
        # Nível
        level_text = self.font.render(f"Nível: {self.level}", True, WHITE)
        self.screen.blit(level_text, (info_x, info_y + 80))
        
        # Controles
        controls_y = info_y + 150
        controls = [
            "Controles:",
            "A/D ou Setas: Mover",
            "S ou Seta: Queda rapida",
            "W ou Seta: Rotacionar",
            "Espaco: Drop",
            "P: Pausar",
            "R: Reiniciar"
        ]
        
        for i, control in enumerate(controls):
            if i == 0:
                text = self.font.render(control, True, WHITE)
            else:
                text = self.small_font.render(control, True, WHITE)
            self.screen.blit(text, (info_x, controls_y + i * 25))

    def draw_game_over(self):
        """Desenha a tela de game over"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Texto de game over
        game_over_text = self.font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(game_over_text, text_rect)
        
        # Pontuação final
        final_score = self.font.render(f"Pontuação Final: {self.score}", True, WHITE)
        score_rect = final_score.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(final_score, score_rect)
        
        # Instrução para reiniciar
        restart_text = self.small_font.render("Pressione R para reiniciar ou ESC para sair", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)

    def draw_pause(self):
        """Desenha a tela de pausa"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font.render("PAUSADO", True, YELLOW)
        text_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(pause_text, text_rect)
        
        continue_text = self.small_font.render("Pressione P para continuar", True, WHITE)
        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
        self.screen.blit(continue_text, continue_rect)

    def draw(self):
        """Desenha tudo na tela"""
        self.screen.fill(BLACK)
        
        self.draw_grid()
        self.draw_next_piece()
        self.draw_info()
        
        if self.game_over:
            self.draw_game_over()
        elif self.paused:
            self.draw_pause()
        
        pygame.display.flip()

    def restart(self):
        """Reinicia o jogo"""
        self.grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.fall_time = 0
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        self.game_over = False
        self.paused = False

    def handle_events(self):
        """Gerencia eventos do pygame"""
        keys_pressed = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                
                elif event.key == pygame.K_r:
                    self.restart()
                
                elif event.key == pygame.K_p:
                    if not self.game_over:
                        self.paused = not self.paused
                
                elif not self.game_over and not self.paused:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.move_piece(-1, 0)
                    
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.move_piece(1, 0)
                    
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.move_piece(0, 1)
                    
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.rotate_piece()
                    
                    elif event.key == pygame.K_SPACE:
                        self.hard_drop()
        
        return True

    def run(self):
        """Loop principal do jogo"""
        running = True
        
        while running:
            dt = self.clock.tick(FPS)
            
            running = self.handle_events()
            self.update(dt)
            self.draw()
        
        pygame.quit()
