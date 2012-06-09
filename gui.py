# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.html

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PicasaWeb Downloader", pos = wx.DefaultPosition, size = wx.Size( 950,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel, wx.ID_ANY, u"PicasaWeb Root or Gallery URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_tbxRootUrl = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_tbxRootUrl, 1, wx.ALL, 5 )
		
		self.m_btnGetGalleries = wx.Button( self.m_panel, wx.ID_ANY, u"Get Gallery List", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_btnGetGalleries, 0, wx.ALL, 5 )
		
		bSizer3.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Gallery List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		m_lstGalleriesChoices = []
		self.m_lstGalleries = wx.ListBox( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lstGalleriesChoices, 0 )
		bSizer3.Add( self.m_lstGalleries, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_lstImagesChoices = []
		self.m_lstImages = wx.ListBox( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lstImagesChoices, wx.LB_EXTENDED )
		bSizer5.Add( self.m_lstImages, 2, wx.ALL|wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_htmlThumb = wx.html.HtmlWindow( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
		bSizer6.Add( self.m_htmlThumb, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btnPreview = wx.Button( self.m_panel, wx.ID_ANY, u"<-- Preview", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_btnPreview, 0, wx.ALL, 5 )
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer3.Add( bSizer5, 2, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Destination Folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer4.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		
		bSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_chkAddToPath = wx.CheckBox( self.m_panel, wx.ID_ANY, u"Add Gallery Name to Path", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_chkAddToPath, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_tbxDestFolder = wx.TextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_tbxDestFolder, 1, wx.ALL, 5 )
		
		self.m_btnBrowse = wx.Button( self.m_panel, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer4.Add( self.m_btnBrowse, 0, wx.ALL, 5 )
		
		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		self.m_btnDownload = wx.Button( self.m_panel, wx.ID_ANY, u"Download Images", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_btnDownload, 0, wx.ALL, 5 )
		
		self.m_panel.SetSizer( bSizer3 )
		self.m_panel.Layout()
		bSizer3.Fit( self.m_panel )
		bSizer2.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar = wx.MenuBar( 0 )
		self.m_mnFile = wx.Menu()
		self.m_mniPreferences = wx.MenuItem( self.m_mnFile, wx.ID_PREFERENCES, u"P&references", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniPreferences )
		
		self.m_mnFile.AppendSeparator()
		
		self.m_mniExit = wx.MenuItem( self.m_mnFile, wx.ID_EXIT, u"&Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniExit )
		
		self.m_menubar.Append( self.m_mnFile, u"&File" ) 
		
		self.m_mnHelp = wx.Menu()
		self.m_mniAbout = wx.MenuItem( self.m_mnHelp, wx.ID_ABOUT, u"&About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnHelp.AppendItem( self.m_mniAbout )
		
		self.m_menubar.Append( self.m_mnHelp, u"&Help" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		
		# Connect Events
		self.m_btnGetGalleries.Bind( wx.EVT_BUTTON, self.m_btnGetGalleriesClick )
		self.m_lstGalleries.Bind( wx.EVT_LISTBOX, self.m_lstGalleriesOnListBox )
		self.m_lstImages.Bind( wx.EVT_LISTBOX, self.m_lstImagesOnListBox )
		self.m_btnPreview.Bind( wx.EVT_BUTTON, self.m_btnPreviewClick )
		self.m_btnBrowse.Bind( wx.EVT_BUTTON, self.m_btnBrowseClick )
		self.m_btnDownload.Bind( wx.EVT_BUTTON, self.m_btnDownloadClick )
		self.Bind( wx.EVT_MENU, self.m_mniPreferencesClick, id = self.m_mniPreferences.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniExitClick, id = self.m_mniExit.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniAboutClick, id = self.m_mniAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_btnGetGalleriesClick( self, event ):
		event.Skip()
	
	def m_lstGalleriesOnListBox( self, event ):
		event.Skip()
	
	def m_lstImagesOnListBox( self, event ):
		event.Skip()
	
	def m_btnPreviewClick( self, event ):
		event.Skip()
	
	def m_btnBrowseClick( self, event ):
		event.Skip()
	
	def m_btnDownloadClick( self, event ):
		event.Skip()
	
	def m_mniPreferencesClick( self, event ):
		event.Skip()
	
	def m_mniExitClick( self, event ):
		event.Skip()
	
	def m_mniAboutClick( self, event ):
		event.Skip()
	

