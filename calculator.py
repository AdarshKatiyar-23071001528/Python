x=int(input())
y=int(input())
op=input()
match op :
    case "+": print(x,"+",y,"=",x+y)
    case "-": print(x-y)
    case "*": print(x*y)
    case "/": print(x/y)
    case _  : print("Not valid")