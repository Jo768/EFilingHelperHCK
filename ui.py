import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tk_functions import CreateToolTip
import tkinterDnD
from functions import *

colours=["#2A2F32","#0D8ABF","#02C39A"]

window=tkinterDnD.Tk()
window.geometry("600x600")
window.title("E-FILING HELPER")
window.configure(bg=colours[0])
window.resizable(height=0, width=0)
window.iconbitmap("assets/app_icon.ico")

icons=[PhotoImage(file='assets/settings.png'),PhotoImage(file='assets/help.png'),PhotoImage(file='assets/csv.png'),PhotoImage(file='assets/excel.png'),PhotoImage(file='assets/mail.png'),PhotoImage(file='assets/DnD.png'),PhotoImage(file='assets/next.png'),PhotoImage(file='assets/retry.png'),PhotoImage(file='assets/dbs.png')]

def button_pressed(id):
    if id == 0: # mail button  
        UI_destroy()
        mail_ui()
    elif id == 1: # help button
        UI_destroy()
        help_ui()
    elif id == 2: # settings button
        UI_destroy()
        settings_ui()
    elif id == 3: # next button
        try:
            UI_destroy()
        except:
            choose_path_label.place(x=200, y=350)
            window.after(3000, choose_path_label.place_forget)
    elif id == 4: # choose file button
        window.filename = filedialog.askopenfilename(initialdir="Documents", title="Select CSV file", filetypes=[("csv files","*.csv")])
        listb.insert("end", window.filename)
    elif id == 5: # clear button
        selection = listb.curselection()
        try:
            listb.delete(selection)
        except:
            pass
    elif id == 6: # clear all button
        list_size=listb.size()
        listb.delete(0, list_size)

def dnd_listbox(event):
    listb.insert("end", event.data)

def UI_destroy():
    mail_button.place_forget()
    help_button.place_forget()
    settings_button.place_forget()
    next_button.place_forget()
    choose_file_button.place_forget()
    clear_button.place_forget()
    clear_all_button.place_forget()
    listb.place_forget()
    DnD_icon.place_forget()
    DnD_label.place_forget()

def UI_build():
    mail_button.place(x=480, y=10)
    help_button.place(x=5, y=545)
    settings_button.place(x=10, y=10)
    next_button.place(x=500, y=505)
    choose_file_button.place(x=165, y=450)
    clear_button.place(x=280, y=450)
    clear_all_button.place(x=350, y=450)
    listb.place(x=50, y=90)
    DnD_icon.place(x=252, y=210)
    DnD_label.place(x=250, y=300)

def callback():
    # if messagebox.askokcancel("Quit", "Quit the software?"):
    window.destroy()
    raise SystemExit

listb=tk.Listbox(window, selectmode=tk.SINGLE, bg=colours[0], fg=colours[2], font=("Roboto" , 10, 'bold'), height=23, width=70, borderwidth=5)

mail_button=tk.Button(window,command=lambda: button_pressed(0), image=icons[4], borderwidth =0, bg=colours[0], activebackground=colours[2], height=50, width=50)
help_button=tk.Button(window,command=lambda: button_pressed(1), image=icons[1], borderwidth =0, bg=colours[0], activebackground=colours[2], height=48, width=48)
settings_button=tk.Button(window,command=lambda: button_pressed(2),image=icons[0], borderwidth = 0, bg=colours[0], activebackground=colours[2], height=64, width=64)
next_button=tk.Button(window,command=lambda: button_pressed(3), image=icons[6], borderwidth =0 , bg=colours[0], activebackground=colours[2], height=48, width=48)
choose_file_button=tk.Button(window,command=lambda: button_pressed(4), text="CHOOSE FILE",font=("Roboto" , 10, 'bold') , bg=colours[1], activebackground=colours[2])
clear_button=tk.Button(window,command=lambda: button_pressed(5), text="CLEAR",font=("Roboto" , 10, 'bold') , bg=colours[1], activebackground=colours[2])
clear_all_button=tk.Button(window,command=lambda: button_pressed(6), text="CLEAR ALL",font=("Roboto" , 10, 'bold') , bg=colours[1], activebackground=colours[2])

DnD_icon=tk.Label(window, image=icons[5], bg=colours[0])
DnD_label=tk.Label(window, text="DROP THE WORD FILE",font=("Roboto" , 8, 'bold'), bg=colours[0], fg=colours[1])
choose_path_label=tk.Label(window, text="PLEASE SELECT A FILE!",font=("Roboto" , 12, 'bold'), bg=colours[0], fg=colours[1])



# fix code!!!

DnD_icon.register_drop_target("*")
DnD_icon.bind("<<Drop>>", dnd_listbox)

DnD_icon.register_drag_source("*")
DnD_icon.bind("<<DragInitCmd>>", dnd_listbox)

listb.register_drop_target("*")
listb.bind("<<Drop>>", dnd_listbox)

listb.register_drag_source("*")
listb.bind("<<DragInitCmd>>", dnd_listbox)

# DnD_icon.register_drag_source("*")
# listb.register_drag_source("*")
# DnD_icon.bind("<<Drop>>", dnd_listbox)
# listb.bind("<<Drop>>", dnd_listbox)

CreateToolTip(mail_button, text="Mail report")
CreateToolTip(help_button, text="Help")
CreateToolTip(settings_button, text="Settings")
CreateToolTip(next_button, text="Next")
CreateToolTip(choose_file_button, text="Choose file")
CreateToolTip(clear_button, text="Clear")
CreateToolTip(clear_all_button, text="Clear All")

window.protocol("WM_DELETE_WINDOW", callback)

def help_ui():
    def help_destroy():
        back_button.place_forget()
        
    def back():
        help_destroy()
        UI_build()

    back_button=tk.Button(window,command= back, text="Back", font=("Roboto" , 13, 'bold') , bg=colours[1], activebackground=colours[2])
    back_button.place(x="14",y="14")

    CreateToolTip(back_button, text="Back to Main Menu")

def settings_ui():

    def settings_destroy():
        path_label.place_forget()
        path_button.place_forget()
        mail_creds_label.place_forget()
        mail_creds_button.place_forget()
        back_button.place_forget()
        try:
            id_label.place_forget()
            id_input.place_forget()
            pass_label.place_forget()
            pass_input.place_forget()
            enter_button.place_forget()
        except:
            pass

    def settings_build():
        path_label.place(x=160, y=60)
        path_button.place(x=250, y=130)
        mail_creds_label.place(x=150, y=200)
        mail_creds_button.place(x=250, y=250)
        back_button.place(x=15, y=15) 
        window.after(500, path_label.config(text="EXPORT PATH IS: \n"+read_from_bin(0)))

    def choose_path():
        window.filename = filedialog.askdirectory(initialdir="Documents", title="Select Export Path")
        path=window.filename
        path_label.config(text="EXPORT PATH IS: \n"+path)
        write_to_bin(1,path, None, None)

    def mail_creds_input():
        
        def enter():
            mail_id=id_input.get()
            password=pass_input.get()
            id_input.delete(0, 'end')
            pass_input.delete(0, 'end')
            write_to_bin(0,None,mail_id, password)
            id_label.place_forget()
            id_input.place_forget()
            pass_label.place_forget()
            pass_input.place_forget()
            enter_button.place_forget()
            mail_creds_button.place(x=230, y=170)
        
        mail_creds_button.place_forget()
        id_label.place(x=140, y=240)
        id_input.place(x=240, y=240)
        pass_label.place(x=100, y=280)
        pass_input.place(x=240, y=280)
        enter_button.place(x=270, y=320)
        enter_button.config(command=enter)

    def back():
        settings_destroy()
        UI_build()

    path_label=tk.Label(window, text="EXPORT PATH IS: \n",font=("Roboto" , 14, 'bold'), bg=colours[0], fg=colours[2])
    path_button=tk.Button(window,command=choose_path, text="CHOOSE PATH",font=("Roboto" , 10, 'bold') , bg=colours[1], activebackground=colours[2])
    mail_creds_label=tk.Label(window, text="SAVE EMAIL CREDENTIALS",font=("Roboto" , 14, 'bold'), bg=colours[0], fg=colours[2])
    mail_creds_button=tk.Button(window,command=mail_creds_input, text="SAVE CREDS",font=("Roboto" , 10, 'bold') , bg=colours[1], activebackground=colours[2])
    id_label=tk.Label(window, text="MAIL ID: ",font=("Roboto" , 12, 'bold'), bg=colours[0], fg=colours[1])
    id_input=tk.Entry(window, font=("Roboto" , 12, 'bold'), width=24)
    pass_input=tk.Entry(window,show="*", font=("Roboto" , 12, 'bold'), width=24)
    pass_label=tk.Label(window, text="PASSWORD: ",font=("Roboto" , 12, 'bold'), bg=colours[0], fg=colours[1])
    enter_button=tk.Button(window, text="SAVE",font=("Roboto" , 10, 'bold') , bg=colours[1], activebackground=colours[2])
    back_button=tk.Button(window,command= back, text="Back",font=("Roboto" , 11, 'bold') , bg=colours[1], activebackground=colours[2])

    path_label.place(x=160, y=60)
    path_button.place(x=250, y=130)
    mail_creds_label.place(x=150, y=200)
    mail_creds_button.place(x=250, y=250)
    back_button.place(x=15, y=15) 
    
    CreateToolTip(back_button, text="Back to Main Menu")
    window.after(500, path_label.config(text="EXPORT PATH IS: \n"+read_from_bin(0)))

def mail_ui():

    cred_type=""

    def mail_destroy():
        use_tmp_creds_button.place_forget()
        use_saved_creds_button.place_forget()
        back_button.place_forget()
        select_table_label.place_forget()
        select_table.place_forget()
        mail_button.place_forget()
        try:
            host_label.place_forget()
            host_input.place_forget()
            user_label.place_forget()
            user_input.place_forget()
            pass_label.place_forget()
            pass_input.place_forget()
            dbs_label.place_forget()
            dbs_input.place_forget()
            connect_button.place_forget()
        except:
            pass

    def back():
        mail_destroy()
        UI_build()

    def mail():
        global cred_type
        table=tables.get()
        table=table_name(table)
        try:
            send_mail(cred_type,table)
        except:
            retry_label.config(text="Please check your\nEmail credentials")
            retry_label.place(x=180, y=530)

    def use_saved_creds():
        global cred_type
        host,user,password,database=read_dbs_creds("saved")
        try:
            dbs_connect(host, user, password, database)
            connection_label.config(text="CONNECTION ESTABLISHED")
            connection_label.place(x=180, y=530)
            mail_button.config(state="active")
            cred_type="saved"
            window.after(3000, connection_label.place_forget)
        except Exception as e:
            connection_label.config(text="SOMETHING WENT WRONG\nPLEASE TRY AGAIN")
            connection_label.place(x=180, y=530)
            window.after(3000, connection_label.place_forget)

        return cred_type

    def use_tmp_creds():
        use_tmp_creds_button.place_forget()
        host_label.place(x=100, y=80)
        host_input.place(x=240, y=80)
        user_label.place(x=100, y=140)
        user_input.place(x=240, y=140)
        pass_label.place(x=100, y=200)
        pass_input.place(x=240, y=200)
        dbs_label.place(x=100, y=260)
        dbs_input.place(x=240, y=260)
        connect_button.place(x=280, y=300)

    def enter():
        global cred_type
        host=host_input.get()
        host_input.delete(0, 'end')
        user=user_input.get()
        user_input.delete(0, 'end')
        password=pass_input.get()
        pass_input.delete(0, 'end')
        dbs=dbs_input.get()
        dbs_input.delete(0, 'end')

        try:
            dbs_connect(host, user, password, dbs)
            dbs_write_to_bin(1,host, user, password, dbs)
            connection_label.config(text="CONNECTION ESTABLISHED")
            connection_label.place(x=180, y=530)
            mail_button.config(state="active")
            cred_type="tmp"
            window.after(3000, connection_label.place_forget)
        except Exception as e:
            connection_label.config(text="SOMETHING WENT WRONG\nPLEASE TRY AGAIN")
            connection_label.place(x=180, y=530)
            window.after(3000, connection_label.place_forget)
        
        return cred_type

    table_options =["Raw attendance","Points","Monthly attendance"]
    tables = StringVar()
    tables.set( "Raw attendance" )

    select_table_label=tk.Label(window, text="Mail\t\t\t    table", font=("Roboto", 15, 'bold'), bg=colours[0], fg=colours[2])
    select_table=tk.OptionMenu(window, tables, *table_options)
    select_table.config(bg=colours[1],font=("Roboto" , 10, 'bold'))
    host_label=tk.Label(window, text="HOST: ",font=("Roboto" , 12, 'bold'), bg=colours[0], fg=colours[1])
    host_input=tk.Entry(window, font=("Roboto" , 12, 'bold'), width=24)
    user_label=tk.Label(window, text="USER: ",font=("Roboto" , 12, 'bold'), bg=colours[0], fg=colours[1])
    user_input=tk.Entry(window, font=("Roboto" , 12, 'bold'), width=24)
    pass_label=tk.Label(window, text="PASSWORD: ",font=("Roboto" , 12, 'bold'), bg=colours[0], fg=colours[1])
    pass_input=tk.Entry(window,show="*", font=("Roboto" , 12, 'bold'), width=24)
    dbs_label=tk.Label(window, text="DATABASE: ",font=("Roboto" , 12, 'bold'), bg=colours[0], fg=colours[1])
    dbs_input=tk.Entry(window, font=("Roboto" , 12, 'bold'), width=24)
    connect_button=tk.Button(window,command=enter, text="CONNECT", font=("Roboto" , 10, 'bold') , bg=colours[1], activebackground=colours[2])
    connection_label=tk.Label(window,font=("Roboto" , 12, 'bold'), bg=colours[0], fg=colours[2])
    retry_label=tk.Label(window,font=("Roboto" , 12, 'bold'), bg=colours[0], fg=colours[2])
    use_tmp_creds_button=tk.Button(window,command=use_tmp_creds, text="USE TEMPORARY CREDS",font=("Roboto" , 10, 'bold') , bg=colours[1], activebackground=colours[2])
    use_saved_creds_button=tk.Button(window,command=use_saved_creds, text="USE SAVED CREDS",font=("Roboto" , 10, 'bold') , bg=colours[1], activebackground=colours[2])
    back_button=tk.Button(window,command= back, text="Back",font=("Roboto" , 11, 'bold') , bg=colours[1], activebackground=colours[2])
    mail_button=tk.Button(window,command= mail, state="disabled", text="MAIL",font=("Roboto" , 13, 'bold') , bg=colours[1], activebackground=colours[2])

    use_tmp_creds_button.place(x=230, y=50) 
    use_saved_creds_button.place(x=245, y=350) 
    back_button.place(x=10, y=10) 
    select_table_label.place(x=170, y=390)
    select_table.place(x=260, y=390)
    mail_button.place(x=270, y=440) 

    CreateToolTip(back_button, text="Back to Main Menu")

def UI():
    mail_button.place(x=480, y=10)
    help_button.place(x=5, y=545)
    settings_button.place(x=10, y=10)
    next_button.place(x=500, y=505)
    choose_file_button.place(x=165, y=450)
    clear_button.place(x=280, y=450)
    clear_all_button.place(x=350, y=450)
    listb.place(x=50, y=90)
    DnD_icon.place(x=252, y=210)
    DnD_label.place(x=250, y=300)

    window.mainloop()

if __name__ == "__main__":
    UI()

