from art import logo
import random
from replit import clear


#Repartidor de Cartas.
def dealCard():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)== 21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(userScore, computerScore):
    if userScore == computerScore:
        return 'Draw'
    elif computerScore == 0:
        return 'Lose, opponent has a Blackjack'
    elif userScore == 0:
        return 'You win! BlackJack!'
    elif userScore > 21:
        return 'You went over. You Lose!'
    elif computerScore > 21:
        return 'Opponent went over. You win!'
    elif userScore > computerScore:
        return 'You Win!'
    else:
        return 'You Lose!'

def playgame():
    print(logo)

    userCards=[]
    computerCards=[]
    isGameOver=False

    for i in range(2):
        userCards.append(dealCard())
        computerCards.append(dealCard())

    while not isGameOver:
        userScore=calculate_score(userCards)
        computerScore=calculate_score(computerCards)
        print(f'    Your Cards {userCards}, current Score: {userScore}')
        print(f'    Computer First card: {computerCards[0]}')

        if userScore == 0 or computerScore == 0 or userScore > 21:
            isGameOver=True
        else:
            x=input('You want to draw another card? Type "y" to draw or "n" to Pass!: ')
            if x == 'y':
                userCards.append(dealCard())
            else:
                isGameOver=True

    while computerScore !=0 and computerScore < 17:
        computerCards.append(dealCard())
        computerScore= calculate_score(computerCards)
            
    print(f'Your final hand: {userCards}, final score: {userScore}')
    print(f'Oponnet final hand: {computerCards}, final score: {computerScore}')
    print(compare(userScore,computerScore))

while input('Do you want to restart the game? Type "y" or "n" to exit: ') == 'y':
    clear()
    playgame()


























# #Usercode
# playerCards=random.choices(cards,k=2)
# sumPlayerCards=playerCards[0]+playerCards[1]
# userBlackJack=blackJack-sumPlayerCards


# #DealerCode
# dealerCards=random.choices(cards,k=2)
# sumDealerCards=dealerCards[0]+dealerCards[1]
# dealerBlackJack=blackJack-sumDealerCards

# #Flag
# blackJackGame=True

# starting=input('Do you want to play a game of BlackJack? Type "y" or "n": ')
# while blackJackGame:
#     if starting == 'y':
#         print(logo)
#         print(f'Your cards: {playerCards}, Current Score: {sumPlayerCards}')
#         if sumPlayerCards== blackJack:
#             print('BlackJack, You win!')
#         else:
#             print(f'Computer first card: {dealerCards[0]}')
#             secondRound=input('Type "y" to get another card, type "n" to pass: ')  
#             if secondRound == 'y':
#                 thirdCard=random.choice(cards)
#                 totalSumPlayer=sumPlayerCards+thirdCard
#                 print(f'Your third card is {thirdCard} you get a total of {totalSumPlayer}')
#                 if totalSumPlayer == blackJack:
#                     print(f'BLACK JACK! You win with {totalSumPlayer}!')
#                 elif totalSumPlayer > blackJack:
#                     print(f'You score is over with {totalSumPlayer}. You Lose!')
#                     blackJackGame==False
#                     clear()
#             elif secondRound == 'n':
#                 secondCardDealer=random.choice(cards)
#                 totalSumDealer=dealerCards[0]+secondCardDealer
#                 print(f'The Dealer Second Card is {secondCardDealer}, Current Score:{totalSumDealer} ')
#                 if totalSumDealer == blackJack:
#                     print(f'Dealer win with {totalSumDealer}')
#                 elif totalSumDealer > blackJack:
#                     print(f'The Dealer over pass with {totalSumDealer}, You win!')
#     else:
#         print('Goodbye')
#         blackJackGame==False     
#         clear()   



