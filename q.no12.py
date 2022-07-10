

string=input("enter a string: ")
n=int(input("enter no of char to be removed: "))
new_string=string.replace(string[0:n],"")
print(new_string)