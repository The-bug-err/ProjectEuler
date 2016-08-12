"""
Author: Vivek Rana
Usage : Just run the script in a Python enabled computer.
Date :  12-Aug-2016
"""

def main():
    for T in range(int(input("Number of test cases : "))):
        N = int(input("case "+str(T+1)+" : "))
        a = 0
        b = 1
        evenSum = 0
        while(b < N):
            a, b = b, b + a
            if b < N and b%2 == 0 :
                evenSum += b
        print(evenSum)
    return

if __name__ == '__main__':  #IF the script is called from cmd or directly executed
    main()
    input('Press any key to exit.')
