# coding: utf-8
import os,sys,time

def bersih ():
        os.system("clear")
usr="rj"
pwd="rj"    

def login():
    bersih()
    print("\033[1;34m+\033[1;31m==========================\033[1;34m")
    print("\033[1;31msubrek \033[1;37mTUTORIAL @NDROID")
    print("\033[1;34m+\033[1;31m=========================\033[1;34m")
    x = raw_input("\033[1;31mUsername \033[1;37m:")
    y = raw_input("\033[1;31mPassword \033[1;37m:")
    if x==usr and y==pwd:
        print("\033[1;34mLogin Berhasil")
        time.sleep(1)
        bersih()
    elif x==""" and y==""":
       print("\033[1;31moke mantap")
       os.system("python2 home.py")
    else:
       print("\033[1;37mPassword salah")
       os.system("python2 home.py")
       

login()