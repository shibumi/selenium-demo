# Selenium Sauce Demo

This is a small demo for using Selenium in combination with the test website selenium.

## How to use this

Note: You need the `geckodriver` for Firefox in your PATH.

1. `git  clone https://github.com/shibumi/selenium-demo.git`
2. `python3 -m venv env`
3. `source env/bin/activate`
4. `pip install -r requirements.txt.lock`
5. `python3 selenium-demo.py`

## What is this doing?

This project takes a few demo users on `https://www.saucedemo.com/"` and checks if the login works as expected.