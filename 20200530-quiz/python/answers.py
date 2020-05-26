import sys
import os
import pickle

target = list(filter(lambda x: x.startswith(sys.argv[1]), os.listdir('answers')))[0]

parts = target.split('.')[0].split('-')
header = f"Round {parts[0]} - {' '.join(parts[1:]).capitalize()}"
print('-' * 80)
print(f"{header}")
print('-' * 80)
print("\n\n".join(pickle.load(open(f'answers/{target}', 'rb'))))
print('-' * 80)
