#create set 

s = set()
s.add(2)
s.add(4)
s.add("dipti")
s.add(29)
s.add(20.5)
print(type(s))
print(s)

# <class 'set'>
# {2, 4, 20.5, 'dipti', 29}


# Remove data 

s.remove("dipti")
print(s)                     # {2, 4, 20.5, 29}

s.remove(20.5)
print(s)                        #{2, 4, 29}


# pop data

print(s.pop())
print(s)                          #2

# discard data
print(s.discard("dipti"))
print(s)                             #{2, 4, 20.5, 29}


# clear a  data 
s.clear()
print(s)                               # set()   



# itration on s

i  = {2,4,"dipti",29,20.5}
for i in i:
    print(i)      
  


# using list duplication is removing

s = [10,20,20,30,40,40]
s1 = set(s)
print(s1)                         # {40, 10, 20, 30}


# tuple of string to set

name = ("dipti","divya","sanika","disha")
n = set(name)
print(n)                                     #{'dipti', 'divya', 'disha', 'sanika'}


#difference on set

s={11,22,33,44,55}
s1={33,44,55,66,77,88}
print(s.difference(s1))                # {11, 22}

s={11,22,33,44,55}
s1={33,44,55,66,77,88}
print(s1.difference(s))                    #{88, 66, 77}


#intersection of set

s={10,20,30,40,50}
s1={30,40,50,70,80,90}
print(s.intersection(s1))                    #{40, 50, 30}

s={10,20,30,40,50}
s1={30,40,50,70,80,90}
print(s1.intersection(s))                       # {40, 50, 30}
