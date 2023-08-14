print("Welcome to the Love Calculator!")
name1 = input("What is your name : \n").lower()
name2 = input("What is his/her name :  \n").lower()

t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')

l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')

true_total = t + r + u + e 
love_total = l + o + v + e
love_score = str(true_total) + str(love_total)
print("Here is your love score : " + str(love_score))

if(int(love_score) < 10):
    print("Sorry to say that it ain't no good homie")
elif(int(love_score) > 90):
    print('Blud think they romeo juliet lmao')
else:
    print("Mid tbh")