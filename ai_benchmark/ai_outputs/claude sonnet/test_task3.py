import sys
import os

# Thêm thư mục gốc của dự án vào sys.path
# __file__ là đường dẫn đến file test hiện tại.
# os.path.dirname(__file__) sẽ lấy thư mục chứa file test.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from tasks.common import is_prime

def test_zero(): assert not is_prime(0)
def test_one(): assert not is_prime(1)
def test_two(): assert is_prime(2)
def test_seventeen(): assert is_prime(17)
def test_eighteen(): assert not is_prime(18)
def test_nineteen(): assert is_prime(19)
def test_large_prime(): assert is_prime(101)
def test_large_composite(): assert not is_prime(100)
