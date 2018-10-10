print('it is working now')

P = 10 ** 7
r = 5 / 100 /12
n = 20 * 12
A = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
print('P=',P)
print('r=',r)
print('n=',n)
print('A=',A)

## print header
#print('Month\tInstalment\tInterest\tPrincipal\tOutstanding')
## print first row
#Outstanding = P
#Month = 1
#Instalment = A
#Interest = Outstanding * r
#Principal = A - Outstanding * r
#Outstanding = Outstanding - Principal
#print('{0:03d}\t{1:.02f}\t{2:.02f}\t{3:.02f}\t{4:.02f}'.format(Month,Instalment,Interest,Principal,Outstanding))
#
#Month = Month + 1
#Instalment = A
#Interest = Outstanding * r
#Principal = A - Outstanding * r
#Outstanding = Outstanding - Principal
#print('{0:03d}\t{1:.02f}\t{2:.02f}\t{3:.02f}\t{4:.02f}'.format(Month,Instalment,Interest,Principal,Outstanding))
#
#Month = Month + 1
#Instalment = A
#Interest = Outstanding * r
#Principal = A - Outstanding * r
#Outstanding = Outstanding - Principal
#print('{0:03d}\t{1:.02f}\t{2:.02f}\t{3:.02f}\t{4:.02f}'.format(Month,Instalment,Interest,Principal,Outstanding))
#
#for i in range(237):
#    Month = Month + 1
#    Instalment = A
#    Interest = Outstanding * r
#    Principal = A - Outstanding * r
#    Outstanding = Outstanding - Principal
#    print('{0:03d}\t{1:.02f}\t{2:.02f}\t{3:.02f}\t{4:.02f}'.format(Month,Instalment,Interest,Principal,Outstanding))


month = 0
outstanding = P

def print_one_month(month, outstanding):
    month = month + 1
    interest = outstanding * r
    principal = A - interest
    outstanding = outstanding - principal
    print('{0:03d}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}'.format(month, A, interest, principal, outstanding))
    return month, outstanding


for i in range(240):
    month, outstanding = print_one_month(month, outstanding)
