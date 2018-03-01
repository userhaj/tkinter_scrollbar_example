from tkinter import *


class App:

    def __init__(self, master):
        # Allows update in later method
        self.master = master

        # Create scroll bar
        self.y_axis_scrollbar = Scrollbar(self.master)

        # Create canvas with yscrollcommmand from scrollbar, use xscrollcommand for horizontal scroll
        self.main_canvas = Canvas(self.master, yscrollcommand=self.y_axis_scrollbar.set)

        # Configure and pack/grid scrollbar to master
        self.y_axis_scrollbar.config(command=self.main_canvas.yview)
        self.y_axis_scrollbar.pack(side=RIGHT, fill=Y)

        # This is the frame all content will go to. The 'master' of the frame is the canvas
        self.content_frame = Frame(self.main_canvas)

        # Place canvas on app pack/grid
        self.main_canvas.pack(side='left', fill='both', expand='True')

        # create_window draws the Frame on the canvas. Imagine it as another pack/grid
        self.main_canvas.create_window(0, 0, window=self.content_frame, anchor='nw')

        # Your first content you are adding to the Frame that sits on a canvas
        Button(self.content_frame, text='Add Buttons to Canvas', command=self.create_buttons).pack()

        # Call this method after every update to the canvas
        self.update_scroll_region()


    def update_scroll_region(self):
        ''' Call after every update to content in self.main_canvas '''
        self.master.update()
        self.main_canvas.config(scrollregion=self.main_canvas.bbox('all'))

    def create_buttons(self):
        for index in range(20):
            Button(self.content_frame, text=str(index)).pack()

        self.update_scroll_region()


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
