from main import generate_user
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
options = Options()
# options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
options.add_argument("--disable-blink-features=AutomationControlled")


def test_form():
    user = generate_user()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.set_window_size(1920, 1080)
    title = driver.title
    assert title == "DEMOQA"
    driver.implicitly_wait(5)
    #Selectors
    firstName = driver.find_element(by=By.ID, value="firstName")
    lastName = driver.find_element(by=By.ID, value="lastName")
    email = driver.find_element(by=By.ID, value="userEmail")
    gender = driver.find_element(by=By.ID, value="gender-radio-"+ user[3])
    phone = driver.find_element(by=By.ID, value="userNumber")
    birthDate = driver.find_element(by=By.ID, value="dateOfBirthInput")
    subject = driver.find_element(by=By.ID, value="subjectsInput")
    address = driver.find_element(by=By.ID, value="currentAddress")
    hobbies = driver.find_element(by=By.ID, value="hobbies-checkbox-" + user[10])
    state = driver.find_element(by=By.ID, value="react-select-3-input")
    city = driver.find_element(by=By.ID, value="react-select-4-input")
    submit_button = driver.find_element(by=By.CLASS_NAME, value="btn-primary")

    #Actions
    firstName.send_keys(user[0])
    lastName.send_keys(user[1])
    email.send_keys(user[2])
    ActionChains(driver).click(gender).perform()
    phone.send_keys(user[4])
    birthDate.click()
    birthDate.send_keys(Keys.CONTROL, "a")
    birthDate.send_keys(Keys.SPACE)
    birthDate.send_keys(user[6])
    birthDate.send_keys(Keys.RETURN)
    driver.implicitly_wait(2)
    subject.send_keys('Phy')
    subject.send_keys(Keys.RETURN)
    subject.click()
    subject.send_keys('Art')
    subject.send_keys(Keys.RETURN)
    driver.implicitly_wait(2)
    ActionChains(driver).click(hobbies).perform()
    address.send_keys(user[5])
    ActionChains(driver).click(state).perform()
    driver.implicitly_wait(2)
    state.send_keys(4 * Keys.ARROW_DOWN, Keys.RETURN)
    ActionChains(driver).click(city).perform()
    city.send_keys(Keys.ARROW_DOWN, Keys.RETURN)
    ActionChains(driver).move_to_element(submit_button).perform()
    ActionChains(driver).click(submit_button).perform()
    driver.implicitly_wait(2)

    #AssertionSelectors
    modal = driver.find_element(by=By.ID, value="example-modal-sizes-title-lg")
    wait.until(EC.visibility_of(modal))
    driver.implicitly_wait(2)
    AssertNameSurname = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[1]/td[2]")
    AssertEmail = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[2]/td[2]")
    AssertGender = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[3]/td[2]")
    AssertMobile = driver.find_element(by=By.XPATH,
                                       value="/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[4]/td[2]")
    AssertBirth = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[5]/td[2]")
    AssertSubject = driver.find_element(by=By.XPATH,
                                        value="/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[6]/td[2]")
    AssertHobbies = driver.find_element(by=By.XPATH,
                                        value="/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[7]/td[2]")
    AssertAddress = driver.find_element(by=By.XPATH,
                                        value="/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[9]/td[2]")
    AssertStateCity = driver.find_element(by=By.XPATH,
                                          value="/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[10]/td[2]")

    #Assertions
    try:
        assert user[11] in AssertNameSurname.text
        print("\nStudent Name matched:")
        print(f'{user[11]} = {AssertNameSurname.text}\n')
    except Exception as e:
        print("TEST FAILED")

    try:
        assert user[2] in AssertEmail.text
        print("Student Email matched:")
        print(f'{user[2]} = {AssertEmail.text}\n')
    except Exception as e:
        print("TEST FAILED")

    try:
        if user[3] == '1':
            assert 'Male' in AssertGender.text
            print("Gender matched:")
            print(f'Male = {AssertGender.text}\n')
        elif user[3] == '2':
            assert 'Female' in AssertGender.text
            print("Gender matched:")
            print(f'Female = {AssertGender.text}\n')
        else:
            assert 'Other' in AssertGender.text
            print("Gender matched:")
            print(f'Other = {AssertGender.text}\n')
    except Exception as e:
        print("TEST FAILED")

    try:
        assert str(user[4]) in AssertMobile.text
        print("Mobile matched:")
        print(f'{user[4]} = {AssertMobile.text}\n')
    except Exception as e:
        print("TEST FAILED")

    try:
        assert user[12] in AssertBirth.text
        print("Birth Date matched:")
        print(f'{user[12]} = {AssertBirth.text}\n')
    except Exception as e:
        print("TEST FAILED")

    try:
        assert 'Physics, Arts' in AssertSubject.text
        print("Subject matched:")
        print(f'Physics, Arts = {AssertSubject.text}\n')
    except Exception as e:
        print("TEST FAILED")

    try:
        if user[10] == '1':
            assert 'Sports' in AssertHobbies.text
            print("Hobbies matched:")
            print(f'Sports = {AssertHobbies.text}\n')
        elif user[10] == '2':
            assert 'Reading' in AssertHobbies.text
            print("Hobbies matched:")
            print(f'Reading = {AssertHobbies.text}\n')
        else:
            assert 'Music' in AssertHobbies.text
            print("Hobbies matched:")
            print(f'Music = {AssertHobbies.text}\n')
    except Exception as e:
        print("TEST FAILED")

    try:
        assert user[5].replace("\n", " ") in AssertAddress.text
        print("Address matched:")
        print(f'{user[5]} = {AssertAddress.text}\n')
    except Exception as e:
        print("TEST FAILED")

    try:
        assert 'NCR Gurgaon' in AssertStateCity.text
        print("State and City matched:")
        print(f'NCR Gurgaon = {AssertStateCity.text}\n')
    except Exception as e:
        print("TEST FAILED")
    driver.quit()