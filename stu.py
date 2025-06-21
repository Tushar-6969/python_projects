from time import *
import random as rd

def mistke(par,userinut):
    error=0
    for i in range(len(par)):
        try:
            if par[i]!=userinut[i]:
                error=error+1
        except:
            error=error+1
    return error                

def speedtime(st,et,ui):
    timedelay=et-st
    tdr=round(timedelay,2)
    speed=len(ui)/tdr
    rs=round(speed)
    return rs




while True:
    print("type yes to play or not to not play")
    up=input("enter yes or no  ")
    if up=="yes":
        test=["my name is tushar","my age is 21"]
        test1=rd.choice(test)
        print(" typing speed test game started in 5 second  ")
        sleep(5)
        print("now type")
        print(test1)
        print("\n \n \n")
        time_s=time()
        testinpput=input("enter: ")
        time_e=time()

        print("speed =",speedtime(time_s,time_e,testinpput),"word per second","\n")
        print("error :",mistke(test1,testinpput))
    elif up=="no":
        print(" thanks for visiting us ")
        break

    else:
        print("invalid input ")
               
