from mobile_shop import mobiles
def get_all_mobiles():
    return mobiles


def search_mobile(keyword):
    keyword = keyword.lower()

    result = list(
        filter(
            lambda mobile:
            keyword in mobile["brand"].lower()
            or keyword in mobile["model"].lower(),
            mobiles
        )
    )

    return result


def search_by_budget(budget):
    result = list(
        filter(
            lambda mobile: mobile["price"] <= budget,
            mobiles
        )
    )

    # Highest rating first
    result = sorted(
        result,
        key=lambda mobile: mobile["rating"],
        reverse=True
    )

    return result