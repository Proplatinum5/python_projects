#jabber = open('Jabberwocky.txt', 'r')
#
#for line in jabber:
#    print(line.strip())
## print(len(line))
#
#jabber.close()

#with open('Jabberwocky.txt', 'r') as jabber:
#     # for line in jabber:
#     #   print(line.rstrip())
#    lines = jabber.readlines()
#
#print(lines)
#print(lines[-1:])
#
#for line in reversed(lines):
#    print(line, end='') # do some processing in reversed order.
#
##
#with open('Jabberwocky.txt') as jabber:
#    text = jabber.read()
#
#for character in reversed(text):
#    print(character, end='')
#
with open('Jabberwocky.txt')as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)

with open('Jaberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break




