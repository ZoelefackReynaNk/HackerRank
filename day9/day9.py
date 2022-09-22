import time

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

def searching(querry, book):
    names = list(book.keys())
    numbers = list(book.values())
    if querry in names:
        i = names.index(querry)
        print(f"{querry}={numbers[i]}")
    else:
        print("Not found")

if __name__ == '__main__':
    #querry = ""
    book = { }
    for i in range(n):
        name, contact = list(map(str, input().rstrip().split()))
        book.update({name: contact})
    querries = [ ]
    #for i in range(n):
    while True:
        if len(querries)<= 100000:
            try:
                querry = input()
            #if querry:
            #if querry == str(querry):
                # if querry == querry.islower():
                #     querries.append(querry)
                #     continue
                # else:
                #     break
                #querries.append(querry)
                time.sleep(0.1)
                if querry:
                     querries.append(querry)
                     continue
                else:
                    break
                
            except EOFError:
                #querry = input()
                #querry, other = others   
                break
        else:
            break      
    for i in range(len(querries)):
        searching(querries[i], book)
       
    
#Code base 2:


# import time

# # Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())

# def searching(querry, book):
#     names = list(book.keys())
#     numbers = list(book.values())
#     if querry in names:
#         i = names.index(querry)
#         print(f"{querry}={numbers[i]}")
#     else:
#         print("Not found")

# if __name__ == '__main__':
#     #querry = ""
#     book = { }
#     if n <= 100000:
#         for i in range(n):
#             name, contact = list(map(str, input().rstrip().split()))
#             book.update({name: contact})
#         querries = [ ]
#     #for i in range(n):
#     while True:
#         if len(querries) < 100000:
#             try:
#                 querry = input()
#                 if querry:
#                      querries.append(querry)
#                      #continue
#                 else:
#                     break
                
#             except EOFError:  
#                 break
              
#     for i in range(len(querries)):
#         searching(querries[i], book)
        
        
#import time
from threading import Timer

n = int(input())

def searching(querry, book):
    #names = list(book.keys())
    #numbers = list(book.values())
    d, index = 0, 0
    for i in range(n): 
        if book[i][0] == querry:
            d += 1
            index += i
            break
        else:
            continue
    if d >= 1:
        print(f"{querry}={book[i][1]}")
    else:
        print("Not found")
if __name__ == '__main__':
    #querry = ""
    book = [ ]
    if n <= 100000:
        for i in range(n):
            names_contacts = list(map(str, input().rstrip().split()))
            book.append(names_contacts)
    querries = [ ]
    for i in range(100000):
        #if len(querries) < 100000:
        try:
            
            def list_add(querry, querries):
                if querry:
                    querries.append(querry)
                    #continue   
            timeout = 2.5
            querry = input()
            t = Timer(timeout, input, args=("enter a value", ))
            t.start()
            #prompt = "You have %d seconds to choose the correct answer...\n" % timeout
            t.cancel()
                
        except EOFError:  
            break
            
    for i in range(len(querries)):
        searching(querries[i], book)
        
        
