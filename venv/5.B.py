name = "Anupreet Kaur"
print(name, type(name), hex(id(name)))
print(len(name))
print(max(name))
print(min(name))


print(name[1])
print(name[len(name)-1])

print(name[1:5])
print("K" in name)

email = "anupreet@example.com"

if ("@" in email) and ("." in email):
    print("valid email")

else:
    print("invalid emial")