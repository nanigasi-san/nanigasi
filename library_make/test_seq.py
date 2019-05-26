from nanigasi_sequence import Sequence,ArithmeticalProgression,GeometricProgression,Zennka1,Zennka2

a = Sequence("3**n+2")
def test_seq1():
    assert a.get_term(3) == 29

def test_seq2():
    assert list(a.enumeration(2,5)) == [11,29,83,245]

def test_seq3():
    assert a.sigma(1,10) == 88592


b = ArithmeticalProgression(5,2)
def test_ari1():
    assert b.get_term(3) == 9

def test_ari2():
    assert list(b.enumeration(1,10)) == [5,7,9,11,13,15,17,19,21,23]

def test_ari3():
    assert b.sigma(3,8) == 84


c = GeometricProgression(5,3)
def test_geo1():
    assert c.get_term(4) == 135

def test_geo2():
    assert list(c.enumeration(5,9)) == [405,1215,3645,10935,32805]

def test_geo3():
    assert c.sigma(1,4) == 200


d = Zennka1(3,"a_n**2+n")

def test_zen1():
    assert list(d.enumeration(1,4)) == [3,11,124,15380]
def test_zen2():
    assert d.sigma(2,4) == 15515
