from logical_mod import and_logical_easy,and_logical,nand_logical,or_logical

class TestClass1():
    def test_and_1(self):
        assert and_logical_easy(0,0)==0
    def test_and_2(self):
        assert and_logical_easy(0,1)==0
    def test_and_3(self):
        assert and_logical_easy(1,0)==0
    def test_and_4(self):
        assert and_logical_easy(1,1)==1

#
class TestClass2():
    def test_and_1(self):
        assert and_logical(0,0)==0
    def test_and_2(self):
        assert and_logical(0,1)==0
    def test_and_3(self):
        assert and_logical(1,0)==0
    def test_and_4(self):
        assert and_logical(1,1)==1

class TestClass3():
    def test_and_1(self):
        assert nand_logical(0,0)==1
    def test_and_2(self):
        assert nand_logical(0,1)==1
    def test_and_3(self):
        assert nand_logical(1,0)==1
    def test_and_4(self):
        assert nand_logical(1,1)==0

#
class TestClass4():
    def test_and_1(self):
        assert or_logical(0,0)==0
    def test_and_2(self):
        assert or_logical(0,1)==1
    def test_and_3(self):
        assert or_logical(1,0)==1
    def test_and_4(self):
        assert or_logical(1,1)==1
