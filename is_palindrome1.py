def is_palindrome(n):
	L = str(n)
	N = len(L)
	i = 0
	while i < N-1:
		if L[i] == L[N-1-i]:
			i += 1
			continue
		else:
			return False
	return True

output = filter(is_palindrome, range(1, 1000))
print(list(output))