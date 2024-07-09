import random

balance = 1000
deck = {
    'Ace': 11, 'King': 10, 'Queen': 10, 'Joker': 10, 'Ten': 10, 'Nine': 9,
    'Eight': 8, 'Seven': 7, 'Six': 6, 'Five': 5, 'Four': 4, 'Three': 3, 'Two': 2
}

def shuffle_deck(deck):
    '''
    Extracts the keys from the dictionary and stores them in a list 
    called 'keys'. Then shuffles this list and stores it in 'shuffled_list'.
    '''

    keys = list(deck.keys())
    shuffled_list = sorted(keys * 4, key=lambda x: random.random())
    return shuffled_list

def draw_card(shuffled_list):
    '''
    Checks if the shuffled list exists, then pops the first 
    element from 'shuffled_list' and stores it in the variable 'drawn_card'.
    '''

    if not shuffled_list:
        return None
    drawn_card = shuffled_list.pop(0)
    return drawn_card

def bet_amount():
    '''
    Asks the player for the amount of the bet and then returns the bet.
    '''

    while True:
        try:
            bet = int(input('Please place a bet: '))
            if bet <= 0:
                print('You need to bet a positive amount!')
            elif bet > balance:
                print('You cannot bet more than your balance!')
            else:
                return bet
        except ValueError:
            print('Please enter a valid integer.')

def calculate_hand(hand, deck):
    '''
    Sums up the values in the hand by using the dictionary keys to access the values.
    Checks if the hand contains an Ace. If the hand contains an Ace, it checks the conditions.
    '''

   
    count = sum(deck[card] for card in hand)
    if 'Ace' in hand and count > 21:
        count -= 10
    return count

def game():
    
    '''
    Game section of the code where both the dealer and the player draw 2 cards each. One of the dealer's cards must be hidden.
    The game then asks the player for their decision: hit or stand. The player needs to decide for themselves.
    It's Blackjack!
    '''

  
    global balance
    game_deck = shuffle_deck(deck)
    player_hand = []
    dealer_hand = []
    
    bet = bet_amount()
    
    player_hand.append(draw_card(game_deck))
    player_hand.append(draw_card(game_deck))
    dealer_hand.append(draw_card(game_deck))
    dealer_hand.append(draw_card(game_deck))
    
    print('******************************')
    print(f"Player's hand: {player_hand}")
    print(f"Dealer's hand: {dealer_hand[0]} and [Hidden]")
    print('******************************')
    
    player_score = calculate_hand(player_hand, deck)
    dealer_score = calculate_hand(dealer_hand, deck)
    
    while player_score < 21:
        action = input("Hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(draw_card(game_deck))
            player_score = calculate_hand(player_hand, deck)
            print(f"Player's hand: {player_hand} (score: {player_score})")
        elif action == 's':
            break
        else:
            print("Invalid input, please enter 'h' for hit or 's' for stand.")
    
    while dealer_score < 17:
        dealer_hand.append(draw_card(game_deck))
        dealer_score = calculate_hand(dealer_hand, deck)
    
    print(f"Dealer's hand: {dealer_hand} (score: {dealer_score})")
    
    if player_score > 21:
        print("Player busts! Dealer wins.")
        balance -= bet
    elif dealer_score > 21 or player_score > dealer_score:
        print("Player wins!")
        balance += bet
    elif player_score < dealer_score:
        print("Dealer wins!")
        balance -= bet
    else:
        print("It's a tie!")
    
    print(f"Current balance: {balance}")

def main():
    global balance
    while balance > 0:
        print(f"\nCurrent balance: {balance}")
        game()
        if balance <= 0:
            print("You're out of balance! Game over.")
            break
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()
