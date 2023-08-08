import time

start = time.time()
def fact(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
        yield num


for i, num in enumerate(fact(100_000), 1):
    a = {i: num}
end = time.time() - start
print(end)

start = time.time()
def fact2(n):
    num = 1
    result = []
    for i in range(1,n + 1):
        num *= i
        result.append(num * 1)
    return result


for i, num in enumerate(fact2(100_000), 1):
    a = {i: num}

end = time.time() - start
print(end)
