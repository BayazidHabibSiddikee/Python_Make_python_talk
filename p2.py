import time, threading, random, sys, arrow
import turtle as t
from tkinter import messagebox

class GuessTheWordGame:
    def __init__(self):
        """Initialize the Guess the Word game"""
        # Word list
        self.words = [
            "nice","want","have","need","wish","give","take","love","care","help",
            "hold","keep","know","send","make","find","feel","look","show","move",
            "live","stay","join","play","work","read","talk","hear","plan","hope",
            "deal","lead","grow","rise","fall","meet","save","open","shut","turn",
            "stop","wait","walk","jump","rest","pick","push","pull","pack","pass",
            "sign","test","call","cook","bake","wash","boil","flip","stir","pour",
            "peel","feed","lift","sort","draw","type","edit","sing","snap","film",
            "zoom","chat","mail","link","code","load","sync","view","copy","clip",
            "text","post","roll","spin","calm","kind","fair","good","fine","pure",
            "true","easy","fast","slow","soft","hard","busy","cool","warm","mild",
            "bold","cute","neat","sure","okay","able","just","even","else","only",
            "some","many","more","less","most","ever","once","then","when","soon",
            "later","here","away","down","back","over","into","onto","from","with",
            "amid","upon","near","side","area","line","part","item","unit","word",
            "gate","door","room","hall","yard","park","lake","tree","rock","road",
            "path","hill","farm","ship","boat","crew","port","zone","city","town",
            "site","shop","bank","mall","home","desk","seat","lamp","wire","pipe",
            "wall","roof","tile","belt","ring","tool","card","note","form","file",
            "data","info","page","user","name","like","tell","warn"
        ]
        
        # Setup screen
        self.screen = t.Screen()
        self.screen.bgcolor("lavender")
        self.screen.setup(600, 500)
        t.hideturtle()
        t.tracer(False)
        t.up()
        
        # Create drawing turtle
        self.drawer = t.Turtle()
        self.drawer.hideturtle()
        self.drawer.up()
        
        # Game state
        self.word = ""
        self.score = 6
        self.missed = []
        self.right = []
        self.circles = []
        self.title_thread = None
        self.running = True
    
    def update_title(self):
        """Update title with time and hints"""
        while self.running:
            current_time = arrow.now().format('h:mm A')
            hint1 = random.choice(self.words)
            hint2 = random.choice(self.words)
            t.title(f"Guess the Word Game   |   {current_time}  |  Hint1: {hint1}    |   Hint2: {hint2}")
            time.sleep(1)
    
    def show_intro(self):
        """Display introduction messages"""
        messages = [
            ("Welcome to the Guess the Word Game!", ("Arial", 20, "bold"), 2),
            ("Try to guess the 4-letter word!", ("Arial", 16, "normal"), 2),
            ("You have 6 attempts. Good luck!", ("Arial", 16, "normal"), 2)
        ]
        
        for msg, font, delay in messages:
            t.goto(-270, 200)
            t.write(msg, font=font)
            t.update()
            time.sleep(delay)
            t.clear()
    
    def draw_blanks(self):
        """Draw blank lines for each letter"""
        for i in range(len(self.word)):
            self.drawer.goto(-270 + 150 * i, -200)
            self.drawer.pendown()
            self.drawer.forward(100)
            self.drawer.penup()
        t.update()
    
    def create_circles(self):
        """Create attempt indicator circles"""
        for i in range(6):
            c = t.Turtle("circle")
            c.shapesize(3)
            c.color("black", "sky blue")
            c.up()
            c.goto(-150 + 50 * i, 0)
            self.circles.append(c)
        t.update()
    
    def update_score_display(self):
        """Update the score display"""
        t.goto(-270, 200)
        t.write(f"Attempts left: {self.score}", font=("Arial", 16, "normal"))
        t.update()
    
    def update_missed_display(self):
        """Update the incorrect guesses display"""
        t.goto(-270, 150)
        t.clear()
        t.write("Incorrect guesses: " + ", ".join(self.missed), font=("Arial", 16, "normal"))
        t.update()
    
    def draw_letter(self, letter, position):
        """Draw a correctly guessed letter"""
        self.drawer.goto(-270 + 150 * position, -200)
        self.drawer.write(letter.upper(), font=("Arial", 48, "bold"))
        t.update()
    
    def check_win(self):
        """Check if all letters have been guessed"""
        return all(letter in self.right for letter in self.word)
    
    def handle_correct_guess(self, inp_word):
        """Handle a correct letter guess"""
        self.right.append(inp_word)
        for i in range(len(self.word)):
            if self.word[i] == inp_word:
                self.draw_letter(inp_word, i)
        
        if self.check_win():
            self.running = False
            messagebox.showinfo("Congratulations!", f"You guessed the word '{self.word.upper()}' correctly!")
            return True
        return False
    
    def handle_incorrect_guess(self, inp_word):
        """Handle an incorrect letter guess"""
        self.missed.append(inp_word)
        self.score -= 1
        self.update_missed_display()
        
        # Hide one circle
        self.circles[-(6 - self.score)].hideturtle()
        self.update_score_display()
        
        if self.score == 0:
            self.running = False
            messagebox.showinfo("Game Over", f"You've run out of attempts! The word was '{self.word.upper()}'.")
            return True
        return False
    
    def get_user_input(self):
        """Get and validate user input"""
        while True:
            inp_word = t.textinput("Guess the Word", "Enter a letter:")
            
            if inp_word is None:
                return None
            
            inp_word = inp_word.lower()
            
            # Validate input
            if len(inp_word) != 1 or not inp_word.isalpha():
                messagebox.showwarning("Warning", "Please enter a single letter.")
                continue
            
            if inp_word in self.missed or inp_word in self.right:
                messagebox.showwarning("Already Guessed", "You already guessed that letter!")
                continue
            
            return inp_word
    
    def game_loop(self):
        """Main game loop"""
        while True:
            inp_word = self.get_user_input()
            
            if inp_word is None:
                self.running = False
                sys.exit()
            
            if inp_word in self.word:
                if self.handle_correct_guess(inp_word):
                    break
            else:
                if self.handle_incorrect_guess(inp_word):
                    break
    
    def setup_game(self):
        """Setup the game board"""
        self.show_intro()
        
        # Choose random word
        self.word = random.choice(self.words)
        
        # Setup initial display
        self.update_score_display()
        t.goto(-270, 150)
        t.write("Incorrect guesses:", font=("Arial", 16, "normal"))
        t.update()
        
        # Draw game board
        self.draw_blanks()
        self.create_circles()
    
    def start(self):
        """Start the game"""
        # Start title update thread
        self.title_thread = threading.Thread(target=self.update_title, daemon=True)
        self.title_thread.start()
        
        # Setup and run game
        self.setup_game()
        self.game_loop()
        
        # Cleanup
        self.running = False
        t.done()
        try:
            t.bye()
        except:
            pass


# Run the game
if __name__ == "__main__":
    game = GuessTheWordGame()
    game.start()