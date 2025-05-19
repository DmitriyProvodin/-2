from src.models import Product, Category
from src.load_data import load_categories_from_json


if __name__ == "__main__":
    # Ручное создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Вывод атрибутов каждого продукта
    for product in [product1, product2, product3]:
        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity)

    # Создание категории и вывод атрибутов
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.name)
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    # Ещё один продукт и категория
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4]
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    for p in category2.products:
        print(p.name, p.price)

    print(Category.category_count)
    print(Category.product_count)

    # Загрузка из JSON (доп. задание)
    print("\nЗагрузка из файла products.json...\n")
    categories = load_categories_from_json("data/products.json")
    for category in categories:
        print(f"{category.name} ({len(category.products)} товаров):")
        for product in category.products:
            print(f"- {product.name}: {product.price}₽ ({product.quantity} шт.)")

    print(f"\nВсего категорий (с учётом загрузки из файла): {Category.category_count}")
    print(f"Всего товаров (с учётом загрузки из файла): {Category.product_count}")
