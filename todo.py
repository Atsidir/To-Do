def lista():

    f=open('todo.txt','r')

    for i in f:
        print(i,end="")    
    f.close()

lista()

