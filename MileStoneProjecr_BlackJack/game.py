from classes import Deck, Hand, Card, Chips

playing = True


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?  '))
        except:
            print('Enter integer, please!')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you not enough chips. You have {chips.total}')
            else:
                print(f"thank You. Bet Value is :  {chips.bet}")
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s ')
        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print('Player Stands Dealer-s Turn')
            playing = False

        else:
            print('Sorry, again h or s')
            continue

        break


def show_some(player, dealer):

    print('\nDealer Hands: ')
    print('One card hidden')
    print(dealer.cards[1])
    print('\n')
    print('Players Hand :  ')
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print('\nDealers Hand: ')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Players Hand :  ')
    for card in player.cards:
        print(card)

def player_busts(player, dealer, chips):
    print('Bust Player!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player Wins!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Player Wins! Dealer Busted')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer Wins!')
    chips.lose_bet()


def push(player, dealer):
    print('tie ! Push')


player_chips = Chips()

# ვიწყებთ თამაშოს აწყობას
if __name__ == "__main__":
    while True:
        print('Welcome To BlackJack')

        # ვქმნით კარტებს და ვურევთ
        deck = Deck()
        deck.shuffle()

        # ვაძლევთ ორ ორ კარტს დილერს და მოთამაშეს
        player_hand = Hand()
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())

        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # vusazRvravT moTamaSes მონეტების რაოდენობას

        # მოთამაშე განსაზღვრავს ფსონის რაოდენობას
        take_bet(player_chips)

        show_some(player_hand, dealer_hand)

        while playing:
            hit_or_stand(deck, player_hand)

            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)


        print('\nPlayer total chips ar at : {}'.format(player_chips.total))

        new_game = input('Woulds you like to play another hand? y/n ')

        if new_game[0].lower() == 'y':
            playing = True
            continue

        else:
            print('Thanks for playing!')
            break






