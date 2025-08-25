'''Write a program to print the following star pattern. 
* * * 
*   *   for n = 3 
* * * '''

n = 3
for i in range(1, n + 1):
    if i == 1 or i == n:
        print('* ' * n)
    else:
        print('*' + ' ' * (2 * (n - 1) - 1) + '*')