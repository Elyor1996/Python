 # looplar bilan ishlash for operatori bilan 
 # range() bu funksiya oraliqdagi sonlarni chiqaradi yani 
 # range(1,32) 1 dan 32 gacha bo`lgan sonlarni chiqaradi 
 # for ishlashi 
 # for variable in [sequence]
#--------------------------------------------------------
# Masala

# a = int(input('son kiriting:'))
# s = 0
# k = 0 
# for s in range(1,10):
#     k = a*s
#     print("{} x {} = {}" .format(a,s,k))

#---------------------------------------------------------
# Topshiriq

n = int(input('n = '))
k = 0 
m = 0
for k in range(1, n):
    if k%2 == 0:
        m += k

print (m) 