import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from allure import attach, title, description, feature, story
from allure_commons.types import AttachmentType
from base_test import BaseTest

@feature("File Uploaded")
class TestFileUpload(BaseTest):

    @story("Successful Upload")
    @title("Test successful file upload")
    @description("This test verifies that a file can be successfully uploaded to the server.")
    def test_successful_file_upload(self):
        
        try:
            self.upload_url = "https://the-internet.herokuapp.com/upload"
            self.file_path = r"C:\Users\Betancourt\Downloads\royal-blue.png"  

            
            if not os.path.exists(self.file_path):
                pytest.fail(f"Error: File not found at {self.file_path}")
                return  # Exit test if the file does not exist

            self.driver.get(self.upload_url)
            file_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "file-upload"))
            )
            file_input.send_keys(self.file_path)

            upload_button = self.driver.find_element(By.ID, "file-submit")
            upload_button.click()

            success_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "example"))
            )
            assert "File Uploaded!" in success_message.text
            attach(self.driver.get_screenshot_as_png(), name="File Uploaded", attachment_type=AttachmentType.PNG)

        except Exception as e:
            attach(self.driver.get_screenshot_as_png(), name="File Upload Failed", attachment_type=AttachmentType.PNG)
            pytest.fail(f"Error during file upload: {str(e)}")

    @story("File Doesn't Exist")
    @title("Test handling when the file does not exist")
    @description("This test verifies that an error is handled if the upload file isn't found")
    def test_non_existent_file(self):
        try:
            self.upload_url = "https://the-internet.herokuapp.com/upload"
            self.file_path = r"C:\Users\Betancourt\Downloads\NONEXISTENT_FILE.png"  # A file that will NOT exist

            
            self.driver.get(self.upload_url)
            with pytest.raises(Exception) as excinfo:
                file_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "file-upload"))
                )
                file_input.send_keys(self.file_path)

                upload_button = self.driver.find_element(By.ID, "file-submit")
                upload_button.click()

            success_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "example"))
            )

        except Exception as e:
            attach(self.driver.get_screenshot_as_png(), name="File Upload NonExistent - Test Failed", attachment_type=AttachmentType.PNG)
            pytest.fail(f"Error during file upload: {str(e)}")
