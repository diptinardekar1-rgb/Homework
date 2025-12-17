#using for loop make oprations on string 

s = "Ditpt Dilip Nardekar"

1.name print
for ch in s:
    print(s)


2.count of white spaces

count = 0
for ch in s:
    if ch ==" ":
        count = count + 1
print(f"There are{count} white spaces in {s}.")

3. enter find to charachter using user

char = input("Enter any char to find count = ")

count = 0
for i in s:
    if i == char:
        count = count + 1

print(f"there are {count} {char} s in {s}") 

4. count how many i in string

count = 0
for i in s:
    if i =="i":
        count = count + 1
print("Total count of char i=",count)

5. count how many d  in string

count = 0
for i in s:
    if i == "d":
        count = count + 1
print("Total count of char d=",count)      


6. vowels count in string  
 
vowels = "aeiouAEIOU"

count = 0
for ch in s:
    if ch in vowels:
        count= count+1

print("total numbers of vowels in string=",count)      

7 
s1 = "i miss you mummy ❤︎"

for i in s1:
    print(s1)


print(s.upper())                      #upper
print(s.lower())                      #lower
print(s.title())                     #title
print(s.capitalize())                #capitalize
print(s.index("N"))                  #index
print(s.count("i"))                 #count
print(s.isalpha())                  #isalpha
print(s.isalnum())                 #isalnum
print(s.replace("Dipti","Divya"))  #replace
print(s.split())                    #split
sorted(s)                            #sorted




  
   







