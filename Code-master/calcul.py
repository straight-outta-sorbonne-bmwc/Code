# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 00:48:36 2019

@author: franc
"""
import math 

def distance(a,b): #calcule la distance entre 2 points, prend en paramètre 2 points de la forme (x, y)
    return round(math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2), 2) #retourne la distance entre le point a et b et l'arrondie à 2 chiffres aprés la virgule 

def calculvecteur(a, b): #calcule les coordonnées du vecteur ab, prend paramètre 2 points de la forme (x, y)
    u=b[0]-a[0]
    v=b[1]-a[1]
    return u,v #retourne les coordonnés du vecteur ab sous la forme d'un tuble

def normevecteur(a): #calcule la norme du vecteur a, prend en paramètre les coordonnées d'un vecteur de la forme (x, y)
    return round(math.sqrt(a[0]*a[0]+a[1]*a[1]), 2) #retourne le résultat arrondie à 2 chiffres après la virgule

def normalize(a): #normalise un vecteur et prend en paramètre les coordonnées d'un vecteur sous la forme (x, y)
    n=normevecteur(a)/4
    return round(a[0]/n,2), round(a[1]/n,2) #retourne un tuple

def angle2vect(a,b): #calcule l'angle entre le vecteur a et b prend en paramétre les coordonnées des vecteurs sous la forme (x, y)
    in1=a[0]*b[0]+a[1]*b[1]
    in2=normevecteur(a)*normevecteur(b)
    return round(math.acos(in1/in2)*(180/math.pi), 2) #retourne la valeur de l'angle en degré arrondi à 2 chiffres après la virgule
