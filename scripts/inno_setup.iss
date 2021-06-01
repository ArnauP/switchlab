[Setup]
AppName=KB Switch simulator
AppVersion=1.0.0
AppPublisher=ArnauP
DefaultDirName={pf}\KBSS
DisableProgramGroupPage=yes
OutputBaseFilename=KB Switch Simulator 1.0.0
Compression=lzma
SolidCompression=yes
LicenseFile=license.rtf
UninstallDisplayIcon={app}\kbss\kbss.exe
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
Name: "{commonprograms}\KB Switch Simulator 1.0.0"; Filename: "{app}\kbss\kbss.exe"
Name: "{commondesktop}\KB Switch Simulator 1.0.0"; Filename: "{app}\kbss\kbss.exe"; Tasks: desktopicon


[InstallDelete]
Type: files; Name: "{commonprograms}\KB Switch Simulator*.lnk"
Type: files; Name: "{commondesktop}\KB Switch Simulator*.lnk"

[Run]
Filename: "{app}\kbss\kbss.exe"; Description: "{cm:LaunchProgram,KB Switch Simulator}"; Flags: nowait postinstall skipifsilent

[Code]
// Utility functions for Inno Setup
//   used to add/remove programs from the windows firewall rules
// Code originally from http://news.jrsoftware.org/news/innosetup/msg43799.html
