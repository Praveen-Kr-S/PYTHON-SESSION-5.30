import tkinter as tk

def sp(pg):
    pg.tkraise()

main = tk.Tk()
main.geometry("1366x768")
conatiner = tk.Frame(main,background="gray")
conatiner.place(width=1366,height=768,x=0,y=0)
rg = tk.Frame(conatiner,background="black")
lg = tk.Frame(conatiner,background="gray")
dg = tk.Frame(conatiner,background="green")

for page in (rg,lg,dg):
    page.place(width=1366,height=768,x=0,y=0)

#   Register Page
tk.Label(rg,bg="black",fg="orange",text="Register Form",font=("Arial bold",35)).place(x=550,y=100)
# user name
tk.Label(rg,bg="black",fg="light blue",text="User Name :",font=("Arial bold",20)).place(x=450,y=200)
rg_name = tk.Entry(rg,bg="black",fg="light blue",font=("Arial bold",20))
rg_name.place(x=630,y=200)
#user phone
tk.Label(rg,bg="black",fg="light blue",text="User Phone :",font=("Arial bold",20)).place(x=450,y=270)
rg_phone = tk.Entry(rg,bg="black",fg="light blue",font=("Arial bold",20))
rg_phone.place(x=630,y=270)
#user email
tk.Label(rg,bg="black",fg="light blue",text="User Email :",font=("Arial bold",20)).place(x=450,y=340)
rg_email = tk.Entry(rg,bg="black",fg="light blue",font=("Arial bold",20))
rg_email.place(x=630,y=340)
#user Password
tk.Label(rg,bg="black",fg="light blue",text="Password :",font=("Arial bold",20)).place(x=450,y=410)
rg_pass = tk.Entry(rg,bg="black",fg="light blue",font=("Arial bold",20),show="*")
rg_pass.place(x=630,y=410)
tk.Button(rg,bg="black",fg="light blue",font=("Arial bold",20),text="Login Form",command=lambda:sp(lg)).place(x=500,y=510)


#   Login Page
tk.Label(lg,bg="gray",fg="orange",text="Login Form",font=("Arial bold",35)).place(x=550,y=100)
#login email
tk.Label(lg,bg="black",fg="light blue",text="User Email :",font=("Arial bold",20)).place(x=450,y=340)
lg_email = tk.Entry(lg,bg="black",fg="light blue",font=("Arial bold",20))
lg_email.place(x=630,y=340)
#login Password
tk.Label(lg,bg="black",fg="light blue",text="Password :",font=("Arial bold",20)).place(x=450,y=410)
lg_pass = tk.Entry(lg,bg="black",fg="light blue",font=("Arial bold",20),show="*")
lg_pass.place(x=630,y=410)
tk.Button(lg,bg="black",fg="light blue",font=("Arial bold",20),text="Register Form",command=lambda:sp(rg)).place(x=500,y=510)
tk.Button(lg,bg="black",fg="light blue",font=("Arial bold",20),text="login",command=lambda:sp(dg)).place(x=730,y=510)


rg.tkraise()
main.mainloop()
