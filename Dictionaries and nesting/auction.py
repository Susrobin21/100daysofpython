import os

def clear():
    os.system('cls')


bids = {}
end_bid = False
winner = []
def highest_bidder(bidding_record):
    highest_bidder = 0
    winner = ""
    for bidder in bidding_record :
        bidding_amount = bidding_record[bidder]
        bidding_amount = int(bidding_amount)
        if bidding_amount > highest_bidder :
            highest_bidder = bidding_amount
            winner= bidder 
    print(f'The winner is {winner} who has won the bid with the amount ₹ {highest_bidder}')


while end_bid == False :
    name = input('Enter your name : ')
    price = int(input('Enter your bidding price : ₹ '))
    bids[name] =  price
    another_bid = input('Does anyone else want to bid ? : ')
    if another_bid == 'no' :
        end_bid = True
        highest_bidder(bids)
    elif another_bid == 'yes' :
        clear()
        end_bid