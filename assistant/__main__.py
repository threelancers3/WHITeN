import os
from .gui.window import setup
from .ai_m2 import reply
from PySide6 import QtWidgets as qtw, QtCore as qtc
from markdown import markdown as md

def setup_reply_function(input_box: qtw.QLineEdit, label: qtw.QLabel):
    label.setTextFormat(qtc.Qt.RichText)
    def reply_function():
        text = input_box.text()
        input_box.setText("")
        res = reply(text, label=label)
        if type(res) == tuple:
            os.system("curl -L -o test.jpg "+res[1])
            label.setText('<img src="file:///test.jpg" style="width:20px;"/><br/>'+md(res[0]).replace('\n',"<br/>"))
            input_box.setFocus()
            return
        label.setText(md(res).replace('\n',"<br/>"))
        input_box.setFocus()
    return reply_function

if __name__ == '__main__':
    setup(setup_reply_function)
