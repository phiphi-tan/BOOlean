import tkinter as tk

from services.chatgptAPI import get_response

# https://stackoverflow.com/questions/63828120/how-to-make-tkinter-text-widget-read-only-on-certain-characters-and-sentences


class ConsoleText(tk.Text):
    INTRO_TEXT = 'Hello! How can I help you?'

    def __init__(self, master=None, **kw):
        tk.Text.__init__(self, master, **kw)

        self.insert('1.0', f'{self.INTRO_TEXT}\n\n>>> ')
        self.mark_set('input', 'insert')

        # create input mark
        self.mark_gravity('input', 'left')
        # create proxy
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)
        # binding to Enter key
        self.bind("<Return>", self.enter)

    def _proxy(self, *args):
        largs = list(args)

        if args[0] == 'insert':
            if self.compare('insert', '<', 'input'):
                # move insertion cursor to the editable part
                # you can change 'end' with 'input'
                self.mark_set('insert', 'end')
        elif args[0] == "delete":
            if self.compare(largs[1], '<', 'input'):
                if len(largs) == 2:
                    return  # don't delete anything
                largs[1] = 'input'  # move deletion start at 'input'
        result = self.tk.call((self._orig,) + tuple(largs))
        return result

    def enter(self, event):
        command = self.get('input', 'end')
        # execute code
        response = get_response(command)
        # display result and next prompt
        self.insert('end', f'\n{response}\n\n>>> ')
        # move input mark
        self.mark_set('input', 'insert')
        return "break"  # don't execute class method that inserts a newline


def openChatGPTWindow(event, window, xPos, yPos):
    xPos = xPos + 150
    yPos = yPos - 400
    textInputWindow = tk.Toplevel(window)
    textInputWindow.geometry('200x200+' + str(xPos) + f'+{yPos}')
    textInput = ConsoleText(textInputWindow)
    textInput.pack()
    textInput.focus_set()

    return textInputWindow
