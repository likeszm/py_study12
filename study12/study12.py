#学习记录12: 函数
"""
1.函数内部想操作全局变量需要global关键字声明
2.传入参数的个数可变，通过列表（准确说是数组指针）来实现
3.关键字可变参数: 通过双星号接收并存储为字典
"""

#1.局部变量和全局变量
"""
Var_1 = 11
Var_2 = 22

def fun_change_var():
    global Var_2
    Var_1 = 0
    Var_2 = 0
    print("函数内部:")
    print(f"var1 = {Var_1}, var2 = {Var_2}")

print("运行函数前:")
print(f"var1 = {Var_1}, var2 = {Var_2}")
fun_change_var()
print("运行函数后:")
print(f"var1 = {Var_1}, var2 = {Var_2}")
"""

#2.函数传入可变个数的参数（类似 C的数组指针）
"""
studentInfo = {
    '张飞' :  18,
    '赵云' :  17,
    '许褚' :  16,
    '典韦' :  18,
    '关羽' :  19,
}

def fun_output(*list) :
    for name in list :
        print(f"name: {name} age: {studentInfo[name]}")

fun_output("张飞")
fun_output("张飞","关羽")

onebatch = ['张飞', '典韦', '关羽']
fun_output(*onebatch)
"""

#3.关键字可变参数
"""
def test_fun( **dict ) :
    print(type(dict))
    for key, value in dict.items() :
        print(f"key= {key}, value= {value}")

test_fun(A = '0', B = '1', C = '2')
"""


