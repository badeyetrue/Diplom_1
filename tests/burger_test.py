import pytest
from unittest.mock import Mock
from praktikum.burger import Burger 

class TestBurger:

    def test_set_buns_sets_bun_correctly(self):
        # Arrange
        burger = Burger()
        mock_bun = Mock()
        
        # Act
        burger.set_buns(mock_bun)
        
        # Assert
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_to_list(self):
        # Arrange
        burger = Burger()
        mock_ingredient = Mock()
        
        # Act
        burger.add_ingredient(mock_ingredient)
        
        # Assert
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_removes_from_list(self):
        # Arrange
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        
        # Act
        burger.remove_ingredient(0)
        
        # Assert
        assert mock_ingredient not in burger.ingredients
        assert len(burger.ingredients) == 0

    def test_move_ingredient_changes_position(self):
        # Arrange
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        
        # Act: перемещаем первый ингредиент (индекс 0) на позицию второго (индекс 1)
        burger.move_ingredient(0, 1)
        
        # Assert
        assert burger.ingredients[0] == mock_ing_2
        assert burger.ingredients[1] == mock_ing_1

    def test_get_price_calculates_total_correctly(self):
        # Arrange
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        
        mock_ing_1 = Mock()
        mock_ing_1.get_price.return_value = 50.0
        mock_ing_2 = Mock()
        mock_ing_2.get_price.return_value = 70.0
        
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        
        expected_price = 320.0  # (100 * 2) + 50 + 70
        
        # Act
        actual_price = burger.get_price()
        
        # Assert
        assert actual_price == expected_price

    @pytest.mark.parametrize(
        "bun_name, bun_price, ing_type, ing_name, ing_price, expected_receipt",
        [
            (
                "Краторная булка", 100.0, 
                "SAUCE", "Соус Chili", 50.0,
                "(==== Краторная булка ====)\n= sauce Соус Chili =\n(==== Краторная булка ====)\n\nPrice: 250.0"
            ),
            (
                "Флуоресцентная булка", 150.0, 
                "FILLING", "Говяжий котлет", 100.0,
                "(==== Флуоресцентная булка ====)\n= filling Говяжий котлет =\n(==== Флуоресцентная булка ====)\n\nPrice: 400.0"
            ),
        ]
    )
    def test_get_receipt_formats_correctly(self, bun_name, bun_price, ing_type, ing_name, ing_price, expected_receipt):
        # Arrange
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        mock_ing = Mock()
        mock_ing.get_type.return_value = ing_type
        mock_ing.get_name.return_value = ing_name
        mock_ing.get_price.return_value = ing_price
        burger.add_ingredient(mock_ing)
        
        # Act
        receipt = burger.get_receipt()
        
        # Assert
        assert receipt.strip() == expected_receipt.strip()
