def z_score(x, mean, st_dev):
    z = (x - mean) / st_dev
    return z

#answer1 = z_score(5,7,2)
#print(answer1)

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

#answer2 = mean()
#print(answer2)

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

#answer3 = sample_st_dev(2)
#print(answer3)

def pop_st_dev(n):
    import math
    n_copy_3 = n
    sum = 0
    mean3 = mean()
    while n_copy_3 > 0:
        item = int(input("Enter item: "))
        step = (item - mean3) ** 2
        sum += step
        n_copy_3 -= 1
    s = math.sqrt(sum / n)
    return s

#answer3_2 = pop_st_dev(3)
#print(answer3_2)

def sample_var(n):
    import math
    s = sample_st_dev(n)
    return (s ** 2)

#answer4 = sample_var(2)
#print(answer4)

def pop_var(n):
    import math
    s = pop_st_dev(n)
    return (s ** 2)

#answer4_2 = pop_var(3)
#print(answer4_2)

def factorial(n):
    answer = n
    while n > 1:
        n-= 1
        answer *= n
    return answer

#answer5 = factorial(7)
#print(answer5)

def permutation(m, r):
    perm = factorial(m) / factorial(m-r)
    return perm

#answer6 = permutation(5,3)
#print(answer6)

def combination(m, r):
    comb = factorial(m) / (factorial(r) * factorial(m-r))
    return comb

#answer7 = combination(5,3)
#print(answer7)

def binomial_prob(n, x, p):
    comb = combination(n, x)
    p1 = comb * p ** x * (1-p) ** (n-x)
    return p1

#answer8 = binomial_prob(5,3,0.7)
#print(answer8)

def binomial_mean(n, p):
    mean = n * p
    return mean

#answer9 = binomial_mean(5,3)
#print(answer9)

def binomial_var(n, p):
    variance = n * p * (1-p)
    return variance

#answer10 = binomial_var(5,0.7)
#print(answer10)

def binomial_st_dev(n, p):
    import math
    v = binomial_var(n,p)
    return math.sqrt(v)

#answer11 = binomial_st_dev(5,0.7)
#print(answer11)

def half_of_range_1(conf, st_dev, n):
    import math
    if conf == 80:
        z = 1.282
    elif conf == 90:
        z = 1.645
    elif conf == 95:
        z = 1.96
    elif conf == 98:
        z = 2.326
    elif conf == 99:
        z = 2.576
    hr = z * st_dev / math.sqrt(n)
    return hr

#answer12 = half_of_range_1(90,5,10)
#print(answer12)

def half_of_range_2(conf, s, n):
    import math
    if conf == 80:
        z = 1.282
    elif conf == 90:
        z = 1.645
    elif conf == 95:
        z = 1.96
    elif conf == 98:
        z = 2.326
    elif conf == 99:
        z = 2.576
    hr = z * s / math.sqrt(n)
    return hr

#answer13 = half_of_range_2(90,5,10)
#print(answer13)

def half_of_range_3(t, s, n):
    import math
    hr = t * s / math.sqrt(n)
    return hr

#answer14 = half_of_range_3(1.7,5,10)
#print(answer14)

def find_sample_size(z, st_dev, E):
    n = (z ** 2 * st_dev ** 2) / (E ** 2)
    return n

#answer15 = find_sample_size(1.7,5,2)
#print(answer15)
