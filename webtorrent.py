import pyperclip,subprocess,time,datetime,psutil,os,shutil,wx


def main(magnet):
    timestart = time.time()
    launch(magnet)
    seek = False
    with open(r'C:\Users\vl70x\AppData\Roaming\mpv\log') as mpvlogfile:
        mpvlog = mpvlogfile.readlines()
    for x in mpvlog:
        if 'duration' in x:
            x = int(x.split(': ')[1].split('.')[0])
            break
    for y in mpvlog:
        if 'seek to' in y:
            seek = True
            y = int(y.split('to ')[1].split('.')[0])
            break
    if seek:
        timeleft = x-y
    else:
        timeleft = x-(time.time()-timestart)
    if timeleft>x*0.1 and dialog('restart? '+str(datetime.timedelta(seconds=timeleft))+' left to watch',''):
        main(magnet)


def launch(magnet):
    return subprocess.call('webtorrent '+magnet+' --mpv',shell=True)


def txtdialog(parent=None, message='insert magnet link'):
    dlg = wx.TextEntryDialog(parent, message)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    return result


def dialog(header,message):
    dlg = wx.MessageDialog(None,header,message,wx.YES_NO | wx.ICON_QUESTION)
    result = dlg.ShowModal()
    if result == wx.ID_YES:
        return True


if __name__ == '__main__':
    app = wx.App()
    clipboard = pyperclip.paste()
    if not 'magnet:' in clipboard:
        clipboard = txtdialog()
    main(clipboard.split('&')[0])
