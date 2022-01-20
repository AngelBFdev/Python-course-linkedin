#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
    #    'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    action('keys')
    action('values')
    action()


def print_dict(o):
    #for x in o: print(f'{x}: {o[x]}')
    # easier to understand
    for k, v in o.items(): print(f'{k}: {v}', end=' - ')

def action(opt=''):
    # More readeable way
    animals = dict(kitten= 'meow', puppy= 'ruff!', lion= 'grrr',
        giraffe= 'I am a giraffe!', dragon= 'rawr')

    if(opt==''):
        # print the value in the key 'lion'
        print(animals['lion'])

        # change the value
        animals['lion']='I am a lion'

        # add new key and value
        animals['monkey']='haha'

        # print found when the value is in animals
        print('found!' if 'godzilla' in animals else 'nope')

        # This would throw an error, since godzilla
        # is not in the dictionary
        #print(animals['godzillla'])

        # To get the value of the key,
        # in this case none, since doesn't exist
        print(animals.get('godzillla'))
        print_dict(animals)

    elif(opt=='keys'):
        print('KEYS')
        # animals.keys access to the keys
        for k in animals.keys(): print(k, end=' ')

    elif(opt=='values'):
        print('VALUES')
        # animals.values access to the values
        for v in animals.values(): print(v, end=' ')

    print()

if __name__ == '__main__': main()
