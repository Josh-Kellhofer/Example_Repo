import random

destinations = ["BFE", "Space", "Mom's house", "Walmart"]
restaraunts = ["Olive Garden", "Mcdonalds", "Steak House", "Bob's Burgers"]
transportation = ["Bicycle", "Skateboard", "Greyhound Bus", "Your own two feet"]
entertainment = ["Gladiator arena", "Watching clowns", "Yelling at kids on your lawn", "Wheel of Fortune"]
itinerary = ["{result_1}","{result_2},""{result_3},""{result_4}"]

def random_selection(list_of_options):
  return random.choice(list_of_options)

print("\n")  
print("Hello fellow undecided person! For your place of travel, your food, how you will travel, and what you will do for fun our company will randomly decide for you to avoid unnecessary brain spasms. However, if you don't like your random choices, you may opt to re-randomize each one individually! Makes no sense? Who cares!\n") 

print("HERE ARE YOUR RESULTS!\n")

print(f"Your random destination is: {random_selection(destinations)}")
result_1 = random_selection(destinations)
print(f"Your random restaraunt is: {random_selection(restaraunts)}")
result_2 = random_selection(restaraunts) 
print(f"Your random transportation is: {random_selection(transportation)}")
result_3 = random_selection(transportation)
print(f"Your random entertainment is: {random_selection(entertainment)}\n")
result_4 = random_selection(entertainment)

while True:
  First_question = input(f"Would you like to change your destination (Yes/No)?")
  if First_question == "No":
     break
  change = random_selection(destinations)
  #result_1 = random_selection(destinations)
  print(f"Your NEW random destination is {change}")
  itinerary.append(result_1)
  
while True:
  result_2 = random_selection(restaraunts)
  Second_question = input("Would you like to change your restaraunt (Yes/No)? ")
  if Second_question == "No":
     break
  print(f"Your NEW random restaraunt is {result_2}")
  itinerary.append(result_2)
  
while True:
  result_3 = random_selection(transportation)
  Third_question = input("Would you like to change your transportation (Yes/No)? ")
  if Third_question == "No":
     break
  print(f"Your NEW random transportation is {result_3}")
  itinerary.append(result_3)
   
while True:
  result_4 = random_selection(entertainment)
  Fourth_question = input("Would you like to change your entertainment (Yes/No)? ")
  if Fourth_question == "No":
    break
  print(f"Your NEW random entertainment is {result_4}")
  itinerary.append(result_4)

print("\n")  
print("Here is your selected itinerary:")
print("    -PLEASE ENJOY YOUR DAY-\n")
print(f"Destination:     {result_1}")
print(f"Restaraunt:      {result_2}")
print(f"Transportations: {result_3}")
print(f"Entertainment:   {result_4}")
print("\n")
# for random in itinerary:
#   print(f"Here is your finalized itinerary: {random}")






  


          











