# coding=utf-8
from tkinter import *
from tkinter import messagebox


def closeWindow():  #点击关闭，弹出消息
    messagebox.showinfo(title = '警告',message='你确定?')
    #messagebox.showerror(title = '警告',message='你确定?')
    return
def closeallwindow():
    window.destroy()  #销毁窗口


def Love(): #点击Me too ，弹出窗口
    love = Toplevel(window) #是一个独立的顶级窗口
    love.geometry('300x200+900+300')
    love.title('好巧啊，我也是')
    label = Label(love,text = '好巧，我也是',font= ("楷体",25))
    label.pack()
    btn = Button(love,text = '确定',width = 10,height = 2,command = closeallwindow)
    btn.pack()
    love.protocol('WM_DELETE_WINDOW', closelove)

def closelove():
    #messagebox.showinfo('不在考虑一下吗？',message='在考虑一下吧~~~')
    return

def nolove():
    no_love = Toplevel(window)
    no_love.geometry('300x200+900+300')
    no_love.title('再考虑考虑呗')
    label = Label(no_love, text='再考虑考虑呗', font=("楷体", 25))
    label.pack()
    btn = Button(no_love, text='确定', width=10, height=2, command=no_love.destroy)
    btn.pack()
    no_love.protocol('WM_DELETE_WINDOW', closenolove)

def closenolove():
    nolove()

window = Tk()   #创建窗口
window.title("谢谢你能点开")  #设置标题
window.geometry("545x480")  #窗口大小
window.geometry("+800+200") #窗口位置
window.protocol('WM_DELETE_WINDOW',closeWindow)


#window.geometry("380x420+800+200") #可以合在一起写
label1 = Label(window,text = "你好",font = ('微软雅黑',20),fg = 'red')  #标签控件  font 字体 大小   fg  字体颜色
label1.grid(row = 0,column = 0,sticky = W)   #定位  grid  网格式布局
label2 = Label(window,text = '我喜欢你，你呢？',font = ('微软雅黑',40))
label2.grid(row = 1,column = 1,sticky = E)  #sticky对齐方式 N E W S
photo = PhotoImage(file = './cc..png')
imageLable = Label(window,image = photo)
imageLable.grid(row = 2,columnspan = 2) #columnspan 组件所跨越的列数
btn1 = Button(window,text = 'Me too',width = 15,height = 2,command = Love) #按钮
btn1.grid(row = 3,column = 0,sticky = W)
btn2 = Button(window,text = 'No',command = nolove)
btn2.grid(row = 3,column = 1,sticky = E)



window.mainloop()
