def multi(a,b,c):
    d = a * b
    e = d * c
    print(e)

def drink(x):
    for i in range(x,0,-1):
        print(i," bottles of root beer on da wall")
    


cookie = int(input("how many cookies you got?"))

if cookie < 3:
    print("you need more cookies")
elif cookie <= 10:
    print("amazing cookies")
else:
    print("gimmie a cookie")

starwar = input("are you jedi or sith")

if starwar == "jedi" or starwar == "Jedi":
    print("you get green lightsaber")
elif starwar == "sith" or starwar == "Sith":
    print("W red lightsaber")
else:
    print("L breadsaber")
    
for i in range(4,42,2):
    print(i, end = " ")
    
print(" ")
GG = 100

while GG >= 50:
    print(GG)
    GG -= 10
    
    
fruit = "bannana"

while fruit != "orange":
    print("knock knock, whos there... banan")
    fruit = input()
print("orange you glad i didn't say banan")

multi(2,3,4)

huh = int(input("gimmie number"))

drink(huh)
