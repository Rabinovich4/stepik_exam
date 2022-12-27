from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        url = self.browser.current_url
        assert "login" in url, '"login" not found in url'
        login_link.click()

    def should_be_login_form(self):
        self.should_be_login_url()
        assert self.is_element_present(*LoginPageLocators.AUTORIZATION_FORM), 'AUTORIZATION_FORM is not found'

    def should_be_register_form(self):
        self.should_be_login_url()
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'REGISTRATION_FORM is not found'
