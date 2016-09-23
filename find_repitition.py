import functools

def get_mod(n):
    the_number = n
    arr_lcm = []
    num_till_n = list(range(1, n))
    #print(str(len(num_till_n)))
    place_repeated = 1
    for i in num_till_n:
        raised_by = 2
        curr_num = i
        #print(str(i) + " is the number to be repeated")
        #print(str(raised_by))
        while ((i ** raised_by) % the_number) != curr_num:
            #print(str((i ** raised_by) % the_number) + " is the result of ")
            place_repeated = place_repeated + 1
            raised_by = raised_by + 1
        arr_lcm.append(place_repeated)
        place_repeated = 1
    for i in arr_lcm:
        print(str(i))
    result = lcmm(arr_lcm)
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(a_list = []):
    return functools.reduce(lcm, a_list)

#l = [1, 4, 4, 2, 2, 1, 4, 4, 2, 1, 2, 4, 4, 2]
d= get_mod(17)
print("Lcm is: " + str(d))

