#slicing and itration of our name

s = "diptinardekar"
print(s[0:5])     dipti
print(s[5:13])    nardekar
print(s[-13:-8])  dipti
print(s[-8:-3])   narde
print(s[::3])     dtare
print(s[0:5:2])   dpi
print(s[::-1])    rakedranitpid
print(s[1:3])     ip
print(s[5:6:1])    n
print(s[-7:-5:2])   a 


for char in s:
    print(char)


count = 0
for ch in s:
    if ch == "i":
        count = count+1
print("total count of ch a=",count)











