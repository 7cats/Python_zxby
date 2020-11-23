# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 23:29:08 2020

@author: Zixin
"""

import threading

class messenger(threading.Thread):
    
    def run(self):
        for _ in range(100):
            print(threading.currentThread().getName())
            
thread1 = messenger(name = 'send')
thread2 = messenger(name = 'receive')

thread1.start()
thread2.start()