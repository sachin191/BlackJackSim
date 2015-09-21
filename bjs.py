import random

gbjs_num_decks=1
gbjs_cards_dealt_num=0
gbjs_cards_dealt_list=[]

def is_dealt_card(num):
    global gbjs_cards_dealt_list
    for i in range(len(gbjs_cards_dealt_list)):
        if ( num == gbjs_card_dealth_list[i] ): 
          return 1
    return 0

def get_next_card():
    global gbjs_num_decks
    global gbjs_cards_dealt_num

    num_decks = gbjs_num_decks
    max_num = num_decks*52
    num=random.randint(1,max_num)
    if (gbjs_cards_dealt_num > max_num ): 
        return 0

    while (is_dealt_card(num) == 1):
	    num=random.randint(1,max_num)

    # gbjs_cards_dealt_num = gbjs_card_dealt_num + 1 
    gbjs_cards_dealt_num += 1 
    return num

def card_num2str(num):
    deck=num/52
    card=num%52
    suit=card/13
    val=card%13
    return deck, suit, val

def start_game():
    for i in range(0,10):
        num=get_next_card();
        deck, suit, val = card_num2str(num)
        print deck, suit, val

def main():
    start_game()
     

main()
