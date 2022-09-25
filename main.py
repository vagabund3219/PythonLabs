import shutil
import os

def firstTask():
    fileName = input("Input file name")
    with open(f'C:\\Users\lqmn\Desktop\{fileName}.txt', 'r') as someFile:
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
            print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
            print(f'Файлы: {", ".join(file for file in catalog[2])}')
            print('-' * 40)
    print_docs("C:/Users/lqmn//Desktop/dz")

def sixthTask():
    def longest_words(file):
        with open(f'C:\\Users\lqmn\Desktop\{file}.txt', encoding='utf-8') as someFile:
            txt = someFile.read().split()
            max1 = len(max(txt, key=len))
            max_list = list(i for i in txt if len(i) == max1)
            print(max_list)
    longest_words(input("Input file name"))

class Soda:
    def __init__(self, add = (input("Input the additive"))):
        self.Additive = add
    def show_my_drink(self):
        if self.Additive != 0:
            print("Газировка: ", self.name, "Добавка", self.Additive )
        else:
            print("Обычная газировка: ")

def seventhTask():
    A = Soda(input("Input name of soda"))
    B = Soda(input("Input name of soda"))
    A.show_my_drink()
    B.show_my_drink()


if __name__ == '__main__':
    #firstTask()
    #secondTask()
    #thirdTask()
    #forthTask()
    #fifthTask()
    #sixthTask()
    seventhTask()

