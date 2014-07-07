__author__ = 'pavang'
__Date___ = ''

def makeActions():
    acts = []
    for i in range(5):                      # Tries to remember each i
        acts.append(lambda x: i ** x)       # But all remember same last i!
    return acts

def makeActionsDefault():
    acts = []
    for i in range(5):                       # Use defaults instead
        acts.append(lambda x, i = i: i ** x)   # Remember current i
    return acts

if __name__  == '__main__':
    action = makeActionsDefault()
    for number in range(5):
        print(action[number](2))

    print('*' * 100)
    #
    # action = makeActionsDefault()
    # for i in range(5):
    #     print(action[i](2))