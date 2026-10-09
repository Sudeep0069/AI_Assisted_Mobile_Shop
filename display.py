from inventory_search import *
from update_func import *
from stats_func import *
def display_mobiles(data):
    if not data:
        return "No mobiles found."

    text = ""

    for mobile in data:
        text += f"""
### 📱 {mobile['brand']} {mobile['model']}

ID: {mobile['id']}

Price: ₹{mobile['price']:,}

RAM: {mobile['ram']}

Storage: {mobile['storage']}

Rating: ⭐ {mobile['rating']}

Stock: {mobile['stock']}

---
"""

    return text


def show_inventory():
    return display_mobiles(get_all_mobiles())


def search_ui(keyword):
    return display_mobiles(search_mobile(keyword))


def budget_ui(budget):
    return display_mobiles(search_by_budget(budget))


def add_ui(brand, model, price, ram, storage, rating, stock):
    mobile = add_mobile(
        brand, model, price, ram, storage, rating, stock
    )

    return f"✅ Mobile added\n\n{mobile}"


def delete_ui(mobile_id):
    result = delete_mobile(int(mobile_id))

    if result:
        return "✅ Mobile deleted."

    return "❌ Mobile not found."


def purchase_ui(mobile_id):
    result = purchase_mobile(int(mobile_id))
    return result["message"]


def statistics_ui():
    data = shop_statistics()
    best = data["highest_rated"]

    best_text = (
        f"{best['brand']} {best['model']} — ⭐ {best['rating']}"
        if best else "No mobiles available."
    )

    return f"""
# 📊 Shop Statistics

**Total Models:** {data['total_models']}

**Total Stock:** {data['total_stock']}

**Average Price:** ₹{data['average_price']:,.2f}

**Highest Rated:** {best_text}
"""