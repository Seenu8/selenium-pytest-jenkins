import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

def test_register_page(driver):
    driver.get('https://demo.automationtesting.in/Register.html')

    # Fill name fields
    driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("seenu")
    driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Vasan")

    # Select Gender
    driver.find_element(By.XPATH, "//input[@value='Male']").click()

    # Select Hobbies
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for box in checkboxes:
        if box.get_attribute("value") == "Movies":
            box.click()

    # Select skill
    skill_dropdown = driver.find_element(By.ID, "Skills")
    Select(skill_dropdown).select_by_index(1)

    # Navigate to Google and back
    driver.get("https://www.google.co.in/")
    driver.back()

    # Assert back to Register page
    assert "Register" in driver.current_url or "automationtesting" in driver.current_url
