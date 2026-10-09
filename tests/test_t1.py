import pytest

def fibo(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 1:
        return 1
    else:
        x = 0
        y = 1
        
        for i in range(n-2):
            next = x + y
            
            x = y
            y = next
        return next
    


@pytest.mask.parametrize("n,ans",[(-1,None),(0,None),(5,3),(6,5)])
def fibo_test(n,ans):
    assert fibo(n) == ans

