import datetime

user_name = input("What is your name? ")
user_age = int(input("How old are you? "))

current_year = datetime.datetime.now().year
birth_year = current_year - user_age

print(f"Hello {user_name}! You were born in {birth_year}.")