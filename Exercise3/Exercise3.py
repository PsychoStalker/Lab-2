def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input("Enter numbers separated by commas: ")
    input_list = user_input.split(",")
    number_list = []

    for item in input_list:
        try:
            number_list.append(float(item))
        except ValueError:
            print(f"Skipping invalid input: {item}")

    return number_list

# Example usage:
display_main_menu()
numbers = get_user_input()
print("List of numbers:", numbers)