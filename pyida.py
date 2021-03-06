import widgets.quick_menu
from PySide import QtGui,QtCore
import string_refs
import idaapi
import idc
import os
import widgets.find_text_table
import widgets.header_found_table
import widgets.TracebackDialog
import widgets.FindFuncDialog
import widgets.ReplaceDialog
import binary_finder
import decompiled
import wpsearch

def launch_quick_menu():
    widgets.quick_menu.launch()


def export_func_names():
    path = os.path.join(os.getcwd(), 'func_strings.json')
    string_refs.export_func_names(path)


def add_hotkey(hotkey, func):
    hotkey_ctx = idaapi.add_hotkey(hotkey, func)
    if hotkey_ctx is None:
        print "Failed to register hotkey %s for launching %s!" % (hotkey,func.__name__)
        del hotkey_ctx
    else:
        print "Hotkey %s registered for %s" % (hotkey,func.__name__)


def add_menu_item(menupath, name, hotkey, flags, pyfunc,args):
    menuItem = idaapi.add_menu_item(menupath, name, hotkey, flags, pyfunc,args)
    if menuItem is None:
        print "Failed to register menu item  %s for launching %s!" % ( menupath + "->"+ name, pyfunc.__name__)
    else:
        print "Menu item %s registered for launching %s" % ( menupath + "->"+ name, pyfunc.__name__)





#init hotkeys
add_hotkey("Alt-Shift-Q",launch_quick_menu)

add_menu_item("Search/PyIDA/","Find various constants",None,0, wpsearch.launch ,None)
add_menu_item("Search/PyIDA/", "Find Crc tables",None,0, binary_finder.crc_table_find,None)
add_menu_item("Search/PyIDA/", "Find Function","Alt-Shift-O",0,widgets.FindFuncDialog.launch,None)
add_menu_item("Edit/PyIDA/", "Create Crc table here...",None,0, binary_finder.create_crc_table,None)
add_menu_item("Edit/PyIDA/", "Make all strings const",None,0, decompiled.make_strings_const ,None)
add_menu_item("Edit/PyIDA/", "Replace Names",None,0, widgets.ReplaceDialog.launch ,None)
add_menu_item("File/Produce file/PyIDA/", "Create strings-to-function",None,0,export_func_names,None)
add_menu_item("View/PyIDA/","Exception traceback",'Alt-Shift-M',0, widgets.TracebackDialog.launch,None)
add_menu_item("View/PyIDA/","Decompiled search",None,0, widgets.find_text_table.show,None)
add_menu_item("View/PyIDA/","Text search",None,0, widgets.header_found_table.show,None)



globals_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"global_constants.h")
idc.ParseTypes(globals_file, idc.PT_FILE | idc.PT_PAKDEF)

