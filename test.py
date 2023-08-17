# test.py
def prime(n):
    if n == 1 or n == 2:
        for x in range(1, n +1):
            print(f"{x} ", end='')

    else:
        for i in range(2, n):
            if n % i == 0:
                continue
            else:
                print(i)

    
            
   

prime(3)
