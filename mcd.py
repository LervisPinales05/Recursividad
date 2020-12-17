def MCD(a,b):
     if b>a:
          if b%a==0:
              return a
          else: 
               return MCD(b%a,a)

     else:
        if a%b==0:
            return b
        else:
            return MCD(b,a%b)

print(MCD(100,57))