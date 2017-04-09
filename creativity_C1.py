import random


def c113_reverse_list_of_nums(nums):
    reversedNums = []
    for i in nums:
        reversedNums.insert(0, i)
    return reversedNums


def c114_has_odd_products(listOfIntValues):
    odd = False
    for i in listOfIntValues:
        for j in listOfIntValues:
            if i != j and (i * j) % 2 != 0:
                # print(i,j,i*j)
                odd = True
                return odd
    return odd


def numbers_are_distinct(listOfNumbers):
    return len([(x, y) for x in listOfNumbers for y in listOfNumbers if x != y]) == len(listOfNumbers) ** 2 - len(
        listOfNumbers)
    # If result is not cross product minus the length of list, it means that some element was present twice


"""
At Page 25 : As a concrete example,
we present the following implementation of a method named scale that’s primary
purpose is to multiply all entries of a numeric data set by a given factor.

def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
"""


def c116_scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor


def c117_scale(data, factor):
    for val in data:
        val *= factor
        print(val)


def c120_my_shuffle(listOfElements):
    shuffled_list = []
    random_indexes = []
    while len(set(random_indexes)) < len(listOfElements):
        random_index = random.randint(0, len(listOfElements) - 1)
        if random_index not in random_indexes:
            random_indexes.append(random_index)
    for index in random_indexes:
        shuffled_list.append(listOfElements[index])
    return shuffled_list


def c121_EOFError():
    try:
        inputs_from_user = []
        while True:
            inputs_from_user.append(input())
    except EOFError:
        print(sorted(inputs_from_user, reverse=True))


def c122_dot_prod(a, b):
    c = []
    for i in range(len(a)):  # in ques len(a) is n
        c.append(a[i] * b[i])
    return c


def c123_index_oob():
    list1 = [1, 2, 3, 4]
    try:
        list1[6] = "ZOMBIE"
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")


def c124_number_of_vowels(givenString):
    cnt = 0
    for i in givenString.lower():
        if i in ['a', 'e', 'i', 'o', 'u']:
            cnt = cnt + 1
    return cnt


def c124_number_of_vowels_alt(givenString):
    import re
    return len(re.findall(re.compile('[aeiou]'), givenString.lower()))


def c125_remove_punctuation(givenString):
    import re
    return re.sub(r'[^a-zA-Z0-9_\s]', '', givenString)


def c126_arithmetic(a, b, c):
    return a + b == c or a == b - c or a * b == c


def c128_norm(v, p=2):  # p-norm vector of vector
    return sum([x ** p for x in v]) ** (1 / p)


print(c113_reverse_list_of_nums([1, 2, 4, 5, 3]))
print(c114_has_odd_products([1, 2, 3]))
print(numbers_are_distinct([1, 2, 3, 4, 1]))
d1 = [1, 2, 3]
c116_scale(d1, 3)
print(d1)  # prints [3,6,9] because the formal parameter is an alias for the actual parameter in mutable objects,
#  the body of the function in these cases may interact with the object in ways that change its state

"""
c117
Won't work properly. In this case, we are copying the value of list items in val with each pass of loop
"""
d2 = [2, 3, 4]
c117_scale(d2, 2)
print(d2)

print([x * (x + 1) for x in range(10)])  # c118 list comprehension

print([chr(x) for x in range(ord('a'), ord('z') + 1)])  # c119 characters list comprehension

"""
(shuffle in random)
shuffleThisList = [1,2,3,4,5]
random.shuffle(shuffleThisList)
print(shuffleThisList)
"""

print(c120_my_shuffle([1, 2, 3, 4, 5]))  # Works like shuffle() except that this doesn't change the original list

# c121_EOFError()

print(c122_dot_prod([1, 2, 3], [4, 5, 6]))

c123_index_oob()

print(c124_number_of_vowels('Ankur Raina'))

print(c124_number_of_vowels_alt('Ankur Raina'))

print(c125_remove_punctuation("Let's try, Mike."))

print(c126_arithmetic(2, 3, 6))


def factors(n):  # generator that computes factors
    k = 1
    while k * k < n:  # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:  # special case if n is perfect square
        yield k


for i in sorted(factors(100)):  # c127 not sure if this was the expected thing but it provides the expected result
    print(i, sep=' ', end=' ')

print('\n')

print(c128_norm([4, 3]))