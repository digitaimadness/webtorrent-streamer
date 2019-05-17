import pyperclip,subprocess,time,psutil

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

clipboard = pyperclip.paste()
if 'magnet' in clipboard:
    proc = subprocess.Popen('webtorrent '+clipboard+' --mpv',shell=True)
    time.sleep(1)
    subprocess.run('mpv http://localhost:8000/0')
    '''try:
        proc.wait(timeout=3)
    except subprocess.TimeoutExpired:
        kill(proc.pid)'''