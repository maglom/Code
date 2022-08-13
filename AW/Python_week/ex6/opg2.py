captured = ('Pikachu', 'Pidgey', 'Abra', 'Pidgey', 'Eevee', 'Pidgey')

captured.count('Pidgey')

set = set(captured)

poke = input('Input pokemon: ')

if poke in set:
    print(f'{poke} has been catched. There have been catched a total of {len(captured)} pokemon, and a total of {len(set)} unique pokemon.')
elif poke not in set:
    print(f'{poke} has not been catched')