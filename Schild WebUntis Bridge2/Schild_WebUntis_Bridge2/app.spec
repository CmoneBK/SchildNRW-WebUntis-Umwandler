# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [
    ('templates', 'templates')
]

a = Analysis(
    ['app.py'],
    pathex=['C:\\Users\\Chris\\OneDrive\\Lehre\\BI - IT Arbeit\\Digitales Klassenbuch\\ProgrammierungsProjekte\\Schild WebUntis Bridge2\\Schild WebUntis Bridge2'],
             binaries=[],
             datas=added_files,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Schild WebUntis Bridge2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True)