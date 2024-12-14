# Should start with test_
# All code should be in function
# pytest method name should start with test_
# Method name should sensible
# You can mark (tag) with @pytest.mark.smoke option and run wih -m

import pytest

@pytest.mark.smoke              # You can add any TC in group like smoke or regression
@pytest.mark.skip               # You can skip any TC using skip
@pytest.mark.xfail              # If you wants to execute any TC but do not want generate reports
def test_valueCheck():
    name = "Jimmy"
    assert name == "John"

@pytest.mark.skip
def test_firstProgream():
    msg = "Hello"
    assert msg == "hi"

def test_CreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"

