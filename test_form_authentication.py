import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from allure import attach, title, description, feature, story
from allure_commons.types import AttachmentType
from base_test import BaseTest #Import BaseTest file


@feature("Form Authentication")
class TestFormAuthentication(BaseTest):

    @story("Successful Login")
    @title("Test successful login with valid credentials")
    @description("This test verifies that a user can log in with correct credentials and is redirected to the secure area.")
    def test_successful_login(self):
        
        try:
            self.driver.get("https://the-internet.herokuapp.com/login")
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys("tomsmith")

            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys("SuperSecretPassword!")

            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()

            success_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "flash.success"))
            )

            assert "You logged into a secure area!" in success_message.text
            assert "secure" in self.driver.current_url
            attach(self.driver.get_screenshot_as_png(), name="Login Successful", attachment_type=AttachmentType.PNG)

        except Exception as e:
            attach(self.driver.get_screenshot_as_png(), name="Login Failed", attachment_type=AttachmentType.PNG)
            pytest.fail(f"Login test failed: {str(e)}")

    @story("Invalid Login")
    @title("Test login with invalid username")
    @description("This test verifies that an error message is displayed when logging in with an invalid username.")
    def test_invalid_username(self):
        
        try:
            self.driver.get("https://the-internet.herokuapp.com/login")
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys("invaliduser")

            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys("SuperSecretPassword!")

            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()

            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "flash.error"))
            )

            assert "Your username is invalid!" in error_message.text
            attach(self.driver.get_screenshot_as_png(), name="Invalid Username - Error Message", attachment_type=AttachmentType.PNG)

        except Exception as e:
            attach(self.driver.get_screenshot_as_png(), name="Invalid Username - Test Failed", attachment_type=AttachmentType.PNG)
            pytest.fail(f"Invalid username test failed: {str(e)}")

    @story("Invalid Login")
    @title("Test login with invalid password")
    @description("This test verifies that an error message is displayed when logging in with an invalid password.")
    def test_invalid_password(self):
        
        try:
            self.driver.get("https://the-internet.herokuapp.com/login")
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys("tomsmith")

            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys("wrongpassword")

            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()

            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "flash.error"))
            )

            assert "Your password is invalid!" in error_message.text
            attach(self.driver.get_screenshot_as_png(), name="Invalid Password - Error Message", attachment_type=AttachmentType.PNG)

        except Exception as e:
            attach(self.driver.get_screenshot_as_png(), name="Invalid Password - Test Failed", attachment_type=AttachmentType.PNG)
            pytest.fail(f"Invalid password test failed: {str(e)}")

    @story("Invalid Login")
    @title("Test login with empty credentials")
    @description("This test verifies that an error message is displayed when attempting to log in with empty credentials.")
    def test_empty_credentials(self):
        
        try:
            self.driver.get("https://the-internet.herokuapp.com/login")
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys("")

            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys("")

            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()

            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "flash.error"))
            )

            assert "Your username is invalid!" in error_message.text
            attach(self.driver.get_screenshot_as_png(), name="Empty Credentials - Error Message", attachment_type=AttachmentType.PNG)

        except Exception as e:
            attach(self.driver.get_screenshot_as_png(), name="Empty Credentials - Test Failed", attachment_type=AttachmentType.PNG)
            pytest.fail(f"Empty credentials test failed: {str(e)}")
