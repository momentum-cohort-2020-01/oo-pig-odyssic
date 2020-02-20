import random

DIE = [1, 2, 3, 4, 5, 6]
# PLAYERS = [name, DEALERS]
DEALERS = ["Portbelly", "Stewy", "Fragonaard",
           "Tim the Usurper", "Lilian Lovelace"]


class Die:
    def __init__(self, value):
        self.value = value
    pass


class Player:
    def __init__(self, name):
        self.name = name
        self.turn_score = []
        self.score = 0


class Dealer:
    def __init__(self):
        self.name = random.choice(DEALERS)
        self.turn_score = []
        self.score = 0


class Game:
    def __init__(self, player, dealer, die):
        self.player = player
        self.dealer = dealer
        self.die = die
    pass

    def __str__(self):
        print

    def roll(self, participant):
        # def __init__:
        print('Rolling the die...')
        roll = random.choice(DIE)
        return roll
        if self.participant is self.player:
            print(f'You rolled a {roll}')
            turn_score = turn_score(player.turn_score, roll)

        if self.participant is self.dealer:
            print(f'Dealer rolled a {roll}')
            turn_score = turn_score(dealer.turn_score, roll)

    def initial_roll(self):
        roll = random.choice(DIE)
        return roll
        print(f'You rolled a {roll}')

    def turn_score(self, turn_score, roll):
        turn_score.append(int(roll))
        sum(turn_score)

    def game_score(self, player, score):
        self.score

    def print_rules(self):
        pig_rules = "'Notorious P.I.G.' is a game of 'chance' (a.k.a DESTINY)\nThe rules are simple: the first entity to reach 100 wins!\nOn your turn, you roll a 6-sided die as many times as you like. \nYou are able to rack up points on each turn. \n If you roll a '1', you lose the points for that turn. \nIf you choose to 'hold', you keep your points, and your digitized opponent rolls. \nShe will roll until her score is at least twenty, \nor she rolls a '1', and then the proverbial die passes back to you."

        print(pig_rules)

        print("Are you ready to begin?: ")
        self.startgame()

    def startgame(self):
        answer = input('"(Y)es" or "(No)"?')

        if answer is "Y".lower():
            while name == '':
                name = input("Exciting! Please enter your name to proceed: ")
                greeting = f"Welcome to the game {name}! You and your opponent will now each roll to determine who goes first! The lower number goes first."

                print(greeting)

            self.initial_roll()

        if answer is "N".lower():
            print(
                "Please return when you're ready to play dice with the Universe!\nThis game may self destruct!")

            end_game()

        def end_game(self):
            pass


Game(Player, Dealer, Die)
