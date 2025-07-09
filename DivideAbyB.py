def divideAbyB(A,B):
    try:
        sum1=A/B
        return sum1
    except ZeroDivisionError:
        return "ZeroDivisionError"
A=int(input())
B=int(input())
print(divideAbyB(A,B))