l=[]
def create(l):
    name=input("Enter task name")
    l=l.append(name)
    print("Task created successfully")
    return l
def edit(l):
    for a in l:
        print(l.index(a)+1,a)
    n=int(input("Enter serial no you want to edit"))
    change=input("Enter name after editing")
    l[n-1]=change
    print("Editing done successfully")
    return l
def list(l):
    print("Following are the tasks you created")
    for a in l:
        print(l.index(a)+1,a)
def delete(l):
    for a in l:
        print(l.index(a)+1,"=",a)
        n=int(input("Enter serial no you want to delete"))
        l.pop(n-1)
        print("Task deleted succesfully")
        return l
b=True
while b:
    print("1=Create")
    print("2=Edit")
    print("3=List of task")
    print("4=Delete")
    print("5=Exit")
    ch=int(input("Enter your choice"))

    if ch==1:
        create(l)
    elif ch==2:
        edit(l)
    elif ch==3:
        list(l)
    elif ch==4:
        delete(l)
    elif ch==5:
        print("Thankyou")
        b=False
    else:
        print('Invalid choice')

