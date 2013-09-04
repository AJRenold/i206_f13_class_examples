#! usr/bin/env python

__python_version__ = '2.7.3'
__can_anonymously_use_as_example__ = True

import random

def greeting():
  """Prints game instructions"""
  print "Welcome to South Hall! Guess the standing of its residents."
  print "- 1: newbie"
  print "- 2: oldie"
  print "- 3: guardian"
  print ""

def readFile(filename):
  """Reads the input file and saves the contents into a dictionary"""
  infile = open(filename,'r')
  dic = {}
  for line in infile:
    name, standing = line.split(",")
    dic[name.strip()]=standing.strip()
  infile.close()
  return dic

def getRandomName(input_dict):
  """Picks a random name from the keys in the dictionary and
   returns a tuple with name and standing"""
  names = input_dict.keys()
  randomName = random.choice(names)
  standing = input_dict[randomName]
  return (randomName, standing)
    
## name unclear getStandingCategory
def standingNumber(numerical_standing):
  """Takes standing numerical value and returns it as a string"""
  standings = {'1':'newbie', '2':'oldie', '3':'guardian'}
  return standings[numerical_standing]
  
def guessIsValid(user_guess):
  """Checks whether the user input is valid"""
  if user_guess in ['1', '2', '3']:
    return True
  else:
    return False
  
def main():
  points = 0
  greeting()
  residents = readFile('ischoolorder.txt')
  while True:
    (name, standing) = getRandomName(residents)
    print name
    guess = raw_input("--> ")
    while (not guessIsValid(guess)): ## Great validation loop
      print "Invalid input! Your guess should be either 1, 2 or 3!"
      guess = raw_input("--> ")
    if guess == standing:
      points = points + 1
      print "Correct! Your score:", points
      print ""
    else:
      print "Wrong!", name, "is a", standingNumber(standing)+"!"
      print ""
      print "Your final score is", str(points) + "."
      exit()
    

# where code execution begins and invokes main()
if __name__ == "__main__":
    main()  
