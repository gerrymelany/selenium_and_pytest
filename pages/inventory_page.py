from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

class InventoryPage(BasePage):
    inventory_items_locator = (By.CLASS_NAME, "inventory_item")
    inventory_images_locator = (By.CLASS_NAME, "inventory_item_img")
    cart_button_locator_template = "//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
    dropdown_order_locator = (By.CLASS_NAME, "product_sort_container")

    def get_item_count(self):
        return len(self.driver.find_elements(*self.inventory_items_locator))

    def click_item(self, item_name):
        item_locator = (By.XPATH, self.cart_button_locator_template.format(item_name=item_name))
        self.click_element(item_locator)

    def get_item_button_text(self, item_name):
        item_locator = (By.XPATH, self.cart_button_locator_template.format(item_name=item_name))
        element = self.wait_for_element(item_locator)
        return element.text

    def item_is_in_cart(self, item_name):
        return self.get_item_button_text(item_name) == "Remove"

    def order_by_name(self):
        order_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.select_from_dropdown_by_visible_text(order_dropdown, "Name (A to Z)")

    def order_by_price(self):
        order_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.select_from_dropdown_by_visible_text(order_dropdown, "Price (low to high)")

    def get_dropdown_options(self):
        return self.get_select_options(self.dropdown_order_locator)