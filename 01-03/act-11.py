phones = {
    ("Ahmed", "Abdullah"): "555-1234",
    ("Hassan", "Raza"): "555-5678",
    ("Aashir", "Wayne"): "555-9012",
}

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

search_key = (first_name, last_name)
if search_key in phones:
    print(f"{first_name} {last_name}'s phone number is: {phones[search_key]}")
else:
    print("Name not found.")
