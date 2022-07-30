from fractions import Fraction as frac


a, b= eval(input())
c, d = eval(input())

result1, result2, result3, result4 = frac(str(a/b)) - frac(str(c/d)), frac(str(a/b)) + frac(str(c/d)), frac(str(a/b)) * frac(str(c/d)), frac(str(a/b)) / frac(str(c/d))


print(frac(result1), frac(result2), frac(result3), frac(result4))