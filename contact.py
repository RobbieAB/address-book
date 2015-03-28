#!/usr/bin/python3

class Contact(dict):
    """
    A simple contact object class.
    A contact is an extended dictionary, with 5 keys guaranteed to be present.
    """
    def __init__(self, firstname="", surname="", address="", email="", phone=""):
        super(Contact, self).__init__()
        self['firstname']=firstname
        self['surname']=surname
        self['address']=address
        self['email']=email
        self['phone']=phone

if __name__ == "__main__" :
    cont=Contact("robert", "bridge", "My house", "robert@robbieab.com", "+123456789")
    print(cont)
