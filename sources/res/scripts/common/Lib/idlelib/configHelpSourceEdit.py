import os, sys
from Tkinter import *
import tkMessageBox, tkFileDialog

class GetHelpSourceDialog(Toplevel):

    def __init__(self, parent, title, menuItem='', filePath='', _htest=False):
        Toplevel.__init__(self, parent)
        self.configure(borderwidth=5)
        self.resizable(height=FALSE, width=FALSE)
        self.title(title)
        self.transient(parent)
        self.grab_set()
        self.protocol('WM_DELETE_WINDOW', self.Cancel)
        self.parent = parent
        self.result = None
        self.CreateWidgets()
        self.menu.set(menuItem)
        self.path.set(filePath)
        self.withdraw()
        self.update_idletasks()
        self.geometry('+%d+%d' % (
         parent.winfo_rootx() + (parent.winfo_width() / 2 - self.winfo_reqwidth() / 2),
         parent.winfo_rooty() + ((_htest or parent.winfo_height() / 2) - self.winfo_reqheight() / 2 if 1 else 150)))
        self.deiconify()
        self.bind('<Return>', self.Ok)
        self.wait_window()
        return

    def CreateWidgets(self):
        self.menu = StringVar(self)
        self.path = StringVar(self)
        self.fontSize = StringVar(self)
        self.frameMain = Frame(self, borderwidth=2, relief=GROOVE)
        self.frameMain.pack(side=TOP, expand=TRUE, fill=BOTH)
        labelMenu = Label(self.frameMain, anchor=W, justify=LEFT, text='Menu Item:')
        self.entryMenu = Entry(self.frameMain, textvariable=self.menu, width=30)
        self.entryMenu.focus_set()
        labelPath = Label(self.frameMain, anchor=W, justify=LEFT, text='Help File Path: Enter URL or browse for file')
        self.entryPath = Entry(self.frameMain, textvariable=self.path, width=40)
        self.entryMenu.focus_set()
        labelMenu.pack(anchor=W, padx=5, pady=3)
        self.entryMenu.pack(anchor=W, padx=5, pady=3)
        labelPath.pack(anchor=W, padx=5, pady=3)
        self.entryPath.pack(anchor=W, padx=5, pady=3)
        browseButton = Button(self.frameMain, text='Browse', width=8, command=self.browseFile)
        browseButton.pack(pady=3)
        frameButtons = Frame(self)
        frameButtons.pack(side=BOTTOM, fill=X)
        self.buttonOk = Button(frameButtons, text='OK', width=8, default=ACTIVE, command=self.Ok)
        self.buttonOk.grid(row=0, column=0, padx=5, pady=5)
        self.buttonCancel = Button(frameButtons, text='Cancel', width=8, command=self.Cancel)
        self.buttonCancel.grid(row=0, column=1, padx=5, pady=5)

    def browseFile(self):
        filetypes = [
         ('HTML Files', '*.htm *.html', 'TEXT'),
         ('PDF Files', '*.pdf', 'TEXT'),
         ('Windows Help Files', '*.chm'),
         ('Text Files', '*.txt', 'TEXT'),
         ('All Files', '*')]
        path = self.path.get()
        if path:
            dir, base = os.path.split(path)
        else:
            base = None
            if sys.platform[:3] == 'win':
                dir = os.path.join(os.path.dirname(sys.executable), 'Doc')
                if not os.path.isdir(dir):
                    dir = os.getcwd()
            else:
                dir = os.getcwd()
        opendialog = tkFileDialog.Open(parent=self, filetypes=filetypes)
        file = opendialog.show(initialdir=dir, initialfile=base)
        if file:
            self.path.set(file)
        return

    def MenuOk(self):
        menuOk = True
        menu = self.menu.get()
        menu.strip()
        if not menu:
            tkMessageBox.showerror(title='Menu Item Error', message='No menu item specified', parent=self)
            self.entryMenu.focus_set()
            menuOk = False
        elif len(menu) > 30:
            tkMessageBox.showerror(title='Menu Item Error', message='Menu item too long:\nLimit 30 characters.', parent=self)
            self.entryMenu.focus_set()
            menuOk = False
        return menuOk

    def PathOk(self):
        pathOk = True
        path = self.path.get()
        path.strip()
        if not path:
            tkMessageBox.showerror(title='File Path Error', message='No help file path specified.', parent=self)
            self.entryPath.focus_set()
            pathOk = False
        elif path.startswith(('www.', 'http')):
            pass
        else:
            if path[:5] == 'file:':
                path = path[5:]
            if not os.path.exists(path):
                tkMessageBox.showerror(title='File Path Error', message='Help file path does not exist.', parent=self)
                self.entryPath.focus_set()
                pathOk = False
        return pathOk

    def Ok(self, event=None):
        if self.MenuOk() and self.PathOk():
            self.result = (
             self.menu.get().strip(),
             self.path.get().strip())
            if sys.platform == 'darwin':
                path = self.result[1]
                if path.startswith(('www', 'file:', 'http:')):
                    pass
                else:
                    self.result = list(self.result)
                    self.result[1] = 'file://' + path
            self.grab_release()
            self.destroy()

    def Cancel(self, event=None):
        self.result = None
        self.grab_release()
        self.destroy()
        return


if __name__ == '__main__':
    from idlelib.idle_test.htest import run
    run(GetHelpSourceDialog)