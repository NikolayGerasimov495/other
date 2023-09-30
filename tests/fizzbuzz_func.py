


def fizzbuzz(a: int) -> list:
    lst = []
    for i in range(1, a + 1):
        if i % 3 == 0 and i % 5 == 0:
            lst.append('fizzbuzz')
        elif i % 3 == 0:
            lst.append('fizz')
        elif i % 5 == 0:
            lst.append('buzz')
        else:
            lst.append(str(i))
    return lst



print(fizzbuzz(16))
