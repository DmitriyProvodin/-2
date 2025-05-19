import json
from src.models import Category, Product


def load_categories_from_json(filepath: str) -> list[Category]:
    with open(filepath, encoding='utf-8') as file:
        data = json.load(file)

    categories = []
    for cat in data:
        products = [
            Product(
                name=p["name"],
                description=p["description"],
                price=p["price"],
                quantity=p["quantity"]
            )
            for p in cat["products"]
        ]
        category = Category(
            name=cat["name"],
            description=cat["description"],
            products=products
        )
        categories.append(category)

    return categories
