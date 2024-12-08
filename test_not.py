from nand import Nand

def test_not():
    """Test truth table of not gate function"""
    assert Nand(False, False).output() is True
    assert Nand(True, True).output() is False