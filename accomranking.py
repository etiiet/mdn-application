# Get the number of accommodations the user is interested in
while True:
    try:
        numberOfAccom = int(input('Enter how many places you are interested in: '))
        break
    except ValueError:
        print('Invalid input, try again.')

# Initialize a list to store user preferences
preferences = []

# Loop through each accommodation and gather user input
for i in range(1, numberOfAccom + 1):
    response = input(f'Do you like place {i}? (Y/N): ')
    preferences.append({'Place': i, 'Response': response})

# After gathering preferences, you can print them or process them further
print("\nYour preferences:")
for preference in preferences:
    print(f"Place {preference['Place']}: {'Liked' if preference['Response'].upper() == 'Y' else 'Not Liked'}")
