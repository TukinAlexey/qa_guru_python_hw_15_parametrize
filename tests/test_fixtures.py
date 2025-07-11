"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser, have
from conftest import desktop_screen_size_browser
from conftest import mobile_screen_size_browser


def test_sign_in_button_desktop(desktop_screen_size_browser):
    browser.open("https://github.com/")
    browser.element('(//*[contains(text(),"Sign in")])[2]').click()
    browser.element(
        '[class="auth-form-header p-0"]').should(
        have.exact_text(
            "Sign in to GitHub"))


def test_sign_in_button_mobile(mobile_screen_size_browser):
    browser.open("https://github.com/")
    browser.element('//*[contains(text(),"Sign in")]').click()
    browser.element(
        '[class="auth-form-header p-0"]').should(
        have.exact_text(
            "Sign in to GitHub"))
