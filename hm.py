
#6
'''with open(r'D:\hothaifa\file3.txt','w+')as file:
    while True:

        x=input('please enter input')
        if x=='exit':
            break
        file.write(f'{x}\n')
    file.seek(0)
    print(file.readlines())'''

#7
'''def sumFile(path):
    with open(path,'r+') as fileHandler:
        listOfnumers=fileHandler.readlines() #['5\n' ,'98\n']
        sum=0
        for ta in listOfnumers:
            sum+=int(ta)
        fileHandler.write(f'\n\n the sum is : {sum}s')


p=r'D:\hothaifa\file3.txt'
sumFile(p)'''


#8
#readlines ['line1 \n','line\n']
#readline 'line1\n'
#read 'line\nline2\n'



'''def IsWordInFile(path,word):
    with open(path) as fileHandler:
        if word in fileHandler.read():
            return True
        return False

print(IsWordInFile(r'D:\hothaifa\file3.txt','hoot'))'''


#9


'''def copyFile(path1,path2):
    with open(path1) as file1:
        with open(path2,'w') as file2:
            for line in file1:
                file2.write(f'{line[::-1]} \n')'''



try:
    x=int(input())
    z=x/0
except Exception as e:
    print(int)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

for i in range(10):
    print(i)









