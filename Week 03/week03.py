P = 10 ** 7
r = 5 / 100 / 12
n = 20 * 12
A = 50000

month = 0
outstanding = P

def print_one_month(month, outstanding):
    month = month + 1
    interest = outstanding * r
    principal = A - interest
    outstanding = outstanding - principal
    print('{0:03d}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}'.format(month, A, interest, principal, outstanding))
    return month, outstanding

# month, outstanding = print_one_month(month, outstanding)
# month, outstanding = print_one_month(month, outstanding)


while True:
    
    month, outstanding = print_one_month(month, outstanding)
    if outstanding <= 0:
        break

#for i in range(500):
#   month, outstanding = print_one_month(month, outstanding)
#    if outstanding <= 0:
#        break
# if outstanding <= 0 then stop the loop


P = 10 ** 7
r = 5 / 100 / 12
A = 416800
# n = 20 * 12
# A = P * r * (1 + r) ** n / ((1 + r) ** n - 1)

month = 0
outstanding = P

def func(m, o):
    m = m + 1
    interest = o * r
    principal = A - interest
    o = o - principal
    print('{0:03d}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}'.format(m, A, interest, principal, o))
    return m, o

print('Month    Instalment    Interest    Principal    Outstanding')

while True:
    month, outstanding = func(month, outstanding)
    # if outstanding <= 0 then stop the loop
    if outstanding <= 0:
        break



P = 10 ** 7
r = 5 / 100 / 12
A = 416800
# n = 20 * 12
# A = P * r * (1 + r) ** n / ((1 + r) ** n - 1)

month = 0
outstanding = P

headers = ['Month', 'Instalment', 'Interest', 'Principal', 'Outstanding']
for i in range(5):
    #print(i, 'th', 'header')
    # refer to the ith element in the list "header"
    print(headers[i],end='\t')
print()
