from nand import Nand

def test_or():
    """Test truth table of or gate function"""
    assert Nand(Nand(False, False).output(), Nand(False, False).output()).output() is False
    assert Nand(Nand(False, False).output(), Nand(True, True).output()).output() is True
    assert Nand(Nand(True, True).output(), Nand(False, False).output()).output() is True
    assert Nand(Nand(True, True).output(), Nand(True, True).output()).output() is True