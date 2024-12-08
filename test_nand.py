from nand import Nand

def test_nand():
    """Test truth table of nand gate function"""
    assert Nand(False, False).output() is True
    assert Nand(False, True).output() is True
    assert Nand(True, False).output() is True
    assert Nand(True, True).output() is False

def test_nand_update():
    """Test update method of nand gate"""
    nand = Nand(False, False)
    assert nand.output() is True
    nand.update(False, True)
    assert nand.output() is True
    nand.update(True, False)
    assert nand.output() is True
    nand.update(True, True)
    assert nand.output() is False