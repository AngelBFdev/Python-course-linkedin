#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    modified()
    modified('append')
    modified('insert')
    modified('remove')
    modified('pop')
    modified('delete')

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

def modified(opt=''):
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    if (opt==''):
        # print from the second item (paper)
        # stops at 5 and print each 2 item
        # paper lizard
        print(game[1:5:2])

        # Get the index number of the element
        i = game.index('Paper')
        print(game[i])

        # join the array with the value given
        print(', '.join(game))
        print_list(game)

    elif (opt=='append'):
        print('Append')
        # Add computer at the end
        game.append('Computer')
        print_list(game)

    elif (opt=='insert'):
        print('Insert')
        # You can choose where to insert the
        # value. At position 0 in this case
        game.insert(0,'Computer')
        print_list(game)

    elif (opt=='remove'):
        print('Remove')
        # remove item by value
        game.remove('Paper')
        print_list(game)

    elif (opt=='pop'):
        print('Pop')
        # remove value at the end of the list
        # but also return the remove value
        x = game.pop()
        print(x)
        print_list(game)
        # You can also pop a specific item
        game.pop(1)
        print_list(game)

    elif (opt=='delete'):
        print('Delete')
        # You can delete a specific value
        # but also by segment
        del game[1:5:2]
        print_list(game)
    print()


if __name__ == '__main__': main()
