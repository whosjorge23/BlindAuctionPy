from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

bid_dictionary = {}
highest_bid = 0
highest_name = ""

should_continue = True


while should_continue:
  print(logo)
  print("Welcome to the secret auction program.")
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bid_dictionary[name] = bid
  new_user = input("Are there any other bidders? Type 'yes' or 'no'. ")
  clear()

  if new_user == "no":
    for bid in bid_dictionary:
      bid_number = bid_dictionary[bid]
      if bid_number > highest_bid:
        highest_bid = bid_number
        highest_name = bid

      #bids.append(bid_number)
    clear()
    print(f"The auction is won by {highest_name} with ${highest_bid}")
    should_continue == False
