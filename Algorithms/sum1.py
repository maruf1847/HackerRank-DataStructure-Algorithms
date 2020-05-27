def simpleArraySum(ar):
    total = sum(ar)
    return total

ar_c = int(input())
ar = list(map(int, input().rstrip().split()))
print(simpleArraySum(ar))
