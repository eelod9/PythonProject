import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
def checkAnswer(ans):
  if(ans == 'yes'):
    print(chr(27) + "[2J")
    return True
  elif(ans == 'no'):
    return False
bidDict = {}
contin = True
print(logo)
while(contin):
  name = input("What's your name?: ")
  bid = input("What's your bid?: ")
  bidDict[name] = int(bid)
  print(bidDict)
  ans = input("Are there other users to bid?: ")
  contin = checkAnswer(ans)

greatestNum = 0

for key in bidDict:
  value = bidDict[key]
  if (greatestNum < value):
    greatestNum = value
    greatestName = key


print(f"{greatestName} is the highest bidder!")



