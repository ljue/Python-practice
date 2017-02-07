# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определть методы позволяющие вычислить: Площадь, высоту и периметр фигуры

class triangle:
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def perimeter(self):
        return ((self.x2-self.x1)**2+(self.y2-self.y1)**2)**(1/2)+((self.x3-self.x2)**2+(self.y3-self.y2)**2)**(1/2)+ \
               ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** (1 / 2)

    def square(self):
        return (self.perimeter()/2*(self.perimeter()/2-((self.x2-self.x1)**2+(self.y2-self.y1)**2)**(1/2))*\
               (self.perimeter()/2-((self.x3-self.x2)**2+(self.y3-self.y2)**2)**(1/2))*\
               (self.perimeter()/2-((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** (1 / 2)))**(1/2)

    def height(self,x,y):
        if self.x3==x and self.y3==y:
            return 2*self.square()/(((self.x2-self.x1)**2+(self.y2-self.y1)**2)**(1/2))
        elif self.x2 == x and self.y2 == y:
            return 2 * self.square() / (((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** (1 / 2))
        elif self.x1 == x and self.y1 == y:
            return 2 * self.square() / (((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** (1 / 2))
        else:
            return 'Нет такой вершины в этом треугольнике'

tr1=triangle(0,0,0,3,4,0)
print('Площадь =', tr1.square())
print('Периметр =', tr1.perimeter())
print('Высота 1 =', tr1.height(0,0))
print('Высота 2 =', tr1.height(0,3))
print('Высота 3 =', tr1.height(4,0))
print('Выдуманная высота:', tr1.height(5,0))
print()
# Задача-2: Написать Класс Равнобочная трапеция, заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.


class trapeze:
    def __init__(self, x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
        self.x4=x4
        self.y4=y4

    def size(self):
        a=[]
        a.append(((self.x2-self.x1)**2+(self.y2-self.y1)**2)**(1/2))
        a.append(((self.x3-self.x2)**2+(self.y3-self.y2)**2)**(1/2))
        a.append(((self.x3-self.x4)**2+(self.y3-self.y4)**2)**(1/2))
        a.append(((self.x1-self.x4)**2+(self.y1-self.y4)**2)**(1/2))
        return a

    def perimeter(self):
        return sum(self.size())

    def square(self):
        return (self.size()[3]+self.size()[1])/2 * (self.size()[0]**2-(self.size()[3]-self.size()[1])**2/4)**(1/2)

    def revis(self): # хорошо бы проверку засунуть в кончтруктор, где присвоить значения в зависимости от последовательности
        if (self.y2 - self.y1) / (self.x2 - self.x1) == (self.y4 - self.y3) / (self.x4 - self.x3) and \
           (self.y3 - self.y2) / (self.x3 - self.x2) != (self.y4 - self.y1) / (self.x4 - self.x1) and \
            ((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2) ** (1 / 2) == \
             ((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2) ** (1 / 2) or \
              (self.y2 - self.y1) / (self.x2 - self.x1) != (self.y4 - self.y3) / (self.x4 - self.x3) and \
              (self.y2 - self.y3) / (self.x2 - self.x3) == (self.y4 - self.y1) / (self.x4 - self.x1) and \
               ((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** (1 / 2) == \
                ((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2) ** (1 / 2):
            return True
        else: return False

    def revisor(self):   # запуталась в проверках. может вообще необязательно и имелось в виду что дается четкая последовательность вершин? вряд ли.. =(
        if self.revis(self.x1,self.y1,self.x2,self.y2,self.x3,self.y3,self.x4,self.y4) or \
            self.revis(self.x1, self.y1, self.x3, self.y3, self.x4, self.y4, self.x2, self.y2) or \
            self.revis(self.x1, self.y1, self.x4, self.y4, self.x2, self.y2, self.x3, self.y3) or \
            self.revis(self.x1, self.y1, self.x3, self.y3, self.x2, self.y2, self.x4, self.y4):
            return True
        else:
            return False


trap=trapeze(0,0,1,1,3,1,4,0)
print('Равнобокая трапеция?', trap.revis())
print('Стороны =', trap.size())
print('Площадь =', trap.square())
print('Периметр =', trap.perimeter())