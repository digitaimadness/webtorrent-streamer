Name "webtorrent.streamer"
OutFile "setup.exe"
InstallDir "C:\Program Files\webtorrent-streamer"
RequestExecutionLevel admin
Page directory
Page instfiles
Section ""
  SetOutPath $INSTDIR
  File webtorrent.exe
  File mpv.exe
  File mpv.com
  File d3dcompiler_43.dll
  File mpv.conf
  NSISdl::download "http://nodejs.org/dist/v10.15.3/node-v10.15.3-x64.msi" "C:\Windows\Temp\node-v10.15.3-x64.msi"
  ExecWait 'msiexec /i "C:\Windows\Temp\node-v10.15.3-x64.msi"'
  ExecWait 'npm install webtorrent-cli -g'
  ExecWait 'REG ADD HKEY_CLASSES_ROOT\Magnet\shell\open\command /f /t REG_SZ /d "\"C:\\Program Files\\webtorrent-streamer\\webtorrent.exe\" -m \"%1\""'
SectionEnd