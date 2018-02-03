import time

def euclid(m, n):
	while (n != 0):
		r = m % n
		m = n 
		n = r
	return m

def consecIntCheck(m, n):
	t = min(m, n)
	while True:
		if(m%t==0 and n%t==0):
			return t
		else:
			t -= 1

def primeFactors(m):
	factors = []
	t=2
	while (m != 1):
		if(m%t==0):
			factors.append(t)
			m = m/t
			t=2
		else:
			t +=1
	return factors

def middleSchool(m, n):
	mfactors = primeFactors(m)
	nfactors = primeFactors(n)
	gcd = 1
	for mfactor in mfactors:
		if mfactor in nfactors:
			gcd *= mfactor
			nfactors.remove(mfactor)
	return gcd

def effGCD(m, n):
        start = time.clock()
        euclid(m, n)
        end = time.clock()
        print("Euclid time: ", end-start)
        start = time.clock()
        consecIntCheck(m, n)
        end = time.clock()
        print("Consecutive Integer Checking time: ", end-start)
        start = time.clock()
        middleSchool(m, n)
        end = time.clock()
        print("Middle School time: ", end-start)

x = 1
while (x<=3):
        m = int(input("Enter an m (must be an int >0): "))
        n = int(input("Enter an n (must be an int >0): "))
        if(m<=0 or n<=0):
                if(x<3):
                        print("Invalid input. Try again")
                else:
                        print("Invalid input. Goodbye")
                x += 1
                continue
        else:
                print("GCD: ", euclid(m,n))
                effGCD(m,n)
                break

