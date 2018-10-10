def verifica(a,b,c):
    nums = [a,b,c]
    maior = nums[0]
    for x in nums:
        if x > maior:
            maior = x
    print (maior)

        
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

verifica(num1,num2,num3)
