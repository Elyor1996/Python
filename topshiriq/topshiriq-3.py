n = int(input("n:"))
k= 1
c = 1
for k in range(k,n+1):
    c = c * 1/(1+k)**3
print(c)
