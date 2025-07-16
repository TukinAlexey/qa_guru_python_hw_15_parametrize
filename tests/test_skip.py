"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have
from conftest import screen_size_browser_fixture_parametrize


def test_mobile_size_browser_skip(screen_size_browser_fixture_parametrize):
    if screen_size_browser_fixture_parametrize == "mobile":
        pytest.skip("Это мобилное разрешение")
    browser.open("https://github.com/")
    browser.element('(//*[contains(text(),"Sign in")])[2]').click()
    browser.element(
        '[class="SessionsAuthHeader-module__authFormHeaderTitle--Kg7Qt"]').should(
        have.exact_text(
            "Sign in to GitHub"))


def test_desktop_size_browser_skip(screen_size_browser_fixture_parametrize):
    if screen_size_browser_fixture_parametrize == "desktop":
        pytest.skip("Это десктопное разрешение")
    browser.open("https://github.com/")
    browser.element('//*[contains(text(),"Sign in")]').click()
    browser.element(
        '[class="SessionsAuthHeader-module__authFormHeaderTitle--Kg7Qt"]').should(
        have.exact_text(
            "Sign in to GitHub"))
