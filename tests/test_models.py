import pytest
from src.models import Product, Category


def test_product_init():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_init_and_counts():
    # Сбросим счётчики для теста
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Product 1", "Desc", 100.0, 5)
    p2 = Product("Product 2", "Desc", 200.0, 2)
    cat = Category("Category 1", "Desc", [p1, p2])

    assert cat.name == "Category 1"
    assert cat.description == "Desc"
    assert len(cat.products) == 2

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_multiple_categories_count():
    # Сбросим счётчики для теста
    Category.category_count = 0
    Category.product_count = 0

    cat1 = Category("Cat1", "Desc", [])
    cat2 = Category("Cat2", "Desc", [])
    cat3 = Category("Cat3", "Desc", [])

    assert Category.category_count == 3
    assert Category.product_count == 0
