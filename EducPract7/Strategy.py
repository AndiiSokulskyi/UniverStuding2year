from Validation import *
from Iterator import *
from LinkedList import *


class Context:

    def __init__(self, strategy = None):
        self._strategy = strategy

    def get_strategy(self):
        return self._strategy

    def set_strategy(self, strategy = None):
        self._strategy = strategy

    def generation(self, ll, pos, txtorN, obs):
        ll = self._strategy.gener(self, ll, txtorN, pos, obs)
        return ll


class Strategy_Iter():
    def gener(self, ll, N, pos, obs):
        itr = GN_Iterator()
        temp_l = ll.copy()
        if pos == 0:
            for i in range(N):
                elem = next(itr)
                ll.push_back(elem[0])
                ll.push_back(elem[1])
        else:
            for i in range(N):
                elem = next(itr)
                ll.linsert(pos, elem[0])
                ll.linsert(pos + 1, elem[1])
        e = Event("add", temp_l, pos, ll)
        e.notify(obs)
        return ll


class Strategy_File():
    def gener(self, ll, txt, pos, obs):
        temp_l = ll.copy()
        tpos = pos
        file = file_existing(txt, "r")
        while True:
            f = file.readline().strip('\n')
            if not f:
                break
            f = TxtIntValidation(f)
            if pos == 0:
                ll.push_back(f)
            else:
                ll.linsert(tpos, f)
                tpos += 1
        file.close()
        e = Event("add", temp_l, pos, ll)
        e.notify(obs)
        return ll