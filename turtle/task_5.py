import turtle
import tkinter as tk
from tkinter import simpledialog


class Board:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(360, 360)
        self.screen.screensize(360, 360)

        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = self.choose_marker()

        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.width(1)
        self.draw_board()
        self.register_clicks()

        self.steps = 0

    def choose_marker(self):
        marker = self.screen.textinput("Выбор символа", "Выберите символ: 'X' (крестики) или 'O' (нолики)?")
        while marker not in ['X', 'O']:
            marker = self.screen.textinput("Выбор символа", "Пожалуйста, выберите 'X' или 'O': ")
        return marker.lower()

    def draw_row(self):
        for _ in range(3):
            for _ in range(4):
                self.t.forward(120)
                self.t.right(90)
            self.t.forward(120)

    def draw_board(self):
        self.t.penup()
        self.t.goto(-180, 180)
        self.t.pendown()
        for i in range(3):
            self.draw_row()
            self.t.penup()
            self.t.goto(-180, 180 - (i + 1) * 120)
            self.t.pendown()

    def register_clicks(self):
        self.screen.onclick(self.draw_figure)

    def draw_figure(self, x, y):
        row, col = self.get_row_col(x, y)
        if row is not None and col is not None and self.board[row][col] == ' ':
            winner = self.check_winner(self.board)
            if self.player == 'x':
                self.player = 'o'
                self.draw_x(row, col)
                self.board[row][col] = 'X'  # Метка крестика на доске
            else:
                self.player = 'x'
                self.draw_o(row, col)
                self.board[row][col] = 'O'  # Метка нолика на доске

            if winner:
                print(f"Победитель: {winner}")
                self.screen.bye()  # Закрыть окно игры
            else:
                print("Ничья или игра продолжается.")


    def draw_x(self, row, col):
        self.t.color('red')
        self.t.penup()
        self.t.goto(-180 + col * 120 + 63, 180 - row * 120 - 63)
        self.t.pendown()
        self.t.setheading(-45)
        self.t.forward(50)
        self.t.backward(100)
        self.t.forward(50)
        self.t.left(90)
        self.t.backward(50)
        self.t.forward(100)
        self.t.penup()

    def draw_o(self, row, col):
        self.t.color('green')
        self.t.penup()
        self.t.goto(-90 + col * 120 , 90 - row * 120)
        self.t.pendown()
        self.t.circle(45)
        self.t.penup()

    @staticmethod
    def get_row_col(x, y):
        if -180 <= x <= 180 and -180 <= y <= 180:
            row = int((180 - y) // 120)
            col = int((x + 180) // 120)
            return row, col
        return None, None

    def check_winner(self, board):
        self.steps += 1
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return board[i][0] 
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                return board[0][i]
        
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return board[0][0] 
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[0][2]

        if self.steps == 9:
            return 'friendship is winner'
        
        return None


game = Board()
turtle.done()
