# -*- mode: python -*-

block_cipher = None

a = Analysis(['bin/switchlab'],
             pathex=['.'],
             binaries=None,
             datas=[('resources/sfx', 'resources/sfx')],
             hiddenimports=['PyQt5', 'PyQt5.sip', 'six', 'ctypes', 'ctypes.wintypes', 'queue'],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='kbss',
          debug=False,
          strip=False,
          upx=True,
          console=False,
		  icon='resources\\icons\\app_icon.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='kbss')

app = BUNDLE(coll,
             name='kbss.app',
             icon='resources/icons/app_icon.icns',
             bundle_identifier=None)
