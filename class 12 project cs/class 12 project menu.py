import tkinter as tk
import tkinter.font as tkfont
import pickle
import copy
import csv
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import simpledialog
#setting up the window
screen=tk.Tk()
screen.title("MENU BASED PROGRAM")
screen.geometry("1536x864")
#screen.attributes("-fullscreen",True)
bg_label = tk.Label(screen)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()
itemindex=[]
dummyindex=[]
for i in range(0,55):
    itemindex.append(0)
    dummyindex.append(0)
#file handling
fdata=[]
#targe note
def bug(a,b=None):
    i=0     #CONTROLL DEBUG PRINTING
    if i==1:
        print(a,b)
'''pip install Pillow'''
'''py -3.10 -m pip install Pillow'''
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
print(screen_width,screen_height)


#BACKSTAGE
button=[]
selected=False
level="h"
REMBUTTON=[]
items = ["Paneer Tikka", "Veg Samosa","Aloo Tikki Chaat","Chicken Seekh Kebab","Fish Amritsari","Tandoori Chicken Wings","Masala Papad","Garlic Bread","Spring Rolls","Nachos","Chicken Satay","Mini Prawn Tempura","BBQ Chicken Wings","Hummus","Butter Chicken", "Paneer Butter Masala", "Dal Tadka", "Rogan Josh", "Chole Bhature", "Veg Biryani", "Chicken Biryani", "Malai Kofta", "Palak Paneer", "Mutton Curry","Grilled Salmon", "Spaghetti Aglio e Olio", "Chicken Alfredo Pasta", "Margherita Pizza", "Beef Steak with Mashed Potatoes", "Vegetable Lasagna", "Teriyaki Chicken with Steamed Rice", "Falafel Wrap with Tahini Sauce", "Thai Green Curry with Jasmine Rice", "BBQ Ribs with Coleslaw","Molten Chocolate Lava Cake","cake", "Cheesecake", "Tiramisu", "Crème Brûlée", "Gulab Jamun", "Brownie Sundae", "Fruit Tart", "Panna Cotta", "Churros & Chocolate Dip", "Ice Cream Float","Masala Chai", "Lassi", "Filter Coffee", "Rose Sharbat", "Cappuccino", "Latte", "Lemon Iced Tea", "Orange Juice", "Smoothie", "Soft Drinks"]
price=[100,80,60,100,110,140,40,104,168,200.4,288,264.3,400.9,296.2,200,210,150,170,150,200,300,100,150,250,116.8,840,1536,784,1216.2,1656.5,2024,1328.1,920.9,1960.7,100,100,150,200,200,50,80,110,150,110,80,50,50,60,50,100,100,60,50,100,70]
layer=0
sb=tk.Scrollbar(screen,orient=tk.VERTICAL)
order=tk.Listbox(screen,yscrollcommand=sb.set,font=("Bahnschrift Condensed",20))
sb.config(command=order.yview)
sb2=tk.Scrollbar(screen,orient=tk.VERTICAL)
blistbox=tk.Listbox(screen,yscrollcommand=sb2.set,font=("Bahnschrift Condensed",20))
sb2.config(command=blistbox.yview)
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()

#image processing
bg_paths = ["h.png", "c.png", "st.png","d.png","mi.png","mo.png","b.png","f.png"]
preloaded_images = {}
for path in bg_paths:
    img = Image.open(path)
    img = img.resize((screen_width, screen_height), Image.LANCZOS)
    preloaded_images[path] = ImageTk.PhotoImage(img)

#LABEL/ENTRY
pricetag=tk.Label(screen,text="0",width=30,height=2,bg="sky blue",font=("Bahnschrift Condensed",20,"bold")) 
pricetag.lift()
view=tk.Label(screen,text="View::",width=7,height=2,bg="sky blue",font=("Bahnschrift Condensed",20,"bold"))
view.lift()
listname=tk.Label(screen,text="ORDER LIST",width=10,height=2,bg="sky blue",font=("Bahnschrift Condensed",20,"bold"))
listname.lift()
orderr=tk.Label(screen,text="ORDER",width=10,height=2,bg="sky blue",font=("Bahnschrift Condensed",20,"bold"))
orderr.lift()
dell=tk.Label(screen,text="delete::",width=7,height=2,bg="sky blue",font=("Bahnschrift Condensed",20,"bold"))
dell.lift()
evn=tk.Entry(screen,width=10,fg="grey",font=("Bahnschrift Condensed",15,"bold"))
evn.lift()
edn=tk.Entry(screen,width=10,fg="grey",font=("Bahnschrift Condensed",15,"bold"))
edn.lift()
namefeed=tk.Entry(screen,width=15,fg="black",font=("Bahnschrift Condensed",15,"bold"))
namefeed.lift()
commentfeed=tk.Text(screen,width=50,height=10,fg="black",font=("Bahnschrift Condensed",15,"bold"))
commentfeed.lift()
feedback=tk.Text(screen,width=100,height=22,fg="black",font=("Bahnschrift Condensed",15,"bold"))
feedback.lift()
feedback.config(state="disabled")
rate=tk.Scale(screen,from_=1, to=5, orient="horizontal")
placeholder = "enter bill no..."
evn.insert(0, placeholder)
edn.insert(0, placeholder)
#<<<FUNCTION SPACE>>>>
def updatefeed():
    global feedback
    feedback.config(state="normal")
    feedback.delete('1.0',tk.END)
    with open("feedback.csv","r",newline='') as feed:
        reader=csv.reader(feed)
        for i in reader:
            sht = (
            f"NAME   : {i[0]}\n"
            f"RATED  : {i[1]}\n"
            f"COMMENT: {i[2]}\n"
            f"{'='*60}\n")
            feedback.insert(tk.END,sht)
    feedback.config(state="disabled")
def submitit():
    name=namefeed.get()
    rating=rate.get()
    comment=commentfeed.get("1.0",tk.END)
    namefeed.delete(0,tk.END)
    rate.set(1)
    commentfeed.delete('1.0',tk.END)
    if str(name)=="" or str(comment)=="":
        messagebox.showinfo("ERROR","please fill all details...")
    else :
        with open("feedback.csv",mode="a",newline='') as form:
            writer=csv.writer(form)
            l:list[str,int,str]=name,rating,comment
            writer.writerow(l)
            messagebox.showinfo("SUCCESS","feedback submitted!!,thanks for your review!!")
    updatefeed()
def onit():
    global selected
    if selected:
        price: int=sumup()
        ans=simpledialog.askstring(f'PAYMENT',f'AMOUNT,{price},NOTE:extra amount is taken as TIP')
        if ans:
            try:
                if float(ans)==price:
                    messagebox.showinfo("WAITER:THANK YOU","payment done")
                elif float(ans)>price:
                    messagebox.showinfo("WAITER:THANK YOU VERY MUCH!!","payment done,tip added")
                else:
                    messagebox.showwarning("ERROR","unsufficient amount please retry")
            except (TypeError,ValueError):
                    messagebox.showerror("ERROR","PLEASE STOP MESSING AROUND , enter appropriate input")
        else:
            messagebox.showinfo("CANCELLED","PAYMENT CANCELLED")
    else:
        messagebox.showinfo("FAILED","please select an order")
def snoit(a,event=None):
    global order,sb,pricetag,itemindex,fdata,evn,blistbox,selected
    f=open("bills.dat","rb")
    l=pickle.load(open("bills.dat","rb"))
    f.close()
    if l!=[]:
        if a==1:
            try:
                billhist()
                n=int(evn.get())
                if n>0 and (n-1)>=0:
                    itemindex=fdata[(n-1)].copy()
                    selected=True
                    orderit()
                    orderr.place(x=1200,y=100)
                    order.place(x=1000,y=200,width=500,height=600)
                    ordernow.place(x=610,y=800)
                    sb.place(x=1500,y=200,width=20,height=600)
                    pricetag.place(x=1100,y=800)
                    order.lift()
                    sb.lift()
                    pricetag.lift()
                else:
                    messagebox.showerror("ERROR","please enter appropriate bill no")
            except :
                messagebox.showerror("ERROR","please enter appropriate bill no")
        elif a==2:
            orderr.place_forget()
            order.place_forget()
            ordernow.place_forget()
            selected=False
            sb.place_forget()
            pricetag.place_forget()
            try:
                n=int(edn.get())
                if n>0:
                    with open("bills.dat",mode="ab+") as f:
                        f.seek(0)
                        l=pickle.load(f)
                        l.pop((n-1))
                    with open("bills.dat",mode="wb") as f:
                        pickle.dump(l,f)
                    billhist()
                else:
                    messagebox.showerror("ERROR","please enter appropriate bill no")
            except (ValueError,IndexError):
                messagebox.showerror("ERROR","please enter appropriate bill no")
    else:
        messagebox.showerror("ERROR","NO BILL SAVED")
def on_click(a,event=None):
    if a==1:
        if evn.get() == placeholder:
            evn.delete(0, tk.END)
            evn.config(fg="black")
    elif a==2:
        if edn.get() == placeholder:
            edn.delete(0, tk.END)
            edn.config(fg="black")
def on_leave(a,event=None):
    if a==1:
        if evn.get() == "":
            evn.insert(0, placeholder)
            evn.config(fg="grey")
    elif a==2:
        if edn.get() == "":
            edn.insert(0, placeholder)
            edn.config(fg="grey")
def billadd(f):
    with open("bills.dat",mode="rb") as fbill:
        try:
            l=pickle.load(fbill)
            l.append(f)
        except EOFError:
            l=[]
            l.append(f)
    with open("bills.dat",mode="wb") as fbill:
        pickle.dump(l,fbill)
def billhist():
    global fdata,blistbox
    blistbox.delete(0,tk.END)
    fdata=[]
    with open("bills.dat",mode="rb") as fbill:
        try:
            l=pickle.load(fbill)
            count=1
            if l!=[]:
                for i in l:
                    name=i.pop()
                    name=str(count)+". "+name
                    blistbox.insert(tk.END,name)
                    fdata.append(i)
                    count+=1
            else:
                blistbox.insert(0,"no bill saved")
        except EOFError:
            blistbox.insert(0,"no bill saved")
def sumup():
    global itemindex,price,pricetag
    sum: int=0
    for n,i in enumerate(itemindex):
        sum+=(price[n]*i)
    sum=round(sum)
    tag: str="₹"+str(sum)
    pricetag.config(text=tag)
    return sum
def bgloader(path):
    global bg_image, bg_label
    if path in preloaded_images:
        bg_image = preloaded_images[path]
        bg_label.config(image=bg_image)
        bg_label.lower()
def orderit():
    global itemindex,order,items,REMBUTTON,level
    order.delete(0,tk.END)
    sumup()
    flag=False
    for n,i in enumerate(itemindex):
        if i!=0:
            dish=str(items[n])+">>"+str(i)
            order.insert(tk.END,dish)
        
            flag=True
    if flag==False:
        order.insert(0,"*waiter open's his notepaper*")
    for n,i in enumerate(REMBUTTON):
        if level=="s":
            if itemindex[n]!=0:
                if (n+1) <= 7 :
                    i.place(x=555,y=56+((n+1)*54))
                else :
                    i.place(x=555,y=70+((n+1)*54))
                i.lift()
            else:
                i.place_forget()
        elif level=="mi":
            if itemindex[n+14]!=0:
                if (n+1) <= 10 :
                    i.place(x=540,y=70+((n+1)*72))
                i.lift()
            else:
                i.place_forget()
        elif level=="mo":
            
            if itemindex[n+24]!=0:
                if (n+1) <= 10 :
                    i.place(x=800,y=64+((n+1)*70))
                i.lift()
            else:
                i.place_forget()
        elif level=="d":
                if itemindex[n+34]!=0:
                    if (n+1) <= 11 :
                        i.place(x=730,y=40+((n+1)*69))
                    i.lift()
                else:
                    i.place_forget()
        elif level=="b":
            try:
                if itemindex[n+45]!=0:
                    if (n+1) <= 10 :
                        i.place(x=540,y=80+((n+1)*70))
                    i.lift()
                else:
                    i.place_forget()
            except IndexError:
                pass
def exf(event):
    screen.attributes('-fullscreen',False)
def addit(i):
    global itemindex,level
    if level=="s":
        itemindex[i-1]+=1
    elif level=="mi":
        itemindex[i+13]+=1
    elif level=="mo":
        itemindex[i+23]+=1
    elif level=="d":
        itemindex[i+33]+=1
    elif level=="b":
        itemindex[i+44]+=1
    orderit()
def remit(i):
    global itemindex
    if level=="s":
        itemindex[i-1]-=1
    elif level=="mi":
        itemindex[i+13]-=1
    elif level=="mo":
        itemindex[i+23]-=1
    elif level=="d":
        itemindex[i+33]-=1
    elif level=="b":
        itemindex[i+44]-=1
    orderit()
def show_butn():
    global button,itemindex,level
    if level=="s":
        for n,i in enumerate(button):
            if (n+1) <= 7 :
                i.place(x=450,y=56+((n+1)*54))
            else :
                i.place(x=450,y=70+((n+1)*54))
            i.lift()
    elif level=="mi":
        for n,i in enumerate(button):
            if (n+1) <= 10 :
                i.place(x=440,y=70+((n+1)*72))
            i.lift()
    elif level=="mo":
        for n,i in enumerate(button):
            if (n+1) <= 10 :
                i.place(x=700,y=65+((n+1)*70))
            i.lift()
    elif level=="d":
        for n,i in enumerate(button):
            if (n+1) <= 11 :
                i.place(x=630,y=40+((n+1)*69))
            i.lift()
    elif level=="b":
        for n,i in enumerate(button):
            if (n+1) <= 10 :
                i.place(x=440,y=80+((n+1)*70))
            i.lift()
def hide_butn():
    global button,REMBUTTON
    for i in button:
        i.place_forget()
    for i in REMBUTTON:
        i.place_forget()
def back(l=0):
    global layer,order,sb,itemindex,fbill,level,blistbox,sb2
    if layer==1:
        if l==0:
            leave=False
            if  sum(itemindex) != 0:
                leave=messagebox.askyesno("WAITER...","DO YOU WANT TO SAVE THE ORDER,(sir/ma'am)?")
        else :
            if sum(itemindex) != 0:
                leave=True
            else:
                messagebox.showinfo("FAILED","no item selected")
        if leave==True:
            while True:
                name: str=simpledialog.askstring("WAITER...","ENTER A NAME FOR YOUR BILL")
                if name==None:
                    break
                elif name!="":
                    ii=list(itemindex)
                    ii.append(name)
                    billadd(ii)
                    layer=0
                    Hcbill.place(x=600,y=300)
                    Hsbill.place(x=600,y=425)
                    Harv.place(x=600,y=550)
                    closeb.place_forget()
                    orderready.place_forget()
                    startups.place_forget()
                    mains.place_forget()
                    dessert.place_forget()
                    bevrg.place_forget()
                    bgloader("h.png")
                    messagebox.showinfo("done","order saved in bills")
                    break
                else :
                    messagebox.showwarning("WARNING","please enter a name to save file")
        else:
            layer=0
            orderready.place_forget()
            Hcbill.place(x=600,y=300)
            Hsbill.place(x=600,y=425)
            Harv.place(x=600,y=550)
            closeb.place_forget()
            startups.place_forget()
            mains.place_forget()
            dessert.place_forget()
            bevrg.place_forget()
            bgloader("h.png")
    elif layer==2:
        order.place_forget()
        sb.place_forget()
        pricetag.place_forget()
        snext.place_forget()
        orderready.place(x=1200,y=10)
        startups.place(x=100,y=450)
        mains.place(x=650,y=700)
        dessert.place(x=1200,y=450)
        bevrg.place(x=650,y=450)
        closeb.place(x=1400,y=10)
        startups.lift()
        dessert.lift()
        bevrg.lift()
        mains.lift()
        hide_butn()
        layer=1
        level="h"
        bgloader("c.png")
    elif layer==3:
        Hcbill.place(x=600,y=300)
        Hsbill.place(x=600,y=425)
        Harv.place(x=600,y=550)
        listname.place_forget()
        closeb.place_forget()
        sb2.place_forget()
        blistbox.place_forget()
        orderr.place_forget()
        order.place_forget()
        sb.place_forget()
        pricetag.place_forget()
        view.place_forget()
        dell.place_forget()
        evn.place_forget()
        edn.place_forget()
        sno.place_forget()
        sno2.place_forget()
        ordernow.place_forget()
    elif layer==4:
        namefeed.place_forget()
        Hcbill.place(x=600,y=300)
        Hsbill.place(x=600,y=425)
        Harv.place(x=600,y=550)
        bgloader("h.png")
        closeb.place_forget()
        rate.place_forget()
        commentfeed.place_forget()
        submitfeed.place_forget()
        feedback.place_forget()

def crt_bill():
    global layer,itemindex,fbill,dummyindex
    #screen.attributes("-fullscreen",True)
    screen.geometry("1536x864")
    layer=1
    itemindex=list(dummyindex)
    Hcbill.place_forget()
    Hsbill.place_forget()
    Harv.place_forget()
    startups.place(x=100,y=450)
    mains.place(x=650,y=700)
    dessert.place(x=1200,y=450)
    bevrg.place(x=650,y=450)
    closeb.place(x=1400,y=10)
    orderready.place(x=1200,y=10)
    bgloader("c.png")
def show_bill():
    global layer,sb2,blistbox,placeholder,evn
    layer=3
    billhist()
    on_leave(1)
    on_leave(2)
    Hcbill.place_forget()
    Hsbill.place_forget()
    Harv.place_forget()
    closeb.place(x=1400,y=10)
    sb2.place(x=400,y=200,width=20,height=600)
    blistbox.place(x=100,y=200,width=300,height=600)
    view.place(x=450,y=300)
    listname.place(x=200,y=150)
    dell.place(x=450,y=373)
    sno.place(x=640,y=327)
    sno2.place(x=640,y=395)
    evn.place(x=550,y=327)
    edn.place(x=550,y=395)
    blistbox.lift()
    sb2.lift()
def feedbackit():
    global layer
    updatefeed()
    layer=4
    Hcbill.place_forget()
    Hsbill.place_forget()
    Harv.place_forget()
    closeb.place(x=800,y=10)
    namefeed.place(x=1100,y=290)
    rate.place(x=1100,y=380)
    commentfeed.place(x=1000,y=550)
    submitfeed.place(x=1275,y=470)
    feedback.place(x=50,y=300)
    bgloader("f.png")

def start_ups():
    global layer,level,order
    order.place(x=1000,y=200,width=500,height=600)
    sb.place(x=1500,y=200,width=20,height=600)
    pricetag.place(x=1100,y=800)
    order.lift()
    sb.lift()
    layer=2
    level="s"
    orderready.place_forget()
    mains.place_forget()
    dessert.place_forget()
    startups.place_forget()
    bevrg.place_forget()
    closeb.lift()
    show_butn()
    orderit()
    bgloader("st.png")
def mains():
    global layer,level,order,sb
    order.place(x=1000,y=200,width=500,height=600)
    sb.place(x=1500,y=200,width=20,height=600)
    pricetag.place(x=1100,y=800)
    order.lift()
    sb.lift()
    layer=2
    level="mi"
    mains.place_forget()
    snext.place(x=850,y=400)
    snext.lift()
    orderready.place_forget()
    dessert.place_forget()
    startups.place_forget()
    bevrg.place_forget()
    closeb.lift()
    show_butn()
    orderit()
    bgloader("mi.png")
def nextit():
    global level,snext
    if level =="mi":
        snext.place_forget()
        snext.config(text="<=")
        snext.place(x=850,y=400)
        closeb.lift()
        level="mo"
        orderit()
        show_butn()
        bgloader("mo.png")
    else :
        snext.place_forget()
        snext.config(text="=>")
        snext.place(x=850,y=400)
        closeb.lift()
        level="mi"
        orderit()
        show_butn()
        bgloader("mi.png")
def dessert():
    global layer,level,order
    order.place(x=1000,y=200,width=500,height=600)
    sb.place(x=1500,y=200,width=20,height=600)
    pricetag.place(x=1100,y=800)
    order.lift()
    sb.lift()
    layer=2
    level="d"
    orderready.place_forget()
    mains.place_forget()
    dessert.place_forget()
    startups.place_forget()
    bevrg.place_forget()
    closeb.lift()
    show_butn()
    orderit()
    bgloader("d.png")
def bevrg():
    global layer,level,order
    order.place(x=1000,y=200,width=500,height=600)
    sb.place(x=1500,y=200,width=20,height=600)
    pricetag.place(x=1100,y=800)
    order.lift()
    sb.lift()
    layer=2
    level="b"
    orderready.place_forget()
    mains.place_forget()
    dessert.place_forget()
    startups.place_forget()
    bevrg.place_forget()
    closeb.lift()
    show_butn()
    orderit()
    bgloader("b.png")
#BINDING
#screen.bind('<Escape>', exf)
bgloader("h.png")
evn.bind("<Button-1>",lambda e: on_click(1,e))
evn.bind("<FocusOut>",lambda e: on_leave(1,e))
evn.bind("<Return>",lambda e: snoit(1,e))

edn.bind("<FocusIn>",lambda e: on_click(2,e))
edn.bind("<Button-1>",lambda e: on_click(2,e))
edn.bind("<FocusOut>",lambda e: on_leave(2,e))
edn.bind("<Return>",lambda e: snoit(2,e))


# buttons
Hcbill=tk.Button(screen,text="PLACE ORDER",width=30,height=2,bg="sky blue",font=("Bahnschrift Condensed",20,"bold"),command=crt_bill)
Hcbill.place(x=600,y=300)
Hsbill=tk.Button(screen,text="BILLS",width=30,height=2,bg="sky blue",font=("Bahnschrift Condensed",20,"bold"),command=show_bill)
Hsbill.place(x=600,y=425)
Harv=tk.Button(screen,text="GIVE RIVIEW",width=30,height=2,bg="sky blue",font=("Bahnschrift Condensed",20,"bold"),command=feedbackit)
Harv.place(x=600,y=550)
closeb=tk.Button(screen,text="BACK",width=10,font=("Bahnschrift Condensed",20,"bold"),bg="red",fg="black",command=back)
orderready=tk.Button(screen,text="ORDER",width=10,font=("Bahnschrift Condensed",20,"bold"),bg="sky blue",fg="black",command=lambda l=1:back(l))
startups=tk.Button(screen,text="STARTERS",width=20,bg="brown",fg="white",font=("Bahnschrift Condensed",25,"bold"),command=start_ups)
mains=tk.Button(screen,text="MAIN COURSE",width=20,bg="orange",fg="white",font=("Bahnschrift Condensed",25,"bold"),command=mains)
dessert=tk.Button(screen,text="DESSERT",width=20,bg="light pink",fg="white",font=("Bahnschrift Condensed",25,"bold"),command=dessert)
bevrg=tk.Button(screen,text="BEVERAGE",width=20,bg="GREY",fg="white",font=("Bahnschrift Condensed",25,"bold"),command=bevrg)
snext=tk.Button(screen,text="=>",width=5,bg="sky blue",fg="black",font=("ARIAL",25,"bold"),command=nextit)
sno=tk.Button(screen,text="submit",width=5,bg="sky blue",fg="black",font=("ARIAL",10,"bold"),command=lambda a=1:snoit(a))
sno2=tk.Button(screen,text="submit",width=5,bg="sky blue",fg="black",font=("ARIAL",10,"bold"),command=lambda a=2:snoit(a))
ordernow=tk.Button(screen,text="ORDER!",width=15,bg="sky blue",fg="black",font=("ARIAL",15,"bold"),command=onit)
submitfeed=tk.Button(screen,text="SUBMIT",width=15,bg="sky blue",fg="black",font=("Bahnschrift Condensed",15,"bold"),command=submitit)
for i in range (1,8):
    butn=tk.Button(screen,text="+ADD",width=12,bg="grey",fg="white",command=lambda i=i: addit(i))
    button.append(butn)
for i in range (8,15):
    butn=tk.Button(screen,text="+ADD",width=12,bg="grey",fg="white",command=lambda i=i: addit(i))
    button.append(butn)
for i in range (1,8):
    rbutn=tk.Button(screen,text="--",width=5,bg="red",fg="black",command=lambda i=i: remit(i))
    REMBUTTON.append(rbutn)
for i in range (8,15):
    rbutn=tk.Button(screen,text="--",width=5,bg="red",fg="black",command=lambda i=i: remit(i))
    REMBUTTON.append(rbutn)

billhist()
screen.mainloop()
