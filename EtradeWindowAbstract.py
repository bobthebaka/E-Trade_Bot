# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 872,722 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Login", True )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Active", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_List_Active_Symbols = wx.dataview.DataViewListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn3 = self.m_List_Active_Symbols.AppendTextColumn( u"Symbol", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer2.Add( self.m_List_Active_Symbols, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Disabled", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_List_Disabled_Symbols = wx.dataview.DataViewListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn12 = self.m_List_Disabled_Symbols.AppendTextColumn( u"Symbol", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer2.Add( self.m_List_Disabled_Symbols, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( bSizer2, 1, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer7.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_Filter = wx.Button( self.m_panel2, wx.ID_ANY, u"Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button_Filter, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer6.Add( bSizer71, 1, wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Price Range", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )

		bSizer711 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl_Min = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer711.Add( self.m_textCtrl_Min, 1, wx.ALL, 5 )

		self.m_textCtrl_Max = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer711.Add( self.m_textCtrl_Max, 1, wx.ALL|wx.RIGHT, 5 )


		bSizer6.Add( bSizer711, 1, wx.EXPAND, 5 )


		bSizer7.Add( bSizer6, 2, wx.EXPAND, 5 )

		self.m_staticline11 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer7.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Curent Symbol List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer11.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_List_Symbols_Current = wx.dataview.DataViewListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_ROW_LINES )
		self.m_dataViewListColumn31 = self.m_List_Symbols_Current.AppendTextColumn( u"Symbol", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer11.Add( self.m_List_Symbols_Current, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer7.Add( bSizer11, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer7 )
		self.m_panel2.Layout()
		bSizer7.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Stocks", False )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer111 = wx.BoxSizer( wx.VERTICAL )

		self.m_button2 = wx.Button( self.m_panel3, wx.ID_ANY, u"Do Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_textCtrl_Symbols = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"MSFT", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_textCtrl_Symbols, 0, wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self.m_panel3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer111.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer111 )
		self.m_panel3.Layout()
		bSizer111.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"Watch Settings", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_timer1.Start( 1000 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.Connect_Click )
		self.m_button2.Bind( wx.EVT_BUTTON, self.Do_Run_Click )
		self.Bind( wx.EVT_TIMER, self.TimerTick, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Connect_Click( self, event ):
		event.Skip()

	def Do_Run_Click( self, event ):
		event.Skip()

	def TimerTick( self, event ):
		event.Skip()


