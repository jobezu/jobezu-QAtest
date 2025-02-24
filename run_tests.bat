@echo off
pytest --alluredir=QA-test-results
allure serve QA-test-results