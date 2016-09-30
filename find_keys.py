import random
# For RSA

'''
Check if given number is prime.
'''


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def totient(p, q):
    return (p-1) * (q-1)


def regular_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_inv(a, n):
    if regular_gcd(a, n) != 1:
        return None
    s1, s2, s3 = 1, 0, a
    t1, t2, t3 = 0, 1, n
    while t3 != 0:
        quotient = s3 // t3
        t1, t2, t3, s1, s2, s3 = (s1 - quotient * t1), (s2 - quotient * t2), (s3 - quotient * t3), t1, t2, t3
    return s1 % n


def get_keys(p, q):
    if not is_prime(p) and is_prime(q):
        raise ValueError('p & q should be prime')

    f = p * q
    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)
    gcd_result = regular_gcd(e, phi)
    while gcd_result != 1:
        e = random.randrange(1, phi)
        gcd_result = regular_gcd(e, phi)

    private_key =  find_inv(e, phi)

    print('Public keys are: (' + str(e) + ', ' + str(f) + ').')
    print('Private keys are: (' + str(e) + ', ' + str(private_key) + ').')


get_keys(5, 7)