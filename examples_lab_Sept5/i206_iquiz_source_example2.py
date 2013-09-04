#! usr/bin/env python 
__python_version__ = '2.7.5'
__can_anonymously_use_as_example__ = True

from random import choice

class Person:
  '''Person class with name, role number, and role name attributes'''

  def __init__(self, name, role_number):
    self.name = name
    self.role_number = role_number
    self.role_name = self.role_name(role_number)

  def role_name(self, role):
    if role == 1:
      return 'newbie'
    elif role == 2:
      return 'oldie'
    elif role == 3:
      return 'guardian'


class IQuiz:

  def __init__(self):
    ''' Initiate quiz game with a score of 0 and
    a call to the method of sanitize(), which prepares
    the text file and creates a Person object for each
    person listed in the text file, thereby giving the
    game a list of Person objects to choose from.'''

    self.score = 0
    self.ischool_order = self.sanitize()

  def sanitize(self):
    ''' Opens the file, splits the file on newline
    characters and then on commas to create an array
    of arrays: [['name', 'role], etc.]. The array of
    arrays are iterated over and Person objects are 
    created for each sub-array.'''

    text = open('ischoolorder.txt', 'r').read()
    lines = text.split('\n')
    pairs = [line.split(',') for line in lines]
    people = []
    for pair in pairs:

      ## Commitment to int will cause problems later
      ischooler = Person(pair[0], int(pair[1]))
      people.append(ischooler)
    return people

  def getPlayerGuess(self, person):
    """ Added as part of the example, showing encapsulation of tasks
    in functions and a correct try/except example"""

    while True:
      try:
        guess = int(raw_input(person.name + '\n'))
        break
      except ValueError:
        print "Oops!  That was not a valid number.  Try again..."
    return guess

  def play(self):
    ''' Acts as controller of game because it contains logic.'''

    print 'Welcome to South Hall! Guess the standing of its residents.'
    print '\n- 1: newbie\n- 2: oldie\n- 3: guardian'

    person = choice(self.ischool_order)
    ## You're casting the input as an int without checking it!
    guess = int(raw_input(person.name + '\n'))

    ## Added example of Try Except
    #guess = self.getPlayerGuess(person)

    while guess == person.role_number:
      self.score += 1
      print 'Correct! your score: %(score)s.' % {'score': self.score}
      person = choice(self.ischool_order) 
      guess = self.getPlayerGuess(person)
    print 'Wrong! %(person_name)s is a %(role_name)s.' % {'person_name': person.name, 'role_name': person.role_name}
    print '\n\n Your final score is %(score)s.' % {'score': self.score}


game = IQuiz()
game.play()


