import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "expenses.csv"

# Function to load data
def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        return pd.DataFrame(columns=["Date", "Category", "Amount"])

# Save data function
def save_data(df):
    df.to_csv(FILE_NAME, index=False)

# Streamlit UI
st.title("💰 Expense Tracker Web App")

st.sidebar.header("Add New Expense")

date = st.sidebar.date_input("Select Date")
category = st.sidebar.text_input("Enter Category (Food, Travel, etc.)")
amount = st.sidebar.number_input("Enter Amount", min_value=0.0, step=0.5)

if st.sidebar.button("Add Expense"):
    df = load_data()
    new_data = {"Date": date, "Category": category, "Amount": amount}
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    save_data(df)
    st.sidebar.success("Expense Added Successfully!")

# Display Data
st.subheader("📄 Expense Records")
df = load_data()

if df.empty:
    st.info("No expenses recorded yet. Add some!")
else:
    st.write(df)

    # Summary
    st.subheader("📊 Expense Summary by Category")
    summary = df.groupby("Category")["Amount"].sum()

    st.write(summary)

    # Pie Chart
    st.subheader("🟠 Spending Distribution (Pie Chart)")
    fig1, ax1 = plt.subplots()
    ax1.pie(summary, labels=summary.index, autopct='%1.1f%%')
    ax1.axis("equal")
    st.pyplot(fig1)

    # Bar Chart
    st.subheader("🔵 Spending by Category (Bar Chart)")
    st.bar_chart(summary)
