import measure
import functools

def countingsort(a, n):
	c = [0] * n
	b = [None] * len(a)
	for x in a:
		c[x] += 1
	for i in xrange(1, len(c)):
		c[i] = c[i] + c[i-1]
	for x in a:
		b[c[x]-1] = x
		c[x] -= 1
	return b

func = functools.partial(countingsort, n = 300000)
print measure.time(func)