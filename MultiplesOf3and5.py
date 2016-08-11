"""
Author: Vivek Rana
Usage : Just run the script in a Python enabled computer.
Date :  11-/aug-2016
"""

def main():
    print("Input number of testcases followed by value of n for each case:")
    for _ in range(int(input())):
        N = int(input())- 1
        mul3 = N//3
        mul5 = N//5
        mul15 = N//15 if N>14 else 0
        Sum3 = 3*(mul3*(mul3+1)//2)
        Sum5 = 5*(mul5*(mul5+1)//2)
        Sum15 = 15*(mul15*(mul15+1)//2)
        total = Sum3 + Sum5 - Sum15
        print(total)
    return

if __name__ == '__main__':  #IF the script is called from cmd or directly executed
    main()
    input('Press any key to exit.')
