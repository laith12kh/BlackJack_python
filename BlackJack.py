import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def play():
    print(logo)

# the user card
    your_cards=[]
    # the computer card
    comp_cards=[]

    #flag to stop the game
    flag = False
    # the function that dialing the cards
    def deal():
        #the cards we play with
        play_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        card = random.choice(play_cards)
        return card

    # the function to calculate the sum
    def calc_sumof_cards(cards):
        # check ig its black jack 
        if 11  in cards and 10 in cards and len(cards) == 2:
            return 0
        # if the Ace is on of the cards replace its value (11) to 1 
        if 11 in cards and sum(cards) > 21 :
            cards.remove(11)
            cards.append(1)
        
        return sum(cards)

    #compare the cards 
    def compare_cards(your_score , computer_score) :
        # check if its draw (the scores is equal)
        if comp_score == your_score :
            return "Draw"
        
        # check if you have blackjack
        elif your_score == 0 :
            return "You Win , you have BlackJack tou will earn 1.5%"
        
        # ckeck if the computer has blackjack
        elif comp_score == 0 :
            return "You Lose the computer has BlackJack !!" 
        
        #check if your score above 21
        elif your_score > 21 :
            return f"You Lose , your score {your_score} is above 21"
        
        #check if the computer score above 21
        elif comp_score > 21 :
            return f"You win , computer score {comp_score} is above 21"
        
        # find the winner 
        #if your score higher than the computer score 
        elif your_score > comp_score :
            return f"You win with score {your_score}"
        else:
            return f"You Lose the computer score was higher than yours"
        

    for card_num in range(2):
        ny_card = deal()
        your_cards.append(ny_card)
        nc_card = deal()
        comp_cards.append(nc_card)
    while not flag:
    # clac your score
        your_score = calc_sumof_cards(your_cards)
        print(f"your cards {your_cards} , your score is {your_score}")
        # calc computer score
        comp_score = calc_sumof_cards(comp_cards)
        print(f"computer first card is {comp_cards[0]}")

        # cjeck if blackjack
        if your_score == 0 or comp_score==0 or your_score > 21 :
            flag=True
        else:
            choice = input("type y to take another card or type n to stop : ")
            if choice == 'y' :
                your_cards.append(deal())
            elif choice == 'n' : 
                flag = True

    while comp_score != 0 and comp_score < 17 :
        comp_cards.append(deal())
        comp_score = calc_sumof_cards(comp_cards)
        
    print(f"your final cards {your_cards} and your score is {your_score}")
    print(f"computer final cards {comp_cards} and the score {comp_score}")
    print(compare_cards(your_score , comp_score))

while input("Do you want to play again ? , prees y to play again and n to leave : ") == 'y' : 
    clear_screen()
    play()
