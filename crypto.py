import itertools

# can be used in future for making combinations of input
def make_pair(n):
	# Creating a new list from 1 to n
	myList = list(range(1, n))
	# using itertools.combination to make tuples
	pair_list = list(itertools.combinations_with_replacement(myList, 2))
	# Pass that list to another function that calculates
	# GCD of each pair to check if it equals 1
	return pair_list

def regular_gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a
# multi
def mult_inv(n):
	# getting the list of all possible
	# pairs as tuples
	result_list = []
	num_till_n = list(range(1, n))
	for tup in num_till_n:
		# print('gcd of ' + str(tup)  + ' is: ' + str(gcd(n, tup)))
		# call find_inv to find the inverse
		sol = find_inv(tup, n)
		if sol is not None:
			a_tup = (tup, sol)
			result_list.append(a_tup)
	return result_list

def find_inv(a, n):
	if regular_gcd(a, n) != 1:
		return None
	s1, s2, s3 = 1, 0, a
	t1, t2, t3 = 0, 1, n
	while t3 != 0:
		quotient = s3 // t3
		t1, t2, t3, s1, s2, s3 = (s1 - quotient * t1), (s2 - quotient * t2), (s3 - quotient * t3), t1, t2, t3
	return s1 % n
