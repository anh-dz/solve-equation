from sympy import solve
print("Chương trình giải phương trình phiên bản 1.0")
user = "2x+5=10"
for i in range(10):
	user = user.replace(str(i)+'x', str(i)+'*x').replace(')x',')*x').replace('x(', 'x*(')
user = user.split("=")
st = user[0]+'-' #Vế trái
lst = list(user[1]) #Vế phải

check = 0
for i in lst:
	if check != 0 or i == '(':
		check = 1
		st += i
		if st[-1] == ')':
			check = 0
	else:
		if i == '-':
			st+="+"
		elif i == '+':
			st+="-"
		elif i == '(' or i == 'n':
			st+="("
			check = True
		else:
			st+=i

ans = solve(st)
print("S =", ans)