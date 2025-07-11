"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have
from conftest import desktop_screen_size_browser
from conftest import mobile_screen_size_browser


@pytest.mark.parametrize("desktop_screen_size_browser", [
    (1920, 1080),
    (2560, 1440)
], indirect=True)
def test_sign_in_button_desktop_indirect(desktop_screen_size_browser):
    browser.open("https://github.com/")
    browser.element('(//*[contains(text(),"Sign in")])[2]').click()
    browser.element(
        '[class="auth-form-header p-0"]').should(
        have.exact_text(
            "Sign in to GitHub"))


@pytest.mark.parametrize("mobile_screen_size_browser", [
    (375, 667),
    (414, 896)
], indirect=True)
def test_sign_in_button_mobile_indirect(mobile_screen_size_browser):
    browser.open("https://github.com/")
    browser.element('//*[contains(text(),"Sign in")]').click()
    browser.element(
        '[class="auth-form-header p-0"]').should(
        have.exact_text(
            "Sign in to GitHub"))
