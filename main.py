import shutil
import os

def firstTask():
    fileName = input("Input file name")
    with open(f'C:\\Users\lqmn\Desktop\{fileName}.txt',encoding='utf-8') as someFile:
        print(someFile.read())

def secondTask():
    fileName = input("Input file name")
    fileNameCopy = input("Input file name for copy")
    shutil.copyfile(f'C:\\Users\lqmn\Desktop\{fileName}.txt', f'C:\\Users\lqmn\Desktop\{fileNameCopy}.txt' )
    num = 1
    with open(f'C:\\Users\lqmn\Desktop\{fileNameCopy}.txt', encoding='utf-8') as someFile:
        txt = someFile.readlines()
        for i in txt:
            print(num , i)
            num+=1

def thirdTask():
    fileName = input("Input file name")
    with open(f'C:\\Users\lqmn\Desktop\{fileName}.txt', 'w+') as someFile:
        someFile.write(input("Input text in").upper())
    with open(f'C:\\Users\lqmn\Desktop\{fileName}.txt', 'r') as someFile:
            print(someFile.read())

def forthTask():
    def read_last(lines, file):
        if lines > 0:
            with open(f'C:\\Users\lqmn\Desktop\{file}.txt', encoding='utf-8') as someFile:
                txt = someFile.readlines()
                for i in range(-1, -lines-1, -1):
                    print(txt[i].strip())
    read_last(int(input("Count of rows")), input("File name"))

def fifthTask():
    def print_docs(directory):
        all_files = os.walk(directory)
        for catalog in all_files:
            print(f'Папка {catalog[0]} содержит:')
            print(f'Директории: {", ".join(catalog[1])}')
            print(f'Файлы: {", ".join(catalog[2])}')
            print('-' * 40)
    print_docs("C:/Users/lqmn/Desktop")

def sixthTask():
    def longest_words(file):
        with open(f'C:\\Users\lqmn\Desktop\{file}.txt', encoding='utf-8') as someFile:
            txt = someFile.read().split()
            max1 = len(max(txt, key=len))
            max_list = list(i for i in txt if len(i) == max1)
            print(max_list)
    longest_words(input("Input file name"))

class Soda:
    def __init__(self, additive=None):
        if isinstance(additive, str):
            self.additive = additive
        else:
            self.additive = None

    def show_my_drink(self):
        if self.additive:
            print("Газировка", self.additive)
        else:
            print("Обычная Газировка")

def  seventhTask():
    A = Soda("sugar")
    B = Soda()
    A.show_my_drink()
    B.show_my_drink()

class TriangleChecker:
    def __init__(self, kat1, kat2, gip):
        self.kat1 = kat1
        self.kat2 = kat2
        self.gip = gip

    def is_triangle(self):
        if (isinstance(self.kat1, str) or isinstance(self.kat2, str) or isinstance(self.gip, str)):
            print("Нужно вводить только числа!")
        elif (self.kat1 < 0 or self.kat2 < 0 or self.gip < 0):
            print("С отрицательными числами ничего не выйдет!")
        elif (self.kat1 > 0 and self.kat2 > 0 and self.gip > 0 and (self.kat1 + self.kat2) > self.gip):
            print("Ура, можно построить треугольник!")
        else:
            print("Жаль, но из этого треугольник не сделать")

def  eighthTask():
            B = TriangleChecker(1,"hhk", "kk")
            B.is_triangle()




def ninethTask(lst, text):
    arg = []
    for i in range(len(lst)):
        try:
            (int(lst[i]))
        except:
            try:
                float(lst[i])
            except:
                arg.append(lst[i])

    #arg = list(i for i in lst if isinstance(i, str))
    def foo(*args):
        for i in args:
            print(i.__dict__)
    MyClass = type(text, (object,), dict(foo = foo))
    Obj = MyClass()
    for i in range (len(arg)):
        setattr(Obj,f"{arg[i]}",i)
    Obj.foo()


class Ten:
    def __init__(self, *args):
        for i in range (len(args)):
            setattr(self,f"{i}",args[i])
    def display(self):
        for i, j in self.__dict__.items():
            print(i, "-", j)

def tenthTask(obj):
    newObj = copy.deepcopy(obj)
    for i in obj.__dict__:
        delattr(newObj, i)
    for i, j in obj.__dict__.items():
        try:
            int(j)
            setattr(newObj, i,j)
        except:
            continue
    print(type(newObj))
    newObj.display()






import copy
if __name__ == '__main__':
    x = int(input("Number of the task"))
    match x:
        case 1:
            firstTask()
        case 2:
            secondTask()
        case 3:
            thirdTask()
        case 4:
            forthTask()
        case 5:
            fifthTask()
        case 6:
            sixthTask()
        case 7:
            seventhTask()
        case 8:
            eighthTask()
        case 9:
            lst = []
            for i in range((int(input("Number of elem ")))):
                lst.append(input("Input "))
            text = input("Input name of class ")
            ninethTask(lst, text)
        case 10:
            obj = Ten(10, "str", 54)
            tenthTask(obj)












