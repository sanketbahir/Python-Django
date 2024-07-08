def Addtion(A,B):
    return A+B

def Calculate(Traget,Value1,Value2):
    return Traget(Value1,Value2)

Result = Calculate(Traget=Addtion,Value1=10,Value2=15)
print("Addtion:",Result)


def Subtraction(A,B):
    return A-B

def Calculate(reduce,Value3,Value4):
    return reduce(Value3,Value4)

output = Calculate(reduce=Subtraction,Value3=50,Value4=30)
print(output)
