#!/usr/bin/env python3
"""
Script de teste para verificar se o jogo Tetris está funcionando corretamente.
Este script não executa o jogo completo, mas testa as funcionalidades principais.
"""

import sys
import os

# Adicionar o diretório atual ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Testa se todos os módulos podem ser importados"""
    print("🔍 Testando imports...")
    try:
        import pygame
        print("✅ pygame importado com sucesso")
        
        import config
        print("✅ config.py importado com sucesso")
        
        from piece import Piece
        print("✅ piece.py importado com sucesso")
        
        from game import Game
        print("✅ game.py importado com sucesso")
        
        return True
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        return False

def test_piece_creation():
    """Testa a criação de peças"""
    print("\n🎮 Testando criação de peças...")
    try:
        from piece import Piece
        
        # Criar uma peça
        piece = Piece(5, 0)
        piece.shape = 0  # Peça I
        
        # Testar métodos básicos
        blocks = piece.get_blocks()
        print(f"✅ Peça criada com {len(blocks)} blocos")
        
        # Testar rotação
        original_rotation = piece.rotation
        piece.rotate()
        new_rotation = piece.rotation
        print(f"✅ Rotação testada: {original_rotation} -> {new_rotation}")
        
        # Testar cópia
        copied_piece = piece.copy()
        print("✅ Cópia de peça funcionando")
        
        return True
    except Exception as e:
        print(f"❌ Erro nos testes de peça: {e}")
        return False

def test_game_initialization():
    """Testa a inicialização do jogo (sem interface gráfica)"""
    print("\n🎯 Testando inicialização do jogo...")
    try:
        import pygame
        
        # Inicializar pygame sem display (modo headless)
        pygame.init()
        
        # Verificar se pygame foi inicializado
        if pygame.get_init():
            print("✅ Pygame inicializado com sucesso")
        
        pygame.quit()
        print("✅ Pygame finalizado com sucesso")
        
        return True
    except Exception as e:
        print(f"❌ Erro na inicialização: {e}")
        return False

def test_config():
    """Testa as configurações"""
    print("\n⚙️ Testando configurações...")
    try:
        import config
        
        # Verificar se as constantes estão definidas
        required_constants = [
            'SCREEN_WIDTH', 'SCREEN_HEIGHT', 'GRID_WIDTH', 'GRID_HEIGHT',
            'BLOCK_SIZE', 'BLACK', 'WHITE', 'PIECE_COLORS', 'FPS'
        ]
        
        for constant in required_constants:
            if hasattr(config, constant):
                value = getattr(config, constant)
                print(f"✅ {constant}: {value}")
            else:
                print(f"❌ Constante {constant} não encontrada")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Erro nas configurações: {e}")
        return False

def test_piece_shapes():
    """Testa se todas as formas de peças estão definidas"""
    print("\n🔧 Testando formas das peças...")
    try:
        from piece import Piece
        
        # Verificar se todas as 7 peças estão definidas
        expected_pieces = 7
        if len(Piece.SHAPES) == expected_pieces:
            print(f"✅ Todas as {expected_pieces} peças estão definidas")
        else:
            print(f"❌ Esperado {expected_pieces} peças, encontrado {len(Piece.SHAPES)}")
            return False
        
        # Testar cada peça
        for i, shape_rotations in enumerate(Piece.SHAPES):
            print(f"✅ Peça {i}: {len(shape_rotations)} rotações")
        
        return True
    except Exception as e:
        print(f"❌ Erro nas formas das peças: {e}")
        return False

def run_all_tests():
    """Executa todos os testes"""
    print("🚀 Iniciando testes do Tetris...")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_config,
        test_piece_shapes,
        test_piece_creation,
        test_game_initialization
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        else:
            break
    
    print("\n" + "=" * 50)
    print(f"📊 Resultado: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! O jogo está pronto para ser executado.")
        print("\n🎮 Para jogar, execute: python main.py")
        return True
    else:
        print("⚠️ Alguns testes falharam. Verifique as dependências e arquivos.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
