import allure

from pages import BasePage


class AlertPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.alert = self.browser.locator('[role="alert"]')

    @allure.step('Wait for alert to appear')
    def wait_for_alert(self):
        self.alert.wait_for(state='visible', timeout=10000)
