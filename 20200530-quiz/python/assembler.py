import os
import yaml
from random import shuffle
import pickle
from tidylib import tidy_document


presentation = open('python/templates/index.html').read()
section = open('python/templates/round.html').read()

class QuizRound:
  def __init__(self, name):
    self.name = name
    self.body = ''
    self.answers = []
    questions = yaml.safe_load(open(f'questions/{self.name}/questions.yaml').read())
    self.count = len(questions)
    for j, question in enumerate(questions):
      self.body += f"<section>{j + 1}: {question['question']}</section>"
      self.answers.append(f"{j + 1}:\t{question['question']}\n\t{question['answer']}")
    self.index = 0

  def title(self):
    return self.name.replace('-', ' ').capitalize()

  def set_index(self, value):
    self.index = value

  def save_answers(self):
    with open(f'answers/{self.index}-{self.name}.pickle', 'wb') as a:
      pickle.dump(self.answers, a)

  def __str__(self):
    return section.replace('NUMBER', f"{self.index}").replace('TITLE', self.title()).replace('COUNT', str(self.count)).replace('QUESTIONS', self.body)

class PictureRound(QuizRound):
  def __init__(self, name):
    self.name = name

    self.data = yaml.safe_load(open(f'questions/{self.name}/symbols.yaml').read())
    self.body = f"<section><h2>{self.data['premise']}</section></h2>"
    self.count = len(self.data['pictures'])
    self.answers = list(map(lambda x: f"{x[0]}: {x[1]}", self.data['pictures'].items()))

    for k, img in enumerate(sorted(os.listdir(f'questions/{name}/'))):
      if img.endswith('jpg'):
        self.body += '<section data-background-color="rgb(255, 255, 255)">'
        self.body += '<span class="symbol">'
        self.body += f'<h3>{k + 1}: </h3>'
        self.body += f'<img data-src="highway-code/{img}" width="400px"/>'
        self.body += '</span>'
        self.body += '</section>'

class MatcherRound(QuizRound):
  def __init__(self, name):
    self.name = name
    self.data = yaml.safe_load(open(f'questions/{name}/events.yaml').read())
    self.events = self.data['events']
    shuffle(self.events)
    self.count = len(self.events)
    self.answers = list(map(lambda x: f"{self.data['premise']} {x['event']} {x['year']}", self.events))

    self.body = '<section>'
    self.body += f'<h4>{self.data["premise"]}</h4>'
    self.body += '<ul>'
    for event in self.events:
      self.body += f'<li class="fragment">{event["event"]}</span>'

    self.body += '</ul>'
    self.body += '</section>'

rounds = []

for rnd in [
  'food-and-drink',
  'ireland',
  'celebrity-gossip',
  'childrens-literature',
  ]:

  quiz_round = QuizRound(rnd)
  rounds.append(quiz_round)

rounds.insert(2, PictureRound('highway-code'))
rounds.insert(5, MatcherRound('the-90s'))

output = ''
for i, rnd in enumerate(rounds):
  rnd.set_index(i + 1)
  print(f"Writing round {rnd.index} - {rnd.title()}")
  output += str(rnd)
  rnd.save_answers()

final = presentation.replace('CONTENT', output).replace('BACKGROUND_IMAGE', 'images/pub.jpg')

document, errors = tidy_document(final, options={'numeric-entities':1})

with open('reveal.js-master/index.html', 'w') as output:
  output.write(document)
