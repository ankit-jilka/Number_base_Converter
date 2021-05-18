from tkinter import *
from tkinter import ttk
from array import *
from tkinter import messagebox
import math

root = Tk()
root.title("  Number Base Converter")
icon = PhotoImage(file='C:\icon3.png')
root.iconphoto(False,icon)
root.geometry("820x670")
root.minsize(820,670)
root.maxsize(820,670)
root.configure(bg = "#E8EFFD")
title = Label(root, text = "NUMBER  BASE  CONVERTER" , fg = "#525C65" , bg = "#FFAEB9" , font = ('Stencil',40,'bold'))
title.pack(fill='x',side = 'top')

def choose_frombase(com_get1):       # fun_2  ...  this fun. check value in combobox and return value
   if com_get1 == 'base 2(binary)':
      return 2
   elif com_get1 == 'base 3(ternary)':
      return 3
   elif com_get1 == 'base 4(quarternary)':
      return 4
   elif com_get1 == 'base 5(quinary)':
      return 5
   elif com_get1 == 'base 6(senary)':
      return 6
   elif com_get1 == 'base 7(septenary)':
      return 7
   elif com_get1 == 'base 8(octal)':
      return 8
   elif com_get1 == 'base 9(nonary)':
      return 9
   elif com_get1 == 'base 10(decimal)':
      return 10
   elif com_get1 == 'base 11(undecimal)':
      return 11
   elif com_get1 == 'base 12(dozenal)':
      return 12
   elif com_get1 == 'base 13(tredecimal)':
      return 13
   elif com_get1 == 'base 14':
      return 14
   elif com_get1 == 'base 15':
      return 15
   elif com_get1 == 'base 16(hex)':
      return 16
   elif com_get1 == 'base 17':
      return 17
   elif com_get1 == 'base 18':
      return 18
   elif com_get1 == 'base 19':
      return 19
   elif com_get1 == 'base 20':
      return 20
   elif com_get1 == 'base 21':
      return 21
   elif com_get1 == 'base 22':
      return 22
   elif com_get1 == 'base 23':
      return 23
   elif com_get1 == 'base 24':
      return 24
   elif com_get1 == 'base 25':
      return 25
   elif com_get1 == 'base 26':
      return 26

def chk_val(r,from_b):    # fun_3  ....  this fun check value in range in given option
   for x in r:
      if x>=0 and x<from_b:
         pass
      else:
         messagebox.showwarning('WARNING !!', "PLEASE  ENTER  VALID  VALUE")
         #value_take.delete(0,END)
         value_take.focus()
         return
   return r,from_b


def befo_decimal(ar,from_b):        # fun_4  ...  this fun convert given number which is before decimal point  into decimal
   sum = 0
   l1 = len(ar) - 1
   for x in ar:
     sum = sum + (x * pow(from_b,l1))
     l1 = l1 - 1
   return sum

def after_decimal(ar,from_b):    # fun_4  this fun convert given number which is after decimal point  into decimal
    sum = 0
    l1 = len(ar)
    ar.reverse()
    for x in ar:
        sum = sum + (x * pow(from_b,-l1))
        l1 = l1 - 1
    return sum

def to_aft_deci(su , to_b):
    list = []
    b1 = su * to_b
    b2 , a2 = math.modf(b1)
    list.append(int(a2))
    b3 = round(b2,16)
    num = 0
    while b3 != int(0000000000000000) and num <= 13:
       b3 = b3 * to_b
       b3, a1 = math.modf(b3)
       b3 = round(b3,16)
       list.append(int(a1))
       num = num + 1
    return list



def to_bef_deci(kul,to_b):    # fun_6  ...  this fun convert decimal into given to_base  number
   arr2 = array('i',[])
   list = []
   while kul != 0:
     arr2.append(int(kul % to_b))
     kul = int(kul / to_b)
   arr2.reverse()
   return arr2

def last_cov(arr2):       # this fun convert  decimal value into alphabets
   ar3 = []
   for j in arr2:
      if j == 10:
         j = 'A'
      if j == 11:
         j = 'B'
      if j == 12:
         j = 'C'
      if j == 13:
         j = 'D'
      if j == 14:
         j = 'E'
      if j == 15:
         j = 'F'
      if j == 16:
         j = 'G'
      if j == 17:
         j = 'H'
      if j == 18:
         j = 'I'
      if j == 19:
         j = 'J'
      if j == 20:
         j = 'K'
      if j == 21:
         j = 'L'
      if j == 22:
         j = 'M'
      if j == 23:
         j = 'N'
      if j == 24:
         j = 'O'
      if j == 25:
         j = 'P'
      if j == 26:
         j = 'Q'
      ar3.append(j)
   global s
   s = ""
   for p in ar3:
       s = str(s + str(p))
   return s

def con_in_num(rr):                   # fun_2  this fun convert all value in numbers and return in array type
    arr1 = []
    for j in rr:
        if ((j >= 'A' or j >= 'a') and (j <= 'R' or j <= 'r')) or (j.isdigit() == 1):
            if j == 'a' or j == 'A':
                j = 10
            if j == 'b' or j == 'B':
                j = 11
            if j == 'c' or j == 'C':
                j = 12
            if j == 'd' or j == 'D':
                j = 13
            if j == 'e' or j == 'E':
                j = 14
            if j == 'f' or j == 'F':
                j = 15
            if j == 'g' or j == 'G':
                j = 16
            if j == 'h' or j == 'H':
                j = 17
            if j == 'i' or j == 'I':
                j = 18
            if j == 'j' or j == 'J':
                j = 19
            if j == 'k' or j == 'K':
                j = 20
            if j == 'l' or j == 'L':
                j = 21
            if j == 'm' or j == 'M':
                j = 22
            if j == 'n' or j == 'N':
                j = 23
            if j == 'o' or j == 'O':
                j = 24
            if j == 'p' or j == 'P':
                j = 25
            if j == 'q' or j == 'Q':
                j = 26
            x = int(j)
            arr1.append(x)
        else:
            messagebox.showwarning('WARNING !!', 'PLEASE  ENTER  VALID  NUMBER ')
            #value_take.delete(0, END)
            value_take.focus()
            return
    return arr1

def append_array():           # fun_1  ...  this function like home page fun.  because all fun call from it
   arr1 = []
   bef_deci_1 = []
   aft_deci_1 = []
   bef_deci_2 = []
   aft_deci_2 = []
   bef_deci_3 = []
   aft_deci_3 = []
   bef_deci_4 = []
   aft_deci_4 = []
   value_get2 = str(value_take.get())
   if value_get2 == "":
       messagebox.showwarning('WARNING !!',"PLEASE  ENTER  A  NUMBER")
       value_take.focus()
       return

   for i in value_get2:
       arr1.append(i)

   no = 0
   for z in arr1:
      if z == '.':
         no = no + 1

   num = 0
   if no != 0:
     for q in arr1:
       if q  != '.' and num < arr1.index('.'):      # this for digits of before decimal point
           bef_deci_1.append(q)
           num = num + 1
       elif q != '.' and num >= arr1.index('.'):    # this for digits of after decimal point
           aft_deci_1.append(q)
           num = num +1
       else:
          pass
   else:                          #  this for without decimal value
      for q in arr1:
        bef_deci_1.append(q)

   bef_deci_2 = con_in_num(bef_deci_1)
   aft_deci_2 = con_in_num(aft_deci_1)

   ch_1 = choose_frombase(from_option.get())

   bef_deci_3,ch_3  = chk_val(bef_deci_2,ch_1)
   aft_deci_3,ch_3  = chk_val(aft_deci_2,ch_1)

   before_sum = befo_decimal(bef_deci_3,ch_3)
   after_sum = after_decimal(aft_deci_3,ch_3)

   ch_11 = choose_frombase(to_option.get())

   bef_deci_4 = to_bef_deci(before_sum, ch_11)
   bef_str = last_cov(bef_deci_4)

   aft_deci_4 = to_aft_deci(after_sum,ch_11)
   aft_str = last_cov(aft_deci_4)

   if aft_str == '0':
       sv1.set(bef_str)
   else:
       sv1.set(bef_str + '.' + aft_str)

def newwin():
   new = Toplevel(root)
   new.title("  Gray Code Conversion ")
   icon = PhotoImage(file="C:\icon3.png")
   new.iconphoto(False, icon)
   new.geometry("700x400")
   new.minsize(700, 500)
   new.maxsize(700, 500)
   new.configure(bg="#EEE9E9")

   tit_lb = Label(new , text = '  Gray Code Conversion ' , bg = "#FBEC5D" , fg = "#FF3300" , font = ('Constantia',30,'bold'))
   tit_lb.pack(side = 'top' , fill = 'x')

   def fcon():    # this fun check value and append in array
     val = en1.get()
     if val == "":
        messagebox.showwarning("WARNING !!","PlEASE  ENTER  A  NUMBER")
        en1.delete(0,END)
        en1.focus()
        return
     if val.isdigit() == 0:
        messagebox.showwarning("WARNING !!", "PLEASE  ENTER  ONLY  NUMBER  IN  0   or  1")
        #en1.delete(0,END)
        en1.focus()
        return
     arr4 = array('i',[])
     arr5 = array('i',[])
     for t in val:       # all value append in array
           arr4.append(int(t))

     for c in arr4:
       if c>=0 and c<2:
          pass
       else:
         messagebox.showwarning('WARNING !!','PLEASE  ENTER  ONLY  0  or  1 ')
         #en1.delete(0,END)
         en1.focus()
         return

       arr5.append(int(c))
     return arr5
      #print(arr5)


   def fgray1():
     en1.focus()
     ar7 = array('i',[])
     ar7 = fcon()        # after checking value comes into ar7

     arr6 = array('i',[])
     num = 0
     arr6.append(int(ar7[0]))
     while num != (len(ar7)-1):      # transfer value of arr7  into arr6
       m = ar7[num] ^ ar7[num+1]
       arr6.append(m)
       num = num + 1
     global g
     g = ""
     for r in arr6:
        g = str(g + str(r))
     sv2.set(g)
     #print(g)

   def fbin1():
      ar8 = array('i', [])
      ar8 = fcon()               # after checking value comes into ar8
      ar9 = array('i',[])
      num = 0
      ar9.append(int(ar8[0]))
      while num != (len(ar8)-1):            # transfer value of ar8 into ar9
        m = ar9[num] ^ ar8[num+1]
        ar9.append(m)
        num = num + 1
      #print(ar9)
      global h
      h = ""
      for q in ar9:
          h = str(h + str(q))
      sv3.set(h)

   en_num = Label(new, text="Enter Number", fg="black", bg="#EEE9E9", font=('Constantia', 18, 'bold'))
   en_num.place(x=30, y=90)
   en1 = Entry(new, font=('Rockwell', 18), width=35, bd=3)
   en1.place(x=225, y=90)
   en1.focus()
   not1 = Label(new, text=''' NOTE :  By  Pressing  "Into Gray"  You  Will  Get  Gray  Code  Of  Enterd  Number  ''',
              fg="#2B4F81", bg="#EEE9E9", font=('Constantia', 14))
   not1.place(x=10, y=400)
   not2 = Label(new, text='''And  By Pressing "Into Binary"  You  Will  Get  Binary  Number  Of ''', fg="#2B4F81",
              bg="#EEE9E9", font=('Constantia', 15))
   not2.place(x=85, y=430)
   not3 = Label(new, text='''Enterd  Number''', fg="#2B4F81", bg="#EEE9E9", font=('Constantia', 15))
   not3.place(x=85, y=460)


   res_gray = Label(new , text = 'Result In Gray : ' , fg = "black" , bg = "#EEE9E9" , font = ('Constantia',18,'bold'))
   res_gray.place(x=43,y=270)
   sv2 = StringVar(new)
   res_no_gray = Label(new , textvariable  = sv2 , fg = "red" ,bg = "#EEE9E9" , font = ('Cooper',22))
   res_no_gray.place(x=230,y=270)

   res_bin = Label(new , text = 'Result In Binary : ' , fg = "black" ,bg = "#EEE9E9",  font = ('Constantia',18,'bold'))
   res_bin.place(x=30,y=315)
   sv3 = StringVar(new)
   res_no_bin = Label(new, textvariable  = sv3 , fg = "red" ,bg = "#EEE9E9" , font = ('Cooper',22))
   res_no_bin.place(x=230, y=315)


   h1_can = Canvas(new, width=630, height=2, background='#FFA812')
   h1_can.place(x=25, y=260)

   h2_can = Canvas(new, width=630, height=2, background='#FFA812')
   h2_can.place(x=25, y=360)

   v1_can = Canvas(new, width=2, height=100, background='#FFA812')
   v1_can.place(x=24, y=260)

   v2_can = Canvas(new, width=2, height=100, background='#FFA812')
   v2_can.place(x=656, y=260)

   btn_gray = Button(new , text = "Into Gray" ,fg = "#603311", bg = "#70DB93" ,width = 13 ,font = ('Constantia',16,'bold'),command = fgray1)
   btn_gray.place(x = 100, y= 160)
   btn_bin = Button(new , text = "Into Binary" ,fg = "#603311", bg = "#70DB93" ,width = 13 ,font = ('Constantia',16,'bold'),command = fbin1)
   btn_bin.place(x = 380, y= 160)

   new.mainloop()

def close_win():
   ans = messagebox.askquestion("Confirm Exit !!","ARE  YOU  SURE  WANT  TO  EXIT ?")
   if ans == 'yes':
      messagebox.showinfo("GREETING","THANKS  FOR  VISIT !!")
      root.destroy()


take = Label(root , text = "Enter Number" ,fg = "black" , font = ('Constantia',18,'bold'))
take.place(x = 50,y=110)
value_take = Entry(root, font = ('Rockwell',18),width = 40,bd=3)
value_take.place(x=233,y=113)
value_take.focus()

from_base = Label(root,text = 'From Base' , fg = "black" , font = ('Constantia',16,'bold'))
from_base.place(x=30,y=200)

to_base = Label(root,text = 'To Base' , fg = "black" , font = ('Constantia',16,'bold'))
to_base.place(x=455,y=200)

tkvar1 = StringVar(root)
# for create dropdown menu....
#option = ['base 2(binary)','base 3','base 4','base 5','base 6','base 7','base 8(octal)','base 9','base 10(decimal)','base 11','base 12','base 13','base 14','base 15','base 16(hex)','base 17','base 18','base 19','base 20','base 21']
#tkvar1.set('base 2(binary)')
#dropdown = OptionMenu(root,tkvar1,*option)
#dropdown.place(x=400,y=500)

from_option = ttk.Combobox(root,width = 18,font = ('Rockwell',15),textvariable = tkvar1)
from_option['values'] = ('base 2(binary)','base 3(ternary)','base 4(quarternary)','base 5(quinary)','base 6(senary)','base 7(septenary)','base 8(octal)','base 9(nonary)','base 10(decimal)', 'base 11(undecimal)','base 12(dozenal)','base 13(tredecimal)','base 14','base 15','base 16(hex)','base 17','base 18','base 19','base 20','base 21','base 22','base 23','base 24','base 25','base 26')
from_option.place(x=147,y=200)
from_option.current(0)
root.option_add('*TCombobox*Listbox.font',('Rockwell',14))

tkvar2 = StringVar(root)
to_option = ttk.Combobox(root,width=20,font = ('Rockwell',15),textvariable = tkvar2)
to_option['values'] = ('base 2(binary)','base 3(ternary)','base 4(quarternary)','base 5(quinary)','base 6(senary)','base 7(septenary)','base 8(octal)','base 9(nonary)','base 10(decimal)','base 11(undecimal)','base 12(dozenal)','base 13(tredecimal)','base 14','base 15','base 16(hex)','base 17','base 18','base 19','base 20','base 21','base 22','base 23','base 24','base 25','base 26')
to_option.place(x=545,y=200)
to_option.current(8)
root.option_add('*TCombobox*Listbox.font',('Rockwell',14))

re = Label(root,text = 'Result Number : ', fg = "black" , font = ('Constantia',18,'bold'))
re.place(x=90,y=369)
sv1 = StringVar()
re_num = Label(root , textvariable  = sv1 , fg = 'red',bg = "#E8EFFD" ,font = ('Cooper',22,'bold'),borderwidth=10)
re_num.place(x=100,y=408)


h1_can = Canvas(root,width = 670 , height = 2 , background = '#FFA812')
h1_can.place(x=80,y=400)

h2_can = Canvas(root,width = 670 , height = 2 , background = '#FFA812')
h2_can.place(x=80,y=465)

v1_can = Canvas(root,width = 2 , height = 65 , background = '#FFA812')
v1_can.place(x=82,y=400)

v2_can = Canvas(root,width = 2 , height = 65 , background = '#FFA812')
v2_can.place(x=748,y=400)


convert = Button(root,text ="CONVERT",bg = "#70DB93" , fg = "#603311", font = ('Arial Rounded MT',18,'bold'),width = 15,command=append_array)
convert.place(x=300,y=280)

gray_convert = Button(root,text ="Gray Code Conversion",bg = "#70DB93" , fg = "#603311", font = ('Arial Rounded MT',18,'bold'),width = 20,command=newwin)
gray_convert.place(x=90,y=530)

exit = Button(root,text ="EXIT",bg = "#70DB93" , fg = "#603311", font = ('Arial Rounded MT',18,'bold'),width = 12,command=close_win)
exit.place(x=530,y=530)

dev = Label(root , text = "devloped by  ANKIT  JILKA" , fg = "#00009C", bg = "#97C0DC" , font = ('Arial Rounded MT',20,'italic'))
dev.pack(fill = 'x',side = 'bottom')

root.mainloop()