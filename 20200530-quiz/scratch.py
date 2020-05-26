# from os import listdir, remove, rename
# from random import shuffle

from yaml import dump

# remove('questions/highway-code/symbols.yaml')

# symbols = listdir('questions/highway-code')
# shuffle(symbols)

# data = {}
# for index, file in enumerate(symbols):
#   name = file.replace('.jpg', '').replace('-', ' ').capitalize()
#   label = f"{index + 1:02}"
#   rename(f'questions/highway-code/{file}', f'questions/highway-code/{label}.jpg')
#   data[label] = name

# with open('questions/highway-code/symbols.yaml', 'w') as y:
#   y.write(dump(data))

# inputs = open('questions/celebrity-gossip/questions.txt').read().split("\n\n")

# def reform(q):
#   bits = q.split("\n")
#   return {
#     'question': bits[0][3:],
#     'answer': bits[1][3:]
#   }

# questions = list(map(reform, inputs))
# with open('questions/celebrity-gossip/questions.yaml', 'w') as y:
#   y.write(dump(questions))
