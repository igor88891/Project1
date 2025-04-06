import pytest
from src.decorators import  my_function, log

# Тест функции с делением на ноль
@log(filename="mylog.txt")
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)