import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/50be865c4d5094ed05822ad31f3bfc7d/flightDeals/users'

print("Welcome to Kanishk's Flight Club.")
print("We find the best flight deals for you.")
first_name = input("What is your first name? : ")
last_name = input("Enter your second name?: ")
email = input("Enter your email: ")
email2 = input("Enter your email again: ")

if email == email2:
    user_data = {
        "First Name": first_name,
        "Last Name": last_name,
        "Email": email2
    }
    responses = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}", json=user_data)
    print(responses.text)
    print("Your email is verified")
else:
    print("Pls enter the email correctly.")
