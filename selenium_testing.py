import unittest,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSelenium(unittest.TestCase):

    def setUp(self):
            # Create a new instance of the Firefox driver
        self.driver = webdriver.Firefox()

    def testTitle(self):
        self.driver.get("http://67.205.175.115:8000/")
        assert "Jbay" in self.driver.title

    def testLogin(self):
        self.driver.get("http://67.205.175.115:8000/login")
        username = self.driver.find_element_by_id("username")
        password = self.driver.find_element_by_id("password")
        submit = self.driver.find_element_by_xpath("//input[@value='Submit']");

        username.send_keys('Harold Smith')
        password.send_keys('harold1')
        submit.click()
        self.driver.implicitly_wait(1) # seconds
        worked = self.driver.find_element_by_link_text("Back to home page")
        assert "Back to home page" in worked.text

    def testLogout(self):
        self.driver.get("http://67.205.175.115:8000/login")
        username = self.driver.find_element_by_id("username")
        password = self.driver.find_element_by_id("password")
        submit = self.driver.find_element_by_xpath("//input[@value='Submit']");

        username.send_keys('Harold Smith')
        password.send_keys('harold1')
        submit.click()
        time.sleep(1)
        self.driver.get("http://67.205.175.115:8000")
        logout = self.driver.find_element_by_link_text("Logout")
        logout.click()
        time.sleep(1)
        login_present = self.driver.find_element_by_link_text("Login")
        # logged out
        assert "Login" in login_present.text

    def testUserAccountAdd(self):
        self.driver.get("http://67.205.175.115:8000/login")
        signup = self.driver.find_element_by_link_text("Sign up here if you want to join JBay")
        signup.click()
        time.sleep(1)

        name = self.driver.find_element_by_id("name")
        address = self.driver.find_element_by_id("address")
        cart = self.driver.find_element_by_id("cart")
        password = self.driver.find_element_by_id("password")
        submit = self.driver.find_element_by_xpath("//input[@value='Submit']");

        name.send_keys('Internet Scale')
        address.send_keys('123 UVA')
        cart.send_keys('new balance 474')
        password.send_keys('isa1')
        submit.click()
        time.sleep(1)
        confirm = self.driver.find_elements_by_css_selector("h1")

        assert "User Account Created!" in confirm[1].text

    def testAddShoe(self):
        self.driver.get("http://67.205.175.115:8000/login")
        username = self.driver.find_element_by_id("username")
        password = self.driver.find_element_by_id("password")
        submit = self.driver.find_element_by_xpath("//input[@value='Submit']");

        username.send_keys('Harold Smith')
        password.send_keys('harold1')
        submit.click()
        time.sleep(1)
        self.driver.get("http://67.205.175.115:8000/create_shoe/")

        shoe = self.driver.find_element_by_id("shoe")
        brand = self.driver.find_element_by_id("brand")
        text = self.driver.find_element_by_id("text")
        submit = self.driver.find_element_by_xpath("//input[@value='Submit']");
        shoe.send_keys('EQT Support')
        brand.send_keys('Adidas')
        text.send_keys('full length support')
        submit.click()
        time.sleep(1)
        confirmation = self.driver.find_elements_by_css_selector("h1")
        assert "Shoe Listing Added!" in confirmation[1].text

    def testSearch(self):
        self.driver.get("http://67.205.175.115:8000/")
        search_box = self.driver.find_element_by_name("search_box")
        search_box.send_keys('EQT Support')
        self.driver.find_element_by_css_selector("button").submit()
        results = self.driver.find_elements_by_link_text("EQT Support")
        assert "EQT Support" in results[0].text

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
