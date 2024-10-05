# Projeção 3D

Este projeto é um jogo de simulação de projeções em 3D. O jogador analisa como um objeto em um espaço tridimensional é projetado em uma tela bidimensional. O objetivo é ajudar o jogador a compreender a matemática por trás das projeções 3D em diferentes distâncias.

## Como funciona

O jogo utiliza **projeção em perspectiva**, onde objetos tridimensionais são projetados em uma tela 2D, semelhante à forma como uma câmera captura uma imagem. O usuário pode alterar a distância entre o objeto e a tela (pinhole), o que afeta a forma como o objeto é projetado.

### Funcionalidades principais:

- Projeção de objetos em diferentes distâncias.
- Interface visual usando Pygame para simular a visualização 2D de objetos 3D.
- Cálculo dinâmico das projeções em tempo real.
- Controle interativo via teclado para ajustar a visualização e projeções.

## Controles do jogo

O jogo permite que o jogador manipule as projeções utilizando as teclas do teclado. Aqui estão os controles disponíveis:

- **Tecla `W`**: Move o objeto para cima.
- **Tecla `S`**: Move o objeto para baixo.
- **Tecla `A`**: Move o objeto para a esquerda.
- **Tecla `D`**: Move o objeto para a direita.
- **Seta para cima (`↑`)**: Rotaciona o objeto no sentido horário.
- **Seta para baixo (`↓`)**: Rotaciona o objeto no sentido anti-horário.
- **Seta para esquerda (`←`)**: Rotaciona o objeto no sentido anti-horário.
- **Seta para direita (`→`)**: Rotaciona o objeto no sentido horário.


## Instalação

Para instalar o projeto localmente, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/aninhaabc/projecao.git
   cd projecao

2. **Instalar o jogo com 'pip'**
    ```bash
    pip install git+https://github.com/aninhaabc/projecao.git

3. **Executar o jogo**
    ```bash
    projecao

## Estrutura do projeto

- **`projecao/`**: Diretório contendo o código-fonte do jogo.
  - **`main.py`**: Arquivo principal do jogo. Responsável por carregar o ambiente e **rodar a lógica do jogo**.
  - **`transformations.py`**: Arquivo contendo as principais funções para criar as rotações nos eixos x, y e z.

- **`requirements.txt`**: Lista de dependências necessárias para rodar o projeto.
- **`setup.py`**: Arquivo de configuração para instalação do pacote.