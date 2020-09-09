contact_list=[]
def display():
    print("S.No\tname\tphone.no\taddress")
    for i in range(len(contact_list)):
        for j in range(len(contact_list[i])):
            print(contact_list[i][j],end="\t")
        print()

def add():
    while(True):
        l=[]
        while(True):
            c=0
            m=input("Enter S.No: ")
            for i in range(len(contact_list)):
                if m == contact_list[i][0]:
                    c=1
                    break
            if(c==1):
                print("S.No already there, try another")
            else:
                l.append(m)
                break
        while(True):
            c=0
            m=input("Enter name: ")
            for i in range(len(contact_list)):
                if m == contact_list[i][1]:
                    c=1
                    break
            if(c==1):
                print("S.No already there, try another")
            else:
                l.append(m)
                break
        while(True):
            c=0
            m=input("Enter Address: ")
            for i in range(len(contact_list)):
                if m == contact_list[i][2]:
                    c=1
                    break
            if(c==1):
                print("S.No already there, try another")
            else:
                l.append(m)
                break
        while(True):
            c=0
            m=input("Enter Phone Number: ")
            for i in range(len(contact_list)):
                if m == contact_list[i][3]:
                    c=1
                    break
            if(c==1):
                print("S.No already there, try another")
            else:
                l.append(m)
                break
        contact_list.append(list(l))
        m=int(input("\nDO YOU WANT ADD ANYTHING(enter 1)"))
        if(m!=1):
            break
    display()

def edit():
    while(True):
        t=0
        k=input("enter name to edit")
        for i in range(len(contact_list)):
            for j in range(len(contact_list[i])):
                if k==contact_list[i][j] :
                    t=1
                    print("found")
                    print("1.change name")
                    print("2.change address")
                    print("3.change phone no")
                    h=int(input("enter choice"))
                    if h==1:
                        contact_list[i][h]=input("enter name")
                        break
                    elif h==2:
                        contact_list[i][h]=input("enter address")
                        break
                    elif h==3:
                        contact_list[i][h]=input("enter phoneno")
                        break
                    else:
                        print("no choice")
                        break
        if t==0:
            print("not found")
        m=int(input("\n DO YOU WANT TO EDIT ANYTHING(enter 1)"))
        if(m!=1):
            break
    display()

def search():
    while(True):
        t=0
        print("1.name")
        print("2.address")
        print("3.phone no")
        k=int(input("enter choice in which way you want to search"))
        if k==1:
            o=input("enter name")
        elif k==2:
            o=input("enter address")
        elif k==3:
            o=input("enter phone no")
        for i in range(len(contact_list)):
            for j in range(len(contact_list[i])):
                if o==contact_list[i][j] :
                    t=1
                    print("found")
                    break
        if t==0:
            print("not found")
        m=int(input("\n DO YOU WANT TO SEARCH ANYTHING(enter 1)"))
        if(m!=1):
            break
    display()
       
       
def delete():
    while(True):
        t=0
        k=input("enter name to delete")
        for i in range(len(contact_list)):
            for j in range(len(contact_list[i])):
                if k==contact_list[i][j] :
                    t=1
                    print("found")
                    del contact_list[i]
                    break

       
        if t==0:
            print("not found")
        m=int(input("\n DO YOU WANT TO DEL ANYTHING(enter 1)"))
        if(m!=1):
            break
    display()      
       
   
print("1.ADD")
print("2.EDIT")
print("3.SEARCH")
print("4.DELETE")
n=1
while(True):
    n=int(input("enter choice"))
    if n==1:
        add()
    elif n==2:
        edit()
    elif n==3:
        search()
    elif n==4:
        delete()
    else:
        print("no choice")
    d=int(input("\n 1 to continue"))
    if(d!=1):
        break
