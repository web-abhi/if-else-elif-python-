print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >=120:
  print("You're eligible.")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("You have to pay $5.")
  elif age <= 18:
    bill = 7
    print("You have to pay $7.")
  else:
    bill = 12
    print("You have to pay $12.")

  photos = input("Do you want photos Y or N:")
  if photos == "Y":
    bill +=3

  print(f"Here is your final bill {bill}")
  
else:
  print("Sorry, you have to grow taller before you can ride.")
