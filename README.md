# 🎮 Tetris Game

Um jogo clássico de Tetris implementado em Python usando Pygame.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-v2.5.2-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📋 Características

- ✨ Gráficos coloridos e suaves
- 🎯 Sistema de pontuação completo
- 📊 Níveis progressivos de dificuldade
- ⏸️ Função de pausa
- 🔄 Opção de reiniciar
- 🎮 Controles intuitivos
- 📱 Interface limpa e moderna

## 🎯 Como Jogar

O objetivo é completar linhas horizontais movendo e rotacionando as peças que caem. Quando uma linha é completada, ela desaparece e você ganha pontos!

### 🕹️ Controles

| Tecla | Ação |
|-------|------|
| `←` `→` | Mover peça para esquerda/direita |
| `↓` | Queda rápida |
| `↑` | Rotacionar peça |
| `Espaço` | Drop instantâneo |
| `P` | Pausar/Despausar |
| `R` | Reiniciar jogo |
| `ESC` | Sair do jogo |

### 🏆 Sistema de Pontuação

- **1 linha**: 100 × nível
- **2 linhas**: 300 × nível  
- **3 linhas**: 500 × nível
- **4 linhas (Tetris)**: 800 × nível

O nível aumenta a cada 10 linhas completadas, tornando o jogo mais rápido e desafiador!

## 🚀 Instalação e Execução

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Passos

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/MichelZero/jogo-tretis.git
   cd jogo-tretis
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o jogo:**

   ```bash
   python main.py
   ```

## 📁 Estrutura do Projeto

```text
jogo-tretis/
├── main.py           # Arquivo principal para executar o jogo
├── game.py           # Lógica principal do jogo
├── piece.py          # Definição das peças do Tetris
├── config.py         # Configurações e constantes
├── requirements.txt  # Dependências do projeto
├── README.md         # Este arquivo
└── LICENSE          # Licença do projeto
```

## 🎨 Capturas de Tela

### Tela Principal

- Grid de jogo 10×20
- Visualização da próxima peça
- Informações de pontuação, linhas e nível
- Controles exibidos na tela

### Recursos Visuais

- Peças coloridas diferentes para cada tipo
- Animações suaves
- Interface clara e organizada
- Feedback visual imediato

## 🔧 Configuração

Você pode personalizar o jogo editando o arquivo `config.py`:

- **Dimensões da tela**: `SCREEN_WIDTH`, `SCREEN_HEIGHT`
- **Tamanho do grid**: `GRID_WIDTH`, `GRID_HEIGHT`
- **Tamanho dos blocos**: `BLOCK_SIZE`
- **Cores das peças**: `PIECE_COLORS`
- **Velocidade**: `FALL_TIME`, `FAST_FALL_TIME`

## 🎮 Tipos de Peças

O jogo inclui todas as 7 peças clássicas do Tetris:

- **I** (Linha) - Ciano
- **J** (L invertido) - Azul
- **L** (L normal) - Laranja  
- **O** (Quadrado) - Amarelo
- **S** (Z invertido) - Verde
- **T** (T) - Roxo
- **Z** (Z normal) - Vermelho

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abrir um Pull Request

## 🐛 Reportar Bugs

Se encontrar algum bug, por favor abra uma [issue](https://github.com/MichelZero/jogo-tretis/issues) descrevendo:

- O que você estava fazendo
- O que deveria acontecer
- O que realmente aconteceu
- Passos para reproduzir o bug

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

Michel Zero

- GitHub: [@MichelZero](https://github.com/MichelZero)

## 🙏 Agradecimentos

- Pygame community pela excelente biblioteca
- Alexey Pajitnov pelo jogo original Tetris
- Todos os contribuidores e testadores

---

⭐ Se você gostou do projeto, não esqueça de dar uma estrela no repositório!
jogo-tretis
