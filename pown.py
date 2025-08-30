
def _pow_pos(x: float, n: int) -> float:
    if n == 1:
        return x
    elif n == 0:
        return 1

    half_pow = _pow_pos(x, int(n / 2))

    if n & 1 == 0:
        return half_pow * half_pow
    else:
        return half_pow * half_pow * x

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / _pow_pos(x, n)
        else:
            return _pow_pos(x, n)


    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3 != 0:
                return False
            n = int(n / 3)

        return n == 1
        
