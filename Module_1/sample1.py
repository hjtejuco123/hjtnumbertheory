# GCD
def gcd_simulation(a,b):
    print ("GCD Simulation")

    step = 1
    while b!=0:
        quotient = a//b
        remainder = a%b    
        print (f"Step {step}: {a} / {b} = {quotient} remainder {remainder}")
        a = b 
        b = remainder  
        step += 1
    print (f"GCD is {a}")
    return a

#input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Call the function 
gcd_simulation(num1, num2)