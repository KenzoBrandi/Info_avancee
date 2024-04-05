#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:31:53 2024

@author: e2305563
"""
from os import listdir

def read_corpus(f):
    with open(f,"r",encoding="utf-8") as flux:
        texte = flux.read()
        texte = texte.replace('\n', '')
        
        dic = {}
        for lettre in texte:
            if lettre in dic:
                dic[lettre] += 1
            else:
                dic[lettre] = 1
                
        longueur = len(texte)
        
        return { key : value/longueur for key,value in dic.items()}
   


def read_references(dirpath):
    fichiers = listdir(dirpath)
    dic = {}
    for fichier in fichiers:
        file_path = str(dirpath)+ fichier
        dic[fichier] = read_corpus(file_path)
    return dic
         
print(read_references("Data\\Data\\Test\\"))

    
