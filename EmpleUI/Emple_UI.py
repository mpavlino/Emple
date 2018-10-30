from tkinter import *
from tkinter.font import Font
from PIL import Image

def raise_frame(frame):
    frame.tkraise()

root = Tk()
text = Text(root)

myFont = Font(family="Century Gothic", size=18)
text.configure(font=myFont)

catFont = Font(family="Century Gothic", size=16, weight = "bold")
infoFont = Font(family="Century Gothic", size=16, slant = "italic")

food_text = '#%02x%02x%02x' % (175, 76, 89)
bar_color = '#%02x%02x%02x' % (216, 165, 137)

f1 = Frame(root, height="800", width="480", bg="bisque")
f2 = Frame(root, height="800", width="480", bg="white")
f3 = Frame(root, height="800", width="480", bg="white")
f4 = Frame(root, height="800", width="480", bg="white")
f5 = Frame(root, height="800", width="480", bg="bisque")
f6 = Frame(root, height="800", width="480", bg="white")

for frame in (f1, f2, f3, f4, f5, f6):
    frame.grid(row=0, column=0, sticky='news')


##########################################################################################################

#FRAME 1

#drink button
drbutton=PhotoImage(file='button_order.png')
a=Button(f1,image=drbutton,bg='white',borderwidth=0,highlightthickness=0,compound=CENTER,command=lambda:raise_frame(f2))
a['border']='0'
a.grid(row=1, column = 1, columnspan=2, sticky="nsew")

#food button
fdbutton=PhotoImage(file='food_button.png')
b=Button(f1,image=fdbutton,bg='white',borderwidth=0,highlightthickness=0,command=lambda:raise_frame(f3))
b['border']='0'
b.grid(row=2, column = 1, columnspan=2, sticky="nsew")

#call waiter button
wtbutton=PhotoImage(file='waiter_button.png')
c=Button(f1,image=wtbutton,bg='white',borderwidth=0,highlightthickness=0,command=lambda:raise_frame(f4))
c['border']='0'
c.grid(row=3, column = 1, columnspan=2, sticky="nsew")

#progress button
prbutton=PhotoImage(file='progress_button.png')
d=Button(f1,image=prbutton,bg='white',borderwidth=0,highlightthickness=0)
d['width']='105'
d['border']='0'
d.grid(row=4, column = 0, columnspan=2, sticky="nsew")


#info button
inbutton=PhotoImage(file='info_button.png')
e=Button(f1,image=inbutton,bg='white',borderwidth=0,highlightthickness=0,command=lambda:raise_frame(f5))
e['width']='105'
e['border']='0'
e.grid(row=4, column = 2, columnspan=2, sticky="nsew")


###################################################################################################################

#FRAME 2

C = Canvas(f2, height=800, width=480)
filename = PhotoImage(file = "coffe_table2.png")
background_label = Label(f2, image=filename, compound=CENTER)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#Status bar
status_label = Label(f2, text = "Choose a category", fg = "white", font = myFont, bg = bar_color, compound=LEFT)
status_label['width'] = '34'
status_label['height'] = '2'
label_button_window = C.create_window(0, 0, anchor='nw', window=status_label)

#Back button
bckbutton2_f2 = PhotoImage(file = "back_button2.png")
bck_f2 = Button(f2, image = bckbutton2_f2, compound=LEFT, borderwidth=0, highlightthickness=0, border=0, command=lambda:raise_frame(f1))
bck_button_window_f2 = C.create_window(4, 4, anchor='nw', window=bck_f2)

#Hot drinks
#status_label = Label(f2, text = "Hot drinks", fg = bar_color, font = "Arial 16", bg = "grey", compound=LEFT)
#status_label['width'] = '40'
#status_label['height'] = '2'
#label_button_window = C.create_window(0, 62, anchor='nw', window=status_label)

#Hot drinks
hdrinks=PhotoImage(file='Hot_drinkss.png')
hot_drinks=Button(f2,image = hdrinks, text = "Hot drinks", fg = bar_color, font = catFont, compound=CENTER, command=lambda:raise_frame(f6))
hot_drinks['border']='0'
hot_drinks_window = C.create_window(0, 62, anchor='nw', window=hot_drinks)

#Soft drinks
sdrinks=PhotoImage(file='Soft_drinks.png')
soft_drinks=Button(f2,image = sdrinks, text = "Soft drinks", fg = bar_color, font = catFont, compound=CENTER, command=lambda:raise_frame(f6))
soft_drinks['border']='0'
soft_drinks_window = C.create_window(0, 148, anchor='nw', window=soft_drinks)

#Beer
bdrinks=PhotoImage(file='beer.png')
beer_drinks=Button(f2,image = bdrinks, text = "Beer", fg = bar_color, font = catFont, compound=CENTER, command=lambda:raise_frame(f6))
beer_drinks['border']='0'
beer_drinks_window = C.create_window(0, 234, anchor='nw', window=beer_drinks)

#Alcohol drinks
aldrinks=PhotoImage(file='Alcohol_drinks.png')
alcohol_drinks=Button(f2,image = aldrinks, text = "Alcohol drinks", fg = bar_color, font = catFont, compound=CENTER, command=lambda:raise_frame(f6))
alcohol_drinks['border']='0'
alcohol_drinks_window = C.create_window(0, 320, anchor='nw', window=alcohol_drinks)

#Wine
wdrinks=PhotoImage(file='wine.png')
wine_drinks=Button(f2,image = wdrinks, text = "Wine", fg = bar_color, font = catFont, compound=CENTER, command=lambda:raise_frame(f4))
wine_drinks['border']='0'
wine_drinks_window = C.create_window(0, 406, anchor='nw', window=wine_drinks)

C.grid()

#######################################################################################################################################################


#FRAME 3

C3 = Canvas(f3, height=800, width=480)
filename_f3 = PhotoImage(file = "food_background.png")
background_label_f3 = Label(f3, image=filename_f3, compound=CENTER)
background_label_f3.place(x=0, y=0, relwidth=1, relheight=1)


#Status bar
status_label_f3 = Label(f3, text = "Choose a category", fg = "white", font = myFont, bg = food_text, compound=LEFT)
status_label_f3['width'] = '34'
status_label_f3['height'] = '2'
label_button_window_f3 = C3.create_window(0, 0, anchor='nw', window=status_label_f3)


#Back button
bckbutton2_f3 = PhotoImage(file = "back_button3.png")
bck_f3 = Button(f3, image = bckbutton2_f3, compound=LEFT, borderwidth=0, highlightthickness=0, border=0, command=lambda:raise_frame(f1))
bck_button_window_f3 = C3.create_window(4, 4, anchor='nw', window=bck_f3)

#Pizza
pizza_f3 = PhotoImage(file = "pizza.png")
pizza_food=Button(f3,image = pizza_f3, text = "Pizza", fg = food_text, font = catFont, compound=CENTER, command=lambda:raise_frame(f6))
pizza_food['border']='0'
pizza_food_window = C3.create_window(0, 62, anchor='nw', window=pizza_food)


#Pasta
pasta_f3 = PhotoImage(file = "pasta.png")
pasta_food=Button(f3,image = pasta_f3, text = "Pasta", fg = food_text, font = catFont, compound=CENTER, command=lambda:raise_frame(f6))
pasta_food['border']='0'
pasta_food_window = C3.create_window(0, 148, anchor='nw', window=pasta_food)

#Salad
salad_f3 = PhotoImage(file = "salad.png")
salad_food=Button(f3,image = salad_f3, text = "Salad", fg = food_text, font = catFont, compound=CENTER, command=lambda:raise_frame(f6))
salad_food['border']='0'
salad_food_window = C3.create_window(0, 234, anchor='nw', window=salad_food)

#Soups
soups_f3 = PhotoImage(file = "soups.png")
soups_food=Button(f3,image = soups_f3, text = "Soups", fg = food_text, font = catFont, compound=CENTER, command=lambda:raise_frame(f6))
soups_food['border']='0'
soups_food_window = C3.create_window(0, 320, anchor='nw', window=soups_food)

#Desserts
deserts_f3 = PhotoImage(file = "Deserts.png")
desserts_food=Button(f3,image = deserts_f3, text = "Desserts", fg = food_text, font = catFont, compound=CENTER, command=lambda:raise_frame(f6))
desserts_food['border']='0'
desserts_food_window = C3.create_window(0, 406, anchor='nw', window=desserts_food)

#Grilled
grilled_f3 = PhotoImage(file = "grilled.png")
grilled_food=Button(f3,image = grilled_f3, text = "Grilled", fg = food_text, font = catFont, compound=CENTER, command=lambda:raise_frame(f6))
grilled_food['border']='0'
grilled_food_window = C3.create_window(0, 492, anchor='nw', window=grilled_food)

C3.grid()

#################################################################################################################################3


#FRAME 4

C4 = Canvas(f4, height=800, width=480)
filename_f4 = PhotoImage(file = "menu_background_tran.png")
background_label_f4 = Label(f4, image=filename_f4, compound=CENTER)
background_label_f4.place(x=0, y=0, relwidth=1, relheight=1)


#Status bar
#status_label_f4 = Label(f4, text = "Choose a category", bg = bar_color, compound=RIGHT)
#status_label_f4['width'] = '36'
#status_label_f4['height'] = '2'
#label_button_window_f4 = C4.create_window(0, 0, anchor='nw', window=status_label_f4)


#Bell button
bellimg = PhotoImage(file = "button_bell.png")
bll_f4 = Button(f4, image = bellimg, compound=CENTER, borderwidth=0, highlightthickness=0, border=0, command=lambda:raise_frame(f6))
bll_button_window_f4 = C4.create_window(135, 280, anchor='nw', window=bll_f4)

C4.grid()

###########################################################################################################


#FRAME 5

C5 = Canvas(f5, height=800, width=480)
background_label = Label(f5, bg="bisque", compound=CENTER)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#Status bar
status_label_f5 = Label(f5, text = "About us", fg = "white", font = myFont, bg = bar_color, compound=CENTER)
status_label_f5['width'] = '33'
status_label_f5['height'] = '2'
label_button_window_f5 = C5.create_window(0, 0, anchor='nw', window=status_label_f5)

emple_photo = PhotoImage(file = "emple_team.png")
emple_team = Label(f5, bg = "bisque", image = emple_photo, compound = CENTER)
emple_team['height'] = '1'
emple_team.place(x=1, y=120, relwidth=1, relheight=1)

#Text label
T = Text(f5, height = 5, width = 40, bg = "bisque", fg = food_text, font = infoFont, borderwidth=0)
text_button_window_f5 = C5.create_window(45, 150, anchor='nw', window=T)
T.insert(END, "Emple is Croatian startup from Zagreb.\nThree ambitious young men have\nfounded it, and they are going to take\nStartup factory money prize! :)")

#Back button
bckbutton2 = PhotoImage(file = "back_button2.png")
bck_f5 = Button(f5, image = bckbutton2, compound=LEFT, borderwidth=0, highlightthickness=0, border=0, command=lambda:raise_frame(f1))
bck_button_window_f5 = C5.create_window(4, 4, anchor='nw', window=bck_f5)


C5.grid()


#################################################################################################################################################

#FRAME 6

C6 = Canvas(f6, height=800, width=480)
filename_f6 = PhotoImage(file = "menu_background_tran.png")
background_label_f6 = Label(f6, image=filename_f6, compound=CENTER)
background_label_f6.place(x=0, y=0, relwidth=1, relheight=1)

#Waiter button
waiterimg = PhotoImage(file = "button_waiter.png")
wtr_f6 = Button(f6, image = waiterimg, compound=CENTER, borderwidth=0, highlightthickness=0, border=0) 
wtr_button_window_f6 = C6.create_window(135, 280, anchor='nw', window=wtr_f6)


C6.grid()


raise_frame(f1)
root.mainloop()
