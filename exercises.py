def multipleOf3And5():
    total = 0
    for i in range(1, 1000, 1):
        if i % 5 == 0 or i % 3 == 0:
            total += i
    print(total)


def evenFibonacci():
    first = 1
    second = 2
    sum = 0
    while second <= 4000000:
        if second % 2 == 0:
            sum += second
        tmp = second
        second = first + second
        first = tmp
    print(sum)


def largestPrimeFactor(n):
    largest = 0
    for i in range(2, n + 1):
        if n % i == 0:
            count = 1
            for j in range(2, (i//2 + 1)):
                if(i % j == 0):
                    count = 0
                    break
            if(count == 1):
                print(i)

