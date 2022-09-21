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
                querries.append(querry)
                time.sleep(0.5)
                break
                
            except EOFError:
                #querry = input()
                #querry, other = others   
                break
        else:
            break      
    for i in range(len(querries)):
        searching(querries[i], book)
        
        
