import time
import random

def build_table(text):
	n = len(text)
	if n == 0: return []
	if n == 1: return [0]
	t = [None] * n	
	t[0] = 0		
	pos = 1
	cnd = 0
	while pos < n:		
		if text[pos] == text[cnd]:			
			cnd += 1
			t[pos] = cnd
			pos += 1
		elif cnd > 0:
			cnd = t[cnd]
		else:
			t[pos] = 0
			pos += 1

	return t

def search(text, pattern):
	t = build_table(text)
	n = len(text)
	m = len(pattern)
	pos = 0
	i = 0
	while i < m and pos < n - m + 1:		
		if pattern[i] == text[pos + i]:				
			i += 1
			if i == m:
				return pos
		elif t[i] > 0:
			pos = pos + i - t[i]
			i = t[i]
		else:
			i = 0
			pos += 1


start = time.time()
rnd = [chr(random.randrange(97, 100)) for x in range(1000000)]
end = time.time()
print end - start
start = time.time()
print search(rnd, "ababccabababccbabca")
end = time.time()
print end - start
