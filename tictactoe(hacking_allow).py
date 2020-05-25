# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 03:06:49 2020

@author: Duong Vu Tuan Minh
@content: Tic Tac Toe game(project 3)
"""

from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7]+" | "+board[8]+" | "+board[9])
    print(board[4]+" | "+board[5]+" | "+board[6])
    print(board[1]+" | "+board[2]+" | "+board[3])

def player_input():
    marker = ""
    while marker != "X" and marker != "O":
        print("Choose X or O: \n")
        marker = input().upper()
        
    player1 = marker
    
    if player1 == "X":
        player2 = "O"
    else: 
        player2 = "X"
        
    return (player1,player2)


#(player1,player2) = player_input()
    
def play_marker(board, player, position):
    board[int(position)] = str(player)
    display_board(board)

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
def switch_turn(player):
    if player =="X":
        player = "O"
    else:
        player = "X"
    return player
        
def player_go_first(p1,p2):
    marker = ""
    list_of_players = ['p1','p2']
    choice = random.choice(list_of_players)
    if choice == "p1":
        print("Player with maker X will go first")
        marker = "X"
    else:
        print("Player with maker O will go first")
        marker = "O"
    return marker
def space_check(board,position):
    return board[position] == " "

def check_full_board(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

        
#return True must be line up with the for statement, because it need to finish checking
#all the space in the board, if we put it align with the if statement nested inside the for
#loop the after 1 move, the game will be draw!!!

def main():
    current_board = [" "]*10
    game_on = True
    (player1,player2) = player_input()
    player = player_go_first(player1,player2)
    
    while game_on:
        if player == "X":
            print("Player with marker X please go!")   
            move = input()
            play_marker(current_board, player, move)
                
            if win_check(current_board,player):
                print(f"Player with marker X has won the game")
                game_on = False
            else:
                if check_full_board(current_board):
                    print("Draw!")
                    game_on = False
                else:
                    player = "O"
        else:
            print("Player with marker O please go!")
            move = ""
            move = input()
            play_marker(current_board, player, move)
                
            if win_check(current_board,player):
                print(f"Player with marker Y has won the game")
                game_on = False
            else:
                if check_full_board(current_board):
                    print("Draw!")
                    game_on = False
                else:
                    player = "X"
    
main()
        
    

        