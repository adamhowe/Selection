#Adam Howe
#Development Exercise 2 - Selection
#08/10/2014

temperature = int(input("Enter the temperature of the water: "))

if temperature <= 0:
    print("The water is freezing")
elif temperature >= 100:
    print("The water is boiling")
else:
    print("The water is neither boiling nor freezing")
