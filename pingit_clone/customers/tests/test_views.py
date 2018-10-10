from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class NewUserTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.browser.wait = WebDriverWait(self.browser, 10)

    def tearDown(self):
        self.browser.quit()

    def user_login(self):
        import json
        with open("taskbuster/fixtures/google_user.json") as f:
            credentials = json.loads(f.read())
        self.get_element_by_id("identifierId").send_keys(credentials["Email"])
        self.get_button_by_id("identifierNext").click()
        self.get_element_by_name("password").send_keys(credentials["Passwd"])
        self.get_button_by_id("passwordNext").click()
        return

    def get_element_by_name(self, element_name):
        return self.browser.wait.until(EC.presence_of_element_located(
            (By.NAME, element_name)))

    def get_element_by_id(self, element_id):
        return self.browser.wait.until(EC.presence_of_element_located((By.ID, element_id)))

    def get_button_by_id(self, element_id):
        return self.browser.wait.until(EC.element_to_be_clickable((By.ID, element_id)))

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_homepage(self):
        self.browser.get("http://localhost:8000")
        self.assertIn(self.browser.title, 'Home')

    def test_google_login(self):
        self.browser.get(self.get_full_url("home"))
        google_login = self.get_element_by_id("google_login")
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("logout")
        self.assertEqual(
            google_login.get_attribute("href"),
            self.live_server_url + "/accounts/google/login"
        )
        google_login.click()
        self.user_login()
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("google_login")
        google_logout = self.get_element_by_id("logout")
        google_logout.click()
        google_login = self.get_element_by_id("google_login")
