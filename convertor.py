#Receving the user input

user_input = float(input("Enter the temperature: "))

#Choices

print("--- What converter do you want? ---")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

#User choice

user_choice = int(input("Enter the corespondenting number: "))

#Making decisions

if user_choice == 1:
    print((user_input * 9/5) + 32,  "° Fahrenheit")
elif user_choice == 2:
    print(user_input + 273.15, "° Kelvin")
elif user_choice == 3:
    print((user_input - 32) * 5/9, "° Celcius")
elif user_choice == 4:
    print((user_input - 32) * 5/9 + 273.15, "° Kelvin")
elif user_choice == 5:
    print(user_input - 273.15, "° Celcius")
elif user_choice == 6:
    print((user_input - 273.15) * 9/5 + 32, "° Fahrenheit")