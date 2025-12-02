names = []
phone_numbers = []
num = int(input("Enter the number of contact(s) you want to save: "))
for i in range(num):
    name = names.append(input("Enter the name of the contact: "))
    phone_numbers.append(input("Enter the phone number of the contact: "))

print("\n Names \t\t\t Phone numbers \n")
for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))
search_term = input("Enter the search term: ")
if search_term in names:
    index = names.index(search_term)
    phone_numbers = phone_numbers[index]
    print("Name: {},\nPhone Number: {} ".format(search_term,phone_number))
else:
    print("Name not found")