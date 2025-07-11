import pytest
from selene import browser


@pytest.fixture(params=[
    (375, 667),
    (414, 896),
    (360, 640),
    (768, 1024)
])
def mobile_screen_size_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[
    (1366, 768),
    (1920, 1080),
    (2560, 1440),
    (3840, 2160)
])
def desktop_screen_size_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[
    (375, 667),
    (414, 896),
    (360, 640),
    (768, 1024),
    (1366, 768),
    (1920, 1080),
    (2560, 1440),
    (3840, 2160)
])
def screen_size_browser_fixture_parametrize(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 800:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()
