# Example login data where passwordRevisionDate is present
login_data = {
    'username': 'user123',
    'password': 'securepassword',
    'passwordRevisionDate': '2023-06-01'
}

# Example login data where passwordRevisionDate is not present
# login_data = {
#     'username': 'user123',
#     'password': 'securepassword'
# }

# Login data is None
# login_data = None

if login_data and 'passwordRevisionDate' in login_data:
    print("Password revision date is available.")
    # You can access the password revision date here
    password_revision_date = login_data['passwordRevisionDate']
    print(f"Password was last revised on: {password_revision_date}")
else:
    print("Password revision date is not available.")

