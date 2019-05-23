.exe version:
https://github.com/digitalmadness/webtorrent.streamer/releases/download/3.1/setup.exe

.py version:
(1) download zip and extract to C:\Program Files\
(2) install https://nodejs.org/en/download/
(3) run in cmd:
     npm install webtorrent-cli -g
     REG ADD HKEY_CLASSES_ROOT\Magnet\shell\open\command /f /t REG_SZ /d "\"C:\Program Files\webtorrent.streamer-master\magnethandler.bat\" \"%1\""