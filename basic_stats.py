def z_score(x, mean, st_dev):
    z = (x - mean) / st_dev
    return z

answer1 = z_score(5,7,2)
print(answer1)

def mean():
    n = int(input("How many items? "))
    n_copy = n
    sum = 0
    while n_copy > 0:
        item = int(input("Enter item: "))
        sum += item
        n_copy -= 1
    mean = sum / n
    return mean

answer2 = mean()
print(answer2)

def sample_st_dev(n):
    import math
    n_copy_2 = n
    sum = 0
    mean2 = mean()
    while n_copy_2 > 0:
        item = int(input("Enter item: "))
        step = (item - mean2) ** 2
        sum += step
        n_copy_2 -= 1    
    s = math.sqrt(sum / (n-1))
    return s

answer3 = sample_st_dev(2)
print(answer3)

def sample_var(n):
    import math
    s = sample_st_dev(n)
    return (s ** 2)

answer4 = sample_var(2)
print(answer4)

def factorial(n):
    answer = n
    while n > 1:
        n-= 1
        answer *= n
    return answer

answer5 = factorial(7)
print(answer5)

def permutation(m, r):
    perm = factorial(m) / factorial(m-r)
    return perm

answer6 = permutation(5,3)
print(answer6)

def combination(m, r):
    comb = factorial(m) / (factorial(r) * factorial(m-r))
    return comb

answer7 = combination(5,3)
print(answer7)
