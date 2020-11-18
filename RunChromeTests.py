from selenium import webdriver


class RunChromeTests:

    @staticmethod
    def test():
        driver = webdriver.Chrome()
        driver.get('https://mingle-ci01-portal.mingle.awsdev.infor.com/CI_TST')


RunChromeTests.test()
