import streamlit as st

from database import create_table, add_expense, get_total_expenses
create_table()

# Page configuration
st.set_page_config(
    page_title="AI Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# Title
st.title("💰 AI Expense Tracker")

# Subtitle
st.write("Track your expenses and understand your spending.")

# Sidebar
st.sidebar.header("Add Expense")

amount = st.sidebar.number_input(
    "Amount (₹)",
    min_value=0.0,
    step=10.0
)

category = st.sidebar.selectbox(
    "Category",
    ["Food", "Travel", "Shopping", "Education", "Entertainment", "Other"]
)

description = st.sidebar.text_input("Description")

if st.sidebar.button("Add Expense"):
    add_expense(amount, category, description)
    st.success(f"Expense of ₹{amount} added successfully!")

# Dashboard
st.header("📊 Dashboard")

col1, col2, col3 = st.columns(3)

total_expenses = get_total_expenses()

with col1:
    st.metric("Total Expenses", f"₹{total_expenses:.2f}")

with col2:
    st.metric("This Month", "₹0")

with col3:
    st.metric("Savings", "₹0")

st.info("Your expense analytics will appear here.")