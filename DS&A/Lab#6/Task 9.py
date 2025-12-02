choice = input("Convert to (C/F)? ").upper()
temp = float(input("Enter the temperature: "))

if choice == "C":
    result = (temp - 32) * 5/9
    print("Temperature in Celsius:", result)
elif choice == "F":
    result = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", result)
else:
    print("Invalid choice")
