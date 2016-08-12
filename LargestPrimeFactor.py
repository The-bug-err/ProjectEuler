"""
Author: Vivek Rana
Usage : Just run the script in a Python enabled computer.
Date :  12-Aug-2016
"""

def findPrime(N):
    while( N%2 == 0):
        N = N//2
    if N == 1:
        return 2
    i = 3
    sqrtN = int(N**0.5)
    while(i<=sqrtN and i<N):
        if (N%i == 0):
            N = N//i
            i = 3
        else:
            i += 2
    if N > 2:
        return N
    else:
        return i

def main():
    for T in range(int(input("Test cases : "))):
        N = int(input("Number "+str(T+1)+" : "))
        print(findPrime(N))
    return

if __name__ == '__main__':  #IF the script is called from cmd or directly executed
    main()
    input('Press any key to exit.')
