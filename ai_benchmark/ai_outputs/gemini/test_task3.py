import sys
import os

# Thêm thư mục gốc của dự án vào sys.path
# __file__ là đường dẫn đến file test hiện tại.
# os.path.dirname(__file__) sẽ lấy thư mục chứa file test.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from tasks.common import is_prime

def test_is_prime_edge_cases():
    """
    Kiểm tra hàm is_prime với các trường hợp biên: 0, 1, 2, 17, 18, 19.
    """
    # Các số không phải số nguyên tố
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(18) == False # Số chẵn không phải 2

    # Các số nguyên tố
    assert is_prime(2) == True   # Số nguyên tố nhỏ nhất
    assert is_prime(17) == True
    assert is_prime(19) == True

def test_is_prime_small_numbers():
    """
    Kiểm tra is_prime với một số số nhỏ khác.
    """
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(9) == False # Số lẻ nhưng không phải số nguyên tố
    assert is_prime(11) == True
    assert is_prime(13) == True

def test_is_prime_larger_numbers():
    """
    Kiểm tra is_prime với một vài số lớn hơn.
    """
    assert is_prime(23) == True
    assert is_prime(25) == False # 5 * 5
    assert is_prime(29) == True
    assert is_prime(31) == True
    assert is_prime(89) == True
    assert is_prime(97) == True
    assert is_prime(100) == False
    assert is_prime(101) == True # Số nguyên tố lớn hơn

def test_is_prime_negative_numbers():
    """
    Kiểm tra is_prime với các số âm (đáng lẽ phải trả về False).
    """
    assert is_prime(-1) == False
    assert is_prime(-5) == False
    assert is_prime(-100) == False
