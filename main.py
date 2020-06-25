from tkinter import *
import tkinter.font

# --------define class-----------------------------------

class PaintApp:

# --------define class variables-------------------------

        drawing_tool='text'
        left_but='up'
        x_pos, y_pos=None,None
        x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt=None,None,None,None

# --------catch mouse down--------------------------------

        def left_but_down(self,event=None):
                self.left_but='down'
                self.x1_line_pt=event.x
                self.y1_line_pt=event.y

# -------catch mouse up------------------------------------

        def left_but_up(self,event=None):
                self.left_but='up'
                self.x_pos=None
                self.y_pos=None
                self.x2_line_pt=event.x
                self.y2_line_pt=event.y

                if self.drawing_tool=="line":
                        self.line_draw(event)
                if self.drawing_tool=="oval":
                        self.oval_draw(event)
                if self.drawing_tool=="rectangle":
                        self.rectangle_draw(event)
                if self.drawing_tool=="arc":
                        self.arc_draw(event)
                if self.drawing_tool=="text":
                        self.text_draw(event)

# --------catch mouse move-----------------------------------

        def motion(self,event=None):
                if self.drawing_tool=='pencil':
                        self.pencil_draw(event)

# ---------Draw Pencil---------------------------------------

        def pencil_draw(self,event=None):
                if self.left_but=="down":
                        if self.x_pos is not None and self.y_pos is not None:
                                event.widget.create_line(self.x_pos,self.y_pos,event.x,event.y,smooth=TRUE)
                        self.x_pos=event.x
                        self.y_pos=event.y

# ----------draw line------------------------------------------
        def line_draw(self,event=None):
                if None not in (self.x1_line_pt,self.y1_line_pt,self.x2_line_pt,self.y2_line_pt):
                        event.widget.create_line(self.x1_line_pt,self.y1_line_pt,self.x2_line_pt,self.y2_line_pt,smooth=TRUE,fill='green')

# ----------draw arc------------------------------------------
        def arc_draw(self,event=None):
                if None not in (self.x1_line_pt,self.y1_line_pt,self.x2_line_pt,self.y2_line_pt):
                        coords=self.x1_line_pt,self.y1_line_pt,self.x2_line_pt,self.y2_line_pt
                        event.widget.create_arc(coords,start=0,extent=150,style=ARC)

# -----------draw oval-----------------------------------------
        def oval_draw(self,event=None):
                if None not in (self.x1_line_pt,self.y1_line_pt,self.x2_line_pt,self.y2_line_pt):
                        event.widget.create_oval(self.x1_line_pt,self.y1_line_pt,self.x2_line_pt,self.y2_line_pt,smooth=TRUE,fill='light blue',outline='blue',width=2)

# -----------draw rectangle---------------------------------------

        def rectangle_draw(self,event=None):
                if None not in (self.x1_line_pt,self.y1_line_pt,self.x2_line_pt,self.y2_line_pt):
                        event.widget.create_rectangle(self.x1_line_pt,self.y1_line_pt,self.x2_line_pt,self.y2_line_pt,smooth=TRUE,fill='light blue',outline='blue',width=2)

# -----------draw text--------------------------------------------

        def text_draw(self,event=None):
                if None not in (self.x1_line_pt,self.y1_line_pt):
                        # print(tkinter.font.families())
                        text_font= tkinter.font.Font(family="Helvetica", size=20,weight='bold',slant="italic")
                        event.widget.create_text(self.x1_line_pt,self.y1_line_pt,fill="green",font=text_font,text='WOW')

# -----------Initialize--------------------------------------------

        def __init__(self,root):
                drawing_area=Canvas(root)
                drawing_area.pack()
                drawing_area.bind("<Motion>",self.motion)
                drawing_area.bind("<ButtonPress-1>",self.left_but_down)
                drawing_area.bind("<ButtonRelease-1>",self.left_but_up)

root=Tk()
paint_app=PaintApp(root)
root.mainloop()
