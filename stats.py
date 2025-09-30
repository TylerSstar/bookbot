def num_words(a):
        b = a.split()
        c = len(b)
        print(f"Found {c} total words")


def count_char(txt):
	a = []
	d = {}
	for i in txt.lower():
		if i not in a:
			a.append(i)
	for i in a:
		c = txt.lower().count(i)
		d.update({i:c})
	return d

def sort_dict(d):
	a = list(d.keys())
	b = list(d.values())
	f = []
	for i in range(len(a)):
		f.append({"char":a[i],"num":b[i]})
	def sort_on(items):
		return items["num"]
	f.sort(reverse=True,key=sort_on)
	return f
