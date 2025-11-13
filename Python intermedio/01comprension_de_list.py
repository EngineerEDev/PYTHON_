##list compreshensionsion
my_original_list = [1,2,3,4,5,6,7]
my_list= [i*2 for i in my_original_list]
print("lista oroginal:", my_original_list)
print("nueva lista:", my_list)

def fibo (n):
    a,b=0,1
    my_fibo_list=[]
    for _ in range (n):
        my_fibo_list.append(b)
        a,b=b,a+b
    return my_fibo_list
my_list= fibo(0)
print("secuencia de fibonacci:", my_list)


print(sorted("bairon"))