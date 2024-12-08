from nand import Nand

def test_and():
    """Test truth table of and gate function"""
    # A = False, B = False -> Output should be False
    assert Nand(Nand(False, False).output(), Nand(False, False).output()).output() is False
    # A = False, B = True -> Output should be False
    assert Nand(Nand(False, True).output(), Nand(False, True).output()).output() is False
    # A = True, B = False -> Output should be False
    assert Nand(Nand(True, False).output(), Nand(True, False).output()).output() is False
    # A = True, B = True -> Output should be True
    assert Nand(Nand(True, True).output(), Nand(True, True).output()).output() is True