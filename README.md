## Python Assignment: Pizza Ordering System

### Objective:
Create a program that simulates a pizza ordering system. The program should allow the user to choose a pizza size and calculate the total cost based on the selected size.

### Instructions:
1. **Input**: Prompt the user to enter their name and choose a pizza size (small, medium, or large).
2. **Variables**: Store the user's name, chosen pizza size, and the corresponding price in variables.
3. **Conditional Statements**: Use `if`, `elif`, and `else` statements to determine the price based on the chosen pizza size.
4. **Output**: Print a message with the user's name, chosen pizza size, and the total cost.

### Requirements:
1. The program should display a menu with the following pizza sizes and prices:
   - Small: $8.00
   - Medium: $10.00
   - Large: $12.00
2. The user should be able to select a pizza size and see the total cost.
3. The program should handle invalid inputs gracefully.

### Example:
```python
def main():
    # Step 1: Display menu
    print("Welcome to the Pizza Ordering System!")
    print("Pizza Sizes and Prices:")
    print("1. Small: $8.00")
    print("2. Medium: $10.00")
    print("3. Large: $12.00")

    # Step 2: Get user input
    name = input("Please enter your name: ")
    size = input("Please choose a pizza size (small, medium, large): ").lower()

    # Step 3: Initialize variables
    price = 0

    # Step 4: Determine price based on pizza size
    if size == "small":
        price = 8.00
    elif size == "medium":
        price = 10.00
    elif size == "large":
        price = 12.00
    else:
        print("Invalid size selected. Please choose small, medium, or large.")
        return

    # Step 5: Output the order summary
    print(f"\nOrder Summary:")
    print(f"Name: {name}")
    print(f"Pizza Size: {size.capitalize()}")
    print(f"Total Cost: ${price:.2f}")

if __name__ == "__main__":
    main()
```

### Additional Challenge (Optional):
- Add functionality to allow the user to order multiple pizzas and calculate the total cost.
- Include options for additional toppings with corresponding prices.

---

Feel free to adjust the assignment as needed for your class! If you have any other requirements or need further assistance, let me know.
```
