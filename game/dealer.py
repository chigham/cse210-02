from game.card import Card

class Dealer:
    """A person who directs the game. 
    
    The responsibility of a Dealer is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        previous (int): The value of the previous card.
        current (int): The value of the current card.
        hi_lo (string): The answer of the player to the question High/Low.
        total_score (int): The score for the entire game.
        first_turn (boolean): Whether or not the first turn is being played.
        hi_lo_options (list): List of hi_lo input options that are acceptable.
    """


    def __init__(self):
        """Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.is_playing = True
        self.previous = 0
        self.current = Card()
        self.hi_lo = ""
        self.total_score = 300
        self.first_turn = True
        self.hi_lo_options = ['h', 'l']


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()


    def reset_hi_lo(self):
        """Sets a clean slate to collect input for the game.

        Args:
            self (Dealer): an instance of Dealer.
        """
        self.hi_lo = ""


    def get_inputs(self):
        """Ask the user if they want to play. Draw a card before the first turn.
           Then ask the user to guess if the next card is higher or lower.

        Args:
            self (Dealer): An instance of Dealer.
        """
        # The first card needs to be handled differently
        if self.first_turn:
            print()
            temp_card = Card()
            temp_card.pick()
            self.previous = temp_card.value
            print(f"Let's begin. Your starting score is {self.total_score}")
            print(f"Your first card is {self.previous}")
        
        # Reset input
        self.reset_hi_lo()

        # Collect input
        while not self.hi_lo in self.hi_lo_options:
            self.hi_lo = input("Higher or lower? [h/l] ").lower()
            
            # Handle bad input
            if not self.hi_lo in self.hi_lo_options:
                print("Not a valid answer. Please try again. [h/l]")
        
 
    def do_updates(self):
        """Updates the player's score and prints the value of the
           second card

        Args:
            self (Dealer): An instance of Dealer.
        """
        # Early exit?
        if not self.is_playing:
            return 

        # Identify previous card value, depending on first turn or not
        if self.first_turn:
            self.first_turn = False
        else:
            self.previous = self.current.value
        
        # Draw the next card
        self.current.pick()
        print(f"Next card is {self.current.value}")
        
        # Add to the total score (100, -75, 0) based on input and card drawn
        if self.hi_lo == 'h' and self.current.value > self.previous:
            self.total_score += 100
        elif self.hi_lo == 'h' and self.current.value < self.previous:
            self.total_score += -75
        elif self.hi_lo == 'l' and self.current.value > self.previous:
            self.total_score += -75
        elif self.hi_lo == 'l' and self.current.value < self.previous:
            self.total_score += 100
        else:
            self.total_score += 0

     
    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to draw again. 

        Args:
            self (Director): An instance of Director.
        """
        # What if you are such a loser you lose all your points??
        if self.total_score <= 0:
            self.is_playing = False
            print(f"You lose. Your score is {self.total_score}")
        
        # Present score, ask if user wants to continue playing
        print(f"Your score is: {self.total_score}")
        keep_playing = input("Draw again? [y/n] ")
        self.is_playing = (keep_playing == "y")
        print()

        # Exit the game gracefully
        if not self.is_playing:
            print(f"Thanks for playing. Your final score is: {self.total_score}")
