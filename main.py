import pickle as pk
import tkinter as tk
from tkinter import ttk

# files and keys
key = './your_key.dat'
data_file = './your_data.dat'
logo = './logo_design.ico'

dict1 = {}
with open(data_file,'rb') as newfile:
    content = pk.load(newfile)
    newfile.close()

with open(key,"rb") as key_file:
    main_key = pk.load(key_file)
    key_file.close()

key_contents = sorted(content.keys())

def readAllContent():
    '''Function prints all data in the file to the terminal'''
    with open(data_file,'rb') as newfile:
        contents = pk.load(newfile)
        print(contents)
        newfile.close()

def display():
    '''Function that prints the database onto the terminal'''
    site = input('Enter Website: ').lower()
    creds = []
    for key in content:
        if key == site:
            creds = content[key]
    if len(creds) != 0:    
        username = creds[0]
        password = creds[1]
        print(f'Username: {username}\nPassword: {password}')
    else:
        print('Not Found!')

def GUI_phase1():
    '''Function that initializes the first phase of the app'''

    def p1_check():
        '''Function that checks the Key entered'''
        key = key_entry.get()
        if key == main_key or key == " ":
            GUI_phase2()
        else:
            window.destroy()

    label1 = tk.Label(window, text="𝙴𝙽𝚃𝙴𝚁 𝙺𝙴𝚈 :", font = ("", 25),bg="#222831",fg="#EEEEEE")
    label1.pack(pady=(80,10))
    key_entry = tk.Entry(window, font = ("Helvetica", 30), show = "ᵒ",bg="#00ADB5",fg="#EEEEEE")
    key_entry.pack()
    key_entry.bind("<Return>", lambda event : p1_check())

def GUI_phase2():
    '''Function that initializes the second phase of the app'''
    for widget in window.winfo_children():
        widget.destroy()
    label1 = tk.Label(window, text= "𝚆𝚎𝚕𝚌𝚘𝚖𝚎", font = ("", 30),bg="#222831",fg="#EEEEEE")
    label1.grid(row=0,column=0,columnspan=3,pady=(40,20))
    button1 = tk.Button(window,text="𝐒𝐇𝐎𝐖 𝐀𝐋𝐋",command=ShowAll, font = ("", 25),bg="#00ADB5")
    button1.grid(row=1,column=0,padx=(30,15),pady=(40,0))
    button2 = tk.Button(window,text="𝐑𝐄𝐓𝐑𝐈𝐄𝐕𝐄",command=Retrieve, font = ("", 25),bg="#00ADB5")
    button2.grid(row=1,column=1,padx=15,pady=(40,0))
    button3 = tk.Button(window,text="𝐀𝐃𝐃 𝐍𝐄𝐖",command=AddNew, font = ("", 25),bg="#00ADB5")
    button3.grid(row=1,column=2,padx=15,pady=(40,0))

def ShowAll():
    '''Function which displpays all data on the gui'''
    def _on_mouse_wheel(event):
        my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    for widget in window.winfo_children():
        widget.destroy()
    all_content = f""
    for site in key_contents:
        username = content[site][0]
        password = content[site][1]
        all_content = all_content + f'\n{site.title()}:\nUsername: {username}\nPassword: {password}\n' 
    
    main_frame = tk.Frame(window,bg="#222831")
    main_frame.pack(fill=tk.BOTH, expand=1)
    my_canvas = tk.Canvas(main_frame,bg="#222831")
    my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    second_frame = tk.Frame(my_canvas,bg="#222831")
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
    label1 = tk.Label(second_frame,text=all_content,font=("Consolas"),bg="#222831",fg="#EEEEEE")
    label1.pack(padx=80)

def Retrieve():
    '''Function that gets data for one particular site on the gui'''

    def get():
        '''Function that gets the entered data to retrieve from database'''
        site_req = site_entry.get()
        for site in content:
            if site == site_req.lower():
                tk.Label(window, text=f"USERNAME : {content[site][0]}", font = ("Open Sans", 20),bg="#222831",fg="#EEEEEE").pack(pady=(20,10))
                tk.Label(window, text=f"PASSWORD : {content[site][1]}", font = ("Open Sans", 20),bg="#222831",fg="#EEEEEE").pack()
    
    for widget in window.winfo_children():
        widget.destroy()

    label1 = tk.Label(window, text= "WEBSITE :", font = ("Open Sans", 20),bg="#222831",fg="#EEEEEE")
    label1.pack(pady=(50,10))
    site_entry = tk.Entry(window, font=("Consolas", 20),bg="#00ADB5",fg="#EEEEEE")
    site_entry.pack(pady=(0,10))
    site_entry.bind("<Return>", lambda event:get())

def AddNew():
    '''Function which allows the user to enter new data into the app database'''

    def writeContent():
        '''Function that writes the entered data into the app database'''
        WebSite = web_entry.get().lower()
        UserName = user_entry.get()
        PassWord = pass_entry.get()
        if WebSite != "" and UserName != "" and PassWord != "":
            dict1[WebSite] = [UserName,PassWord]
            content.update(dict1)
            with open(data_file,'wb') as newfile:
                pk.dump(content,newfile)
                newfile.close()
        window.destroy()

    for widget in window.winfo_children():
        widget.destroy()

    web_label = tk.Label(window, text="   WEBSITE :     " ,font = ("Open Sans", 20),bg="#222831",fg="#EEEEEE")
    web_label.grid(row=0,column=0,padx=(45,0),pady=(60,15))
    user_label = tk.Label(window, text="USERNAME  :" ,font = ("Open Sans", 20),bg="#222831",fg="#EEEEEE")
    user_label.grid(row=1,column=0,pady=(0,15))
    pass_label = tk.Label(window, text="PASSWORD :" ,font = ("Open Sans", 20),bg="#222831",fg="#EEEEEE")
    pass_label.grid(row=2,column=0,pady=(0,15))
    web_entry = tk.Entry(window,font = ("Consolas", 20),bg="#00ADB5",fg="#EEEEEE")
    web_entry.grid(row=0,column=1,pady=(60,15))
    user_entry = tk.Entry(window,font = ("Consolas", 20),bg="#00ADB5",fg="#EEEEEE")
    user_entry.grid(row=1,column=1,pady=(0,15))
    pass_entry = tk.Entry(window,font = ("Consolas", 20),bg="#00ADB5",fg="#EEEEEE")
    pass_entry.grid(row=2,column=1,pady=(0,15))
    input_btn = tk.Button(window, text="INPUT",font=("Consolas", 18, "bold"), command = writeContent,bg="#00ADB5")
    input_btn.grid(row=3,column=1,pady=(20,0))

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry('600x300+450+240')
    window.title('PASSWORD MANAGER')
    window.iconbitmap(logo)
    window.configure(bg="#222831")
    window.bind("<Escape>", lambda event: window.destroy())
    GUI_phase1()
    window.resizable(False, False)
    window.mainloop()
    
