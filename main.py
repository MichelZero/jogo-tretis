#!/usr/bin/env python3
"""
Tetris Game
Um jogo clássico de Tetris implementado em Python usando Pygame.

Para jogar:
1. Instale as dependências: pip install -r requirements.txt
2. Execute: python main.py

Controles:
- Setas ← → : Mover peça
- Seta ↓ : Queda rápida
- Seta ↑ : Rotacionar peça
- Espaço : Drop instantâneo
- P : Pausar/"Despausar"
- R : Reiniciar jogo
- ESC : Sair
"""

from game import Game

def main():
    """Função principal"""
    print("Iniciando Tetris...")
    print("Controles:")
    print("  ← → : Mover peça")
    print("  ↓ : Queda rápida")
    print("  ↑ : Rotacionar peça")
    print("  Espaço : Drop instantâneo")
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
