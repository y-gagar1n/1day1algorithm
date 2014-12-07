#Rabin-Karp algorithm

def search(text, pattern):
	d = 256
	q = 101
	m = len(pattern)
	n = len(text)
	p = 0
	t = 0
	h = 1
	for i in range(m-1):
		h = (h * d) % q

	for i in range(m):
		p = (p * d + ord(pattern[i])) % q
		t = (t * d + ord(text[i])) % q

	for i in range(n - m + 1):
		if p == t:
			k = 0
			for k in range(m):
				if pattern[k] != text[i + k]:
					break		
				if k == m - 1:
					print i
		else:
			t = ((d * (t - ord(text[i]) * h) + ord(text[i + m]))) % q
			if t < 0:
				t += q

search("abracadabra", "br")