# Question 45 : -
# Take a image file from user and edit as black and white image editor 
# ask a user to the file name save it.

# Solution : - 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from tkinter import filedialog as fd
from PIL import Image, ImageEnhance


class Browse(tk.Frame):
    """ Creates a frame that contains a button when clicked lets the user to select
    a file and put its filepath into an entry.
    """

    def __init__(self, master, initialdir='', filetypes=()):
        super().__init__(master)
        self.filepath = tk.StringVar()
        self._initaldir = initialdir
        self._filetypes = filetypes
        self._create_widgets()
        self._display_widgets()

    def _create_widgets(self):
        self._entry = tk.Entry(self, textvariable=self.filepath)
        self._button = ttk.Button(self, text="Browse...", command=self.browse)

    def _display_widgets(self):
        self._entry.pack(fill='x', expand=True)
        self._button.pack(anchor='se')

    def getPath(self):
        return self.filepath.get()
    
    def browse(self):
        """ Browses a .png file or all files and then puts it on the entry.
        """

        self.filepath.set(fd.askopenfilename(initialdir=self._initaldir,
                                             filetypes=self._filetypes))
        

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Chetan")

    # label frame
    label_frame = tk.LabelFrame(root, text=" B/W Image Editor ")
    label_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

    # create labels
    file_label = ttk.Label(label_frame, text="Choose a image file : ")
    file_label.grid(rowspan = 1, column = 0, pady=10)

    new_name = ttk.Label(label_frame, text="Enter the new file name without extension : ")
    new_name.grid(row=2, column=0)

    # create entry box
    file_browser = Browse(label_frame, initialdir=r"C:\Users", filetypes = (('Joint Photographic experts Group', '*.jpg'),
                                                                            ('Portable Network Graphics','*.png'),
                                                                            ('Joint Photographic Experts Group', '*.jpeg'),
                                                                            ('Tagged Image File Format', '*.tiff'),
                                                                            ("All files", "*.*")))
    file_browser.grid(row=0, column=2, pady=5, padx=10)
    
    name_var = tk.StringVar()
    name_entrybox = tk.Entry(label_frame, width=20, textvariable = name_var)
    name_entrybox.grid(row=2, column=2)

    # create button
    def action():
        path = file_browser.getPath()
        try :
            img1 = Image.open(path)
        except :
            print("May be you select wrong image file.\nTry again......")

        file_path = path[:-(path[::-1].find('/'))]

        color_enhancer = ImageEnhance.Color(img1)
        color_enhancer.enhance(0).save(f"{file_path}{name_var.get()}.{path[-(path[::-1].find('.')):]}")

        for i in range(18):
            print("Processing.......")
            
        # messagebox
        m_box.showinfo("Success", "Your Image Successfully Edited.")
        ans = m_box.askyesno("Question : ", "Would you want to open an edited image?")
        if ans:
            color_enhancer.enhance(0).show()
        
        root.quit()


    submit_btn = ttk.Button(root, text="Submit", command=action)
    submit_btn.grid(row=1, column=0, pady=5)

    root.mainloop()
