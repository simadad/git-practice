def numb():                 # ####### make sure customer press a number ########
    while True:
        try:
            n = input('integer larger than 3 please: ')
            return n
        except NameError:
            continue
        except SyntaxError:
            continue


def size():         # ######## make sure the number is a integer and larger than 3 ########
    while True:
        nn = numb()
        if nn < 3:
            continue
        elif nn % 1 != 0:
            continue
        else:
            return nn

number = size()
nS = 0
nM = 1
print (1)
for i in range(number - 1):
    nL = nM + nS
    nS = nM
    nM = nL
    print (nL)
