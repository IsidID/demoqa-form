import time
import requests
from main import user_login as user
from main import generate_user
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from pathlib import Path
options = Options()
# options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
options.add_argument("--disable-blink-features=AutomationControlled")


def test_register():
    username = user()['username']
    password = user()['password']
    request = requests.post("https://demoqa.com/Account/v1/User", json = {"userName":username, "password": password})
    assert request.status_code == 201
    responseData = request.json().get('userID')
    return {"username":username, "password":password}
def test_token():
    username = test_register()['username']
    password = test_register()['password']
    login_request = requests.post("https://demoqa.com/Account/v1/GenerateToken", json = {"userName":username, "password": password})
    assert login_request.status_code == 200
    token = login_request.json().get('token')
    expires = login_request.json().get('expires')
    return {'token':token, 'expires':expires}
def test_log():
    username = test_register()['username']
    password = test_register()['password']
    login_request = requests.post("https://demoqa.com/Account/v1/Login", json = {"userName":username, "password": password})
    assert login_request.status_code == 200
    userId = login_request.json().get('userId')
    return {'userId': userId, 'username': username}

def test_books():
    driver.get("https://demoqa.com/login")
    driver.set_window_size(1920, 1080)
    driver.execute_cdp_cmd('Storage.clearDataForOrigin', {
        "origin": '*',
        "storageTypes": 'all',
    })
    bookname = 'Speaking JavaScript'
    usernameField = driver.find_element(by=By.ID, value='userName')
    passwordField = driver.find_element(by=By.ID, value='password')
    loginButton = driver.find_element(by=By.ID, value='login')
    bookstore = driver.find_element(by=By.XPATH, value='//span[contains(text(), "Book Store")]')
    usernameField.send_keys(test_register()['username'])
    passwordField.send_keys(test_register()['password'])
    loginButton.click()
    time.sleep(1)
    ActionChains(driver).click(bookstore).perform()
    searchbookField = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='searchBox']")))
    searchbookField.send_keys(bookname)
    title = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Speaking JavaScript')]")))
    assert bookname in title.text
    wait.until(EC.element_to_be_clickable(title)).click()
    AssertionDescription = driver.find_element(by=By.ID, value='description-wrapper')
    AddButton = driver.find_element(by=By.XPATH, value='//button[contains(text(), "Add To Your Collection")]')
    assert 'Like it or not, JavaScript is everywhere' in AssertionDescription.text
    AddButton.click()
    alert = wait.until(EC.alert_is_present())
    assert 'Book added to your collection.' in alert.text
    alert.accept()
    driver.get("https://demoqa.com/profile")
    wait.until(EC.url_to_be("https://demoqa.com/profile"))
    deleteButton = driver.find_element(by=By.ID, value='delete-record-undefined')
    deleteButton.click()
    alert2 = driver.find_element(by=By.CLASS_NAME, value="modal-body")
    assert 'Do you want to delete this book?' in alert2.text
    modal = driver.find_element(by=By.CLASS_NAME, value="modal-content")
    footer = modal.find_element(by=By.CLASS_NAME, value="modal-footer")
    acceptButton = footer.find_element(by=By.ID, value="closeSmallModal-ok")
    acceptButton.click()
    alert2 = wait.until(EC.alert_is_present())
    assert 'Book deleted.' in alert2.text
    alert2.accept()
    norows = driver.find_element(by=By.CLASS_NAME, value="rt-noData")
    assert  'No rows found' in norows.text


