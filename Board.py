# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:40:28 2024

@author: samso
"""

class Board:
    
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = {1: 'X', 2: 'O'}
        self.current_player = 1
        self.winner = None
        
    def setPlayer(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
            
    def getPlayer(self):
        return self.current_player
    
    def setWinner(self):
        for i in range(3):
            #check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.winner = self.current_player
            #check columns
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                self.winner = self.current_player
                
        #check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = self.current_player
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = self.current_player
        
    def getWinner(self):
        return self.winner
    
    def setTile(self, row: int, col: int):
        if (self.current_player == 1):
            self.board[row][col] = 'X'
        else:
            self.board[row][col] = 'O'
            
    def getTile(self, row: int, col: int):
        return self.board[row][col]