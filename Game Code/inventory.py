# inventory.py
import time
import keyboard

inventory_items = {}  # Dictionary to store items and their counts

def pick_up_item(cell):
    """Add items from the provided cell to the inventory."""
   # print("Debug: Cell contents in pick_up_item:", cell)  # Debug statement

    if "items" in cell and cell["items"]:  # Check if there are items in the cell
        for item in cell["items"]:
            if item in inventory_items:
                inventory_items[item] += 1  # Increment the count if item exists
            else:
                inventory_items[item] = 1  # Add the item with count 1 if it doesn't exist
            print(f"You picked up a {item}!")
        cell["items"] = []  # Clear items from cell after picking up
    else:
        print("There is nothing to pick up here.")
    time.sleep(0.5)

def show_inventory():
    """Display the player's inventory."""
    print("Inventory (press 'e' to exit)")
    last_displayed_inventory = None  # Track the last displayed inventory state

    while True:
        # Only display inventory if it has changed
        if last_displayed_inventory != inventory_items:
            if inventory_items:
                for item, count in inventory_items.items():
                    print(f"{item}: {count}")
            else:
                print("Your inventory is empty.")
            last_displayed_inventory = inventory_items.copy()  # Update the last displayed inventory state

        # Exit the inventory if 'e' is pressed
        if keyboard.is_pressed('e'):
            print("Exiting inventory.")
            time.sleep(0.5)
            break

        time.sleep(0.1)  # Small delay to reduce CPU usage
