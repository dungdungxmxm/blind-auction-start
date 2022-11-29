from replit import clear
import art

# bid_records = {"dung": 234, "hoa": 133}
bids = {}
end_bid = False


def find_win_bid(bids):
  bid_max = 0
  bid_name = ""
  for name in bids:
    bid_amount = bids[name]
    if bid_max < bid_amount:
      bid_max = bid_amount
      bid_name = name
  print(f'The winner is {bid_name} with a bid of ${bid_max}.')
  
#Print logo 
print(art.logo)

while not end_bid:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bids[name] = bid
  
  continues = input("Are there any other bidders? Type 'yes or 'no'.")

  if continues == 'yes':
    clear()
  else:
    find_win_bid(bids)
    end_bid = True;
    
  