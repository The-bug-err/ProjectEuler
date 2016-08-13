"""
Author: Vivek Rana
Usage : Just run the script in a Python enabled computer.
Date :  13-Aug-2016
"""

ListOfPalindromes = list()

def checkPalindrome(num):
    strNum = str(num)
    half = len(strNum)//2
    for i in range(half):
        if strNum[i] != strNum[-(i+1)]:
            return False
    return True

def findPalindromes():
    for i in range(110,999,11):
        for j in range(100,999):
            num = i*j
            if(checkPalindrome(num)):
                ListOfPalindromes.append(num)
def main():
    findPalindromes()
    ListOfPalindromes.sort()
    for T in range(int(input("Number of test cases : "))):
        N = int(input("Case "+str(T+1)+":"))
        for i in ListOfPalindromes[::-1]:
            if i < N :
                print(i)
                break

if __name__ == '__main__':  #IF the script is called from cmd or directly executed
    main()
    input('Press any key to exit.')
