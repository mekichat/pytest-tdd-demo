from app.string_utils import my_capitalize, my_title

# # AAA -metoden
# # Arrange, Act, Assert
# def test_capitalize():
#     # Arrange
#     my_input = "kimmo"
    
#     # Act
#     result = my_capitalize(my_input)
    
#     # Assert    
#     assert result == "Kimmo"
    
# def test_capitalize_with_empty_string():
#     assert "" == my_capitalize("")
    
# def test_capitalize_with_None():
#     assert "" == my_capitalize(None)
    
# def test_capitalize_with_numbers():
#     assert "1abc" == my_capitalize("1ABC")
    
# def test_capitalize_with_single_characters():
#     assert "A" == my_capitalize("a")
#     assert "B" == my_capitalize("b")
#     assert "1abc" == my_capitalize("1ABC")
#     assert "" == my_capitalize(None)
#     assert "" == my_capitalize("")
    

import pytest

@pytest.mark.parametrize(
    "input, expected",
    [
        ("kimmo", "Kimmo"),
        ("  kimmo  ", "Kimmo"), # detta borde också fungera
        ("KIMMO AHOLA", "Kimmo ahola"),
        ("a", "A"),
        ("123ABC", "123Abc"), # hade vänt 
        (None, ""),
        ("ÅÄÖ", "Åäö")
        
    ]
)
def test_capitalization(input, expected):
    assert my_capitalize(input) == expected
    

@pytest.mark.parametrize(
    "input, expected",
    [
        ("KIMMO AHOLA", "Kimmo Ahola"),
        ("britte-marie", "Britte-Marie"),
        ("23KIMMO AHOLA", "23Kimmo Ahola"),
        ("45ÅÄÖ", "45Åäö"),
        ("34britte-marie", "34Britte-Marie"),
        ("o'connor", "O'Connor"),
        (None, ""),
        ("!cat","!Cat"),
        ("!cat.dog","!Cat.Dog")
        
    ]
)
def test_title(input, expected):
    assert my_title(input) == expected