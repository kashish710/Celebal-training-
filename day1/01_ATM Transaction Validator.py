balance=int(input())
n=int(input())

for i in range(n):
    amount=int(input())
if amount%100==0 and amount<=balance: 
     balance -= amount
     print("Success")
else:
    print("FAILED")
print(balance)