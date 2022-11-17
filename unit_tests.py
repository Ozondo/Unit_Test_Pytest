import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

url1 = "http://suninjuly.github.io/registration1.html"
url2 = "http://suninjuly.github.io/registration2.html"
driver = webdriver.Chrome()
class TestSites(unittest.TestCase):
    def test_first(self):
        driver.get(url1)

        name = driver.find_element(By.CSS_SELECTOR, "div[class='first_block'] input[class='form-control first']")
        name.send_keys("123")

        surname = driver.find_element(By.CSS_SELECTOR, "div[class='first_block'] input[class='form-control second']")
        surname.send_keys("123")

        email = driver.find_element(By.CSS_SELECTOR, "div[class='first_block'] input[class='form-control third']")
        email.send_keys("123@mail.ru")

        button = driver.find_element(By.TAG_NAME, "button")
        button.click()

        final = driver.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(final, "Congratulations! You have successfully registered!")

    def test_second(self):
        driver.get(url2)

        name = driver.find_element(By.CSS_SELECTOR,
                                   "div[class='first_block'] input[class='form-control first']")
        name.send_keys("123")

        surname = driver.find_element(By.CSS_SELECTOR,
                                      "div[class='first_block'] input[class='form-control second']")
        surname.send_keys("123")

        email = driver.find_element(By.CSS_SELECTOR,
                                    "div[class='first_block'] input[class='form-control third']")
        email.send_keys("123@mail.ru")

        button = driver.find_element(By.TAG_NAME, "button")
        button.click()

        final = driver.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(final, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()

