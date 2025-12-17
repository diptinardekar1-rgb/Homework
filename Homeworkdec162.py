Mi_2025=["Naman Dhir", "Ryan Rickelton","Sherfane Rutherford","Rohit Sharma","Suryakumar Yadav", "Raj Bawa","Corbin Bosch","Will Jacks","Hardik Pandya"
"Mitchell Santner","Tilak Varma", "Jasprit Bumrah"]
 


Rcb_2025=["Virat Kohli","Rajat Patidar","Josh Hazlewood","Yash Dayal","Swapnil Singh","Swastik ChikarTim David","Bhuvneshwar Kumar","Jitesh Sharma","Liam Livingstone"
"Nuwan Thushara"]



pbks_2025=["Aaron Hardie","Arshdeep Singh","Azmatullah Omarzai","Glenn Maxwell","Harnoor Singh","Harpreet Brar","Josh Inglis","Kuldeep Sen",
"Kyle Jamieson","Lockie Ferguson","Marco Jansen"]


Gt_2025=["Shubman Gill","Anuj Rawat", "Arshad Khan","Gurnoor Brar","Ishant Sharma","Jayant Yadav","Jos Buttler","Kagiso Rabada","Kumar Kushagra",
"Manav Suthar","Mohammed Siraj"]

for i in Mi_2025:
    print(i)


for i in Rcb_2025:
    print(i)    

for i in pbks_2025:
    print(i)

for i in Gt_2025:
    print(i)


for i in range(0,len(Mi_2025)):
    if i%2 ==1:
        print(i,"------>",Mi_2025[i])

# 1 ------> Ryan Rickelton
# 3 ------> Rohit Sharma
# 5 ------> Raj Bawa
# 7 ------> Will Jacks
# 9 ------> Tilak Varma    


l =[]
for i in range(len(Mi_2025)):
    l.append(Mi_2025[3])
print(l)                          #Rohit sharm


l =[]
for i in range(len(Gt_2025)):
    l.append(Gt_2025[0])
print(l)                                 #Shubman Gill


l=[]

for i in range(len(Rcb_2025)):
    l.append(Rcb_2025[0:5])
    print(l)                             #Virat Kohli', 'Rajat Patidar', 'Josh Hazlewood', 'Yash Dayal', 'Swapnil Singh'


for i in range(0,len(Rcb_2025)):
    if i%3 == 2:
        print(i,"----->",Rcb_2025[i])

# 2 -----> Josh Hazlewood
# 5 -----> Swastik ChikarTim David
# 8 -----> Liam LivingstoneNuwan Thushara

