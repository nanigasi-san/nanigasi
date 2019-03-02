from logical_mod import and_logical,and_logical_array,nand_logical_array,or_logical_array

class TestClass1():
    def test_and_1(self):
        assert and_logical(0,0)==0
    def test_and_2(self):
        assert and_logical(0,1)==0
    def test_and_3(self):
        assert and_logical(1,0)==0
    def test_and_4(self):
        assert and_logical(1,1)==1

#
class TestClass2():
    def test_and_1(self):
        assert and_logical_array(0,0)==0
    def test_and_2(self):
        assert and_logical_array(0,1)==0
    def test_and_3(self):
        assert and_logical_array(1,0)==0
    def test_and_4(self):
        assert and_logical_array(1,1)==1

class TestClass3():
    def test_and_1(self):
        assert nand_logical_array(0,0)==1
    def test_and_2(self):
        assert nand_logical_array(0,1)==1
    def test_and_3(self):
        assert nand_logical_array(1,0)==1
    def test_and_4(self):
        assert nand_logical_array(1,1)==0

#
class TestClass4():
    def test_and_1(self):
        assert or_logical_array(0,0)==0
    def test_and_2(self):
        assert or_logical_array(0,1)==1
    def test_and_3(self):
        assert or_logical_array(1,0)==1
    def test_and_4(self):
        assert or_logical_array(1,1)==1
