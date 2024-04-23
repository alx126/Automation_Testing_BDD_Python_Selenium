from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    PRODUCT_ITEM = (By.CLASS_NAME, "product-item")
    PRODUCT_TITLE = (By.CLASS_NAME, "product-title")

    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "product-box-add-to-cart-button")
    ADD_TO_WISHLIST_BUTTON = (By.CLASS_NAME, "add-to-wishlist-button")

    CONFIRMATION_MESSAGE = (By.CLASS_NAME, "bar-notification.success")
    CONFIRMATION_MESSAGE_TEXT_1 = (By.XPATH, '//*[@id="bar-notification"]//p[text()]')
    CONFIRMATION_MESSAGE_TEXT_2 = (By.XPATH, '//*[@id="bar-notification"]//a[text()]')
    CONFIRMATION_MESSAGE_LINK = (By.XPATH, '//*[@id="bar-notification"]//a')

    SHOPPING_CART_LINK = 'https://demo.nopcommerce.com/cart'
    WISHLIST_LINK = 'https://demo.nopcommerce.com/wishlist'

    def are_all_products_displayed(self):
        self.wait_for_element_to_be_present(self.PRODUCT_ITEM, 3)
        product_item_list = self.find_all(self.PRODUCT_ITEM)
        # assert len(product_item_list) > 0
        for item in product_item_list:
            if not item.is_displayed():
                return False

        return True

    def are_all_titles_containing_text(self, text: str):
        titles_list = self.find_all(self.PRODUCT_TITLE)
        # assert len(titles_list) > 0
        for title in titles_list:
            if text.lower() not in title.text.lower():
                return False

        return True

    def click_add_to_cart_button(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def click_add_to_wishlist_button(self):
        self.click(self.ADD_TO_WISHLIST_BUTTON)

    def is_confirmation_message_displayed(self):
        assert self.wait_for_element_to_be_present(self.CONFIRMATION_MESSAGE, 1).is_displayed() == True
        # assert self.wait_for_element_to_be_present(self.CONFIRMATION_MESSAGE_TEXT, 1).text == text
        # return self.find(self.CONFIRMATION_MESSAGE)

    def is_confirmation_message_containing_text(self, text):
        assert self.wait_for_text_to_be_present_in_element(self.CONFIRMATION_MESSAGE_TEXT_1, text, 1)

    def is_confirmation_message_text_displayed(self, text):
        message = self.wait_get_element_text(self.CONFIRMATION_MESSAGE_TEXT_1, 2)
        assert message == text, f'The message is: {message}'

    def is_confirmation_message_containing_link_to_cart(self):
        assert self.find(self.CONFIRMATION_MESSAGE_LINK).get_attribute('href') == self.SHOPPING_CART_LINK

    def is_confirmation_message_containing_link_to_wishlist(self):
        assert self.find(self.CONFIRMATION_MESSAGE_LINK).get_attribute('href') == self.WISHLIST_LINK
