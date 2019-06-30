SETUP
(1) download https://github.com/digitalmadness/webtorrent.streamer/releases/download/1.4.8.8/streamer.exe to C:\Program Files\webtorrent.streamer\
(2) install https://nodejs.org/en/download/
(3) run in cmd:
     npm install webtorrent-cli -g
(4) open regedit and navigate to HKEY_CLASSES_ROOT\magnet\shell\open\command
(5) add string with value "C:\Program Files\webtorrent.streamer\streamer.exe" -m "%1"
PROFIT
downloaded files are stored at %localappdata%\Temp\webtorrent
