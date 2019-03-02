import module_nanigasi
def func(n):
    return n**2

def test_answer():
    assert func(2)==4

def test_nanigasi():
    assert module_nanigasi.nanigasi(1,2,3) == 6
