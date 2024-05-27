#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Time to do the easy calculations for you!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip? "))
split = int(input("How many people are paying? "))
tip_percent = tip / 100
total_tip = bill * tip_percent
total = bill + total_tip
total_split = total / split
final_amount = round(total_split, 2)
if split < 2:
  print(f"You need to pay ${final_amount}.")
else:
  final = input(f"Each person needs to pay ${final_amount}.")
if final.lower() in ["thank you", "thanks"]:
  print("You're welcome!")
