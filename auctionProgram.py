from replit import clear
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
    return True
  else(ans == 'no'):
    return False

contin = True
print(logo)
while(contin):
  
  name = input("What's your name?: ")
  bid = input("What's your bid?: ")
  ans = input("Are there other users to bid?: ")
  contin = checkAnswer(ans)
