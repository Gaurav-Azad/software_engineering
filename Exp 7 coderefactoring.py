data = [10, 20, 30, 10, 40, 30]
unique_data = []
for item in data:
    if item not in unique_data:
        unique_data.append(item)

total = 0
for item in unique_data:
    total += item
average = total / len(unique_data)
print("Average is", average)
##################################code refactoring ######################################
def remove_duplicates(data):
    """Remove duplicates from a list while maintaining order."""
    return list(dict.fromkeys(data))

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0  # Avoid division by zero
    return sum(numbers) / len(numbers)

def main():
    data = [10, 20, 30, 10, 40, 30]
    
    unique_data = remove_duplicates(data)
    average = calculate_average(unique_data)
    print("Average is", average)

if __name__ == "__main__":
    main()
