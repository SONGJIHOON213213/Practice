N = int(input())
for i in range(1 , N+1):
    stars = '*' * i
    spaces = ' ' * (N - i) 
    print(f'{spaces}{stars}')  
