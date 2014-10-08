#Adam Howe
#07/10/2014
#Development Exercise 1

number = int(input("Enter a number between 1 and 12: "))

if number == 1:
    month = "January"
elif number == 2:
    month = "Feburary"
elif number == 3:
    month = "March"
elif number == 4:
    month = "April"
elif number == 5:
    month = "May"
elif number == 6:
    month = "June"
elif number == 7:
    month = "July"
elif number == 8:
    month = "August"
elif number == 9:
    month = "September"
elif number == 10:
    month = "October"
elif number == 11:
    month = "November"
elif number == 12:
    month = "December"
else:
    print("That is not a number between 1 and 12")

print(month)
