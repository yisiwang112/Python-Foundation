#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:02:02 2017

@author: ywang
"""

import urllib

def read_text():
    quotes = open("/Users/ywang/Documents/AI/movie_quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    text = urllib.parse.quote(text_to_check)
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    print(output)
    connection.close()
    if output == b'true':
        print("Profanity Alert!!")
    elif output == b'false':
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()