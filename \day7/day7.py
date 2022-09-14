# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

def even_index(list):
    '''decom = []
    res = ""
    for i in range(0, len(list) - 1):
        if i%2 == 0:
            #res = res + list[i]
            decom.append(list[i])
        else:
            continue
    for i in range(0, len(list) - 1):
        if i%2 != 0:
            #res = res + list[i]
            decom.append(list[i])
        else:
            continue
    for i in range(0, len(decom)-1):
        if i% 2 <= (len(decom)) // 2:
            res = res + decom[i]
        else:
            res = " " + res
            res = res + decom[i]'''
    even = ""
    odd = ""
    for i in range(0, len(list)):
        if i%2 == 0:
            even = even + list[i]
        else:
            odd = odd + list[i]
    
    out = even + " " + odd
    print(out)

for i in range(t):
    S = input()
    even_index(S)
