# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class People:
    def __init__(self,fam,im,ot):
        self.fam=fam
        self.im=im
        self.ot=ot

    def form(self):
        return self.fam+' '+self.im[0]+'.'+self.ot[0]+'.'

    def __str__(self):
        return self.fam + ' ' + self.im + ' ' + self.ot

class Student(People):
    def __init__(self, fam,im,ot, mum, pap, clss):
        People.__init__(self,fam,im,ot)
        self.mum=mum
        self.pap=pap
        self.clss=clss

    def form(self):
        return self.fam + ' ' + self.im[0] + '.' + self.ot[0] + '.'

class Teacher:
    def __init__(self,fam,im,ot, science, *clsst):
        People.__init__(self, fam, im, ot)
        self.science=science
        self.clsst=(list)(*clsst)

    def form(self):
        return self.fam + ' ' + self.im[0] + '.' + self.ot[0] + '.'


school = [Student('Иванов', 'Василий', 'Андреевич', People('Иванова', 'Мария', 'Игоревна'), People('Иванов', 'Андрей', 'Сергеевич'), '5А'), \
        Student('Кочетков', 'Василий', 'Андреевич', People('Кочеткова', 'Мария', 'Игоревна'), People('Кочетков', 'Андрей', 'Сергеевич'), '5А'), \
        Student('Петров', 'Василий', 'Андреевич', People('Петрова', 'Мария', 'Игоревна'), People('Петров', 'Андрей', 'Сергеевич'), '8А'), \
          Teacher('Левитан', 'Евгений', 'Артемович', 'Русский язык', ['5А', '6Б', '7В']), \
          Teacher('Терминасова', 'Анна', 'Анатольевна', 'Английский язык', ['5А','8A', '6Б', '7В']), \
          Teacher('Звагельский', 'Ростислав', 'Викторович', 'Алгебра', ['5А','8A', '9Б', '7В']), \
          Teacher('Звагельский', 'Ростислав', 'Викторович', 'Геометрия', ['5А','8A', '9Б', '7В']),\
          ]

def school_classes(school):
    spisok_classov=[]
    for rect in school:
        if rect.__class__.__name__=='Student':
            spisok_classov.append(rect.clss)
        elif rect.__class__.__name__=='Teacher':
            spisok_classov+=rect.clsst
    spisok_classov =list(set(spisok_classov))
    spisok_classov.sort()
    return spisok_classov

print('Список классов школы:', school_classes(school))


acl = input('Список учеников какого класса вы хотите получить? ')

def spisok_uch_cl(school,acl):
    spisok_stud=[]
    if acl.upper() in school_classes(school):
        for rect in school:
            if rect.__class__.__name__ == 'Student' and rect.clss==acl.upper():
                spisok_stud.append(rect.form())
        if spisok_stud:
            return spisok_stud
        else: return 'Класс пуст'
    else: return 'Такого класса нет'


print(spisok_uch_cl(school,acl))


# acl=input('Введите Фамилию И.О. ученика ').title()
def spisok_sci(school,acl):
    spisok_s=[]
    cl=''
    for rect in school:
        if rect.__class__.__name__ == 'Student' and rect.form()==acl:
            cl=rect.clss
    if cl!='':
        for rect in school:
            if rect.__class__.__name__ == 'Teacher' and cl in rect.clsst:
                spisok_s.append(rect.science)
        return spisok_s
    else:
        return 'Такого ученика нет'

stud='Иванов В.А.'
print(stud)
print(spisok_sci(school,stud))

def fio_parents(school,stud):
    for rect in school:
        if rect.__class__.__name__ == 'Student' and rect.form()==stud:
            return str(rect.mum)+', '+str(rect.pap)
    return 'Такого ученика нет'


print(fio_parents(school,stud))

def spisok_teach(school,acl):
    spisok=[]
    if acl.upper() in school_classes(school):
        for rect in school:
            if rect.__class__.__name__ == 'Teacher' and acl.upper() in rect.clsst:
                spisok.append(rect.form())
        return spisok
    else:
        return 'Такого класса нет'

print(spisok_teach(school,acl))