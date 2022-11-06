#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:09:18 2022

@author: mohammad
"""


class Read_file():
    def __init__(self, path):
        self.path=path
        
    def read_data (self):
        
        f = open(self.path, encoding="utf-8")
   
        sentence = []
        all_sentence=[]
        labels = []
        all_labels=[]
        sent_num = 1
        all_words=[]
        all_words_labels=[]

        lines=f.readlines()
    
        for line in lines:
            temp=line.split()
            try:
            
                if not temp:
                    _list=[]
                    _list.append(sent_num)

                    _list.append(' '.join(sentence))

                    _list.append(' '.join(labels))
                    
                    all_sentence.append([' '.join(sentence)])
                    all_labels.append([' '.join(labels)])
                    sent_num += 1           
                    sentence = []
                    labels = []
                
                    if sent_num % 100 == 0:
                        print('sent_num=', sent_num)
                    
                
                
                if len(temp)==2:
                    word = temp[0]
                    label = temp[1]
                
                
                    sentence.append(word)
                    labels.append(label.replace('\n', ''))
                
            
                    all_words.append(word)
                    all_words_labels.append(label)

                
            except:
                print(line)
        return all_sentence, all_labels, all_words, all_words_labels
