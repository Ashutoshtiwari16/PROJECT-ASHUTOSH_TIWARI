from analytics import get_expenses

def generate_insights():
    expenses = get_expenses()

    if not expenses:
        return "No expenses available for analysis."

    total = sum(expense[1] for expense in expenses)

    insights = []

    if total > 10000:
        insights.append("Your total spending is quite high. Try to reduce unnecessary expenses.")

    if total < 5000:
        insights.append("Your spending is currently under control. Keep maintaining your budget.")

    return insights

print(generate_insights())