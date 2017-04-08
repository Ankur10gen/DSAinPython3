import random
def r11_is_multiple(n: int,m: int):
    return n/m == int(n/m)

def r12_is_even(k):
    return divmod(k,2)[1] == 0

def r13_minmax(data):
    sorteddata = sorted(data)
    return (sorteddata[0],sorteddata[-1])

def sq_of_num(num):
    return num ** 2

def r14_sq_less_n(n):
    sumOfSquares = 0
    while n != 0:
        sumOfSquares = sumOfSquares + sq_of_num(n)
        n -= 1
    return sumOfSquares

def r112_my_choice(data):
    return data[random.randrange(0,len(data))]

print(r11_is_multiple(10,4))
print(r12_is_even(12))
print(r13_minmax([3,1,5,2]))
print(r14_sq_less_n(4))
print(sum([x**2 for x in range(1,4+1)])) # ex_r_1_7
print([x**2 for x in range(10)][8]) # ex_r_1_8 ans: -k j = n-k
print([x for x in range(50,90,10)]) # ex_r_1_9
print([x for x in range(8,-10,-2)]) # ex_r_1_10
print([2 ** x for x in range(0,9)]) # ex_r_1_11
print([r112_my_choice([2 ** x for x in range(0,9)])])