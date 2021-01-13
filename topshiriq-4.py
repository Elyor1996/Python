s = input("Matnni kiriting : ")

def check_for_unli(text):
    unli_cnt = 0
    unli = ['a' , 'o' , 'i', 'e' , 'u' , 'o`'']
    for i in unli:
        unli_cnt +=text.count(i)
    return unli_cnt

def check_for_undosh(text):
    undosh_cnt = 0
    undosh = ['b','d','f']
    for i in undosh:
        undosh_cnt+=text.count(i)
    return undosh_cnt


print ("Unlilar : " , check_for_unli(s) , "\nUndoshlar : " , check_for_undosh(s))
