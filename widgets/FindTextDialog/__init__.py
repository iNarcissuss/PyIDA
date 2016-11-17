from PySide import QtGui
import idaapi
import widgets.find_text_table
from widgets import visual_style
from  widgets.FindTextDialog.find_text_dialog_pyside import Ui_FindTextDialog


class Dialog(Ui_FindTextDialog):

    def __init__(self):

        super(Ui_FindTextDialog,self).__init__()
        self.d = QtGui.QDialog()

        self.setupUi(self.d)
        self.selected_text = idaapi.get_highlighted_identifier()
        self.ok_btn.clicked.connect(self.ok_btn_clicked)
        self.cancel_btn.clicked.connect(self.cancel_btn_clicked)
        visual_style.set(self.d)


    def launch(self):
        self.text_edit.setText(self.selected_text if self.selected_text else "")
        self.d.exec_()

    def ok_btn_clicked(self):
        self.d.accept()
        import decompiled
        t = decompiled.find_text(self.text_edit.text(), only_named = self.only_named_functions.isChecked(),
                                 regex = self.regex_cbox.isChecked(), standalone= self.varname_cbox.isChecked())
        widgets.find_text_table.search_ctx.refresh_search_results(t)

    def cancel_btn_clicked(self):
        self.d.accept()


def launch():
    dialog = Dialog()
    dialog.launch()