import time
import random
import itertools

def search(text, pattern):
	n = len(text)
	m = len(pattern)

	for i in range(n - m + 1):
		t = 0
		for k in range(m):
			if text[i + k] == pattern[k]:
				t += 1
			else: 
				break
		if t == m: 
			return i