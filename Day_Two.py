# print("Welcome to the tip calculator")
# bill_amount = float(input("What was the total bill? $"))
# split = float(input("How many people to split the bill? "))
# tip = float(input("What Percentage tip would you like to give? 10,12, or 15? "))
#
# split_amount = bill_amount / split
# tip_amount = (tip / 100) * bill_amount
# tip_add = tip_amount / split
# paid_amount = split_amount + tip_add
# print("Each person should pay", round(paid_amount, 1))


# print(round(25.77))
# -------------------------------------------
# print(8//3) ans=2
# -------------------------------------------
# score = 0
# height = 11.6
# winning = True
# print(f"Your score is {score},your height is {height},You are winning is {winning} ")
# print("Your score is {0},your height is {1},You are winning is {2} ".format(score,height,winning))
# -------------------------------------------
#Days left

age = int(input("Enter Age:"))
days_left = (365*90) - (365*age)
weeks_left = (52*90) - (52*age)
months_left = (12*90) - (12*age)
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")