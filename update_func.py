from mobile_shop import mobiles
def add_mobile(brand, model, price, ram, storage, rating, stock):
    new_id = max(
        [mobile["id"] for mobile in mobiles],
        default=0
    ) + 1

    mobile = {
        "id": new_id,
        "brand": brand,
        "model": model,
        "price": int(price),
        "ram": ram,
        "storage": storage,
        "rating": float(rating),
        "stock": int(stock)
    }

    mobiles.append(mobile)
    return mobile


def delete_mobile(mobile_id):
    for mobile in mobiles:
        if mobile["id"] == mobile_id:
            mobiles.remove(mobile)
            return True

    return False


def purchase_mobile(mobile_id):
    for mobile in mobiles:
        if mobile["id"] == mobile_id:
            if mobile["stock"] > 0:
                mobile["stock"] -= 1

                return {
                    "success": True,
                    "message": "Purchase successful",
                    "mobile": mobile
                }

            return {
                "success": False,
                "message": "Mobile is out of stock"
            }

    return {
        "success": False,
        "message": "Mobile not found"
    }