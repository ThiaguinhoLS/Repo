#!usr/bin/python3
# -*- coding: utf-8 -*-

def parse(type, message):

    def xml(message):
        print('Parsing XML')

    def json(message):
        print('Parsing JSON')

    if type == 'json':
        return json(message)
    elif type == 'xml':
        return xml(message)
    else:
        raise ValueError


if __name__ == '__main__':
    parse(type='json', message='my message')
    parse(type='xml', message='my message')
    
