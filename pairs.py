def pairs(l):
	if isinstance(l, list) or isinstance(l, str):
		r = []
		for i in range(len(l)):
			r.append(tuple([i, l[i]]))
		return r
	elif isinstance(l, dict):
		r = []
		i = 0
		for k, v in l.items():
			r.append(tuple([i, k, v]))
			i += 1
		return r