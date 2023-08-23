class Foo:
    def __init__(self, x=None):
        self._x = x


    @property
    def x (self):
        return self._x or 0 
    
    #pra poder realizar o set no X temos que criar o SETTER

    @x.setter
    def x (self,value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0   



foo = Foo(10)
print(foo.x)
foo.x = 5 # adicionando + 5 ao valor de X
print(foo.x)
del foo.x
print(foo.x)




