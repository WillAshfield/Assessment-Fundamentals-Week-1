"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_to_basket(item: dict) -> list:
    """Add an item to the basket."""
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    """Generate a receipt from the basket."""
    if not basket:
        return "Basket is empty"

    # Generate the receipt string
    item_count = {}

    for item in basket:
        # Check if the item has already been seen with counts
        key = (item['name'], item['price'])

        if key in item_count:
            item_count[key] += 1
        else:
            item_count[key] = 1

    receipt = ""
    total = 0

    for (name, price), quantity in item_count.items():
        item_total = price * quantity
        total += item_total

        name_formatted = f"{name} x {quantity}"
        price_formatted = "Free" if item_total == 0 else f"£{item_total:.2f}"

        receipt += f"{name_formatted} - {price_formatted}\n"

    receipt += f"Total: £{total:.2f}"

    return receipt  # return the receipt string


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    finished_receipt = generate_receipt(basket)

    print("```")
    print(finished_receipt)
    print("```")
