import pytest

@pytest.mark.usefixtures("setup")           # fixture applied to all the methods of class
class TestExample:

    def test_demofixture(self):
        print("I will be executing steps in fixuredemo method")

    def test_demofixture1(self):
        print("I will be executing steps in fixuredemo1 method")

    def test_demofixture2(self):
        print("I will be executing steps in fixuredemo2 method")

    def test_demofixture3(self):
        print("I will be executing steps in fixuredemo3 method")