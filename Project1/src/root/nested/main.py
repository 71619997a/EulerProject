'''
Created on Jan 25, 2014

@author: gbeharmarks
'''
import math
import operator

def multList(nums):
    return reduce(operator.mul, nums, 1)

def addList(nums):
    return reduce(operator.add, nums, 1)

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
    for i in range(2,(int)(num**.5)+1):
        if((num*1.0)/(i*1.0)==(int)(num/i)):
            return False
    return True

def primesTo(num):
    primes=[2]
    for i in range(3,num):
        if(isPrime(i)):
            primes.append(i)
    return primes

def isDiv(num,div):
    return (num*1.0)/(div*1.0)==(int)(num/div)
    
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

def split2DString(string,x,digits):
    pass

def addPrimesTo(num):
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

string="08022297381500400075040507785212507791084949994017811857608717409843694804566200814931735579142993714067538830034913366552709523046011426924685601325671370236912231167151676389419236542240402866331380244732609903450244753353783684203517125032988128642367102638406759547066183864706726206802621220956394396308409166499421245558056673992697177878968314883489637221362309750076442045351400613397343133957817532822753167159403800462161409535692163905429635314755588824001754243629855786560048357189070544443744602158515417581980816805944769287392138652177704895540045208839735991607975732162626793327986688366887576220720346336746551232639353690442167338253911249472180846293240627636206936417230238834629969826759857404361620733529783190017431497148868116235705540170547183515469169233486143520189196748"

print dimensionList([2,3,4])