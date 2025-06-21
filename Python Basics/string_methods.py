a = "!!!Nandan !!!! Nandan"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Nandan" , "Aditya"))
print(a.split(" "))

b = "nAnDAn21"
print(b.capitalize())
print(b.center(20))
print(a.count("!"))
print(a.endswith("!"))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(b.isalnum())
print(b.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())

str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization"  #true only when first letter of each word is capital
print(str1.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())