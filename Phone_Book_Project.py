while(1):
    print("Phone Book App")
    print(">Enter 1 to Add new Contact")
    print(">Enter 2 to Delete a Contact")
    print(">Enter 3 to view all Contacts")
    print(">Enter 4 to edit Contact")
    print(">Enter 5 to close app")

    inp=int(input("Choose From 1 to 5:"))

    if inp==1:
        f=open('data.txt','a')
        name=input("Enter name:")
        pno=input("Enter Phone number")
        f.write(name+","+pno+"\n")
        f.close()

    elif inp==2:
        pno=input("Enter Phone Number to Delete:")
        
        f=open('data.txt','r')
        lines=f.readlines()
        f.close()

        f=open('data.txt','w')
        found=False
        for line in lines:
            if pno not in line:
                f.write(line)
            else:
                found=True
        f.close()

        if found:
            print("Deleted")
        else:
            print("not found")

    elif inp==3:
        f=open('data.txt','r')
        record=f.read()
        print("::All Contacts with names::")
        print(record)
        f.close()

    elif inp==4:
        pno=input("Enter Phone number you want to edit:")
        f=open('data.txt','r')
        lines=f.readlines()
        f.close()

        f=open('data.txt','w')
        found=False
        for line in lines:
            if pno in line:
                name=input("Enter New Name:")
                pno1=input("Enter New Number:")
                f.write(name+","+pno1+"\n")
                found=True
            else:
                f.write(line)
        f.close()

        if found:
            print("Edited Sucessfully")
        else:
            print("Not found")


    elif inp==5:
        print("::Closing the app::")
        break

    else:
        print("wrong input, Enter again")