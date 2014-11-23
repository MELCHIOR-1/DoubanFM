#!/usr/bin/python
# -*- coding=utf-8 -*-
import gtk, webkit  
from webkit import WebView

URL = "http://douban.fm/radio"  
NAME = "豆瓣·FM" 
view = webkit.WebView()  
sw = gtk.ScrolledWindow()  
sw.add(view)  
  
win = gtk.Window(gtk.WINDOW_TOPLEVEL)  
win.set_default_size(420,180)  
win.set_title(NAME)  
#win.set_icon_from_file('douban.jpg')
win.connect("destroy",gtk.main_quit)  
win.add(sw)  
  
view.open(URL)  
win.show_all()  
gtk.main() 
