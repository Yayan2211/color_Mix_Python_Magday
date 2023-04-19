# Define a dictionary to map primary color combinations to their corresponding secondary colors
secondary_colors = {
    ('red', 'yellow'): 'orange',
    ('red', 'blue'): 'purple',
    ('yellow', 'blue'): 'green',
    ('blue', 'green'): 'cyan',
    ('red', 'green'): 'brown',
    ('yellow', 'purple'): 'brown',
    ('orange', 'green'): 'brown',
    ('orange', 'purple'): 'brown',
    ('brown', 'blue'): 'gray',
    ('brown', 'yellow'): 'gray',
    ('brown', 'green'): 'gray',
    ('brown', 'orange'): 'gray',
    ('brown', 'red'): 'gray',
    ('gray', 'yellow'): 'olive',
    ('gray', 'blue'): 'indigo',
    ('gray', 'green'): 'teal',
    ('gray', 'red'): 'maroon',
    ('gray', 'purple'): 'lavender'
}

while True:
    # Get input from user for the first color
    first_color = input("Enter first color: ").lower()

    # Get input from user for the second color
    second_color = input("Enter second color: ").lower()

    # Check if the entered colors are valid primary colors
    if (first_color, second_color) not in secondary_colors.keys() and (second_color, first_color) not in secondary_colors.keys():
        print("Invalid input! Please enter valid primary colors.")
    else:
        # Mix the entered colors to get the secondary color
        mixed_color = secondary_colors.get((first_color, second_color), secondary_colors.get((second_color, first_color)))
        print(f"{first_color} + {second_color} = {mixed_color}")

    # Ask user if they want to input another color
    another_color = input("Do you want to input another color? (yes/no): ").lower()
    if another_color != 'yes':
        break

print("Program terminated.")
