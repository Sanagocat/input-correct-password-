#Guess Correct Password
#1.Password is a 4 digit number
#2. When the user enters 4 numbers, it tells whether the password is large or small.
#3. Total 5 input chances are given. if all chances are gone, 
#    print "YOU FAILED!!"
#4. If password is correct, print "correct password!!"

attempts=0
#correct password
answer1 = 5381

print("=======================PASSWORD 1==========================")

while(True):
  huh=int(input("guess the password! I am a 4 digit, Match it!  "))

  if huh==5381:
    print("You are a Genius!")
    break

  attempts = attempts + 1

  if attempts==1:
    print("4 more! I am over 5000 and smaller than 6000")
  elif attempts==2:
    print("3 more! I have less than 5500")
  elif attempts==3:
    print("2 more! a year+16 days")
  elif attempts==4:
    print("Last chance! 53__")
  elif attempts==5:
    print("NO MORE CHANCES LEFT! FAIL!!!!")
    print("Answer was 5381")
    break


print("=======================PASSWORD 2==========================")
#2. When the user enters 4 numbers, it tells whether the password is large or small.
    
answer2 = 1234
while(True):
  yey=int(input("guess the second password! I am a 4 digit, Match it!  "))

  if yey==answer2:
    print("You are a real Genius!")
    break
  elif yey<answer2:
    print("answer is bigger.")
  elif yey>answer2:
    print("answer is smaller")

  attempts = attempts + 1

  if attempts==1:
    print("4 more!")
  elif attempts==2:
    print("3 more!")
  elif attempts==3:
    print("2 more! ")
  elif attempts==4:
    print("Last chance!")
  elif attempts==5:
    print("NO MORE CHANCES LEFT! FAIL!!!!")
    print("Answer was " + str(answer2) )
    break
