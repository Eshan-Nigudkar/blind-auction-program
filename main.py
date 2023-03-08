from replit import clear
from art import logo
print(logo)

bidding={}
def max_value(bids):
  
  highest_bid=0
  winner=""
  for value in bids:
    bid_value=bids[value]
    if bid_value>highest_bid:
      highest_bid=bid_value
      winner=value
  print(f"The winner is {winner} and highest_bid is {highest_bid}.")
      

bid_stop=False
while not bid_stop:
  
  bidname= input("What is your name?: ").lower()
  bidprice=int(input("What is the price price?: $"))
  bidding[bidname]=bidprice
  otheruser=input("Are there more bids? Yes or No: ").lower()
  if otheruser=="yes":     
    clear()
    print(bidding)
    
  else:
    bid_stop=True
    max_value(bidding)