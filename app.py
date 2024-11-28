def get_group_members():
    """Collect group member names."""
    group_members = []
    while True:
        group_member_name = input("Enter member name or ('c' if all members are added): ")
        if group_member_name.lower() == 'c':
            if group_members:
                break
            else:
                print("You must add at least one member.")
        else:
            group_members.append(group_member_name.title())
    return group_members


def collect_expenses():
    """Collect details of all expenses."""
    expenses = []
    while True:
        expense_name = input("Enter the name of the expense (or type 'q' to finish adding expenses): ")
        if expense_name.lower() == 'q':  # Exit the loop
            break
        else:
            try:
                item_count = int(input(f"How many items of {expense_name.title()}? "))
                item_price = float(input(f"Enter the price of one {expense_name.title()}: "))
                total_expense_price = item_count * item_price
                expenses.append((expense_name.title(), total_expense_price))
            except ValueError:
                print("Invalid input. Please enter numeric values for item count and price.")
    return expenses


def calculate_total(expenses):
    """Calculate the total expense."""
    return sum(expense[1] for expense in expenses)


def display_results(group_members, expenses, total_amount):
    """Display all results in a structured format."""
    print("\n------ EXPENSE SPLITTER ------")
    print(f"Group Members: {len(group_members)} ({', '.join(group_members)})")
    
    # Expense details
    print("\n----- EXPENSE DETAILS -----")
    print(f"{'Expense Name':<23} {'Total Amount ($)':<15}")
    print("-" * 39)
    for expense_name, expense_price in expenses:
        print(f"{expense_name:<23} ${expense_price:<15.2f}")
    
    # Summary
    expense_per_person = total_amount / len(group_members)
    print("\n----- SUMMARY -----")
    print(f"{'Total Group Expense:':<23} ${total_amount:.2f}")
    print(f"{'Expense per Person:':<23} ${expense_per_person:.2f}")
    
    # Amount split
    print("\n----- AMOUNT SPLIT -----")
    for member_name in group_members:
        print(f"{member_name:<23} ${expense_per_person:.2f}")
    
    print("-" * 39)
    print("Thank you for using EXPENSE SPLITTER!")

# Main Program
group_members = get_group_members()
expenses = collect_expenses()
total_amount = calculate_total(expenses)
display_results(group_members, expenses, total_amount)