import pytest

from conftest import standard_user_page


def test_iventory_elements_count(standard_user_page):
    assert standard_user_page.get_item_count() == 6, "El número de elementos en el inventario no es 6 para standard_user."

def test_add_to_cart_(standard_user_page):
    item_name = "Sauce Labs Backpack"
    standard_user_page.click_item(item_name)
    assert standard_user_page.item_is_in_cart(item_name), f"El ítem '{item_name}' no fue agregado al carrito correctamente."

def test_add_to_cart_button_changes(standard_user_page):
    initial_text = standard_user_page.get_item_button_text("Sauce Labs Backpack")
    assert initial_text == "Add to cart"
    standard_user_page.click_item("Sauce Labs Backpack")
    updated_text = standard_user_page.get_item_button_text("Sauce Labs Backpack")
    assert updated_text == "Remove"

def test_deporte_dropdown_options(standard_user_page):
    options = standard_user_page.get_dropdown_options()
    expected_options = ["Name (A to Z)", "Name (Z to A)","Price (low to high)", "Price (high to low)"]
    assert all(
        option in options for option in expected_options
    ), "No todas las opciones esperadas están presentes en el dropdown de filtro de productos."
