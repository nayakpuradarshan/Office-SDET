# Should start with test_
# All code should be in function
# pytest method name should start with test_
# Method name should sensible
# You can mark (tag) with @pytest.mark.smoke option and run wih -m
# datadriven and parameterization can be done with return statements in input format
# When you define fixture scope in class only, it will run once class is intiate and at the end

import pytest

@pytest.fixture(scope="class")      # this fixture is applied to class level
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataLoad():
    print("User profile data is beging created!")
    return ["James", "Ocorner", "IsHere"]

@pytest.fixture(params=[("chrome", "Jimmy", "Yash"), ("Firefox", "Sam"), ("Nayan", "IE", "Parimal")])
def crossBrowser(request):          # when you have fixture with value ise "request" in function
    return request.param