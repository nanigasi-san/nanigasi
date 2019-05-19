from nanigasi_sequence import Sequence,ArithmeticalProgression,GeometricProgression

class TestSequence():
    a = Sequence("n**3+4")
    def test_enum1(self):
        assert list(self.a.enumeration(1,5)) == [5,12,31,68,129]
    def test_enum2(self):
        assert sum(self.a.enumeration(1,3)) == 48
