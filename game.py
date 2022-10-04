import random

gajieni = ['akmens', 'papirs', 'skeres']
computer_turn = random.choice(gajieni)

human_turn = input('Ievadi savu gajienu: ')
print(computer_turn, 'vs.', human_turn)

if human_turn == computer_turn:
    print('neizskirts')
elif human_turn == 'akmens' and computer_turn == 'skeres':
    print('cilveks uzvar')
elif human_turn == 'papirs' and computer_turn == 'akmens':
    print('cilveks uzvar')
elif human_turn == 'skeres' and computer_turn == 'papirs':
    print('cilveks uzvar')
else:
    print('dators uzvar')
exit()
