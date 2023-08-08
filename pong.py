import os
import time
import random

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def draw_game(ball_pos, paddle_left, paddle_right):
    clear_screen()
    game_board = [[' ' for _ in range(40)] for _ in range(20)]
    game_board[ball_pos[1]][ball_pos[0]] = 'O'
    for y in range(paddle_left[1] - 1, paddle_left[1] + 2):
        game_board[y][paddle_left[0]] = '|'
    for y in range(paddle_right[1] - 1, paddle_right[1] + 2):
        game_board[y][paddle_right[0]] = '|'

    for row in game_board:
        print(''.join(row))
    print("-" * 40)

def main():
    ball_pos = [20, 10]
    ball_velocity = [1, 1]
    paddle_left = [0, 9]
    paddle_right = [39, 9]

    while True:
        draw_game(ball_pos, paddle_left, paddle_right)

        if ball_pos[1] == 0 or ball_pos[1] == 19:
            ball_velocity[1] *= -1

        if ball_pos[0] == 0:
            if paddle_left[1] - 1 <= ball_pos[1] <= paddle_left[1] + 1:
                ball_velocity[0] *= -1
            else:
                print("Game Over! Right player wins!")
                break
        elif ball_pos[0] == 39:
            if paddle_right[1] - 1 <= ball_pos[1] <= paddle_right[1] + 1:
                ball_velocity[0] *= -1
            else:
                print("Game Over! Left player wins!")
                break

        ball_pos[0] += ball_velocity[0]
        ball_pos[1] += ball_velocity[1]

        if ball_pos[0] < 20:
            if ball_pos[1] < paddle_left[1]:
                paddle_left[1] -= 1
            elif ball_pos[1] > paddle_left[1]:
                paddle_left[1] += 1
        else:
            if paddle_right[1] < ball_pos[1]:
                paddle_right[1] += 1
            elif paddle_right[1] > ball_pos[1]:
                paddle_right[1] -= 1

        time.sleep(0.1)

if __name__ == '__main__':
    main()

