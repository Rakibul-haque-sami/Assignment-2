s = input("Enter something that is atleast 16 digit long: ")

n = ''
l = ''
for i in s:
  if i.isdigit():
    n += i
  else:
    l += i
print(n)
print(l)
e = []
for i in range(0,len(n),2):
  if int(n[i]) % 2 == 0:
    e.append(n[i])
print(e)
print([ord(i) for i in e])
u = []
for i in l:
  if i.isupper():
    u.append(i)
print(u)
print([ord(i) for i in u])
