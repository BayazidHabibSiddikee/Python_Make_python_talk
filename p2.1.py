from turtle import *
from time import sleep
from tkinter import messagebox
from random import choice
import sys

class ConnectFour:
    def __init__(self):
        """Initialize the game"""
        # Setup screen
        self.screen = Screen()
        self.screen.setup(700, 600, 10, 70)
        self.screen.bgcolor('light yellow')
        self.screen.title("Connect Four in Turtle Graphics")
        
        # Setup main turtle
        hideturtle()
        tracer(False)
        
        # Game state
        self.turn = 'red'  # Red player moves first
        self.xs = [-300, -200, -100, 0, 100, 200, 300]  # X-coords of 7 columns
        self.ys = [-250, -150, -50, 50, 150, 250]  # Y-coords of 6 rows
        self.occupied = [list() for _ in range(7)]  # Track occupied cells
        self.validinputs = [1, 2, 3, 4, 5, 6, 7]  # Valid column inputs
        self.rounds = 1
        
        # Create animation turtle
        self.fall = Turtle()
        self.fall.up()
        self.fall.hideturtle()
        
        # Draw the board
        self.draw_board()
        
        # Setup click handler
        self.screen.onscreenclick(self.handle_click)
        self.screen.listen()
    
    def draw_board(self):
        """Draw the game board"""
        # Draw vertical lines
        pensize(5)
        for i in range(-250, 350, 100):
            up()
            goto(i, -350)
            down()
            goto(i, 350)
            up()
        
        # Draw horizontal lines
        pensize(1)
        pencolor('grey')
        for i in range(-200, 300, 100):
            up()
            goto(-350, i)
            down()
            goto(350, i)
            up()
        
        # Draw column numbers
        pencolor('black')
        col = 1
        for x in range(-300, 350, 100):
            up()
            goto(x, 270)
            write(col, font=('Arial', 20, 'normal'))
            col += 1
        
        update()
    
    def horizontal4(self, x, y, turn):
        """Check for 4 connected horizontally"""
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if (occupied[x+dif][y] == turn and 
                    occupied[x+dif+1][y] == turn and
                    occupied[x+dif+2][y] == turn and 
                    occupied[x+dif+3][y] == turn and 
                    x + dif >= 0):
                    win = True
            except IndexError:
                pass
        return win
    
    def vertical4(self, x, y, turn):
        """Check for 4 connected vertically"""
        win = False
        try:
            if (occupied[x][y] == turn and
                occupied[x][y-1] == turn and
                occupied[x][y-2] == turn and
                occupied[x][y-3] == turn and
                y-3 >= 0):
                win = True
        except IndexError:
            pass
        return win
    
    def forward4(self, x, y, turn):
        """Check for 4 connected diagonally (/)"""
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if (occupied[x+dif][y+dif] == turn and
                    occupied[x+dif+1][y+dif+1] == turn and
                    occupied[x+dif+2][y+dif+2] == turn and
                    occupied[x+dif+3][y+dif+3] == turn and
                    x+dif >= 0 and y+dif >= 0):
                    win = True
            except IndexError:
                pass
        return win
    
    def back4(self, x, y, turn):
        """Check for 4 connected diagonally (\)"""
        win = False
        for dif in (-3, -2, -1, 0):
            try:
                if (occupied[x+dif][y-dif] == turn and
                    occupied[x+dif+1][y-dif-1] == turn and
                    occupied[x+dif+2][y-dif-2] == turn and
                    occupied[x+dif+3][y-dif-3] == turn and
                    x+dif >= 0 and y-dif-3 >= 0):
                    win = True
            except IndexError:
                pass
        return win
    
    def win_game(self, col, row, turn):
        """Check if current move wins the game"""
        x = col - 1
        y = row - 1
        
        return (self.vertical4(x, y, turn) or 
                self.horizontal4(x, y, turn) or 
                self.forward4(x, y, turn) or 
                self.back4(x, y, turn))
    
    def animate_drop(self, col, row, color):
        """Animate disc falling"""
        if row <= 6:
            for i in range(6, row, -1):
                self.fall.goto(self.xs[col - 1], self.ys[i - 1])
                self.fall.dot(80, color)
                update()
                sleep(0.08)
                self.fall.clear()
    
    def place_disc(self, col, row, color):
        """Place a disc on the board"""
        up()
        goto(self.xs[col - 1], self.ys[row - 1])
        dot(80, color)
        self.occupied[col - 1].append(color)
        update()
    
    def check_game_end(self, col, row, player_name):
        """Check if game ended (win or tie)"""
        if self.win_game(col, row, self.turn):
            self.validinputs = []
            messagebox.showinfo("End Game", f'{player_name} ({self.turn}) Wins!!!')
            sys.exit()
        elif self.rounds == 42:
            messagebox.showinfo("Tie Game", "Game over, it's a tie!")
            sys.exit()
    
    def switch_turn(self):
        """Switch between red and yellow"""
        self.turn = 'yellow' if self.turn == 'red' else 'red'
    
    def make_move(self, col, player_name):
        """Execute a move for given column"""
        if col not in self.validinputs:
            messagebox.showerror("Error", "Sorry, that's an invalid move!")
            return False
        
        row = len(self.occupied[col - 1]) + 1
        
        if row > 6:
            return False
        
        # Animate and place disc
        self.animate_drop(col, row, self.turn)
        self.place_disc(col, row, self.turn)
        
        # Check game end
        self.check_game_end(col, row, player_name)
        
        # Update game state
        self.rounds += 1
        if len(self.occupied[col - 1]) == 6:
            self.validinputs.remove(col)
        
        self.switch_turn()
        return True
    
    def computer_move(self):
        """Computer makes a random valid move"""
        if len(self.validinputs) == 0:
            return
        
        col = choice(self.validinputs)
        self.make_move(col, "Computer")
    
    def handle_click(self, x, y):
        """Handle mouse click on the board"""
        # Check if click is within board
        if not (-350 < x < 350 and -350 < y < 350):
            print("You clicked outside the game board")
            return
        
        # Calculate column
        col = int((x + 350) // 100) + 1
        
        # Player's move
        if self.make_move(col, "Player"):
            # Computer's turn
            self.computer_move()
    
    def start(self):
        """Start the game loop"""
        self.screen.mainloop()


# Run the game
if __name__ == "__main__":
    game = ConnectFour()
    game.start()