# calculate revenue by category by building a function
orders = [
    {"item": "Keyboard", "category": "Electronics", "price": 75, "status": "completed"},
    {"item": "Guitar Strings", "category": "Music", "price": 15, "status": "completed"},
    {"item": "Laptop", "category": "Electronics", "price": 1200, "status": "cancelled"},
    {"item": "Mouse", "category": "Electronics", "price": 25, "status": "completed"},
    {"item": "Studio Monitor", "category": "Music", "price": 300, "status": "pending"}
]

def calculate_revenue(orders: list, category: str):
    total = 0
    for item in orders:
        if item["category"] == category and  item["status"] == "completed":
            total += item["price"]

    return total

print(calculate_revenue(orders, "Electronics"))
print(calculate_revenue(orders, "Music"))
