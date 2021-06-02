[Setup]
AppName=SwitchLab
AppVersion=0.3.0
AppPublisher=Arnau Plans
DefaultDirName={pf}\SwitchLab
DisableProgramGroupPage=yes
OutputBaseFilename=SwitchLab 0.3.0
Compression=lzma
SolidCompression=yes
LicenseFile=license.rtf
UninstallDisplayIcon={app}\switchlab.exe
UsePreviousAppDir=yes

[Dirs]
Name: "{app}"; Permissions: everyone-full

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Permissions: everyone-full

[Icons]
Name: "{commonprograms}\SwitchLab 0.3.0"; Filename: "{app}\switchlab.exe"
Name: "{commondesktop}\SwitchLab 0.3.0"; Filename: "{app}\switchlab.exe"; Tasks: desktopicon


[InstallDelete]
Type: files; Name: "{commonprograms}\SwitchLab*.lnk"
Type: files; Name: "{commondesktop}\SwitchLab*.lnk"

[Run]
Filename: "{app}\switchlab.exe"; Description: "{cm:LaunchProgram,SwitchLab}"; Flags: nowait postinstall skipifsilent

[Code]
// Utility functions for Inno Setup
//   used to add/remove programs from the windows firewall rules
// Code originally from http://news.jrsoftware.org/news/innosetup/msg43799.html
