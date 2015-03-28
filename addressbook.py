#!/usr/bin/python3

import pickle

from contact import Contact

class AddressBook:
    """ A simple addressbook class"""
    def __init__(self):
        self._data={}

    def add(self, contact):
        self._data[contact['firstname']+' '+contact['surname']]=contact

    def list(self):
        return self._data.keys()

    def __str__(self):
        return self._data.__str__()

    def save(self,savefile='addressbook.pickle'):
        with open(savefile,'wb') as f :
            pickle.dump(self._data, f, pickle.HIGHEST_PROTOCOL)

    def load(self,savefile='addressbook.pickle'):
        with open(savefile,'rb') as f :
            self._data=pickle.load(f)
        
        
if __name__ == "__main__" :
    abook=AddressBook()
    abook.add(Contact("robert", "bridge", "My house", "robert@robbieab.com", "+123456789"))
    abook.add(Contact("roberta", "bridge", "My house", "robert@robbieab.com", "+123456789"))
    print(abook.list())
    print(abook)
    abook.save()
    del abook
    abook=AddressBook()
    abook.load()
    print(abook.list())
    print(abook)



