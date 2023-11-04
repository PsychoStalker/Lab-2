def find_min_max(input_list):
    if not input_list:
        return []

    min_temp = min(input_list)
    max_temp = max(input_list)

    return [min_temp, max_temp]

# Example usage:
temperature_list = [25.5, 30.2, 22.1, 27.8, 18.9]
min_max_temperatures = find_min_max(temperature_list)
print("Minimum and Maximum Temperatures:", min_max_temperatures)

def sort_temperature(input_list):
    if not input_list:
        return []

    sorted_list = sorted(input_list)

    return sorted_list

# Example usage:
temperature_list = [25.5, 30.2, 22.1, 27.8, 18.9]
sorted_temperatures = sort_temperature(temperature_list)
print("Sorted Temperatures:", sorted_temperatures)