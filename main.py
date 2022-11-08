###import
from sub import sub_func
from add import add_func


##변수부 생성
num1, num2, res = 100, 200, 0

##출력
res = add_func(num1, num2)
print(num1, '+', num2, '=', res)

res = sub_func(num1, num2)
print(num1, '-', num2, '=', res)

