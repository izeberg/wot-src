from Tkinter import *
import tkMessageBox

class TextViewer(Toplevel):

    def __init__(self, parent, title, text, modal=True, _htest=False):
        Toplevel.__init__(self, parent)
        self.configure(borderwidth=5)
        self.geometry('=%dx%d+%d+%d' % (750, 500,
         parent.winfo_rootx() + 10,
         parent.winfo_rooty() + (10 if not _htest else 100)))
        self.bg = '#ffffff'
        self.fg = '#000000'
        self.CreateWidgets()
        self.title(title)
        self.protocol('WM_DELETE_WINDOW', self.Ok)
        self.parent = parent
        self.textView.focus_set()
        self.bind('<Return>', self.Ok)
        self.bind('<Escape>', self.Ok)
        self.textView.insert(0.0, text)
        self.textView.config(state=DISABLED)
        self.is_modal = modal
        if self.is_modal:
            self.transient(parent)
            self.grab_set()
            self.wait_window()

    def CreateWidgets(self):
        frameText = Frame(self, relief=SUNKEN, height=700)
        frameButtons = Frame(self)
        self.buttonOk = Button(frameButtons, text='Close', command=self.Ok, takefocus=FALSE)
        self.scrollbarView = Scrollbar(frameText, orient=VERTICAL, takefocus=FALSE, highlightthickness=0)
        self.textView = Text(frameText, wrap=WORD, highlightthickness=0, fg=self.fg, bg=self.bg)
        self.scrollbarView.config(command=self.textView.yview)
        self.textView.config(yscrollcommand=self.scrollbarView.set)
        self.buttonOk.pack()
        self.scrollbarView.pack(side=RIGHT, fill=Y)
        self.textView.pack(side=LEFT, expand=TRUE, fill=BOTH)
        frameButtons.pack(side=BOTTOM, fill=X)
        frameText.pack(side=TOP, expand=TRUE, fill=BOTH)

    def Ok(self, event=None):
        if self.is_modal:
            self.grab_release()
        self.destroy()


def view_text(parent, title, text, modal=True):
    return TextViewer(parent, title, text, modal)


def view_file(parent, title, filename, encoding=None, modal=True):
    try:
        if encoding:
            import codecs
            textFile = codecs.open(filename, 'r')
        else:
            textFile = open(filename, 'r')
    except IOError:
        tkMessageBox.showerror(title='File Load Error', message='Unable to load file %r .' % filename, parent=parent)
    except UnicodeDecodeError as err:
        showerror(title='Unicode Decode Error', message=str(err), parent=parent)
    else:
        return view_text(parent, title, textFile.read(), modal)


if __name__ == '__main__':
    import unittest
    unittest.main('idlelib.idle_test.test_textview', verbosity=2, exit=False)
    from idlelib.idle_test.htest import run
    run(TextViewer)