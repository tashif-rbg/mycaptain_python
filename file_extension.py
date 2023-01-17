# Python program to accept a filename from the user and print the extension of that.
filename = input("input the filename :")
extension = filename.split('.')

print("the extension of the file is :",extension[-1])