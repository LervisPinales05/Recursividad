def SumaRecursion(num):
    if num==1:
        return 1
    else:
        return num+SumaRecursion(num-1)

print(SumaRecursion(10))