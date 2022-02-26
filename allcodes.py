#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[in case of pip can't import the module's]

# UNOFFICAL WINDOWS BINARIES FOR PYTHON EXTENSIONS PACKAGES

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[title bar ]



















# from tkinter import *
# from ctypes import windll
# tk_title = "Jarvis" # Put here your window title
# root=Tk() # root (your app doesn't go in root, it goes in window)
# root.title(tk_title) 
# root.overrideredirect(True) # turns off title bar, geometry
# root.geometry('500x500+75+75') # set new geometry the + 75 + 75 is where it starts on the screen
# # root.iconbitmap("implant.ico") # to show your own icon 
# root.minimized = False # only to know if root is minimized
# root.maximized = False # only to know if root is maximized
# LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
# DGRAY = '#25292e' # window background color               (Hex color)
# RGRAY = '#10121f' # title bar color                       (Hex color)
# root.config(bg="#25292e")
# title_bar = Frame(root, bg=RGRAY, relief='raised', bd=0,highlightthickness=0)
# def set_appwindow(mainWindow): # to display the window icon on the taskbar, 
#                                # even when using root.overrideredirect(True)

#     # Some WindowsOS styles, required for task bar integration
#     GWL_EXSTYLE = -20
#     WS_EX_APPWINDOW = 0x00040000
#     WS_EX_TOOLWINDOW = 0x00000080
#     # Magic
#     hwnd = windll.user32.GetParent(mainWindow.winfo_id())
#     stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
#     stylew = stylew & ~WS_EX_TOOLWINDOW
#     stylew = stylew | WS_EX_APPWINDOW
#     res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)  
#     mainWindow.wm_withdraw()
#     mainWindow.after(10, lambda: mainWindow.wm_deiconify())
# def minimize_me():
#     root.attributes("-alpha",0) # so you can't see the window when is minimized
#     root.minimized = True 
# def deminimize(event):
#     root.focus() 
#     root.attributes("-alpha",1) # so you can see the window when is not minimized
#     if root.minimized == True:
#         root.minimized = False                              
# def maximize_me():

#     if root.maximized == False: # if the window was not maximized
#         root.normal_size = root.geometry()
#         expand_button.config(text=" 🗗 ")
#         root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
#         root.maximized = not root.maximized 
#         # now it's maximized       
#     else: # if the window was maximized
#         expand_button.config(text=" 🗖 ")
#         root.geometry(root.normal_size)
#         root.maximized = not root.maximized
#         # now it is not maximized
# # put a close button on the title bar
# close_button = Button(title_bar, text='  ×  ', command=root.destroy,bg=RGRAY,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
# expand_button = Button(title_bar, text=' 🗖 ', command=maximize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
# minimize_button = Button(title_bar, text=' 🗕 ',command=minimize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
# title_bar_title = Label(title_bar, text=tk_title, bg=RGRAY,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)
# # a frame for the main area of the window, this is where the actual app will go
# window = Frame(root, bg=DGRAY,highlightthickness=0)
# # pack the widgets
# title_bar.pack(fill=X)
# close_button.pack(side=RIGHT,ipadx=7,ipady=1)
# expand_button.pack(side=RIGHT,ipadx=7,ipady=1)
# minimize_button.pack(side=RIGHT,ipadx=7,ipady=1)
# title_bar_title.pack(side=LEFT, padx=10)
# window.pack(expand=1, fill=BOTH) # replace this with your main Canvas/Frame/etc.
# #xwin=None
# #ywin=None
# # bind title bar motion to the move window function
# def changex_on_hovering(event):
#     global close_button
#     close_button['bg']='red'
# def returnx_to_normalstate(event):
#     global close_button
#     close_button['bg']=RGRAY
# def change_size_on_hovering(event):
#     global expand_button
#     expand_button['bg']=LGRAY
# def return_size_on_hovering(event):
#     global expand_button
#     expand_button['bg']=RGRAY
# def changem_size_on_hovering(event):
#     global minimize_button
#     minimize_button['bg']=LGRAY
# def returnm_size_on_hovering(event):
#     global minimize_button
#     minimize_button['bg']=RGRAY
# def get_pos(event): # this is executed when the title bar is clicked to move the window
#     if root.maximized == False:  
#         xwin = root.winfo_x()
#         ywin = root.winfo_y()
#         startx = event.x_root
#         starty = event.y_root
#         ywin = ywin - starty
#         xwin = xwin - startx
#         def move_window(event): # runs when window is dragged
#             root.config(cursor="fleur")
#             root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')
#         def release_window(event): # runs when window is released
#             root.config(cursor="arrow")           
#         title_bar.bind('<B1-Motion>', move_window)
#         title_bar.bind('<ButtonRelease-1>', release_window)
#         title_bar_title.bind('<B1-Motion>', move_window)
#         title_bar_title.bind('<ButtonRelease-1>', release_window)
#     else:
#         expand_button.config(text=" 🗖 ")
#         root.maximized = not root.maximized
# title_bar.bind('<Button-1>', get_pos) # so you can drag the window from the title bar
# title_bar_title.bind('<Button-1>', get_pos) # so you can drag the window from the title 
# # button effects in the title bar when hovering over buttons
# close_button.bind('<Enter>',changex_on_hovering)
# close_button.bind('<Leave>',returnx_to_normalstate)
# expand_button.bind('<Enter>', change_size_on_hovering)
# expand_button.bind('<Leave>', return_size_on_hovering)
# minimize_button.bind('<Enter>', changem_size_on_hovering)
# minimize_button.bind('<Leave>', returnm_size_on_hovering)
# # resize the window width =======================================================================
# resizex_widget = Frame(window,bg=DGRAY,cursor='sb_h_double_arrow')
# resizex_widget.pack(side=RIGHT,ipadx=2,fill=Y)
# def resizex(event):
#     xwin = root.winfo_x()
#     difference = (event.x_root - xwin) - root.winfo_width()
#     if root.winfo_width() > 150 : # 150 is the minimum width for the window
#         try:
#             root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
#         except:
#             pass
#     else:
#         if difference > 0: # so the window can't be too small (150x150)
#             try:
#                 root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
#             except:
#                 pass
#     resizex_widget.config(bg=DGRAY)
# resizex_widget.bind("<B1-Motion>",resizex)
# # resize the window height =======================================================================
# resizey_widget = Frame(window,bg=DGRAY,cursor='sb_v_double_arrow')
# resizey_widget.pack(side=BOTTOM,ipadx=2,fill=X)
# def resizey(event):
#     ywin = root.winfo_y()
#     difference = (event.y_root - ywin) - root.winfo_height()
#     if root.winfo_height() > 150: # 150 is the minimum height for the window
#         try:
#             root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
#         except:
#             pass
#     else:
#         if difference > 0: # so the window can't be too small (150x150)
#             try:
#                 root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
#             except:
#                 pass
#     resizex_widget.config(bg=DGRAY)
# resizey_widget.bind("<B1-Motion>",resizey)
# # some settings
# root.bind("<FocusIn>",deminimize) # to view the window by clicking on the window icon on the taskbar
# root.after(10, lambda: set_appwindow(root)) # to see the icon on the task bar

# #YOUR CODE GOES HERE==================================================================================
# #Label(window,text="Hello :D",bg=DGRAY,fg="#fff").pack(expand=1) # example 

# # ===================================================================================================
# root.mainloop()



















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[date time with save function  ehich can be save in the form of txt]



















# hi=str(input("enter your name please\n"))
# mode=str(input("enter what you want?:....\n"))
# g=hi.capitalize()
# name=mode.capitalize()
# from tkinter import*
# import datetime
# x = datetime.datetime.now() 
# a=x.strftime("%x %A")
# b=x.strftime("%I:%M %p")
# c=x.strftime("%A")
# d=x.strftime("%H:%M")
# e=x.strftime("%C")
# f=(e,"century")
# #date
# if name =="Date":
#     me=Tk()
#     me.geometry("300x50")
#     me.title("Date")
#     melabel = Label(me,text=a,bg='White',font=("Times",30,'bold'))
#     melabel.pack(side=TOP)
# #time both in 12 and 24 Hrs
# elif name=="Time":
#     me=Tk()
#     me.geometry("170x50")
#     me.title("Time in 12 Hrs")
#     melabel = Label(me,text=b,bg='White',font=("Times",30,'bold'))
#     melabel.pack(side=TOP)
#     me=Tk()
#     me.geometry("100x50")
#     me.title("24 Hrs")
#     melabel = Label(me,text=d,bg='White',font=("Times",30,'bold'))
#     melabel.pack(side=TOP)
# #day
# elif name=="Day":
#     me=Tk()
#     me.geometry("170x50")
#     me.title("Time")
#     melabel = Label(me,text=c,bg='White',font=("Times",30,'bold'))
#     melabel.pack(side=TOP)
# #century
# elif name=="Century":
#     me=Tk()
#     me.geometry("180x50")
#     me.title("Century")
#     melabel = Label(me,text=f,bg='White',font=("Times",30,'bold'))
#     melabel.pack(side=TOP)
# f=open('game.txt','w')
# f.write("user name is:-")
# f.write("\n")
# f.write(g)
# f.write("\n")
# f.write("searching for:-")
# f.write("\n")
# f.write(name)
# f.close()



















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Date and Time by taking input by user using input wiget]



















# from tkinter import*
# root=Tk()
# root.geometry("300x300")
# import datetime
# x = datetime.datetime.now() 
# a=x.strftime("%x %A")
# b=x.strftime("%I:%M %p")
# c=x.strftime("%A")
# d=x.strftime("%H:%M")
# e=x.strftime("%C")
# f=(e,"century")
# def getvals():
#     print(f"The value of username is {uservalue.get()}")
#     x=uservalue.get()
#     y=x.capitalize()
#     if y=="Date":
#             me=Tk()
#             me.geometry("360x50")
#             me.minsize(360,50)
#             me.maxsize(360,50)
#             me.title("Date")
#             melabel = Label(me,text=a,bg='White',font=("Times",30,'bold'))
#             melabel.pack(side=TOP)
#             me.mainloop()
#     elif y=="Time":
#         me=Tk()
#         me.geometry("170x50")
#         me.minsize(170,50)
#         me.maxsize(170,50)
#         me.title("Time")
#         melabel = Label(me,text=b,bg='White',font=("Times",30,'bold'))
#         melabel.pack(side=TOP)
#         me.mainloop()
#     elif y=="Day":
#         me=Tk()
#         me.geometry("200x50")
#         me.minsize(200,50)
#         me.maxsize(200,50)
#         me.title("Day")
#         melabel = Label(me,text=c,bg='White',font=("Times",30,'bold'))
#         melabel.pack(side=TOP)
#         me.mainloop()
#     elif y=="Century":
#         me=Tk()
#         me.geometry("200x50")
#         me.minsize(200,50)
#         me.maxsize(200,50)
#         me.title("Century")
#         melabel = Label(me,text=f,bg='White',font=("Times",30,'bold'))
#         melabel.pack(side=TOP)
#         me.mainloop()
#     else:
#         me=Tk()
#         me.geometry("50x80")
#         me.title("sorry")
#         melabel=Label(me,text="sorry",font=("Times",30,'bold'))
#         melabel.pack()
   
# # time
# user=Label(root,text="Entry what you want")
# user.grid()
# uservalue=StringVar()
# userentry=Entry(root,textvariable=uservalue)
# userentry.grid(row=0,column=1)
# Button(text="Submit", command=getvals).grid()

# root.mainloop()



















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[date and time by button widget]



















# from tkinter import*
# import datetime
# x = datetime.datetime.now() 
# a=x.strftime("%x %A")
# b=x.strftime("%I:%M %p")
# c=x.strftime("%A")
# d=x.strftime("%H:%M")
# e=x.strftime("%C")
# f=(e,"century")
# root=Tk()
# root.geometry("350x40")
# root.minsize(350,40)
# root.maxsize(350,40)
# root.title("date and time ")
# hel=Frame(root,borderwidth=6, bg="white",relief=SUNKEN)
# hel.pack(anchor="nw")
# # date
# def date():
#     me=Tk()
#     me.geometry("360x50")
#     me.minsize(360,50)
#     me.maxsize(360,50)
#     me.title("Date")
#     melabel = Label(me,text=a,bg='White',font=("Times",30,'bold'))
#     melabel.pack(side=TOP)
#     me.mainloop()
# # time
# def time():
#     me=Tk()
#     me.geometry("170x50")
#     me.minsize(170,50)
#     me.maxsize(170,50)
#     me.title("Time")
#     melabel = Label(me,text=b,bg='White',font=("Times",30,'bold'))
#     melabel.pack(side=TOP)
#     me.mainloop()
# # day
# def day():
#     me=Tk()
#     me.geometry("200x50")
#     me.minsize(200,50)
#     me.maxsize(200,50)
#     me.title("Day")
#     melabel = Label(me,text=c,bg='White',font=("Times",30,'bold'))
#     melabel.pack(side=TOP)
#     me.mainloop()
# # century
# def century():
#     me=Tk()
#     me.geometry("200x50")
#     me.minsize(200,50)
#     me.maxsize(200,50)
#     me.title("Century")
#     melabel = Label(me,text=f,bg='White',font=("Times",30,'bold'))
#     melabel.pack(side=TOP)
#     me.mainloop()
# # button 
# b1=Button(hel,fg="black",text="Date",command=date)
# b1.pack(padx=23,side=LEFT)
# b2=Button(hel,fg="black",text="Time",command=time)
# b2.pack(padx=23,side=LEFT)
# b3=Button(hel,fg="black",text="Day",command=day)
# b3.pack(padx=23,side=LEFT)
# b4=Button(hel,fg="black",text="Century",command=century)
# b4.pack(padx=23,side=LEFT)
# root.mainloop()



















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[first calculator]



















# from tkinter import*

# me=Tk()
# me.geometry("354x460")
# me.title("CALCULATOR")
# melabel = Label(me,text="CALCULATOR",bg='White',font=("Times",30,'bold'))
# melabel.pack(side=TOP)
# me.config(background='Dark gray')

# textin=StringVar()
# operator=""

# def clickbut(number):   #lambda:clickbut(1)
#      global operator
#      operator=operator+str(number)
#      textin.set(operator)

# def equlbut():
#      global operator
#      add=str(eval(operator))
#      textin.set(add)
#      operator=''
# def equlbut():
#      global operator
#      sub=str(eval(operator))
#      textin.set(sub)
#      operator=''     
# def equlbut():
#      global operator
#      mul=str(eval(operator))
#      textin.set(mul)
#      operator=''
# def equlbut():
#      global operator
#      div=str(eval(operator))
#      textin.set(div)
#      operator=''    

# def clrbut():
#      textin.set('')

     
# metext=Entry(me,font=("Courier New",12,'bold'),textvar=textin,width=25,bd=5,bg='powder blue',justify=RIGHT)
# metext.pack()

# but1=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
# but1.place(x=10,y=100)

# but2=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
# but2.place(x=10,y=170)

# but3=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
# but3.place(x=10,y=240)

# but4=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
# but4.place(x=75,y=100)

# but5=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
# but5.place(x=75,y=170)

# but6=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
# but6.place(x=75,y=240)

# but7=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
# but7.place(x=140,y=100)

# but8=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
# but8.place(x=140,y=170)

# but9=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
# but9.place(x=140,y=240)

# but0=Button(me,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
# but0.place(x=10,y=310)

# butdot=Button(me,padx=47,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
# butdot.place(x=75,y=310)

# butpl=Button(me,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
# butpl.place(x=205,y=100)

# butsub=Button(me,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
# butsub.place(x=205,y=170)

# butmul=Button(me,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
# butmul.place(x=205,y=240)

# butdiv=Button(me,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
# butdiv.place(x=205,y=310)

# butclear=Button(me,padx=14,pady=119,bd=4,bg='white',text="CE",command=clrbut,font=("Courier New",16,'bold'))
# butclear.place(x=270,y=100)

# butequal=Button(me,padx=151,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
# butequal.place(x=10,y=380)
# me.mainloop()




















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[upgraded calculator]



















# import tkinter as tk

# LARGE_FONT_STYLE = ("Arial", 40, "bold")
# SMALL_FONT_STYLE = ("Arial", 16)
# DIGITS_FONT_STYLE = ("Arial", 24, "bold")
# DEFAULT_FONT_STYLE = ("Arial", 20)

# OFF_WHITE = "#F8FAFF"
# WHITE = "#FFFFFF"
# LIGHT_BLUE = "#CCEDFF"
# LIGHT_GRAY = "#F5F5F5"
# LABEL_COLOR = "#25265E"


# class Calculator:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.geometry("375x667")
#         self.window.resizable(0, 0)
#         self.window.title("Calculator")

#         self.total_expression = ""
#         self.current_expression = ""
#         self.display_frame = self.create_display_frame()

#         self.total_label, self.label = self.create_display_labels()

#         self.digits = {
#             7: (1, 1), 8: (1, 2), 9: (1, 3),
#             4: (2, 1), 5: (2, 2), 6: (2, 3),
#             1: (3, 1), 2: (3, 2), 3: (3, 3),
#             0: (4, 2), '.': (4, 1)
#         }
#         self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
#         self.buttons_frame = self.create_buttons_frame()

#         self.buttons_frame.rowconfigure(0, weight=1)
#         for x in range(1, 5):
#             self.buttons_frame.rowconfigure(x, weight=1)
#             self.buttons_frame.columnconfigure(x, weight=1)
#         self.create_digit_buttons()
#         self.create_operator_buttons()
#         self.create_special_buttons()
#         self.bind_keys()

#     def bind_keys(self):
#         self.window.bind("<Return>", lambda event: self.evaluate())
#         for key in self.digits:
#             self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

#         for key in self.operations:
#             self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

#     def create_special_buttons(self):
#         self.create_clear_button()
#         self.create_equals_button()
#         self.create_square_button()
#         self.create_sqrt_button()

#     def create_display_labels(self):
#         total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
#                                fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
#         total_label.pack(expand=True, fill='both')

#         label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
#                          fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
#         label.pack(expand=True, fill='both')

#         return total_label, label

#     def create_display_frame(self):
#         frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
#         frame.pack(expand=True, fill="both")
#         return frame

#     def add_to_expression(self, value):
#         self.current_expression += str(value)
#         self.update_label()

#     def create_digit_buttons(self):
#         for digit, grid_value in self.digits.items():
#             button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
#                                borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
#             button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

#     def append_operator(self, operator):
#         self.current_expression += operator
#         self.total_expression += self.current_expression
#         self.current_expression = ""
#         self.update_total_label()
#         self.update_label()

#     def create_operator_buttons(self):
#         i = 0
#         for operator, symbol in self.operations.items():
#             button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
#                                borderwidth=0, command=lambda x=operator: self.append_operator(x))
#             button.grid(row=i, column=4, sticky=tk.NSEW)
#             i += 1

#     def clear(self):
#         self.current_expression = ""
#         self.total_expression = ""
#         self.update_label()
#         self.update_total_label()

#     def create_clear_button(self):
#         button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
#                            borderwidth=0, command=self.clear)
#         button.grid(row=0, column=1, sticky=tk.NSEW)

#     def square(self):
#         self.current_expression = str(eval(f"{self.current_expression}**2"))
#         self.update_label()

#     def create_square_button(self):
#         button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
#                            borderwidth=0, command=self.square)
#         button.grid(row=0, column=2, sticky=tk.NSEW)

#     def sqrt(self):
#         self.current_expression = str(eval(f"{self.current_expression}**0.5"))
#         self.update_label()

#     def create_sqrt_button(self):
#         button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
#                            borderwidth=0, command=self.sqrt)
#         button.grid(row=0, column=3, sticky=tk.NSEW)

#     def evaluate(self):
#         self.total_expression += self.current_expression
#         self.update_total_label()
#         try:
#             self.current_expression = str(eval(self.total_expression))

#             self.total_expression = ""
#         except Exception as e:
#             self.current_expression = "Error"
#         finally:
#             self.update_label()

#     def create_equals_button(self):
#         button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
#                            borderwidth=0, command=self.evaluate)
#         button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

#     def create_buttons_frame(self):
#         frame = tk.Frame(self.window)
#         frame.pack(expand=True, fill="both")
#         return frame

#     def update_total_label(self):
#         expression = self.total_expression
#         for operator, symbol in self.operations.items():
#             expression = expression.replace(operator, f' {symbol} ')
#         self.total_label.config(text=expression)

#     def update_label(self):
#         self.label.config(text=self.current_expression[:11])

#     def run(self):
#         self.window.mainloop()


# if __name__ == "__main__":
#     calc = Calculator()
#     calc.run()



















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[when button is clicked the text is display in the frame of the root]



















# import tkinter
# from tkinter import *
# from tkinter import messagebox

# def btnclick():
#     messagebox.showinfo("Message","Button is clicked")

# root = tkinter.Tk()
# root.geometry("400x400")

# photo = PhotoImage(file="group.png")
# photo2 = PhotoImage(file="group2.png")
# btn = Button(
#     root,
#     image=photo,
#     command=btnclick,
#     border=0,
# )
# btn.pack(pady=50)

# btn2 = Button(
#     root,
#     image=photo2,
#     command=btnclick,
#     border=0,
# )
# btn2.pack()
# root.mainloop()

















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[ai concept code from google \ youtube]



















#improyting all the required modules
# import speech_recognition as sr#
# import pyttsx3 as tt#
# import datetime as date#
# import shutil#
# import smtplib#
# import wikipedia as wiki#
# import os#
# import webbrowser as wbb#
# import random#
# import wolframalpha as wo#
# import psutil#
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver as wb
# from pynput.mouse import Button, Controller
# import datetime
# import subprocess
# from pygame import mixer 

# #initilizing the required modules
# mouse = Controller()
# en = tt.init()
# vo = en.getProperty('voices')
# en.setProperty('voice', vo[1].id)
# en.setProperty('rate', 160)
# go = 'https://www.google.com'
# yt = 'https://www.youtube.com'
# insta = 'https://www.instagram.com'
# wp = 'https://web.whatsapp.com/'
# woappid = '**YOUR WOLFRAMALPHA API KEY HERE**'


# #defining the required funcitons

# def speak(audio):#used to convert the text to audio
#     en.say(audio)
#     en.runAndWait()



# def take_command():#convert the audio to text
#     try:

#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             r.adjust_for_ambient_noise(source)
#             print('listerning....')
#             audio = r.listen(source)
#             text = r.recognize_google(audio)
#             print('you said: ' + text)
#             return (text.lower())

#     except:
#         print('unable to recognize voice')
#         return 'sr030'
 


# def get_sysinfo():#used to get the system cpu usage
#     info = []
#     cpufreq = psutil.cpu_freq()
#     info.append(f"Current Frequency of the CPU is: {cpufreq.current:.2f} Megahertz")
#     info.append("CPU Usage Per Core:")
#     for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
#         info.append(f"Core {i}: {percentage}%")
#     info.append(f"Total CPU Usage: {psutil.cpu_percent()}%")
#     return info



# def browser(site):#used to open the browse and search in google
#     while True:   
#         if ('google' in site):
#             speak('openning google')
#             driver = wb.Chrome("**CHROME DRIVER PATH*")
#             driver.get(go)
#             time.sleep(2)
#             speak('what do you want to search sir..')
#             search = take_command()
#             if 'sr030' not in search:
#                 bar = driver.find_element_by_name('q')
#                 bar.send_keys(search, Keys.ENTER)
#                 while True:
#                     print('...........____.............')
#                     speak('do you what to exit')
#                     exit = take_command()
#                     if 'sr030' not in exit:
#                         if('down' in exit) or ('scroll down' in exit):
#                             for i in range(5):
#                                 mouse.scroll(0, -1)
#                                 time.sleep(0.5)
#                         elif('up' in exit) or ('scroll up' in exit):
#                             for i in range(5):
#                                 mouse.scroll(0, 1)
#                                 time.sleep(0.5)
#                         if ('yes' in exit) or ('of course' in exit) or ('close' in exit) or ('exit' in exit):
#                             speak('closing browser..')
#                             driver.close()
#                             return 'exit'
#                     else:
#                         speak('hmm')
#                         continue
#             else:
#                 speak('try again')
#                 driver.close()
#                 continue
     
#         elif 'exit' in site:
#             print('definition loop')
#             return 'exit'
#         else:
#             speak('could not recognize, try again')
#             return       
    


# def wish_me():
#     os.startfile('C:\\Program Files\\Rainmeter\\Rainmeter.exe')
#     speak('awaking system protocols')
#     speak('checking network protocols') 
#     speak('getting system information , cpu usage..')
#     info = get_sysinfo()
#     for i in info:
#         speak(i)
#     speak('system is in optimal condition')
#     hu = int(date.datetime.now().hour)
#     if(hu > 0 and hu < 12):
#         speak('Good Morning sir!')
#     elif(hu > 12 and hu < 18):
#         speak('Good Afternoon sir!')
#     else:
#         speak('Good evening sir!')
#     speak('i am your personal Assistant, Draster 2 point o')
#     speak('How can i help you sir?')

    


# def send_email(to, content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('*YOUR MAIL ID*','*YOUR MAIL PASSWORD*')
#     server.sendmail('*YOUR MAIL ID*',to,content)
#     server.close()



# #program starts here
# if "_name_" =='_main_':
#     lambda : os.system('cls')# clearing the terminal

#     mrun = True
#     while mrun:


#         task = take_command().lower()#getting the task from the user in voice form 
#         print(task)
        
#         if 'wikipedia' in task:     #wikipedia searches
#             speak('analysing your command..')
#             speak('Searching Wikipedia...')
#             info = task.replace('wikipedia', '')
#             try :
#                 res = wiki.summary(info, 3)
#                 speak('According to wikipedia..')
#                 print(res)
#                 speak(res)
#             except:
#                 speak('not found in wikipedia , searching on google')
#                 speak('these are the results found on google')

                
#         elif 'send an email to me' in task:
#             speak('analysing your command..')
#             try:
#                 speak('What should I send ')
#                 content = take_command()
#                 to = '*YOUR MAIL ID*'
#                 speak('sending email to '+ to)
#                 send_email(to, content)
#                 speak('email has been sent succesfully sir..')
#             except Exception as e:
#                 print(e)
#                 speak('i am not able to send this email')

#         elif 'send an email' in task:       #send mail to the sepcified emali in the termianl
#             speak('analysing your command..')
#             try:
#                 speak('whom should i send')
#                 to = input('enter the email :')
#                 print(to)
#                 speak('what should i send')
#                 content = take_command()
                
#                 erun = True
#                 while erun:
#                     speak('confirmation needed')
#                     confo = take_command()
#                     if ('send it' in confo) or ('yes' in confo) or ('do it' in confo):
#                         send_email(to, content) 
#                         speak('email sent succesfully..')
#                         print('email sent succesfully..')
#                         erun = False
#                     elif ('don\'t send' in confo) or ('wait' in confo) or ('no' in confo):
#                         speak('as your wish sir, cancelling the email')
#                         erun = False
#                     else:
#                         speak('could not recognize , try again')
#                         continue
                    
#             except:
#                 speak('i am not able to send this email, please try again')

#         elif 'open browser' in task:
#             speak('analysing your command..')
#             site = speak('which site do you want to open?')
#             run = True
#             while run:
#                 site = take_command()
#                 print(site)
#                 speak('just a minute sir')
#                 if 'sr030' not in site:
#                     state = browser(site)
#                 if ('exit' in state) or 'close' in state:
#                     run = False
#                 else:
#                     speak('try again')
#                     continue
            
#         elif "open youtube" in task:    #opens youtube and play the specified sond, try sepaking open youtube and play the song needed
#             speak('analysing your command..')
#             speak('openning youtube..\n')
#             if 'play' in task:
#                 speak('just a minute sir..')
#                 song = task.replace('open','')
#                 song = task.replace('youtube', '')
#                 sond = task.replace('and','')
#                 song = task.replace('play','')
#             else:
#                 wbb.open('youtube.com')

#         elif 'open google' in task:     #open google
#             speak('analysing your command..')
#             speak('hear you go to google')
#             wbb.open('google.com')

#         elif 'open instagram' in task:      #open instagram
#             speak('analysing your command..')
#             speak('openning insta')
#             wbb.open('instagram.com')

#         elif 'exit' in task:        # to exit the loop
#             speak('Thanks for giving me your time')
#             speak('see you later')
#             subprocess.call(['taskkill','/F','/IM','Rainmeter.exe'])
#             mrun = False

#         elif 'song' in task or ('music' in task) or('on pc' in task) or ('in pc' in task):      #to play a random song from the specified folder
#             speak('analysing your command..')
#             i = random.randint(1,'***number of songs +1')
#             speak('playin a song on pc')
#             path = "**folder path containing songs"
#             song_list = os.listdir(path)
#             os.startfile(os.path.join(path, song_list[i]))
        
#         elif 'time' in task:    # to know the time
#             time = datetime.datetime.now().strftime('%I %M %p')
#             print("the current time is ",time)
#             speak("the current time is " + time)

#         elif ('do you know tamil' in task):
#             speak('enaku tamil theriyathu')

#         elif ('open notepad' in task) or ('start notepad' in task):     #open notepad
#             speak('opening notepad')
#             os.startfile('C:\\Windows\\system32\\notepad.exe')

#         elif ('close notepad' in task) or ( 'exit notepad' in task):        #close notepad
#             speak('terminating notepad')
#             subprocess.call(['taskkill','/F','/IM','notepad.exe']) 

#         elif ('open paint' in task) or ('open mspaint' in task) or ('start paint' in task):        #open paint
#             speak('opening microsoft paint')
#             os.startfile('C:\\Windows\\system32\\mspaint.exe')
        
#         elif ('close paint' in task) or ('terminate paint' in task) or ('exit paint' in task):        #closepaint
#             speak('terminating microsoft paint') 
#             subprocess.call(['taskkill','/F','/IM','mspaint.exe']) 

#         elif 'who are you' in task:
#             speak('i am draster , i am your personal assestant . i help you playing youtube videos, musics, getting informations , google searches, excetra')
        
#         elif ('what ' in task) or('who' in task) or ('how' in task) or ('when' in task) or ('where' in task) or ('why' in task) or ('tell' in task):    # to get informations
#             speak('analysing your command..')
#             try:
#                 client = wo.Client(woappid)
#                 res = client.query(task)
#                 ans = next(res.results).text
#                 print(ans)
#                 speak(ans)
#             except:
#                 speak('these are the results found on google')


#         else:
#             print('.....')



















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[loading animation gui concept]



















# from tkinter import *
# from time import sleep
# from tracemalloc import stop
# class loadingsplash:
#     def play_animation(self):
#         for i in range(5):
#             for j in range(16):
#                 Label(self.root,bg="#FFBD09",width=2,height=1).place(x=(j+22)*22,y=350)
#                 sleep(0.06)
#                 self.root.update_idletasks()
#                 Label(self.root,bg="#1F2732",width=2,height=1).place(x=(j+22)*22,y=350)
#                 stop()
#         else:
#             self.root.destroy()
#             exit(0)

#     def __init__(self):
#         self.root=Tk()
#         self.root.config(bg="black")
#         self.root.title("custom  Loader")
#         self.root.attributes("-fullscreen",True)
#         self.root.attributes('-transparentcolor','black')
#         self.root.state('zoomed')
#         Label(self.root,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=490,y=320)
#         for i in range (16):
#             Label(self.root,bg="#1F2732",width=2,height=1).place(x=(i+22)*22,y=350)
#             self.root.update()
#             self.play_animation()
#         self.root.mainloop()


# if __name__=="__main__":
#     loadingsplash()       




















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[save button with the help of image ]



















# from tkinter import*
# root=Tk()
# root.title("button")
# root.geometry("800x800")
# def hi():
#     my_label.config(text="you clicked the button")

# photo=PhotoImage(file="group.png")# put image in place of X
# img_label=Label(image=photo)
# #img_label.pack(pady=20)
# poke=Button(root,image=photo,command=hi,borderwidth=0)
# poke.pack(pady=20)
# my_label=Label(root,text='')
# my_label.pack(pady=20)
# root.mainloop()


















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[form with take the user input and save in the form of txt (notepad)]



















# from tkinter import *
# import tkinter
# from tkinter import messagebox
# def btnclick():
#     messagebox.showinfo("Message","Button is clicked")

# root=Tk()
# def hel():
#     print("Male")
# def heli():
#     print("Female")
# def abcd():
#     root=Tk()
#     root.geometry("400x280")
#     root.config(txt="hello")
#     Label(root, text="Here is Your Data", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)
#     name = Label(root, text="Name")
#     phone = Label(root, text="Phone")
#     gender = Label(root, text="Gender")
#     address = Label(root, text="Address")
#     age = Label(root, text="Age")
#     name.grid(row=1, column=2)
#     phone.grid(row=2, column=2)
#     gender.grid(row=3, column=2)
#     address.grid(row=4, column=2)
#     age.grid(row=5, column=2)
#     a=  (((namevalue.get()).capitalize()))
#     b=  (((phonevalue.get()).capitalize()))
#     c=  (((gendervalue.get()).capitalize()))
#     d=  (((addressvalue.get()).capitalize())) 
#     e= (((agevalue.get()).capitalize()))   
#     name = Label(root, text=a)
#     phone = Label(root, text=b)
#     gender = Label(root, text=c)
#     address = Label(root, text=d)
#     age = Label(root, text=e)
#     name.grid(row=1, column=3)
#     phone.grid(row=2, column=3)
#     gender.grid(row=3, column=3)
#     address.grid(row=4, column=3)
#     age.grid(row=5, column=3)
#     root.mainloop()
# def saveas():
#     a=((namevalue.get()).capitalize())
#     b=((phonevalue.get()).capitalize())
#     c=((gendervalue.get()).capitalize())
#     d=((addressvalue.get()).capitalize())
#     e=((agevalue.get()).capitalize())
#     f=open('now.txt','w')
#     f.write("User Name Is :-   ")
#     f.write("\n")
#     f.write(a)
#     f.write("\n")  
#     f.write("User Phone Number Is :-   ")
#     f.write("\n")
#     f.write(b)
#     f.write("\n")
#     f.write("User Gender Is:-   ")
#     f.write("\n")
#     f.write(c)
#     f.write("\n")
#     f.write("User Address Is:-   ")
#     f.write("\n")
#     f.write(d)
#     f.write("\n")
#     f.write("User Age Is:-   ")
#     f.write("\n")
#     f.write(e)
#     f.close()
# def ge():
#     if(gendervalue.get()).capitalize()=="Male":
#         print("ok")
        
#     elif (gendervalue.get()).capitalize()== "Female":
#         print("ok")
        
#     else:
#         me=Tk()
#         me.geometry("1000x50")
#         me.title("please")
#         melabel=Label(me,text="sorry please enter male or female",font=("Times",30,'bold'))
#         melabel.pack()
# def ages():
#     verma=int(agevalue.get())
#     if verma <=100:
#         print("ok")
#     if verma>100 :
#         me=Tk()
#         me.geometry("1000x50")
#         me.title("please")
#         melabel=Label(me,text="sorry please enter your correct age",font=("Times",30,'bold'))
#         melabel.pack()
# def ph():
#     happy=int(phonevalue.get())
#     if happy>1000000000:
#         print("ok phonenumber")
#     if happy>10000000000:
#         me=Tk()
#         me.geometry("1000x50")
#         me.title("please")
#         melabel=Label(me,text="sorry please enter correct phone number",font=("Times",30,'bold'))
#         melabel.pack()

# root.geometry("644x344")
# background_image = tkinter.PhotoImage(file='landscape.png')
# background_label = tkinter.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)
# photo = PhotoImage(file="group.png")
# foodservicevalue2 = IntVar()
# Label (root,text="welcome buddy",font="comicsansms 13 bold",pady=15,bg="#e1eec4").grid(row=0,column=3)
# Label(root,text="name").grid(row=1, column=2)
# Label(root, text="Phone").grid(row=2, column=2)
# Label(root, text="Gender").grid(row=3, column=2)
# Label(root, text="Address").grid(row=4, column=2)
# Label(root, text="Age").grid(row=5, column=2)
# namevalue = StringVar()
# phonevalue = StringVar()
# gendervalue = StringVar()
# addressvalue = StringVar()
# agevalue = StringVar()
# Entry(root, textvariable=namevalue).grid(row=1, column=3)
# Entry(root, textvariable=phonevalue).grid(row=2, column=3)
# Entry(root, textvariable=gendervalue).grid(row=3, column=3)
# Entry(root, textvariable=addressvalue).grid(row=4, column=3)
# Entry(root, textvariable=agevalue).grid(row=5, column=3)
# def save():
#     btnclick()
#     ph()
#     ge()
#     ages()
#     abcd()
# def hello():
#     messagebox.showinfo("Note","your data is saved secure")
#     me=Tk()
#     me.geometry("1000x50")
#     me.title("Want to book")
#     melabel=Label(me,text="Your extra fast servies is booked",font=("Times",30,'bold'))
#     melabel.pack()
#     f=open("now.txt",'a')
#     f.write( "\n")
#     f.write("want to book a extra")
#     f.close()
# Button(image=photo,command=save,pady=50,borderwidth=0).grid(row=7,column=3)
# Button(text=" save ",command=saveas).grid(row=9,column=3)
# kite=Checkbutton(text="want to keep secure",variable=foodservicevalue2,command=hello)
# kite.grid(row=11,column=3)

# root.mainloop()











#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{weather appilaction gui display}



















# import tkinter
# from tkinter import *
# from tkinter import messagebox
# HEIGHT = 500
# WIDTH = 600
# root = tkinter.Tk()
# #canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH)
# #canvas.pack()
# root.geometry("600x500")
# background_image = tkinter.PhotoImage(file='landscape.png')
# background_label = tkinter.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

# frame = tkinter.Frame(root, bg='#80c1ff', bd=5)
# frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# entry = tkinter.Entry(frame, font=40)
# entry.place(relwidth=0.65, relheight=1)

# button = tkinter.Button(frame, text="view", font=40)
# button.place(relx=0.7, relheight=1, relwidth=0.3)

# lower_frame = tkinter.Frame(root, bg='#80c1ff', bd=10)
# lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# label = tkinter.Label(lower_frame)
# label.place(relwidth=1, relheight=1)

# root.mainloop()


















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[iron man first  gui application display ]



















# from tkinter import *
# from pygame import font
# root= Tk()
# root.title("jarvis")
# root.iconbitmap("artificial-intelligence.ico")
# root.geometry("500x500")
# root.minimized = False # only to know if root is minimized
# root.maximized = False # only to know if root is maximized
# root.wm_attributes('-transparentcolor',root['bg'])
# #root.state('zoomed') #this will show title bar 
# root.wm_attributes('-fullscreen',True) #this will not show title bar
# background_image = PhotoImage(file='hacker.png')
# #root.wm_attributes('-transparentcolor','red')
# #frame=Frame(root,width=200,height=200,bg="red")
# #frame.pack(pady=20,ipadx=20,ipady=20)
# #mylabel=Label(ladel, image=background_image,bg="red",fg="white",font="bookman  13 bold")
# #mylabel.pack(pady=20)
# mylabel=Label(root, image=background_image,fg="white",font="bookman  13 bold")
# mylabel.pack(side=BOTTOM,anchor=SE)
# def minimize_me():
#     root.attributes("-alpha",0) # so you can't see the window when is minimized
#     root.minimized = True  
# def deminimize(event):
#     root.focus() 
#     root.attributes("-alpha",1) # so you can see the window when is not minimized
#     if root.minimized == True:
#         root.minimized = False 
# def set_appwindow(mainWindow): # to display the window icon on the taskbar, 
#                                # even when using root.overrideredirect(True)

#     # Some WindowsOS styles, required for task bar integration
#     GWL_EXSTYLE = -20
#     WS_EX_APPWINDOW = 0x00040000
#     WS_EX_TOOLWINDOW = 0x00000080
# root.bind("<FocusIn>",deminimize) # to view the window by clicking on the window icon on the taskbar
# root.after(10, lambda: set_appwindow(root)) # to see the icon on the task bar
        
# button=Button(root,text="minimze",command=minimize_me,fg="black",font="comics 20 ",bd=0)
# button.pack(side=TOP,anchor=NE)

# close= PhotoImage(file='close1.png')
# button1=Button(root,image=close,command=root.destroy,fg="white",font="comics 5 ",bd=0)
# button1.pack(side=TOP,anchor=E)
# root.mainloop()


















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[first application Note it is use to take user input and save them in the form of txt in the system with the name that user like]



















# # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[importing module's]


# from tkinter import *
# from tkinter import filedialog
# from time import sleep   
# from tracemalloc import stop
# from cgitb import text
# from tkinter import messagebox
# import datetime
# import os

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[loading frame ]

# def nike():

#     ro=Tk()
#     ro.config(bg="black")
#     ro.title("Loading")
#     ro.geometry("350x300+300+300")
#     ro.iconbitmap("notebook.ico")
#     # ro.attributes("-fullscreen",True)
#     # ro.attributes('-transparentcolor','black')
#     # ro.state('zoomed')
#     Label(ro,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=22,y=100)
#     for i in range (13):
#         Label(ro,bg="#1F2732",width=2,height=1).place(x=(i+1)*22,y=150)
#         ro.update()
#         for i in range(3):
#             for j in range(13):
#                 Label(ro,bg="#FFBD09",width=2,height=1).place(x=(j+1)*22,y=150)
#                 sleep(0.06)
#                 ro.update_idletasks()
#                 Label(ro,bg="#1F2732",width=2,height=1).place(x=(j+1)*22,y=150)
#                 stop()
#         else:
#             ro.destroy()
#             ok()
#             break
#     ro.mainloop()

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[frame structure]

# def ok():

#     root = Tk()
#     root.geometry("350x300+300+300")
#     root.title("Notes")
#     root.iconbitmap("notebook.ico")

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[save function]

#     def save():
#         r=Tk()
#         r.geometry("210x70+300+300")
#         r.iconbitmap("notebook.ico")
#         r.title("Save")
#         Label(r, text="Save with the name .....",bg="#1F2732",fg="#FFBD09").grid(sticky=W, pady=4, padx=5)
#         r.config(bg="#1F2732")
#         def printIn():
#             desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
#             fi=filedialog.askdirectory(title="Where you want to save ?",initialdir=desktop)
#             j = jk.get(1.0, "end-1c") 
#             strDate = datetime.datetime.now().strftime("%d:%B:%y")
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             inp = area.get(1.0, "end-1c")
#             foo=open(f"{fi}/{j}.txt","w")
#             foo.write(f"Note of the  Date:- {strDate} \nwhile time was {strTime}")
#             foo.write("\n")
#             foo.write(inp)
#             foo.close()
#             messagebox.showinfo("Saved","your file is saved") 
#             r.destroy()
#             print(j)
#             # messagebox.showerror("Error","your file as not saved")
#             # messagebox.showwarning("Warning","your can't save the file ")
#         jk = Text(r,height=1,width=5,relief=RIDGE,bd=0)
#         jk.grid(row=1, column=0,padx=5,ipady=3, sticky=E+W+S+N)
#         hi=Button(r, text="Save",command=printIn,bg="#1F2732",fg="#FFBD09",borderwidth=2)
#         hi.grid(row=1, column=3)
#         def changex(event):
#             hi['bg']='#3e4042'
#         def returnx(event):
#             hi['bg']="#1F2732"
#         hi.bind('<Enter>',changex)
#         hi.bind('<Leave>',returnx)
#         r.mainloop() 

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[viewing function]

#     def printInput():
#         inp = area.get(1.0, "end-1c")
#         print(inp)
#         rt=Tk()
#         rt.title("View")
#         rt.iconbitmap("notebook.ico")
#         rt.config(bg="#1F2732")
#         rt.geometry("350x300+300+300")
#         Label(rt,text="The text you have wrote",bg="#1F2732",fg="#FFBD09", pady=15).grid(sticky=NW)
#         Label(rt,text=inp,bg="#1F2732",fg="white").grid(sticky=E+W+S+N)
#         rt.mainloop()

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[joing row and column]

#     root.config(bg="#1F2732")
#     root.columnconfigure(1, weight=1)
#     root.columnconfigure(3, pad=7)
#     root.rowconfigure(3, weight=1)
#     root.rowconfigure(5, pad=7)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[labeling the text]

#     lbl = Label(root,text="Don't forget to save before closing",bg="#1F2732",fg="#FFBD09")
#     lbl.grid(sticky=W, pady=4, padx=5)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[entery taking]

#     area = Text(root,bg='#3e4042',fg="white",relief=RIDGE,bd=0)
#     area.grid(row=1, column=0, columnspan=2, rowspan=4,padx=5, sticky=E+W+S+N)
#     inp = area.get(1.0, "end-1c") 

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[view button]

#     abtn = Button(root,text="view",command=printInput,bg="#1F2732",fg="#FFBD09",borderwidth=0)
#     abtn.grid(row=1, column=3,ipadx=2)
#     def changex(event):
#         abtn['bg']='#3e4042'
#     def returnx(event):
#         abtn['bg']="#1F2732"
#     abtn.bind('<Enter>',changex)
#     abtn.bind('<Leave>',returnx)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[colse button]

#     close=Button(root, text='  close  ', command=root.destroy,bg="#1F2732",fg="#FFBD09",bd=0,highlightthickness=0,borderwidth=0)
#     close.grid(row=2, column=3, pady=4)
#     def changex(event):
#         close['bg']='red'
#     def returnx(event):
#         close['bg']="#1F2732"
#     close.bind('<Enter>',changex)
#     close.bind('<Leave>',returnx)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[about button]

#     hbtn = Button(root,text="about",bg="#1F2732",fg="#FFBD09",borderwidth=0,command=aboutview)
#     hbtn.grid(row=5, column=0, padx=5,sticky=W)
#     def changex(event):
#         hbtn['bg']='#3e4042'
#     def returnx(event):
#         hbtn['bg']="#1F2732"
#     hbtn.bind('<Enter>',changex)
#     hbtn.bind('<Leave>',returnx)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[save button]

#     obtn = Button(root, text="Save",command=save,bg="#1F2732",fg="#FFBD09",borderwidth=0)
#     obtn.grid(row=5, column=3)
#     def changex(event):
#         obtn['bg']='#3e4042'
#     def returnx(event):
#         obtn['bg']="#1F2732"
#     obtn.bind('<Enter>',changex)
#     obtn.bind('<Leave>',returnx)

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[frame close]

#     root.mainloop()

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[about creator]
# def aboutview():
#     aro=Tk()
#     aro.config(bg="#1F2732")
#     #ro.config(bg="black")
#     aro.title("About")    
#     aro.iconbitmap("notebook.ico")
#     aro.geometry("350x300+300+300")
#     Label(aro,text="About me :-",font="Bahnschrift 19",bg="#1F2732",fg="#FFBD09").pack(anchor=NW)   
#     Label(aro,
#     text=
#     """my self bhuvnesh verma .
#     The application is created with the
#       help of python and tkinter 
#         hopefully you like it  .""",font="calibri 15",bg="#1F2732",fg="white").pack(anchor=NW)
#     closei=Button(aro, text='  close  ', command=aro.destroy,bg='#10121f',font=("calibri", 13),bd=0,fg='white',highlightthickness=0,pady=3)
#     closei.pack(padx=50,pady=50)
#     def changex(event):
#         closei['bg']='red'
#     def returnx(event):
#         closei['bg']='#10121f'
#     closei.bind('<Enter>',changex)
#     closei.bind('<Leave>',returnx)
#     aro.mainloop()

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[Runing the application]
# if __name__=="__main__":
#     nike()

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[The End.]















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[loading animation with some of the modifation]



















# from tkinter import *
# from time import sleep
# from tracemalloc import stop
# import jk
# class loadingsplash:
#     def play_animation(self):
#         for i in range(5):
#             for j in range(16):
#                 Label(self.root,bg="#FFBD09",width=2,height=1).place(x=(j+22)*22,y=350)
#                 sleep(0.06)
#                 self.root.update_idletasks()
#                 Label(self.root,bg="#1F2732",width=2,height=1).place(x=(j+22)*22,y=350)
#                 stop()
#         else:
#             self.root.destroy()
#             exit(0)

#     def __init__(self):
#         self.root=Tk()
#         self.root.config(bg="black")
#         self.root.title("custom  Loader")
#         self.root.attributes("-fullscreen",True)
#         self.root.attributes('-transparentcolor','black')
#         self.root.state('zoomed')
#         Label(self.root,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=490,y=320)
#         for i in range (16):
#             Label(self.root,bg="#1F2732",width=2,height=1).place(x=(i+22)*22,y=350)
#             self.root.update()
#             self.play_animation()
#         self.root.mainloop()


# if __name__=="__main__":
#     loadingsplash()   

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# from tkinter import *
# from time import sleep
# from tracemalloc import stop
# class loadingsplash:
#     def play_animation(self):
#         for i in range(5):
#             for j in range(16):
#                 Label(self.root,bg="#FFBD09",width=2,height=1).place(x=(j+22)*22,y=350)
#                 sleep(0.06)
#                 self.root.update_idletasks()
#                 Label(self.root,bg="#1F2732",width=2,height=1).place(x=(j+22)*22,y=350)
#                 stop()
#         else:
#             self.root.destroy()
#             exit(0)

#     def __init__(self):
#         self.root=Tk()
#         self.root.config(bg="black")
#         self.root.title("custom  Loader")
#         self.root.attributes("-fullscreen",True)
#         self.root.attributes('-transparentcolor','black')
#         self.root.state('zoomed')
#         Label(self.root,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=490,y=320)
#         for i in range (16):
#             Label(self.root,bg="#1F2732",width=2,height=1).place(x=(i+22)*22,y=350)
#             self.root.update()
#             self.play_animation()
#         self.root.mainloop()


# if __name__=="__main__":
#     loadingsplash() 


















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[text widget working]



















#import tkinter as tk

# # Top level window
# frame = tk.Tk()
# frame.title("TextBox Input")
# frame.geometry('400x200')
# # Function for getting Input
# # from textbox and printing it
# # at label widget

# def printInput():
# 	inp = inputtxt.get(1.0, "end-1c")
# 	print(inp)
# # 	lbl.config(text = "Provided Input: "+inp)

# # TextBox Creation
# inputtxt = tk.Text(frame,
# 				height = 2,
# 				width = 10)

# inputtxt.grid(row=1,column=1,sticky=tk.NW)

# # Button Creation
# printButton = tk.Button(frame,text = "Print", command = printInput)
# printButton.grid(row=1,column=2,sticky=tk.NE)

# # Label Creation
# lbl = tk.Label(frame, text = "")
# lbl.grid(row=2,column=1,sticky=tk.NW)
# frame.mainloop()





















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[clock analog type (project)]



















# import tkinter as ui

# import time
# import math

# window = ui.Tk()
# window.geometry("400x400")


# def update_clock():
#     hours = int(time.strftime("%I"))
#     minutes = int(time.strftime("%M"))
#     seconds = int(time.strftime("%S"))

#     # updating seconds hand
#     seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
#     seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
#     canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

#     # updating minutes hand
#     minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
#     minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
#     canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

#     # updating hours hand
#     hours_x = hours_hand_len * math.sin(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_x
#     hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_y
#     canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

#     window.after(1000, update_clock)


# canvas = ui.Canvas(window, width=400, height=400, bg="black")
# canvas.pack(expand=True, fill='both')

# # create background
# bg = ui.PhotoImage(file='dial_400.png')
# canvas.create_image(200, 200, image=bg)


# # create clock hands
# # seconds hand
# center_x = 200
# center_y = 200

# seconds_hand_len = 95
# minutes_hand_len = 80
# hours_hand_len = 60

# seconds_hand = canvas.create_line(200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill='red')
# # minutes hand
# minutes_hand = canvas.create_line(200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len, width=2, fill='white')
# # hours hand
# hours_hand = canvas.create_line(200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=4, fill='white')

# update_clock()

# window.mainloop()


















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[man walking gui animation]



















# from tkinter import*
# from PIL import Image,ImageTk,ImageSequence
# import time
# root=Tk()
# root.geometry("600x400")
# root.config(bg="white")
# # root.wm_attributes('-transparentcolor',root['bg'])
# def play_gif():
#     global img
#     img=Image.open("first.gif")
#     lbl=Label(root)
#     lbl.place(x=0,y=0)
#     for img in ImageSequence.Iterator(img):
#         img=img.resize((300,300))
#         img=ImageTk.PhotoImage(img)
#         lbl.config(image=img,borderwidth=0)
#         root.update()
#         time.sleep(0.01)
#     root.after(0,play_gif)
# def exit():
#     root.destroy()
# Button(root,text="play",command=play_gif).place(x=500,y=300)
# Button(root,text="exit",command=exit).place(x=450,y=300)
# root.mainloop()


















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[About frame but due to some error it can't be run in Note so i have to change it but it is still cool]




















# from tkinter import *
# def aboutview():
#     ro=Tk()
#     ro.config(bg="#1F2732")
#     #ro.config(bg="black")
#     ro.title("About")    
#     ro.iconbitmap("origami.ico")
#     ro.geometry("380x300+300+300")
#     background_image = PhotoImage(file='imgk.png')
#     Label(ro,image=background_image,fg="#FFBD09",bg="#1F2732",bd=0).pack(anchor=NW)
#     # ro.attributes("-fullscreen",True)
#     # ro.attributes('-transparentcolor','black')
#     # ro.state('zoomed')
#     # # Label(ro,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").pack()
#     Label(ro,text="About me :-",font="Bahnschrift 19",bg="#1F2732",fg="#FFBD09").pack(anchor=NW)   
#     Label(ro,
#     text=
#     """my self bhuvnesh verma .
#     The gui is created with the help
#     of python and tkinter 
#     hopefully you like it  .""",font="calibri 15",bg="#1F2732",fg="white").pack(anchor=NW)
#     close=Button(ro, text='  close  ', command=quit,bg='#10121f',font=("calibri", 13),bd=0,fg='white',highlightthickness=0,pady=3)
#     close.pack()
#     def changex(event):
#         close['bg']='red'
#     def returnx(event):
#         close['bg']='#10121f'
#     close.bind('<Enter>',changex)
#     close.bind('<Leave>',returnx)
#     ro.mainloop()
# aboutview()


















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[calcualator with img [button]]












# from tkinter import *
# root=Tk()
# root.geometry("275x460")
# root.minsize(275,460)
# root.maxsize(275,460)
# root.title("Calculator")
# root.config(bg="black")
# melabel = Label(root,text="",bg='black',fg='white',font=("Times",30,'bold'))
# melabel.pack(side=TOP)
# root.config(bg='Black')
# root.iconbitmap("icon.ico")

# textin=StringVar()
# operator=""

# def clickbut(number):  
#      global operator
#      operator=operator+str(number)
#      textin.set(operator)

# def equlbut():
#      global operator
#      add=str(eval(operator))
#      textin.set(add)
#      operator=''
# def equlbut():
#      global operator
#      sub=str(eval(operator))
#      textin.set(sub)
#      operator=''     
# def equlbut():
#      global operator
#      mul=str(eval(operator))
#      textin.set(mul)
#      operator=''
# def equlbut():
#      global operator
#      div=str(eval(operator))
#      textin.set(div)
#      operator=''    

# def clrbut():
#      textin.set('')

# def close():
#      root.destroy()   
# photo = PhotoImage(file="c.png")
# photo1 = PhotoImage(file="1.png")
# photo2 = PhotoImage(file="2.png")
# photo3 = PhotoImage(file="3.png")
# photo4 = PhotoImage(file="4.png")
# photo5 = PhotoImage(file="5.png")
# photo6 = PhotoImage(file="6.png")
# photo7 = PhotoImage(file="7.png")
# photo8 = PhotoImage(file="8.png")
# photo9 = PhotoImage(file="9.png")
# photo0 = PhotoImage(file="0.png")
# photodot= PhotoImage(file="dot.png")
# photoeq = PhotoImage(file="eq.png")
# photoadd = PhotoImage(file="ad.png")
# photosub = PhotoImage(file="su.png")
# photomul = PhotoImage(file="x.png")
# photodiv = PhotoImage(file="d.png")
# photoquit =PhotoImage(file="quit.png")

# metext=Entry(root,bg='black',fg='white',font=("Rome-B",28,'bold'),textvar=textin,borderwidth=0,justify=RIGHT)
# metext.pack()

# butt=Button(root,bg='black',command=close,image=photoquit,borderwidth=0)
# butt.place(x=75,y=100)

# but1=Button(root,bg='black',command=lambda:clickbut(7),image=photo7,borderwidth=0)
# but1.place(x=10,y=170)

# but4=Button(root,bg='black',command=lambda:clickbut(4),image=photo4,borderwidth=0)
# but4.place(x=10,y=240)

# but1=Button(root,bg='black',command=lambda:clickbut(1),image=photo1,borderwidth=0)
# but1.place(x=10,y=310)

# but8=Button(root,bg='black',command=lambda:clickbut(8),image=photo8,borderwidth=0)
# but8.place(x=75,y=170)

# but5=Button(root,bg='black',command=lambda:clickbut(5),image=photo5,borderwidth=0)
# but5.place(x=75,y=240)

# but2=Button(root,bg='black',command=lambda:clickbut(2),image=photo2,borderwidth=0)
# but2.place(x=75,y=310)

# but9=Button(root,bg='black',command=lambda:clickbut(9),image=photo9,borderwidth=0)
# but9.place(x=140,y=170)

# but6=Button(root,bg='black',command=lambda:clickbut(6),image=photo6,borderwidth=0)
# but6.place(x=140,y=240)

# but3=Button(root,bg='black',command=lambda:clickbut(3),image=photo3,borderwidth=0)
# but3.place(x=140,y=310)

# but0=Button(root,bg='black',command=lambda:clickbut(0),image=photo0,borderwidth=0)
# but0.place(x=10,y=380)

# butdot=Button(root,bg='black',command=lambda:clickbut("."),image=photodot,borderwidth=0)
# butdot.place(x=140,y=380)

# butdiv=Button(root,bg='black',command=lambda:clickbut("/"),image=photodiv,borderwidth=0)
# butdiv.place(x=205,y=100)

# butmul=Button(root,bg='black',command=lambda:clickbut("*"),image=photomul,borderwidth=0)
# butmul.place(x=205,y=170)

# butsub=Button(root,bg='black',command=lambda:clickbut("-"),image=photosub,borderwidth=0)
# butsub.place(x=205,y=240)

# butadd=Button(root,bg='black',command=lambda:clickbut("+"),image=photoadd,borderwidth=0)
# butadd.place(x=205,y=310)

# butclear=Button(root,image=photo,bg='black',command=clrbut,borderwidth=0)
# butclear.place(x=10,y=100)

# butequal=Button(root,bg='black',command=equlbut,image=photoeq,borderwidth=0)
# butequal.place(x=205,y=380)

# root.mainloop()










#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[speak the meaning of the word using python]










'''
[import modulce through pip install]
pip install PyDictionary
pip install pyttsx3 
'''
# import pyttsx3 
# from PyDictionary import PyDictionary


# class Speaking:

# 	def speak(self, audio):
	
# 		# Having the initial constructor of pyttsx3
# 		# and having the sapi5 in it as a parameter
# 		engine = pyttsx3.init('sapi5')
		
# 		# Calling the getter and setter of pyttsx3
# 		voices = engine.getProperty('voices')
		
# 		# Method for the speaking of the the assistant
# 		engine.setProperty('voice', voices[0].id)
# 		engine.say(audio)
# 		engine.runAndWait()


# class GFG:
# 	def Dictionary(self):
# 		speak = Speaking()
# 		dic = PyDictionary()
# 		speak.speak("Which word do u want to find the meaning sir")
		
# 		# Taking the string input
# 		query = str(input())
# 		word = dic.meaning(query)
# 		print(len(word))
		
# 		for state in word:
# 			print(word[state])
# 			speak.speak("the meaning is" + str(word[state]))
		
# 		word_in_hindi = dictionary.translate(query, "hi")    # Language Code for Hindi is hi
# 		word_in_serbian = dictionary.translate(query, "sr")  # Language Code for Serbian is sr
# 		word_in_french = dictionary.translate(query, "fi")   # Language Code for French fi

# 		print(query, " in hindi is => " + word_in_hindi)
# 		print(query, " in serbian is => " + word_in_serbian)
# 		print(query, " in French is => " + word_in_french)


# if __name__ == '__main__':
# 	GFG()
# 	GFG.Dictionary(self=None)
#[Translations from any language to any language in this list are supported. ]

# Afrikaans		af
# Albanian		sq
# Amharic		am
# Arabic		ar
# Armenian		hy
# Azerbaijani	az
# Basque		eu
# Belarusian	be
# Bengali		bn
# Bosnian		bs
# Bulgarian		bg
# Catalan		ca
# Cebuano		ceb 
# Chinese 		zh-CN or zh 	(Simplified)
# Chinese		zh-TW			(Traditional)
# Corsican		co
# Croatian		hr
# Czech			cs
# Danish		da
# Dutch			nl
# English		en
# Esperanto		eo
# Estonian		et
# Finnish		fi
# French		fr
# Frisian		fy
# Galician		gl
# Georgian		ka
# German		de
# Greek			el
# Gujarati		gu
# Haitian Creole	ht
# Hausa			ha
# Hawaiian		haw 
# Hebrew		he or iw
# Hindi			hi
# Hmong			hmn 
# Hungarian		hu
# Icelandic		is
# Igbo			ig
# Indonesian	id
# Irish			ga
# Italian		it
# Japanese		ja
# Javanese		jv
# Kannada		kn
# Kazakh		kk
# Khmer			km
# Kinyarwanda	rw
# Korean		ko
# Kurdish		ku
# Kyrgyz		ky
# Lao			lo
# Latvian		lv
# Lithuanian	lt
# Luxembourgish	lb
# Macedonian	mk
# Malagasy		mg
# Malay			ms
# Malayalam		ml
# Maltese		mt
# Maori			mi
# Marathi		mr
# Mongolian		mn
# Myanmar 		my	(Burmese)
# Nepali		ne
# Norwegian		no
# Nyanja 		ny	(Chichewa)
# Odia 		    or	(Oriya)
# Pashto		ps
# Persian		fa
# Polish		pl
# Portuguese 	pt	(Portugal, Brazil)
# Punjabi		pa
# Romanian		ro
# Russian		ru
# Samoan		sm
# Scots Gaelic	gd
# Serbian		sr
# Sesotho		st
# Shona			sn
# Sindhi		sd
# Sinhala 		si	(Sinhalese)
# Slovak		sk
# Slovenian		sl
# Somali		so
# Spanish		es
# Sundanese		su
# Swahili		sw
# Swedish		sv
# Tagalog		tl 	(Filipino)
# Tajik			tg
# Tamil			ta
# Tatar			tt
# Telugu		te
# Thai			th
# Turkish		tr
# Turkmen		tk
# Ukrainian		uk
# Urdu			ur
# Uyghur		ug
# Uzbek			uz
# Vietnamese	vi
# Welsh			cy
# Xhosa			xh
# Yiddish		yi
# Yoruba		yo
# Zulu			zu










# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[Convert Text to Speech in Python]










# # Import the required module for text
# # to speech conversion

# # '''pip install gTTS'''
# from gtts import gTTS

# # This module is imported so that we can
# # play the converted audio
# import os

# # The text that you want to convert to audio
# mytext = 'hi my self Bhuvnesh verma!'

# # Language in which you want to convert
# language = 'hi'

# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)

# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("welcome.mp3")

# # Playing the converted file
# os.system("welcome.mp3")










#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[message box icon's]










# from tkinter import messagebox 
# messagebox.showinfo(title='Message Box', message='Error message', icon='error')
# messagebox.showinfo(title='Message Box', message='Info message', icon='info')
# messagebox.showinfo(title='Message Box', message='Question message', icon='question')
# messagebox.showinfo(title='Message Box', message='Warning message', icon='warning')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[code of msg]
# from logging import root
# from tkinter import *
# from tkinter import messagebox as msg
# root=Tk()
# root.geometry("500x200")
# root.iconbitmap("origami.ico")
# labeltoop=Label(root,text="plase enter your name")
# labeltoop.grid(row=1,column=1)
# jk=StringVar
# jl=StringVar
# ent=Entry(root,textvariable=jk)
# ent.grid(row=1,column=2)
# labeltp=Label(root,text="plase enter your roll no.")
# labeltp.grid(row=2,column=1)
# ent1=Entry(root,textvariable=jl)
# ent1.grid(row=2,column=2)
# labeltop=Label(root,text="according to user's given infomation it is ....")
# labeltop.grid(row=3,column=1)
# def show_msg():
#     str1="o"
#     str2="l"
#     m1="This is OK Mr {0} \n You Roll No id: {1}".format(str1,str2)
#     my_var=msg.askyesnocancel('Title Here', m1)
#     print(my_var)
#     if my_var==True:
#         labeltop.config(text=str("all the detials are correct"))
#         Button(root,text="    close    ",command=root.destroy).grid(row=5,column=1)
#     elif my_var==False:
#         labeltop.config(text=str(" detials are not  correct"))
#     else:
#         labeltop.config(text=str("mistake")) 
# Button(root,text="ok show",command=show_msg).grid(row=5,column=1)
# root.mainloop()
'''
ASKYESNO
ASKRETRYCANCEL
ASKYESNOCANCEL
messagebox.askretrycancel("Title Here ","Your idea")
messagebox.askyesnocancel("Title Here ","Your choice",default='cancel')
messagebox.askyesnocancel('Title Here', "ok")

messagebox.showinfo("Saved","your file is saved")
messagebox.showerror("Error","your file as not saved")
messagebox.showwarning("Warning","your can't save the file ")

messagebox.showinfo(title='Message Box', message='Error message', icon='error')
messagebox.showinfo(title='Message Box', message='Info message', icon='info')
messagebox.showinfo(title='Message Box', message='Question message', icon='question')
messagebox.showinfo(title='Message Box', message='Warning message', icon='warning')
'''












#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>









#<><><><><><><><><><><><><><><><><><><><><>












#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>









#<><><><><><><><><><><><><><><><><><><><><>












#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>









#<><><><><><><><><><><><><><><><><><><><><>












#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>









#<><><><><><><><><><><><><><><><><><><><><>












#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>









#<><><><><><><><><><><><><><><><><><><><><>












#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[loading frame in tkinter of geometery 350x300]












# from tkinter import *
# from time import sleep
# from tracemalloc import stop
# class loadingsplash:
#     def play_animation(self):
#         for i in range(3):
#             for j in range(13):
#                 Label(self.root,bg="#FFBD09",width=2,height=1).place(x=(j+1)*22,y=150)
#                 sleep(0.06)
#                 self.root.update_idletasks()
#                 Label(self.root,bg="#1F2732",width=2,height=1).place(x=(j+1)*22,y=150)
#                 stop()
#         else:
#             self.root.destroy()
#             break

#     def __init__(self):
#         self.root=Tk()
#         self.root.config(bg="black")
#         self.root.title("custom  Loader")
#       #   self.root.attributes("-fullscreen",True)
#       #   self.root.attributes('-transparentcolor','black')
#       #   self.root.state('zoomed')
#         self.root.geometry("350x300+300+300")
#         Label(self.root,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=22,y=100)
#         for i in range (13):
#             Label(self.root,bg="#1F2732",width=2,height=1).place(x=(i+1)*22,y=150)
#             self.root.update()
#             self.play_animation()
#         self.root.mainloop()


# if __name__=="__main__":
#     loadingsplash()       















#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>









#<><><><><><><><><><><><><><><><><><><><><>












#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>










#<><><><><><><><><><><><><><><><><><><><><>












#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[Iron man code MOST IMPORTANT CODE]
'''
   ***********     ***         ********   **            **   ********   ****    *******                                                                                                                                                                                                                                                                                                    
        **        ** **        **    **    **          **       **       **    ***                                                                                                                                                                                                                                                
        **       **   **       **  **       **        **        **            ***                                                                                                                                                                                                                                                                 
  **    **      *********      ******        **      **         **              ***                                                                                                                                                                                                                                                                                            
   **   **     **       **     **   **        **    **          **                ***                                                                                                                                                                                                                                                                
   **   **    **         **    **    **        **  **           **                  **                                                                                                                                                                                                                                                        
   *******   **           **   **     **        ****         ********          ********  
'''  
"""
! both speak and write +button function in one gui 



"""









# import pyttsx3
# '''pip install pyttsx3'''
# import speech_recognition as sr
# '''pip install speechRecognition'''
# import datetime
# import wikipedia 
# '''pip install wikipedia'''
# import webbrowser 
# '''pip install pycopy-webbrowser'''
# import os 
# '''pip install os-sys'''
# import smtplib 
# ''' pip install secure-smtplib'''
# import random 
# '''pip install random2'''
# import psutil
# '''pip install psutil'''
# import subprocess 
# '''pip install subprocess.run'''
# from playsound import playsound 
# '''pip install playsound'''
# import vlc 
# '''pip install python-vlc'''
# import time
# from googlesearch import search
# '''pip install googlesearch-python'''
# from pygame import mixer 
# ''' Load the popular external library'''




# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voice', voices[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# '''def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")

#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")   

#     else:
#         speak("Good Evening!")  

#     speak("I am Jarvis . ready to run protocol ,checking the processer speed , launching the project alpha , code name #495ai#run.")       
# '''
# def wishMe():
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#     playsound("C:\\Users\\bhuvnesh verma\\Desktop\\study\\python\\ok\\Iron man\\power up.mp3") 
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#     speak('awaking system protocols')
#     speak('checking network protocols') 
#     speak('getting system information , cpu usage..')
#     info = get_sysinfo()
#     hi()
#     for i in info:
#         speak(i)
#     speak('system is in optimal condition')
#     hu = int(datetime.datetime.now().hour)
#     if(hu > 0 and hu < 12):
#         speak('Good Morning sir!')
#     elif(hu > 12 and hu < 18):
#         speak('Good Afternoon sir!')
#     else:
#         speak('Good evening sir!')
#     speak('i am your personal Assistant, Jarvis ,  launching the project alpha ')
#     speak('How can i help you sir?')

# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")  
#         return "None"
#     return query

# def get_sysinfo():#used to get the system cpu usage
#     info = []
#     cpufreq = psutil.cpu_freq()
#     info.append(f"Current Frequency of the CPU is: {cpufreq.current:.2f} Megahertz")
#     info.append("CPU Usage Per Core:")
#     for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
#         info.append(f"Core {i}: {percentage}%")
#     info.append(f"Total CPU Usage: {psutil.cpu_percent()}%")
#     return info


# def hi():
#         strTime = datetime.datetime.now().strftime("%H:%M:%S")  
#         strDate = datetime.datetime.now().strftime("%d:%B:%y") 
#         speak(f"the time is {strTime}" )
#         speak(f" And todays date is {strDate}")

# if __name__ == "__main__":
#     wishMe()                   
#     while True:
#     # if 1:
#         query = takeCommand().lower()

#         # Logic for executing tasks based on query
#         if 'wikipedia' in query:
#             speak('analysing your command..')
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia", "")
#             try :
#                 results = wikipedia.summary(query, sentences=2)
#                 speak("According to Wikipedia")
#                 print(results)
#                 speak(results)
#             except:
#                 speak('not found in wikipedia , searching on google')
#                 speak('these are the results found on google')

#         elif 'open youtube' in query:
#             webbrowser.open("youtube.com")
#             speak("opening youtube")

#         elif 'open google' in query:
#             webbrowser.open("google.com")
#             speak("opening google")

#         elif 'open stackoverflow' in query:
#             webbrowser.open("stackoverflow.com")  
            
 
#         elif 'song' in query:

#             mixer.init()
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>            
#             mixer.music.load("C:\\Users\\bhuvnesh verma\\Desktop\\study\\python\\ok\\Iron man\\Excuses.mp3")
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#             mixer.music.play()
#             while mixer.music.get_busy():  # wait for music to finish playing
#                     time.sleep(1)
#         elif 'play music' in query:
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>           
#             music_dir = 'E:\\bhuvnesh verma\\song\\song'
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#             songs = os.listdir(music_dir)
#             print(songs)    
#             os.startfile(os.path.join(music_dir, (songs[10])))

#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")    
#             speak(f"Sir, the time is {strTime}")

#         elif 'open code' in query:
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>            
#             codePath = "C:\\Users\\bhuvnesh verma\\Desktop\\study\\python\\ok\\ironman.py"
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#             os.startfile(codePath)
        

#         elif ('hey jarvis' in query):
#             speak('Yes sir i am here , Tell me how i can help you ')
           
#         elif ('wake up jarvis' in query):
#             hu = int(datetime.datetime.now().hour)
#             if(hu > 0 and hu < 12):
#                 speak('Good Morning sir!')
#             elif(hu > 12 and hu < 18):
#                 speak('Good Afternoon sir!')
#             else:
#                 speak('Good evening sir!')
#             speak(" Ready for  work ")

#         elif ('do you know tamil' in query):
#             speak('enaku tamil theriyathu')
     
#         elif ('open notepad' in query) or ('start notepad' in query):   
#             speak('opening notepad')
#             os.startfile('C:\\Windows\\system32\\notepad.exe')
     
#         elif ('close notepad' in query) or ( 'exit notepad' in query):        
#             speak('terminating notepad')
#             subprocess.call(['taskkill','/F','/IM','notepad.exe']) 


#         elif ("ok jarvis search for"in query):
#             query = query.replace("ok jarvis search for", "")
#             for j in search(query, tld="co.in", num=10, stop=10, pause=2):
#                     print(j)
#                     speak(j)
           
       
#         elif ('open paint' in query) or ('open mspaint' in query) or ('start paint' in query):        
#             speak('opening microsoft paint')
#             os.startfile('C:\\Windows\\system32\\mspaint.exe')
        
      
#         elif ('close paint' in query) or ('terminate paint' in query) or ('exit paint' in query):        
#             speak('terminating microsoft paint') 
#             subprocess.call(['taskkill','/F','/IM','mspaint.exe'])

#         elif ('jarvis stop' in query) or (' jarvis terminate ' in query) or ('close' in query):        
#             speak('terminating sir') 
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>            
#             os.system("C:\\Users\\bhuvnesh verma\\Desktop\\study\\python\\ok\\Iron man\\powerdown.mp3")
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# #            subprocess.call(['taskkill','/F','/IM','ironman.exe'])










