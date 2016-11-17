from idaapi import PluginForm
from PySide import QtCore, QtGui
from widgets import visual_style
import idaapi
import idc

PLUGIN_NAME = "Decompiled functions search results"


# --------------------------------------------------------------------------
class TableModel_t(QtCore.QAbstractTableModel):
    """Model for the table """
    COL_LINE = 0
    COL_LINENO = 1
    COL_FUNC = 2
    COL_COUNT = 3

    header_names = ['Line', 'LineNo', 'Function']

    # private:

    def _displayHeader(self, orientation, col):
        if orientation == QtCore.Qt.Vertical:
            return None
        if col in [self.COL_LINE,self.COL_LINENO,self.COL_FUNC]:
            return self.header_names[col]
        return None

    def _displayData(self, row, col):
        seek_info = self.results_table[row]
        if col == self.COL_LINE:
            # print "_displayData get seek_info[line]" , seek_info['line']
            return seek_info['line']
        if col == self.COL_LINENO:
            return seek_info['lineno']
        if col == self.COL_FUNC:
            return seek_info['function']
        # print "_displayData get None"
        return None

    def raw_data(self,row, key):
        if len(self.results_table) <= row:
            return None
        seek_info = self.results_table[row]
        if key not in seek_info.keys():
            return None
        return seek_info[key]

    def _displayToolTip(self, row, col):
        return ""

    def _displayBackground(self, row, col):
        return None

    # public:
    def __init__(self):
        super(TableModel_t, self).__init__()
        self.results_table = []

    def refresh(self, results_table):
        self.results_table = results_table

    # Qt4 API
    def rowCount(self, parent):
        # print "get row count = " , len(self.results_table)
        return len(self.results_table)

    def columnCount(self, parent):
        return self.COL_COUNT

    def setData(self, index, content, role):
        # print "set data ",index, content, role
        return False


    def data2(self,row,col,role):

        if len(self.results_table) <= row:
            return None
        seek_info = self.results_table[row]
        if role == QtCore.Qt.UserRole:
            if col == self.COL_LINE:
                # print "data get seek_info[line] == ", seek_info['line']
                return seek_info['line']
            if col == self.COL_LINENO:
                return seek_info['lineno']
            if col == self.COL_FUNC:
                return seek_info['function']
            return None
        elif role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return self._displayData(row, col)
        elif role == QtCore.Qt.ToolTipRole:
            return self._displayToolTip(row, col)
        elif role == QtCore.Qt.BackgroundColorRole:
            return self._displayBackground(row, col)
        else:
            # print "data get None3 role = ", role
            return None

    def data(self, index, role):

        if not index.isValid():
            # print "data get None"
            return None
        col = index.column()
        row = index.row()
        return self.data2(row,col,role)

    def flags(self, index):
        if not index.isValid():
            # print "flags get None2"
            return None
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return self._displayHeader(orientation, section)
        else:
            return None
            # --------------------------------------------------------------------------


class TableView_t(QtGui.QTableView):

    # public
    def __init__(self,  parent=None):
        super(TableView_t, self).__init__(parent=parent)
        self.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        #
        self.setMouseTracking(True)
        self.setAutoFillBackground(True)

    # Qt API

    def get_index_data(self, index):
        if not index.isValid():
            return None

        index_data = index.data(QtCore.Qt.UserRole)
        return index_data

    def mousePressEvent(self, event):
        event.accept()
        super(QtGui.QTableView, self).mousePressEvent(event)


    def mouseDoubleClickEvent(self, event):
        event.accept()
        row  = self.rowAt(event.pos().y())
        m = self.model()
        ea = m.raw_data(row,"ea")
        print "ea = %s" % ea
        idc.Jump(ea)
        super(QtGui.QTableView, self).mouseDoubleClickEvent(event)

    def contextMenuEvent(self,event):
        menu =  QtGui.QMenu()
        menu.addAction("My Menu Item")
        menu.exec_(event.globalPos())

    def OnDestroy(self):
        pass


class TextSearchForm_t(PluginForm):


    def __init__(self):
        super(TextSearchForm_t,self).__init__()
        self.table_model = TableModel_t()

    def OnCreate(self, form):

        """
        Called when the plugin form is created
        """
        # Get parent widget
        self.parent = self.FormToPySideWidget(form)
        # Create view
        self.table_view = TableView_t()
        self.table_view.setModel(self.table_model)
        self.table_view.setSortingEnabled(True)
        self.table_view.setWordWrap(False)
        self.table_view.horizontalHeader().setStretchLastSection(False)
        self.adjustColumnsToContents()
        # #

        self.func_view = QtGui.QTextEdit()
        self.func_view.setReadOnly(True)
#        self.line_edit.setCenterOnScroll(True)
        self.func_view.setPlainText("")

        font = self.func_view.currentFont()
        font.setPointSize(10)
        self.func_view.setCurrentFont(font)

        # Populate PluginForm
        layout = QtGui.QVBoxLayout()
        layout.setSpacing(0)
#        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QtGui.QSplitter()
        splitter.setOrientation(QtCore.Qt.Vertical)

        splitter.addWidget(self.table_view)
        splitter.addWidget(self.func_view)
        layout.addWidget(splitter)

        self.parent.setLayout(layout)
        visual_style.set(self.parent)

        idaapi.set_dock_pos(PLUGIN_NAME, "IDA HExview-1", idaapi.DP_RIGHT)
        # print("TextSearchForm_t::OnCreate")

        self.table_view.clicked.connect(self.table_view_clicked)


    def OnClose(self, form):
        # print("TextSearchForm_t::OnClose")
        pass

    def refresh(self,results_table):
        self.table_model.refresh(results_table)


    def Show(self):
        """Creates the form if not created or focuses it if it was"""
        return PluginForm.Show(self, PLUGIN_NAME, options=PluginForm.FORM_PERSIST)

    def update(self):
        if hasattr(self,'table_view'):
            self.table_view.doItemsLayout()
            #print "update"


    def adjustColumnsToContents(self):
        self.table_view.resizeColumnToContents(0)
        self.table_view.resizeColumnToContents(1)
        self.table_view.resizeColumnToContents(2)

    def table_view_clicked(self,index):
        row  = index.row()
        m = self.table_view.model()
        func_body = m.raw_data(row,"func_body")
        line = m.raw_data(row,"lineno")

        self.func_view.clear()
        l = func_body.split("\n")
        self.func_view.setTextColor( visual_style.text_color)
        for i,ln in enumerate(l):
            if i == line-1:
                self.func_view.setTextColor(visual_style.marked_text_color)
                self.func_view.append(ln)
                self.func_view.setTextColor(visual_style.text_color)
            else:
                self.func_view.append(ln)

        cursor = self.func_view.textCursor()
        cursor.movePosition(QtGui.QTextCursor.Start, QtGui.QTextCursor.MoveAnchor)
        line = max(0,line-4)
        cursor.movePosition(QtGui.QTextCursor.Down, QtGui.QTextCursor.MoveAnchor,line)
        self.func_view.setTextCursor(cursor)
        self.func_view.ensureCursorVisible()


class SearchCtx():

    def __init__(self):
        self.search_text_form = TextSearchForm_t()

    def refresh_search_results(self, results_table):
        self.search_text_form.refresh(results_table)
        self.search_text_form.update()

    def show(self):
        self.search_text_form.Show()


search_ctx = SearchCtx()

def show():
    search_ctx.show()




