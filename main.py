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
