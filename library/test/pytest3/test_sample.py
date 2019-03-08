import numpy as np

import pytest
from sample1 import returnSumArrays
def test1():
    x = np.array([1,2,3,4,5])
    y = np.array([5,4,3,2,1])
    assert list(returnSumArrays(x,y)) == [6,6,6,6,6]
    assert np.sum(returnSumArrays(x,y)) == 30
