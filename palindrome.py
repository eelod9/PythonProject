import math
def palindrome(x):
    j = []
    j= str(x)
    wordcount = len(j)
    print(wordcount)
    firsthalf = int(math.ceil(len(j)/2.0))
    
    print(firsthalf)

   
    for letter in j[0:firsthalf]:
        wordcount -= 1
        if (letter == j[wordcount]):
            #print(f"letter {letter} == {j[wordcount]} wordCount ")
            if(wordcount == firsthalf or wordcount == 0):
                #(print("It's a PALINDROME"))
                return True

        else:
            #print(f"letter {letter} != {j[wordcount]} wordCount ")
           # print("NOT A PALINDROME")
            return False
        
        
print(15/4)
  

print(palindrome(121))