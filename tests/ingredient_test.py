import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
            (INGREDIENT_TYPE_FILLING, "cutlet", 150.50),
            (INGREDIENT_TYPE_SAUCE, "", 0.0),
            ("UNKNOWN_TYPE", "secret ingredient", -10.0),
        ]
    )
    def test_ingredient_initialization_and_getters(self, ingredient_type, name, price):
        # Act
        ingredient = Ingredient(ingredient_type, name, price)
        
        # Assert
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
