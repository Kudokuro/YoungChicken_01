banChar = [
    '\'',
    '"',
    ' or ',
    ' and ',
    '==',
        ]

class _FireWall__LOGIN():
    def __init__(self, **kwarg):
        if 'user' in kwarg.keys():
            self._inputUser = kwarg['user']
        if 'passwd' in kwarg.keys():
            self._inputPass = kwarg['passwd']

    def checkPredicate(self):
        global banChar;
        for i in banChar:
            if i in self._inputUser or i in self._inputPass:
                return False;
        return True;
if __name__ == '__main__':
    a = _FireWall__LOGIN(user = "Bao'or 1 == 1", passwd = 'admin')
    print(a.checkPredicate())
