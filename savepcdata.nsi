Name "Save Pesterchum Data"

OutFile "savepesterchumdata.exe"

InstallDir $DESKTOP

Page directory
Page instfiles


Section "PesterchumData"

  SectionIN RO
  

  IfFileExists "$LOCALAPPDATA\pesterchum" 0 checkbackup
  CreateDirectory $INSTDIR\pesterchumdata
  CopyFiles "$LOCALAPPDATA\pesterchum\*.*" $INSTDIR\pesterchumdata
  MessageBox MB_OK "Pesterchum data saved!"
  Goto done

  checkbackup:
  IfFileExists "$TEMP\pesterchum_backup" 0 nodata
  MessageBox MB_OK "
  nodata:
  MessageBox MB_OK "Data not found!"
  done: