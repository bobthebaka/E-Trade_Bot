import re

def runPass(FileIn,FileOut):
    
    f = open(FileIn)
    results = ""
    for line in f:
        reformed = ''
        if "wx.DATAVIEW_CELL_ACTIVATABLE" in line:
            splits = line.split('wx.DATAVIEW_CELL_ACTIVATABLE')
            reformed = splits[0] + 'wx.dataview.DATAVIEW_CELL_ACTIVATABLE' + splits[1]
            print (reformed)

        if "wx.DATAVIEW_COL_RESIZABLE" in line:
            splits = line.split('wx.DATAVIEW_COL_RESIZABLE')
            reformed = splits[0] + 'wx.dataview.DATAVIEW_COL_RESIZABLE' + splits[1]
            print (reformed)

        if "self.Text_SerialNumber = wx.TextCtrl" in line:
            reformed = line.replace(', 0 )',',wx.TE_PROCESS_ENTER) ')
            
            print (reformed)

        if reformed == '':
            results += line
            
        else:
            results += reformed
            print("adding NewLine")

    f.close()

    out = open(FileOut,mode='w')
    out.write(results)
    out.flush()
    out.close()


if __name__ == "__main__":

    runPass("etrade_python_client.py","etrade_python_client.py")
    runPass("etrade_python_client.py","etrade_python_client.py")
    runPass("etrade_python_client.py","etrade_python_client.py")
    runPass("etrade_python_client.py","etrade_python_client.py")

