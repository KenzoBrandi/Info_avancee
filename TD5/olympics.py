#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:10:02 2024

@author: e2305563
"""

import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def deduplicate(f1, f2):
    li = []
    index = []
    with open(f1) as flux1:
        reader = csv.reader(flux1,delimiter=',')
        for row in reader:
            if not(row[1:] in li):
                li.append(row[1:])
                index.append(row[0])        
        for i in range(len(li)):
            li[i] = [index[i]] + li[i]
                  
    with open(f2,"w", newline='') as flux2:
        writer = csv.writer(flux2,delimiter=',')
        for row in li:
            writer.writerow(row)
        
        
def normalize(f1,f2):
    li = []
    with open(f1) as flux1:
        reader = csv.reader(flux1,delimiter=',')
        for row in reader:
            if row[2] == 'Male':
                row[2] = 'M'
            elif row[2] == 'Female':
                row[2] = 'F'
            li.append(row)       
    with open(f2,"w", newline='') as flux2:
        writer = csv.writer(flux2,delimiter=',')
        writer.writerows(li)
        
def filter_medal(f1, f2):
    li = []
    with open(f1) as flux1:
        reader = csv.reader(flux1,delimiter=',')
        for row in reader:
            if row[0] == '' or int(row[-1]) > 0:
                li.append(row)
    with open(f2,"w", newline='') as flux2:
        writer = csv.writer(flux2,delimiter=',')
        writer.writerows(li)
           
def clean_data(f1, f2): 
    # deduplicate(f1, f2)      
    normalize(f1, f2) 
    filter_medal(f2,f2 )      

def exercice5(file):
    df = pd.read_csv(file)
    print("3 premières lignes: ")
    print(df.head(3))
    print()

    print("3 dernières lignes:")
    print(df.tail(3))
    print()

    print("3 lignes aléatoires:")
    print(df.sample(3))
    print()

    print("Description de la table:")
    print(df.describe())
    print()
    
def exercice6(file):
    df = pd.read_csv(file)
    #les 3 pays qui ont obtenu le plus de médailles
    df_grouped_pays = df.groupby("Team")["Medal"].count()
    df_sorted_pays = df_grouped_pays.sort_values(ascending=False)
    print("les 3 pays qui ont obtenu le plus de médailles: ")
    print(df_sorted_pays.head(3))
    
    #les 3 athlètes féminins qui ont obtenu le plus de médailles d'or
    df_femme = df[ (df["Sex"] == "F") & (df["Medal"] == "1")]
    df_grouped_femme = df.groupby("Name")["Medal"].count()
    df_sorted_femme = df_grouped_femme.sort_values(ascending=False)
    print("les 3 athlètes qui ont obtenu le plus de médailles: ")
    print(df_sorted_femme.head(3))
    
    # les athlètes français qui ont obtenu des médailles d’or après 1980
    df_french_after1980 = df[(df["Year"]>1980) & (df["Team"] == "France")& (df["Medal"] == 1)]
    df_grouped_french_after1980 = df_french_after1980.groupby("Name")["Medal"].count()
    print("les athlètes français qui ont obtenu des médailles d’or après 1980: ")
    print(df_grouped_french_after1980)
    
def exercice7(file):
    df = pd.read_csv(file)
    df_grouped_pays = df.groupby('Team')['Medal'].count()
    ten_teams = df_grouped_pays.head(10).reset_index()
    print(ten_teams)

    sns.barplot(data=ten_teams, x='Team',y='Medal')
    plt.xticks(rotation=90)
    plt.show()
    
def exercice8(file):
    df = pd.read_csv(file)
    df_france_ete = df[(df["Team"] == "France") & (df["Season"] == "Summer")]
    df_grouped = df_france_ete.groupby("Year")["Medal"].count().reset_index()
    sns.barplot(data=df_grouped,x= "Year",y="Medal")
    plt.show()
    
def exercice8_part2(file):
    df = pd.read_csv(file)
    df_or= df[(df["Team"] == "France") & (df["Season"] == "Summer") & (df["Medal"] == 1)]
    df_argent= df[(df["Team"] == "France") & (df["Season"] == "Summer") & (df["Medal"] == 2)]
    df_bronze= df[(df["Team"] == "France") & (df["Season"] == "Summer") & (df["Medal"] == 3)]
    df_or_grouped = df_or.groupby("Year")["Medal"].count().head(10).reset_index()
    df_argent_grouped = df_argent.groupby("Year")["Medal"].count().reset_index()
    df_bronze_grouped = df_bronze.groupby("Year")["Medal"].count().reset_index()   
    sns.histplot(data=df_or_grouped.head(10), x='Year',y='Medal',color='gold')
    sns.histplot(data=df_argent_grouped.head(10), x='Year',y='Medal', color='silver')
    sns.histplot(data=df_bronze_grouped.head(10), x='Year',y='Medal',color='#CD7F32')
    plt.xticks(rotation=90)
    plt.show()
    
clean_data("olympics.csv","olympics.cleaned.csv")
# exercice5("olympics.cleaned.csv")
# exercice6("olympics.cleaned.csv")
# exercice7("olympics.cleaned.csv")
# exercice8("olympics.cleaned.csv")
exercice8_part2("olympics.cleaned.csv")