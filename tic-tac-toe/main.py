import pygame as pg
import math
 
#cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
cinza = (155, 155, 155)

window = pg.display.set_mode((1000,600))
window.fill(branco)

#ininciando fonte
pg.font.init()
#escolhendo a fonte e definindo tamanho
font = pg.font.SysFont("Arial", 30)
board_array = [['n',"n","n"],['n',"n","n"],['n',"n","n"]]

#variavel de clique
click_last_status = 0
#variavel de click on e off
click_on_off = 0
#posição do clique
click_posicion_x = -1
click_posicion_y = -1
#X ou O 
X_or_O_turn = 'x'
#end game
end_game = 0

def grade_no_tabuleiro(window):
    pg.draw.line(window, preto, (205,0),(205,600), 10)
    pg.draw.line(window, preto, (405,0),(405,600), 10)
    pg.draw.line(window, preto, (0,205),(600,205), 10)
    pg.draw.line(window, preto, (0,405),(600,405), 10)

def click_logic(click_on_off, click_last_status, x, y):
    if click[0] == 0 and click_last_status == 1:
        click_on_off = 1
        x = (math.ciel(mouse[0] / 200) - 1)
        y = (math.ciel(mouse[1] / 200) - 1)
    elif click[0] == 0 and click_last_status == 0:
        click_on_off = 0
        x = -1
        y = -1
    return click_on_off, click_last_status, x, y

def draw_selected_cell(window, board_array):
    for n in range(3):
        for nn in range(3):
            if board_array[nn][n] == 'x':
                jogador_x(window, n, nn)
            elif board_array[nn][n] == 'o':
                jogador_o(window, n, nn)
            else:
                pass

def board_array_data(board_array, X_or_O_turn, x, y):
    if x < 3 and y < 3:
        if X_or_O_turn == 'x' and board_array[y][x] == 'n' and x != -1 and end_game == 0:
            board_array[y][x] = 'x'
            X_or_O_turn = 'o'
        if X_or_O_turn == 'o' and board_array[y][x] == 'n' and x != -1 and end_game == 0:
            board_array[y][x] = 'o'
            X_or_O_turn = 'x'
        return board_array, X_or_O_turn

def win_line(window, board_array, end_game, X_or_O_turn):
    if board_array[0][0] == 'x' and board_array[0][1] == 'x' and board_array[0][2] == 'x' or board_array[0][0] == 'o' and board_array[0][1] == 'o' and board_array[0][2] == 'o':
        pg.draw.line(window, verde, (30, 100), (570, 100), 10)
        end_game = 1
    elif board_array[1][0] == 'x' and board_array[1][1] == 'x' and board_array[1][2] == 'x' or board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[0][2] == 'o':
        pg.draw.line(window, verde, (30, 300), (570, 300), 10)
        end_game = 1
    elif board_array[2][0] == 'x' and board_array[2][1] == 'x' and board_array[2][2] == 'x' or board_array[2][0] == 'o' and board_array[2][1] == 'o' and board_array[2][2] == 'o':
        pg.draw.line(window, verde, (30, 500), (570, 500), 10)
        end_game = 1
    elif board_array[0][0] == 'x' and board_array[1][0] == 'x' and board_array[2][0] == 'x' or board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[0][2] == 'o':
        pg.draw.line(window, verde, (30, 300), (570, 300), 10)
        end_game = 1
    elif board_array[0][1] == 'x' and board_array[1][1] == 'x' and board_array[2][1] == 'x' or board_array[0][0] == 'o' and board_array[0][1] == 'o' and board_array[0][2] == 'o':
        pg.draw.line(window, verde, (30, 100), (570, 100), 10)
        end_game = 1
    elif board_array[0][2] == 'x' and board_array[1][1] == 'x' and board_array[2][2] == 'x' or board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[0][2] == 'o':
        pg.draw.line(window, verde, (30, 300), (570, 300), 10)
        end_game = 1
    elif board_array[0][0] == 'x' and board_array[1][1] == 'x' and board_array[2][2] == 'x' or board_array[0][0] == 'o' and board_array[0][1] == 'o' and board_array[0][2] == 'o':
        pg.draw.line(window, verde, (30, 100), (570, 100), 10)
        end_game = 1
    elif board_array[2][0] == 'x' and board_array[1][1] == 'x' and board_array[0][2] == 'x' or board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[0][2] == 'o':
        pg.draw.line(window, verde, (30, 300), (570, 300), 10)
        end_game = 1

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    #declarando variavel da posição do mouse
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    #declarando variavel do click
    click = pg.mouse.get_pressed()

    #jogo
    grade_no_tabuleiro(window)
    click_on_off, click_last_status, click_position_x, click_position_y = click_logic(click_on_off, click_last_status, click_position_x, click_position_y)
    board_array, X_or_O_turn = board_array_data(board_array, X_or_O_turn, x, y)

    #Status do ultimo clique
    if click[0] == 1:
        click_last_status = 1
    else:
        click_last_status = 0

    pg.display.update()