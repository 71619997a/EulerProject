'''
Created on Jan 25, 2014

@author: gbeharmarks
'''
import math
import operator
import time
import numpy
import itertools
from sets import Set
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def multList(nums):
    return reduce(operator.mul, nums, 1)

def addList(nums):
    return reduce(operator.add, nums, 0)

def isInt(num):
    return num == (int)(num)



def getBigFactor(num):
    sqrt=(int)(math.floor(math.sqrt(num)))
    factors={1}
    prime=False
    i=1
    while(i**2<=num):
        if(((num*1.0)/(i*1.0)==math.floor(num/i))):
            num/=i
            i=1
        i+=1
            
    return num

def isPalindrome(num):
    if(len(str(num)) == 1):
        return True
    if(len(str(num)) % 2 == 0):
        first=str(num)[:len(str(num))/2]
        last=str(num)[len(str(num))/2:]
        if(last[::-1]==first):
            return True
        else:
            return False
    else:
        first=str(num)[:(len(str(num))+1)/2]
        last=str(num)[(len(str(num))-1)/2:]
        print first
        print last
        if(last[::-1]==first):
            return True
        else:
            return False
        
def isPrime(num):
    for i in range(2,(int)(int(num)**.5)+1):
        if((int(num)*1.0)/(i*1.0)==(int)(int(num)/i)):
            return False
    return True

def primesTo(num):
    primes=[2,3,5,7,11,13]
    for i in range(17,num):
        for j in primes:
            if((i*1.0)/(j*1.0)==(int)(i/j)):
                break
            if((int)(j*j)>i):
                primes.append(i)
                break
    return primes
        
    return True
    return primes

def isDiv(num,div):
    return num%div==0
    
def sumPower(num,n):
    total=1
    for i in range(2,num+1):
        total+=i**n
    return total    
   
def splitStr(string,size): 
    broken=[]
    for i in range(len(string)-size+1):
        broken.append(string[i:i+size])  
    return broken
     
def strToDigits(string):
    digits=[]
    for i in range(len(string)):
        digits.append(int(string[i:i+1]))
    return digits

def dimensionList(values):
    a=[0 for i in range(values[0])] #first, init base array
    for i in range(1, len(values)): #for number of dimensions:
        a=[a for i in range(values[i])] #the array = the old array but length # of times
    return a #smartness, nice one

def divisors(num):
    div=2
    divisor=[1]
    while(div*div<=num):
        if(isDiv(num,div)):
            divisor.append(div)
            if(not div*div==num):
                divisor.append(num/div)
        div+=1
    divisor.sort()
    divisor.append(num)
    return divisor

def properDivisors(num):
    div=divisors(num)
    div.pop()
    return div

def countCollatzChain(num):
    count=1
    while (num != 1):
        if(num % 2 == 0):
            num/=2
        else:
            num=3*num+1
        count+=1
    return count

def digits(num):
    return strToDigits(str(num))

def factorial(num):
    return multList(range(2,num+1))

def letter(num):
    return alphabet[num-1]

def numLetter(let):
    return ord(let)-ord('A')+1

def abundantNumbersTo(num):
    nums=[]
    for i in range(11,num+1):
        if(addList(properDivisors(i))>i):
            nums.append(i)
    return nums
    

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

def fibonacci():
    back=0
    now=1
    count = 1
    while(True):
        yield now,count
        lol=back
        back=now
        now+=lol
        count+=1
        

def digitsToNum(sett):
    strang=""
    for i in range(len(sett)):
        strang+=str(sett[i])
    return int(strang)

def primeSequence(a,b):
    n=0
    while(isPrime(abs(n**2+a*n+b))):
        n+=1
    return n

def genPyTriple(p,q):
    return [p**2-q**2,2*p*q,p**2+q**2]

def rightPerim(num):
    vals=[]
    div=divisors(num)
    for i in div:
        for j in div:
            trick=j/(2*i)-i
            
            if(j/(2*i)-i<i and j/(2*i)-i>0 and isDiv(j,2*i)):
                vals.append(i)
    for i in range(len(vals)):
        vals[i]=genPyTriple(vals[i],num/(2*vals[i])-vals[i])
    return vals

def cycle(sttr):
    return sttr[-1]+sttr[:-1]

def cycles(sttr):
    cyc=[]
    for i in range(len(sttr)):
        cyc.append(sttr)
        sttr=cycle(sttr)
    return cyc

def digPow(num,pow):
    dig=digits(num)
    ret=0
    for i in dig:
        ret+=i**pow
    return ret

def digFactorial(num):
    dig=digits(num)
    ret=0
    for i in dig:
        ret+=math.factorial(i)
    return ret

def allPositive(arr):
    
    if (filter(lambda x: x>=0, arr)==arr):
        return True 
    else:
        return False

t0time = time.time() #dont fuck wit dis
############################################ HERE IS WHERE DOING STUFF IS ############################################
for i in divisors(120):
    for j in numpy.multiply(120/i,rightPerim(i)):
        if (allPositive(j)):
            print j


t1time = time.time() #dont fuck wit dis
print (t1time - t0time)*1000,"ms" #dont fuck wit dis