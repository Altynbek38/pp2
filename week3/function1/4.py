numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10]

def filter_prime(numbers):
    for i in numbers:
        ok = True
        if i < 2:
            ok = False
        for j in range(2, i):
            if i % j == 0:
                ok = False
        if ok:
            print(i)

    
filter_prime(numbers)