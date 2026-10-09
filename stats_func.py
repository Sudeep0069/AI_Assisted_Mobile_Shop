from mobile_shop import mobiles
def shop_statistics():
    total_models = len(mobiles)

    total_stock = sum(
        mobile["stock"] for mobile in mobiles
    )

    average_price = (
        sum(mobile["price"] for mobile in mobiles) / total_models
        if total_models else 0
    )

    highest_rated = max(
        mobiles,
        key=lambda mobile: mobile["rating"],
        default=None
    )

    return {
        "total_models": total_models,
        "total_stock": total_stock,
        "average_price": average_price,
        "highest_rated": highest_rated
    }