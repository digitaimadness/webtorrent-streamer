setup:
(1) download zip and extract to C:\Program Files\
(2) install Python and https://nodejs.org/en/download/
(3) run in cmd:
pip install pyperclip psutil
     npm install webtorrent-cli -g
     REG ADD HKEY_CLASSES_ROOT\Magnet\shell\open\command /f /t REG_SZ /d "\"C:\Program Files\webtorrent.streamer-master\magnethandler.bat\" \"%1\""
(4) add this to mpv.conf:
     log-file=~~/log
