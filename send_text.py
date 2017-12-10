#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:28:58 2017

@author: ywang
"""

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC72865c58eca1880515a440b957db2cc9"
# Your Auth Token from twilio.com/console
auth_token  = "8f2922234ef74d4001afbeee2199ef67"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+13144842259", 
    from_="+13142070165 ",
    body="Hello from Python!")

print(message.sid)