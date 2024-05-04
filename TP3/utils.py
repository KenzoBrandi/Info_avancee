#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:31:53 2024

@author: e2305563
"""
from os import listdir

def read_corpus(f,n=-1):
    with open(f,"r",encoding="utf-8") as flux:
        texte = flux.read()
        dic = {}
        i  =0
        while (i <= n or n == -1) and i < len(texte):
            if texte[i] in dic:
                dic[texte[i]] += 1
            else:
                dic[texte[i]] = 1
            i += 1
                
        longueur = len(texte)
        
        return { key : value/longueur for key,value in dic.items()}
   


def read_references(dirpath,n=-1):
    fichiers = listdir(dirpath)
    dic = {}
    for fichier in fichiers:
        file_path = str(dirpath)+ fichier
        dic[fichier] = read_corpus(file_path,n=-1)
    return dic


        
    
