s = "0123456789"
a = [1,2,3,4,5,420]
q1a1 = slice(4,8)
q1a2 = slice(4,8,1)
q1b = slice(5, None , 1)
q1c = slice (1,8,2)
q1d = slice (7,0,-2)
print (s[q1a1])
print (s[q1a2])
print (s[q1b])
print (s[q1c])
print (s[q1d])

if "3" in s:
	print("Theres a 3 in variable s")
if "3" not in s:
	print ("There is no 3 in variable s")
print (s+s)
print (s*3)
print (len(s))
print (max(a))
print (min(a))
print (a.index(420))
print (s.count("3"))
del a[2:4]
print (a)
a.append([66, 12])
print(a)
a.extend([66,12])
print (a)
a.insert(1, 1200)
print (a)
a.remove([66,12])
print (a)
print (a.pop())
a.reverse()
print (a)