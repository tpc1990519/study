#使用global定义全局变量
def func():
    global x
    print('x is %d' % x)
    x=2
    print('changed local x to %d' % x)
    
x = 50
func()
print('value of x is %d' % x)
