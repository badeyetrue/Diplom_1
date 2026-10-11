import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_database_initialization_length(self):
        # Arrange & Act
        db = Database()
        
        # Assert
        assert len(db.available_buns()) == 3
        assert len(db.available_ingredients()) == 6

    @pytest.mark.parametrize(
        "index, expected_name, expected_price",
        [
            (0, "black bun", 100),
            (1, "white bun", 200),
            (2, "red bun", 300),
        ]
    )
    def test_available_buns_returns_correct_data(self, index, expected_name, expected_price):
        # Arrange & Act
        db = Database()
        buns = db.available_buns()
        
        # Assert
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    @pytest.mark.parametrize(
        "index, expected_type, expected_name, expected_price",
        [
            (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
        ]
    )
    def test_available_ingredients_returns_correct_data(self, index, expected_type, expected_name, expected_price):
        # Arrange & Act
        db = Database()
        ingredients = db.available_ingredients()
        
        # Assert
        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name
        assert ingredients[index].get_price() == expected_price
