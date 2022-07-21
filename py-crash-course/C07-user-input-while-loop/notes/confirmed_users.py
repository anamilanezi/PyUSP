# Start with users that need to be verified, and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user into the list of confirmed users.
# The loop runs as long as the list unconfirmed_users is not empty
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed: ")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())