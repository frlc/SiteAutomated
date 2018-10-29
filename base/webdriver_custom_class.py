from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from selenium import webdriver


class WebDriverCustomClass:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        elements = self.driver.find_elements(by, value)
        return elements

    def click_on_element(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def send_keys_to(self, by, value, data=""):
        element = self.find_element(by, value)
        element.send_keys(data)

    def hover_over_an_element_and_click_on(self, by, value):
        try:

            element = self.find_element(by, value)
            hover = ActionChains(self.driver)
            hover.move_to_element(element).perform()
        except:
            raise Exception("Elemento {0} não está visivel!".format(value))

    def hover_over_an_element(self, element, by, value):
        try:
            element = self.find_element(by, value)
            hover = ActionChains(self.driver)
            hover.move_to_element(element).perform()
            self.is_element_visible(element).click()
        except:
            raise Exception("Elemento {0} não está visivel!".format(element))

    # retirar?
    def hover_over_first_element_click_on_second(self, *args):
        locator_1, locator_type_1, locator_2, locator_type_2, locator_3, locator_type_3 = args
        locator_type_1.lower()
        locator_type_2.lower()
        locator_type_3.lower()
        main_button = self.get_element(locator_1, locator_type_1)
        second_button = self.get_element(locator_2, locator_type_2)
        third_element = self.get_element(locator_3, locator_type_3)
        hover = ActionChains(self.driver)
        hover.move_to_element(main_button).pause(1).move_to_element(second_button).pause(1).perform()
        third_element.click()

    def scroll_into_view(self, by, value):
        try:
            element = self.find_element(by, value)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            raise Exception("Elemento {0} não está visivel!".format(element))

    def is_element_visible(self, by, value):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((by, value)))
            return True
        except:
            raise Exception("Elemento {0} não está visivel!".format(value))

    def is_element_clickable(self, by, value):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((by, value)))
            return True
        except:
            raise Exception("Elemento {0} não está visivel!".format(value))

    def click_on_returned_element(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def fill_element(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def element_wait(self, by, value):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(by, value))
