def factorial(n):
   if n < 1:   # base case
       return 1
   else:
       N = n * factorial(n - 1)  # recursive call
      # print(str(n) + '! = ' + str(returnNumber))
       return N

n = int(input("N factorialni hisoblash. N ni kiriting. n = "))
print(f" {n} factorial   {n}! = {factorial(n)}")
