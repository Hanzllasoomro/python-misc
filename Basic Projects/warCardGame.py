from random import shuffle
import time

SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

MAX_ROUNDS = 10000  # Prevent infinite loop edge cases

class Deck:
    def __init__(self):
        print("Creating a new ordered deck...")
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling the deck...")
        shuffle(self.allcards)

    def split_in_half(self):
        print("Splitting the deck into halves...")
        return (self.allcards[:len(self.allcards) // 2], self.allcards[len(self.allcards) // 2:])


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return f"Contains {len(self.cards)} cards"

    def draw_card(self):
        if self.cards:
            return self.cards.pop(0)
        return None

    def add_cards(self, new_cards):
        self.cards.extend(new_cards)


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        card = self.hand.draw_card()
        if card:
            print(f"{self.name} played card: {card}")
        else:
            print(f"{self.name} has no more cards to play!")
        return card

    def remove_war_card(self):
        war_cards = []
        for _ in range(min(3, len(self.hand.cards))):
            war_cards.append(self.hand.draw_card())
        return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) > 0


def animate_draw():
    print("Drawing cards", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")


# Game Setup
print("🎮 Welcome to the War Card Game!")
deck = Deck()
deck.shuffle()
half1, half2 = deck.split_in_half()

name = input("Enter your name: ")
user = Player(name, Hand(half2))
computer = Player("Computer", Hand(half1))

total_rounds = 0
war_count = 0

# Game Loop
while user.still_has_cards() and computer.still_has_cards() and total_rounds < MAX_ROUNDS:
    total_rounds += 1
    print(f"\n🕹️ Round {total_rounds}")
    print(f"{user.name} has {len(user.hand.cards)} cards")
    print(f"Computer has {len(computer.hand.cards)} cards")

    # animate_draw()

    table_cards = []

    p_card = user.play_card()
    c_card = computer.play_card()

    if p_card is None or c_card is None:
        break

    table_cards.extend([p_card, c_card])

    if p_card[1] == c_card[1]:
        war_count += 1
        print("🔥 It's WAR! Each player adds 3 face-down cards and 1 face-up.")

        table_cards.extend(user.remove_war_card())
        table_cards.extend(computer.remove_war_card())

        p_card = user.play_card()
        c_card = computer.play_card()

        if p_card is None or c_card is None:
            break

        table_cards.extend([p_card, c_card])

    # Compare final cards
    if RANKS.index(p_card[1]) > RANKS.index(c_card[1]):
        print(f"{user.name} wins the round and takes {len(table_cards)} cards.")
        user.hand.add_cards(table_cards)
    else:
        print(f"Computer wins the round and takes {len(table_cards)} cards.")
        computer.hand.add_cards(table_cards)

    # Immediately break if someone runs out of cards
    if not user.still_has_cards() or not computer.still_has_cards():
        break

# Game Over
print("\n🎯 GAME OVER")
print(f"Total rounds played: {total_rounds}")
print(f"Total wars: {war_count}")
print(f"{user.name}'s cards left: {len(user.hand.cards)}")
print(f"Computer's cards left: {len(computer.hand.cards)}")

if user.still_has_cards() and not computer.still_has_cards():
    print(f"🎉 {user.name} wins the game!")
elif computer.still_has_cards() and not user.still_has_cards():
    print("💻 Computer wins the game!")
elif not user.still_has_cards() and not computer.still_has_cards():
    print("😮 It's a draw! Both players ran out of cards.")
else:
    print("⚠️ Game stopped due to too many rounds. No winner declared.")
