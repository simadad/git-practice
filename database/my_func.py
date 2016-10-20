# -*- coding: utf-8 -*-
def numb(prompt=None):                   # ####### make sure customer press a number ########
    while True:
        try:
            n = input(prompt)
            return n
        except NameError:
            if prompt:
                pass
            else:
                print ('number only')
            continue
        except SyntaxError:
            if prompt:
                pass
            else:
                print ('number only')
            continue
