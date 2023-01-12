
def division(x, y):
    try:                        # try - except指令
        return x / y
    except ZeroDivisionError:
        print("除數為0發生")
    except TypeError:    
        print("使用字元運算異常")
    except SyntaxError:
        print("語法異常")

       
x1 = eval(input("a = "))
print(type(x1))


       
x2 = eval(input("b = "))
print(type(x2))

#if not type(x1) is float:
   #raise TypeError("字元錯誤")
   
   
#if not type(x2) is float:
  # raise TypeError("字元錯誤")
  
print(division(x1, x2))      
