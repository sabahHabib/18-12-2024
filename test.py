#list comprehension
a=[1,3,4,5,6]
res=[i*2 for i in a]
print(res)

result=[val for val in a if val % 2==0]
print (result)

a=[i for i in range(10)]
print(a)

coordinates=[(x,y) for x in range(3) for y in range(5)]
print(coordinates)
#lambda function
square = lambda x:x**2
print(square(5))


multiply=lambda x,y:x*y
print(multiply(2,3))

def my_function(n):
    return lambda x:x*n
doubler=my_function(5)
print(doubler(2))