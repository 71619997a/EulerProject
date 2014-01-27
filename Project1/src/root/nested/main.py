'''
Created on Jan 25, 2014

@author: gbeharmarks
'''
import math
import operator

def multList(nums):
    return reduce(operator.mul, nums, 1)

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
    
num=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
toS=str(num)
print primesTo(200000)[10000]