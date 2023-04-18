from msilib.schema import ListBox
from tkinter import *

goods = ['apple', 'bananas', 'carrot', 'bread','butter', 'meat', 'potato', 'pineapple' ]
goods.reverse()

def add_goods():
    selection = list(list_goods.curselection())
    selection.reverse()

    for i in selection:
        list_order.insert(0, list_goods.get(i))
        list_goods.delete(i)

def to_take_back_Goods():
    selection = list(list_order.curselection())
    selection.reverse()

    for i in selection:
        list_goods.insert(0, list_order.get(i))
        list_order.delete(i)

root = Tk()

frame = Frame()
frame.pack(side=LEFT)
frame2 = Frame()
frame2.pack(side=LEFT)
frame3 = Frame()
frame3.pack(side=LEFT)

list_goods = Listbox(frame, selectmode=EXTENDED, width=15, height=10)
btn_add = Button(frame2, text='>>>', command=add_goods, width=10, height=2)
btn_take_back = Button(frame2, text='<<<',command=to_take_back_Goods, width=10, heigh=2)
list_order = Listbox(frame3, selectmode=EXTENDED, width=15, height=10)

list_goods.pack(side=LEFT)
btn_add.pack()
btn_take_back.pack()
list_order.pack(side=LEFT)

for i in goods :
    list_goods.insert(0, i)

root.mainloop()
