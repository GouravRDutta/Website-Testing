import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
import usercred
class EdurekaSelePro(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\\Users\\GRD\\Downloads\\chromedriver_win32\\chromedriver.exe")
        cls.driver.maximize_window()

    def test1(self):
        self.driver.get("https://www.edureka.co/")
        login=self.driver.find_element_by_xpath("//*[@id='header-II']/section/nav/div/a[2]")
        login.click()
        self.driver.implicitly_wait(2)

        user=self.driver.find_element_by_id("si_popup_email")
        user.send_keys(usercred.username)
        passwd = self.driver.find_element_by_id("si_popup_passwd")
        passwd.send_keys(usercred.password)
        passwd.send_keys(Keys.ENTER)

        pro=self.driver.find_element_by_xpath("//*[@id='header-II']/section/nav/div/ul[2]/li[1]/a")
        pro.click()

        mypro=self.driver.find_element_by_xpath("//*[@id='header-II']/section/nav/div/ul[2]/li[1]/ul/li[1]/a")
        mypro.click()

        self.driver.implicitly_wait(3)
        car=self.driver.find_element_by_xpath("//*[@id='career_interest']")
        car.click()

        self.driver.find_element_by_xpath("//*[@id='onboarding']/div/div[1]/div[1]/app-onboarding-leftnav/ul/li[4]/a").click()

        self.driver.find_element_by_name("companyName").send_keys("Haldia Institute of Technology")
        drop = Select(self.driver.find_element_by_name("currentjob"))
        drop.select_by_visible_text("Not Applicable - Fresher")

        drop2 = Select(self.driver.find_element_by_name("currentIndustry"))
        drop2.select_by_visible_text("IT-Software / Software Services")

        self.driver.find_element_by_name("userSkill").send_keys("Java,python,selenium,linux,html,css,javascript,cloud computing,IOT,data analysis")

        self.driver.find_element_by_xpath("//*[@id='onboarding']/div/div[1]/div[2]/div[2]/app-onboarding-professional-details/accordion/accordion-group/div/div[2]/div/form/button[2]").click()





    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test is successful")


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
