def lista():

    f=open('todo.txt','r')
    line=f.readlines()
    print(len(line))

array=[]


def archive():
    f=open('todo.txt','r')
    
    f.close()

def beolvas():
    f=open('todo.txt','r')
    for i in f:
        array.append(i)
    f.close()

def kiirat():
    for j in range(len(array)):
        print(j+1,". ",array[j],end="",sep="")
    

beolvas()
archive()
kiirat()




