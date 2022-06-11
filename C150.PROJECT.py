from tkinter import *
import random

root =  Tk()

root.title("COUNTRY AND CAPITALS")
root.geometry("400x400")

enter_name = Entry(root)
enter_name.place(relx=0.5,rely=0.2,anchor=CENTER)
enter_name1 = Entry(root)
enter_name.place(relx=0.5,rely=0.2,anchor=CENTER)

friends_list = Label(root)
random_number_label = Label(root)
lucky_family_member = Label(root)

Family_List = []

def add_members():
    family_name = enter_name.get()
    Family_List.append(family_name)
    friends_list["text"] = "YOUR FAMILY LIST : "+str(Family_List)
    
def random_number():
    length = len(Family_List)
    random_no = random.randint(0,length - 1)
    random_number_label["text"] = str(random_no)
    generate_random_number = Family_List[random_no]
    lucky_family_member["text"] = "YOUR LUCKY FAMILY MEMBER IS YOUR "+str(generate_random_number)
    
btn = Button(root,text="ADD FAMILY MEMBER",command=add_members)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

friends_list.place(relx=0.5,rely=0.5,anchor=CENTER)

btn1 = Button(root,text = "WHO IS YOUR LUCKY FAMILY MEMBER ?",command = random_number)
btn1.place(relx=0.5,rely=0.6,anchor=CENTER)

random_number_label.place(relx=0.5,rely=0.7,anchor=CENTER)
lucky_family_member.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()