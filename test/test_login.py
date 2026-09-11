import pytest

@pytest.mark.login
def test_login_standard_user(standard_user_page):
    assert standard_user_page.get_title() == "Swag Labs"

@pytest.mark.login
def test_locked_out_user(locked_out_user_page):
    assert locked_out_user_page.text_locked_out_user() == "Epic sadface: Sorry, this user has been locked out."

@pytest.mark.login
def test_problem_user(problem_user_page):
    assert problem_user_page.get_title() == "Swag Labs"

@pytest.mark.login

def test_performance_glitch_user(performance_glitch_user_page):
    assert performance_glitch_user_page.get_title() == "Swag Labs"

@pytest.mark.login
def test_error_user(error_user_page):
    assert error_user_page.get_title() == "Swag Labs"

@pytest.mark.login
def test_visual_user(visual_user_page):
    assert visual_user_page.get_title() == "Swag Labs"