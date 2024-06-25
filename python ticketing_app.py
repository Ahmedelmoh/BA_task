import os
import json
from datetime import datetime

# Load categories from external file
def load_categories(filename='categories.txt'):
    with open(filename, 'r') as file:
        categories = [line.strip() for line in file.readlines()]
    return categories

# Display the main menu
def display_menu():
    print("Technical Support Ticketing System")
    print("1. Log a new ticket")
    print("2. View existing tickets")
    print("3. Exit")

# Log a new ticket
def log_ticket(tickets, categories):
    print("Log a New Ticket")
    print("Select a category:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    category_choice = int(input("Enter the category number: ")) - 1
    if 0 <= category_choice < len(categories):
        category = categories[category_choice]
        description = input("Enter the issue description: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ticket = {"category": category, "description": description, "timestamp": timestamp}
        tickets.append(ticket)
        save_tickets(tickets)
        print("Ticket logged successfully!")
    else:
        print("Invalid category selected.")

# View existing tickets
def view_tickets(tickets):
    print("Existing Tickets:")
    if not tickets:
        print("No tickets found.")
    else:
        for i, ticket in enumerate(tickets, 1):
            print(f"Ticket {i}:")
            print(f"  Category: {ticket['category']}")
            print(f"  Description: {ticket['description']}")
            print(f"  Timestamp: {ticket['timestamp']}")
            print("-" * 20)

# Save tickets to a file
def save_tickets(tickets, filename='tickets.json'):
    with open(filename, 'w') as file:
        json.dump(tickets, file, indent=4)

# Load tickets from a file
def load_tickets(filename='tickets.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tickets = json.load(file)
    else:
        tickets = []
    return tickets

def main():
    categories = load_categories()
    tickets = load_tickets()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            log_ticket(tickets, categories)
        elif choice == '2':
            view_tickets(tickets)
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
