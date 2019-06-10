#string formatting

name = "fionna"
age = 28
print("welcome to our club %s"%(name))
print("your age is :%d"%(age))
#or
print()
print("hey %s your age is %d"%(name, age))
#other method



#or
print("hey, {} you are {} years old".format( name ,age))

number = input()
for i in range(1, 11):
    print("{} * {} = {}".format(number, i, number*i))