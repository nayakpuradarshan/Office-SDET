# Should start with test_
# All code should be in function
# pytest method name should start with test_
# Method name should sensible
# You can mark (tag) with @pytest.mark.smoke option and run wih -m
# @pytest.mark.fixture = This is kind of setup and tear down method
# fixtures are used for setup and tear down
# conftest file = If you use fixture in conftest then it wille be available to all files
import pytest

def test_firstDemo(setup):
    print("Hello there"
          "My name is james"
          "I'm from america"
          "I'm here to study vedas")

def test_secondTest():
    print("Where is Jimmy ?")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
