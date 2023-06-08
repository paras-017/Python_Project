import random
val = ['stone', 'paper','scissor']
num = random.randint(0,2)
ai = val[num]

user = input('Enter your choice("stone, paper, scissor"): ')
# win [user, ai]--> [s,sc], [p, s], [sc, p]
# tie [user, ai]--> [s,s], [p, p], [sc, sc]
# lose [user, ai]--> [s,p], [p, sc], [sc,s]

match  user, ai:
     case 'stone','scissor': print('You win')
     case 'paper','stone': print('You win')
     case 'scissor','paper': print('You win')
     case 'scissor','stone': print('You lose')
     case 'stone','paper': print('You lose')
     case 'paper','scissor': print('You lose')
     case 'stone','stone': print('match Tied')
     case 'paper','paper': print('match Tied')
     case 'scissor','scissor': print('match Tied')