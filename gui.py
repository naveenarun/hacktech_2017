import Tkinter, Tkconstants, tkFileDialog
import os

class TkFileDialogExample(Tkinter.Frame):

  def __init__(self, root):

    Tkinter.Frame.__init__(self, root)

    # options for buttons
    button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

    # define buttons
    Tkinter.Button(self, text='Select a directory', command=self.askdirectory).pack(**button_opt)

    # define options for opening or saving a file
    self.file_opt = options = {}
    options['defaultextension'] = '.txt'
    options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    options['initialdir'] = 'C:\\'
    options['initialfile'] = 'myfile.txt'
    options['parent'] = root
    options['title'] = 'This is a title'

    # This is only available on the Macintosh, and only when Navigation Services are installed.
    #options['message'] = 'message'

    # if you use the multiple file version of the module functions this option is set automatically.
    #options['multiple'] = 1

    # defining options for opening a directory
    self.dir_opt = options = {}
    options['initialdir'] = 'C:\\'
    options['mustexist'] = False
    options['parent'] = root
    options['title'] = 'This is a title'

  def askdirectory(self):

    """Returns a selected directoryname."""

    mydir = tkFileDialog.askdirectory(**self.dir_opt)
    picture_paths = [os.path.join(dirpath, f) for dirpath, dirnames, files in os.walk(mydir) for f in files if max([f.endswith(i) for i in ('.jpeg','.jpg','.png', '.gif', '.bmp')])]
    for i in picture_paths:
        os.system('python ' + os.getcwd() + '/test.py ' + '\'' + i + '\'')

if __name__=='__main__':
  root = Tkinter.Tk()
  TkFileDialogExample(root).pack()
  root.mainloop()
