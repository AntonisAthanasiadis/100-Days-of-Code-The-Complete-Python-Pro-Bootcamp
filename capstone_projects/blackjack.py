import random

def play_blackjack():
    #card list
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(cards)
    #Remove from card list, put into hands
    player_hand = [cards.pop(), cards.pop()]
    dealer_hand = [cards.pop(), cards.pop()]

    print(f"\nYour hand: {player_hand} (Total: {sum(player_hand)})")
    print(f"Dealer shows: {dealer_hand[0]}")

    #Player's turn
    while sum(player_hand) < 21:
        action = input("\nDo you want to [H]it or [S]tay? ").lower()
        if action == 'h':
            player_hand.append(cards.pop())
            print(f"You drew a {player_hand[-1]}. Your hand: {player_hand} (Total: {sum(player_hand)})")
        else:
            break

    #Check if player lost
    player_total = sum(player_hand)
    if player_total > 21:
        print("You lost! Dealer wins.")
        return

    #Dealer's Turn (Dealer hits until they reach at least 17)
    print(f"\nDealer's full hand: {dealer_hand} (Total: {sum(dealer_hand)})")
    while sum(dealer_hand) < 17:
        new_card = cards.pop()
        dealer_hand.append(new_card)
        print(f"Dealer draws a {new_card}. Dealer total: {sum(dealer_hand)}")

    #Determine Winner
    dealer_total = sum(dealer_hand)
    print(f"\n--- Final Results ---")
    print(f"Your Total: {player_total} | Dealer Total: {dealer_total}")

    if dealer_total > 21:
        print("Dealer lost! You win!")
    elif player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    print("Welcome to Python Blackjack!")
    playing = True
    while playing:
        play_blackjack()

        # Ask the player if they want to go again
        repeat = input("\nPlay another round? (Y/N): ").lower()
        if repeat != 'y':
            playing = False
            print("Thanks for playing!")