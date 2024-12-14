import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfileNUmberTwo(self, dataLoad):
        print(dataLoad)


