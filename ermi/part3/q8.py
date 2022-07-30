x, n  = eval(input())

Y = 5 * pow(x, n+1) + (7/9)*pow(x,n) - 8*pow(x, n-1)


print("{:.5f}".format(Y))