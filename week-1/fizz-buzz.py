class Solution:
    def fizzBuzz(self, n: int) :
        lst = []
        for i in range(1,n+1):
            temp =[]
            if i%3==0 or i%5==0:
            
                if i%3==0:
                    temp.append("Fizz")
                if i%5 ==0:
                    temp.append("Buzz")
            else:
                temp.append(str(i))
            lst.append("".join(temp))
        return lst
        