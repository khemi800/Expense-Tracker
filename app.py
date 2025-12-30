import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "expenses.csv"

# Load data function
def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        return pd.DataFrame(columns=["Date", "Category", "Amount"])

# Save data function
def save_data(df):
    df.to_csv(FILE_NAME, index=False)

# Add expense
def add_expense(date, category, amount):
    df = load_data()
    new_row = {"Date": date, "Category": category, "Amount": amount}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)
    print("Expense Added Successfully!")

# Show all expenses
def show_expenses():
    df = load_data()
    if df.empty:
        print("No expenses recorded yet.")
        return
    print("\n📄 Expense Records")
    print(df)

# Show summary & charts
def show_summary():
    df = load_data()
    if df.empty:
        print("No expenses available for summary.")
        return

    summary = df.groupby("Category")["Amount"].sum()
    print("\n📊 Expense Summary by Category")
    print(summary)

    # Pie Chart
    plt.figure()
    summary.plot.pie(autopct='%1.1f%%')
    plt.title("Spending Distribution")
    plt.axis("equal")
    plt.show()

    # Bar Chart
    plt.figure()
    summary.plot(kind="bar")
    plt.title("Spending by Category")
    plt.ylabel("Amount")
    plt.show()


# ---- Simple CLI Menu ----
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        date = input("Enter Date (YYYY-MM-DD): ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))
        add_expense(date, category, amount)

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        show_summary()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")

