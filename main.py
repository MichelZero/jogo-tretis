#!/usr/bin/env python3
# para gerar os caracteres corretamente, use utf-8
# -*- coding: utf-8 -*-
"""
Tetris Game
Um jogo clássico de Tetris implementado em Python usando Pygame.

Para jogar:
1. Instale as dependências: pip install -r requirements.txt
2. Execute: python main.py

Controles:
- WASD ou Setas: Mover e rotacionar peça
- Seta para baixo ou S: Queda rápida
- Seta para cima ou W: Rotacionar peça
- Espaço : Drop instantâneo
- P : Pausar/Despausar
- R : Reiniciar jogo
- ESC : Sair
"""

from game import Game

def main():
    """Função principal"""
    print("Iniciando Tetris...")
    print("Controles:")
    print("  WASD ou Setas : Mover/Rotacionar")
    print("  S ou Seta Baixo : Queda rapida")
    print("  W ou Seta Cima : Rotacionar peca")
    print("  Espaco : Drop instantaneo")
    print("  P : Pausar/Despausar")
    print("  R : Reiniciar jogo")
    print("  ESC : Sair")
    print()
    
    # Criar e executar o jogo
    game = Game()
    game.run()
    
    print("Obrigado por jogar!")

if __name__ == "__main__":
    main()
