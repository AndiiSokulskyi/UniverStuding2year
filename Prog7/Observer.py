from LinkedList import *
from Validation import *


class Logger:
    def __init__(self, event):
        self._event = event

    def print_to_file(self, f):
       f.write(str(self._event) + '\n')


class Event:
    def __init__(self, name, old_loe, pos, new_l, pos2=None):
        self._observers = []
        self._name = name
        self._old_loe = old_loe
        self._poss = pos
        self._pos2 = pos2
        self._new_l = new_l

    def __str__(self):
        if self._pos2 == None:
            return '"{self._name}" [{self._old_loe}] position(s):{self._poss} [{self._new_l}]'.format(self=self)
        else:
            return '"{self._name}" [{self._old_loe}] position(s):{self._poss}-{self._pos2} [{self._new_l}]'.format(self=self)

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, observer):
        observer.update(self)



class Observer:
    def __init__(self, events = []):
        self._events = events

    def update(self, event):
        self._events.append(event)

    def logger_print_in_file(self, file):
        f = file_existing(file, "w")
        for event in self._events:
            l = Logger(event)
            l.print_to_file(f)
        f.close()




