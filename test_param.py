import pytest
import math

@pytest.mark.parametrize(
    "base, expo, expec",
    [(2,2,4), (2,3,8), (1,9,1), (0,9,0), (3,3,27)],
    ids=["case1", "case2", "case3", "case4", "case5"]
    )

def test_pow(base, expo, expec):
    assert math.pow(base, expo) == expec