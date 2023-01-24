#  Python code to create a function called most_frequent that takes a string and 
# prints the letters in decreasing order of frequency. Use dictionaries.

def most_frequent(string):
    
     print("enter the string " + string)
    
     d = dict() # Empty dictionary

     for i in string:
           if i in d:
            d[i] += 1

           else:

            d[i] = 1

     return d

print(most_frequent("missippi"))



