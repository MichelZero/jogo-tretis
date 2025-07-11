# Guia de Desenvolvimento - Tetris

## 🔧 Configuração do Ambiente de Desenvolvimento

### Pré-requisitos
- Python 3.7+
- pip
- Git

### Configuração Inicial
```bash
# Clone o repositório
git clone https://github.com/MichelZero/jogo-tretis.git
cd jogo-tretis

# Criar ambiente virtual (recomendado)
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

## 📁 Arquitetura do Projeto

### Estrutura de Arquivos

- **`main.py`** - Ponto de entrada da aplicação
- **`game.py`** - Lógica principal do jogo (Game class)
- **`piece.py`** - Definição das peças e suas rotações (Piece class)
- **`config.py`** - Constantes e configurações globais

### Fluxo do Programa

1. **Inicialização** (`main.py`)
   - Configuração inicial
   - Criação da instância do jogo

2. **Loop Principal** (`game.py - Game.run()`)
   - Captura de eventos
   - Atualização do estado
   - Renderização

3. **Gerenciamento de Peças** (`piece.py`)
   - Criação de peças
   - Rotações
   - Posicionamento

## 🎮 Mecânicas do Jogo

### Sistema de Peças

Cada peça é definida por:
- **Forma**: Array 2D representando a peça
- **Rotações**: Diferentes orientações da peça
- **Cor**: Cor visual da peça
- **Posição**: Coordenadas x, y no grid

### Sistema de Pontuação

- **1 linha**: 100 × nível
- **2 linhas**: 300 × nível
- **3 linhas**: 500 × nível
- **4 linhas**: 800 × nível

### Progressão de Nível

- Nível aumenta a cada 10 linhas completadas
- Velocidade de queda aumenta com o nível
- Fórmula: `max(50, FALL_TIME - (level - 1) * 50)`

## 🔄 Funcionalidades Implementadas

### ✅ Básicas
- [x] Movimento de peças (esquerda, direita, baixo)
- [x] Rotação de peças
- [x] Detecção de colisão
- [x] Limpeza de linhas completas
- [x] Sistema de pontuação
- [x] Game Over
- [x] Reiniciar jogo

### ✅ Avançadas
- [x] Visualização da próxima peça
- [x] Sistema de níveis
- [x] Pausa
- [x] Drop instantâneo
- [x] Interface gráfica completa
- [x] Controles responsivos

### 🚀 Possíveis Melhorias

- [ ] Sons e música
- [ ] Efeitos visuais (partículas, animações)
- [ ] Sistema de high scores
- [ ] Diferentes modos de jogo
- [ ] Multiplayer
- [ ] Salvamento de progresso
- [ ] Configurações customizáveis
- [ ] Temas visuais

## 🧪 Testing

Para testar o jogo:

```bash
# Testar sintaxe
python -m py_compile *.py

# Executar o jogo
python main.py
```

### Casos de Teste Manuais

1. **Movimento das Peças**
   - Testar movimento para esquerda/direita
   - Verificar limitação nas bordas
   - Confirmar colisão com peças existentes

2. **Rotação**
   - Testar rotação em espaço livre
   - Verificar bloqueio próximo às bordas
   - Confirmar rotação próximo a outras peças

3. **Limpeza de Linhas**
   - Completar 1, 2, 3, 4 linhas simultaneamente
   - Verificar pontuação correta
   - Confirmar remoção das linhas

4. **Game Over**
   - Preencher o grid até o topo
   - Verificar detecção correta

## 📝 Padrões de Código

### Convenções de Nomenclatura
- **Classes**: PascalCase (`Game`, `Piece`)
- **Funções/Métodos**: snake_case (`move_piece`, `clear_lines`)
- **Constantes**: UPPER_CASE (`SCREEN_WIDTH`, `BLOCK_SIZE`)
- **Variáveis**: snake_case (`current_piece`, `fall_time`)

### Estrutura de Métodos
- Métodos públicos no início da classe
- Métodos privados (com _) no final
- Docstrings para métodos complexos

### Organização do Código
- Imports no topo
- Constantes após imports
- Classes com métodos organizados logicamente

## 🐛 Debug e Troubleshooting

### Problemas Comuns

1. **Pygame não encontrado**
   ```bash
   pip install pygame==2.5.2
   ```

2. **Erro de importação**
   - Verificar se todos os arquivos estão no mesmo diretório
   - Confirmar nome dos arquivos

3. **Performance**
   - Verificar FPS no config.py
   - Otimizar desenho apenas quando necessário

### Logs e Debug

Para adicionar logs de debug, adicione no início dos arquivos:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🔄 Workflow de Desenvolvimento

1. **Fazer alterações**
2. **Testar localmente**
3. **Commit com mensagem descritiva**
4. **Push para repositório**

### Mensagens de Commit
- `feat:` para novas funcionalidades
- `fix:` para correções de bugs
- `docs:` para documentação
- `refactor:` para refatoração
- `test:` para testes

## 📚 Recursos Adicionais

- [Documentação Pygame](https://www.pygame.org/docs/)
- [Python Official Docs](https://docs.python.org/3/)
- [Tetris Guidelines](https://tetris.fandom.com/wiki/Tetris_Guideline)
