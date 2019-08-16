#!/usr/bin/python
# -*- coding: UTF-8 -*-

def switch_channel(token):
    channel = db.select_channel(token)
    channel_num = len(channel)
    print(channel_num)
    #for List_channel in channel:
