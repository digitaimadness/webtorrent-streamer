import pyperclip,subprocess,time,datetime,psutil,os,shutil,wx,argparse,sys


def startup():
    app = wx.App()
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--magnet', default='null')
    args = parser.parse_args()
    if args.magnet == 'null':
        if not 'magnet:' in pyperclip.paste(): #check clipboard if no argument was provided
            launch(magnetdialog('insert magnet link').split('&')[0])  #prompt user
        else:
            launch(pyperclip.paste().split('&')[0])
    elif 'magnet:' in args.magnet:
        launch(args.magnet.split('&')[0])


def launch(magnet):
    seekhappened = False
    timestart = time.time()
    subprocess.call('webtorrent '+magnet+' --mpv',shell=True)
    with open(os.getenv('APPDATA')+r'\mpv\log') as mpvlogfile:
        mpvlog = mpvlogfile.readlines()
    for duration in mpvlog:
        if 'duration' in duration:
            duration = int(duration.split(': ')[1].split('.')[0])
            break
    for lastseek in mpvlog:
        if 'seek to' in lastseek:
            seekhappened = True
            lastseektime = int(float(lastseek.split(']')[0].split('[   ')[1]))
            lastseek = int(lastseek.split('to ')[1].split('.')[0])
            break
    if seekhappened:
        timepassedsincelastseek = int(time.time()-timestart)-lastseektime
        timeleft = duration-(lastseek+int(timepassedsincelastseek))
    else:
        timeleft = duration-int(time.time()-timestart)
    if timeleft>duration*0.1 and dialog('restart? '+str(datetime.timedelta(seconds=timeleft))+' left to watch'):
        launch(magnet)


def magnetdialog(message,parent=None):
    dlg = wx.TextEntryDialog(parent, message)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    if 'magnet:' in result:
        return result
    elif result == '':
        sys.exit()
    else:
        return magnetdialog('not magnet link! try again..')


def dialog(message):
    dlg = wx.MessageDialog(None,message,'',wx.YES_NO | wx.ICON_QUESTION)
    result = dlg.ShowModal()
    if result == wx.ID_YES:
        return True


if __name__ == '__main__':
    startup()
