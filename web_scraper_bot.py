import os
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class WebScraperBot:
    def __init__(self):
        self.driver = self._setup_driver()
        self.wait = WebDriverWait(self.driver, 30)
        self.load_cookies()

    def _setup_driver(self):
        options = Options()
        arguments = [
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--window-size=1920,1080",
            "--disable-gpu",
            "--disable-extensions",
            "--disable-background-networking",
            "--disable-default-apps",
            "--disable-sync",
            "--no-first-run",
            "--enable-automation",
            "--password-store=basic",
            "--use-mock-keychain"
        ]
        for arg in arguments:
            options.add_argument(arg)
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    def save_cookies(self):
        with open("cookies.pkl", "wb") as file:
            pickle.dump(self.driver.get_cookies(), file)

    def load_cookies(self):
        if os.path.exists("cookies.pkl"):
            self.driver.get("https://online.spor.istanbul/anasayfa")
            with open("cookies.pkl", "rb") as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            self.driver.refresh()

    def navigate_and_fill(self):
        try:
            self._open_page("https://online.spor.istanbul/anasayfa")
            self._close_modal()
            self._navigate_to_login()
            self._login("21935167880", "xajmeorDUNekG8N")
            self._close_modal()
            self._select_radio_button()
            self._select_dropdown("FUTBOL", "MALTEPE SAHİL SPOR TESİSİ")
            self._click_search_button()
        except Exception as e:
            print(f"An error occurred: {e}")

    def _open_page(self, url):
        self.driver.get(url)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def _close_modal(self):
        close_modal_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'closeModal')))
        close_modal_button.click()

    def _navigate_to_login(self):
        nav_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/header/div/nav/div/div/div/ul/li[4]/a')))
        nav_button.click()
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def _login(self, username, password):
        self.wait.until(EC.presence_of_element_located((By.ID, 'txtTCPasaport'))).send_keys(username)
        self.wait.until(EC.presence_of_element_located((By.ID, 'txtSifre'))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.ID, 'btnGirisYap'))).click()



    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    bot = WebScraperBot()
    bot.navigate_and_fill()
    input("Press Enter to close the browser...")
    bot.close()