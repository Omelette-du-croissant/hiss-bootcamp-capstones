import random

class Card:
  def __init__(self, suit, val):
    self.suit = suit
    self.value = val

  def price(self):
    if self.value >= 10:
      return 10
    elif self.value == 1:
      return 11
    return self.value

  def show(self):
    print ("{} of {}".format(self.value, self.suit))
    #To do: swap with card ASCII


class Deck:
  def __init__(self):
    self.cards = []
    self.build()

  def build(self):
    for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
      for v in range(1, 14):
        self.cards.append(Card(s,v))

  def show(self):
    for c in self.cards:
      c.show()

  def shuffle(self):
    for i in range(len(self.cards)-1, 0, -1):
      r = random.randint(0, i)
      self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

  def draw_card(self, iteration):
    cards = []
    for l in range(iteration):
      card = random.choice(self.cards)
      self.cards.remove(card)
      cards.append(card)
    return cards

  def count(self):
    return len(self.cards)
    


class Player:
  def __init__(self, is_dealer, deck):
    self.cards = []
    self.is_dealer = is_dealer
    self.deck = deck
    self.score = 0

  def hit(self):
    self.cards.extend(self.deck.draw_card(1))
    self.check_score()
    if self.score >21:
      return 1
    return 0

  def deal(self):
    self.cards.extend(self.deck.draw_card(1))
    self.check_score()
    if self.score == 21:
      return 1
    return 0

  def check_score(self):
    counter = 0
    self.score = 0
    for card in self.cards:
      if card in self.cards:
        if card.price() == 11:
          counter += 1
        self.score += card.price()

    while counter != 0 and self.score >21 :
      counter -= 1
      self.score -= 10
    return self.score

  def show(self):
    if self.is_dealer:
      print("Dealer's Hand")
    else:
      print("Player's Hand")
    for i in self.cards:
      i.show()

    print(f"Score: {str(self.score)}")

  def discard(self):
    return self.hand.pop()
    
    
class Blackjack:
  def __init__(self):
    self.deck = Deck()
    self.deck.shuffle()
    self.player = Player(False, self.deck)
    self.dealer = Player(True, self.deck)

  def play(self):
    player_status = self.player.deal()
    dealer_status = self.dealer.deal()

    self.player.show()

    if player_status == 1 :
      print("Player got Blackjack.")
      if dealer_status == 1 :
        print("It's a push.")
      return 1

    prompt = ""
    while prompt != "Stand":
      bust = 0
      if self.dealer.check_score() < 16:
        self.dealer.hit()
      prompt = input("Hit or Stand? ")
      if prompt == "Hit":
        bust = self.player.hit()
        self.player.show()
        if self.dealer.check_score() < 16:
          self.dealer.hit()
      if bust == 1 :
        respects = input("Player busted. F for respects. ")
        if respects == "F":
          print( 
"""   
      .--.
    .'_\/_'.
    '. /\ .'
      "||"
       ||
       ||
       ||
_______||_______
"""
)
        
        return 1
    print("\n")
    self.dealer.show()
    if dealer_status == 1:
      print("Dealer got Blackjack.")
      return 1

    while self.dealer.check_score() > 17:
      if self.dealer.hit() == 1:
        self.dealer.show()
        print("Dealer busted. GGEZ.")
        return 1
      self.dealer.show()

    if self.dealer.check_score() == self.player.check_score():
      print("It's a push.")
    elif self.dealer.check_score() > self.player.check_score():
      print("Dealer wins.")
    elif self.dealer.check_score() > self.player.check_score():
      print("Player wins.")

game= Blackjack()
game.play()
