import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("Краторная булка", 100.0),
            ("Флуоресцентная булка", 150.55),
            ("Черная булка", 0.0),
            ("", -50.0),
        ]
    )
    def test_bun_initialization_and_getters(self, name, price):
        # Act
        bun = Bun(name, price)
        
        # Assert
        assert bun.get_name() == name
        assert bun.get_price() == price
