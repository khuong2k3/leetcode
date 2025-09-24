
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return "NaN"
        if numerator == 0: 
            return "0"

        isNegative = (numerator // denominator) < 0.0
        numerator = abs(numerator)
        denominator = abs(denominator)

        intPart = numerator // denominator 
        fractPart = numerator % denominator
        if fractPart == 0:
            return ("-" if isNegative else "") + str(intPart)

        existed: set[tuple[int, int]] = set()
        fraction: list[tuple[int, int]] = []

        ans = f'-{intPart}.' if isNegative else f'{intPart}.'

        while fractPart != 0:
            fractPart *= 10

            newFraction = fractPart // denominator
            fractPart -= newFraction * denominator
            if (newFraction, fractPart) in existed:
                # newFractionStr = str(newFraction)
                for i, (c, frac) in enumerate(fraction):
                    if c == newFraction and frac == fractPart:
                        return ans + f'({"".join(map(lambda frac: str(frac[0]), fraction[i:]))})'
                    else:
                        ans += str(c)

                ans += f'({fraction})'
                return ans

            fraction.append((newFraction, fractPart))
            if newFraction != 0:
                existed.add((newFraction, fractPart))

        return ans + f'{"".join(map(lambda frac: str(frac[0]), fraction))}'

sol = Solution()
# print(sol.fractionToDecimal(1, 6))
# # print(sol.fractionToDecimal(4, 333))
print(sol.fractionToDecimal(1, 333))
print(sol.fractionToDecimal(1, 17))
print(sol.fractionToDecimal(1, -1))
