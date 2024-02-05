print('Hello,stupid!')
print(type('Hello,stupid!'))
# Below are some examples of operations
print(12+2.0)
print(0.1+0.2-0.3)
print(8/4)
print(3+6/2)
print(20.5%2**3//4)
# This is a example for how to only show the first two digits of a number
print(15623//1000)
# This is a example for how to only show the last digit of a number
print(3238%323)
'''
I am going to
write some shits here
and nobody will
see it
'''
# The string must have ""'' quotation marks, otherwise might be recongnised as variables
print("box_size")
# How to assign more than one values in one row：use commas to seperate them
a,b,c=1,2,3
# Using input function to get what user typed in, then assign the info to the variable:name
"""
print("Please enter your name:")
name=input()
print(name+" is the best!🤓")
"""

'''
name=input("Who am I speaking with?")
print("Morning my dear darling "+name+"!😘")
scheduel1=input("Do u want some coffee?")
'''

a=1
a+=5
print(a)
print("what the fuck "*5)

# How to show the current character's hp percentage in gaming
hp=343
max_hp=2134
result=hp/max_hp*100
print("Current HP: "+str(int(result))+ "%")

'''
# How to build a simple calculator
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2
def calculator():
    print("Select type of operation: " )
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4):")
    num1=float(input("Enter first number"))
    num2=float(input("Enter second number"))

    if choice == "1":
        print(add(num1,num2))
    elif choice == "2":
        print(sub(num1,num2))
    elif choice == "3":
        print(multiply(num1,num2)) 
    elif choice == "4":
        print(divide(num1,num2))  

calculator()
'''

my_string="Hello, world!"
#length=len(my_string)
#print(length)
#index=my_string.find("w")
#print(index)
#c=my_string.count("l")
#print(c)
#new_string=my_string.replace("world","stupid")
#print(new_string)
is_in="H" in my_string
print(is_in)

a=6
result = a>6
print(result)
print(12==12.0)
print(12=="12")
print("a"=="A")
print("a">"A")

#Tell if the number is even
'''
number=input("Please enter an integer: ")
number=int(number)
if number%2==0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
print("END")
'''

'''
#based on the score to define the level of the test result
score=input("Please enter your score (0-100): ")
score=int(score)
#要先用一个if语句判断分数是否有效，即筛选掉那些大于100满分的和负数的，有效才继续判断等级
if 0<=score<=100:
#注意这里要用==，表示判断两个值的大小关系，==是关系运算符
 if score==100:
    print("S")
#此处也可写成 90<=score<100
 elif score>=90 and score<100:
    print("A")
 elif 80<=score<90:
    print("B")
 elif 70<=score<80:
    print("C")
 elif 60<=score<70:
    print("D")
 else:
    print("E")
else:
    print("The score is invalid.")
'''

#Implement a rock-paper-scissors guessing game 1-剪刀 2-石头 3-布

#列表中如果既有字符串又有数值，则无法进行大小比较，也就无法获取最大或最小的元素，即只能同类型进行比较
a=["stupid","23","45.6","True","emoji"]
#print(max(a))
a.sort()

#换行转义字符的使用
String142="*^ ^*\n  ○"
print(String142)

#格式化数字
pi=-3.1415926
result1=f"圆周率{pi:*^-20.2f}是一个无限不循环小数"
print(result1)

pii=-3.1415926
result2=f"圆周率{pi:*>20.2f}是一个无限不循环小数"
print(result2)

my_list =[12,"A", 3.5, 6, "Hi", True]
my_list[5]=False
print(my_list)

my_list=[12,"A", 3.5, 6, "Hi", True]
print(my_list[3])

my_list=[12,"A", 3.5, 6, "Hi", True]
print(my_list.index(12))

my_list=[12,"A", 3.5, 6, "Hi", True,"A",12]
print(my_list.count(12))

# 调换列表中元素位置
a=["周一","周二","周三","周四","周六","周五","周天"]
a[4],a[5]=a[5],a[4]
print(a)

#将一个字符串分割后形成一个列表
a="周一,周二,周三,周四,周五,周六,周天"
alist=a.split(",")
print(alist)

alist=['周一', '周二', '周三', '周四', '周五', '周六', '周天']
astr="".join(alist)
print(astr)

alist=['周一', '周二', '周三', '周四', '周五', '周六', '周天']
astr="¥".join(alist)
print(astr)

my_list=[4,2,5,6,8]
#my_list.append("5")
#my_list.insert(1,"Hi")
my_list.extend([100,200,300])
print(my_list)

my_list=[4,2,5,6,8]
# 移除列表的最后一个元素
print(my_list.pop())

my_list=[4,2,5,6,8]
my_list.clear()
print(my_list)

t=(1,2,3)
a,b,c=t
print(a,b,c)

# 列表嵌套
my_list=[
         [13,3.5],
         ["A","Hi"],
         [True,False]
]
l=my_list[1] 
print(l[0])
print(my_list[1][0])

# Creat a code to show how many days of a exact month

'''
ldays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
m=input("Please enter the month you want to search:")
month=int(m)
print(f"{m} month has {ldays[month]} days.")
'''

l=list(range(1,101,2))
print(l)

L1=list(range(100))
for item in L1:
    item +=2
    print(item*2)

# while loop
count = 0
while (count < 9):
   print ("The count is:"), count
   count = count + 1
 
print ("Good bye!")

# continue and break 
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     #非双数时跳过
        continue
    print (i)         
 
i = 1
while 1:           
    print (i)         
    i += 1
    if i > 10:     
        break
    
# infinite loop
'''var = 1
while var == 1 :     # always true
   num = input("Enter a number  :")
   print ("You entered:" + num)
 
print ("Good bye!")
'''
# use control+c to stop it


count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")


 
for letter in 'Python':     
   print("当前字母: %s" % letter)
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        
   print ('当前水果: %s'% fruit)
 
print ("Delicious!")


for num in range(10,20):  
   for i in range(2,num): 
      if num%i == 0:      
         j=num/i          
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)
      
    

def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total
 
# 调用sum函数
total = sum( 10, 20 )

 
total = 0 # 这是一个全局变量
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2 # total在这里是局部变量.
   print ("函数内是局部变量 : ", total)
   return total
 
#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)

def vacation_decision():
    answer = input("Does Joyce deserve a vacation? (Please enter 'Yes' or 'No'): ")
    
    if answer.lower() == 'yes':
        return "You are a good guy🥰"
    elif answer.lower() == 'no':
        return "You made Joyce sad😭"
    else:
        return "Invalid input. Please enter 'Yes' or 'No'."

result = vacation_decision()
print(result)



    






