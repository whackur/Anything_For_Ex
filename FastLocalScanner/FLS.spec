# -*- mode: python -*-

block_cipher = None


a = Analysis(['FLS.py'],
             pathex=['C:\\Users\\ioume\\coding\\Anything_For_Ex\\FastLocalScanner'],
             binaries=[('bin/arp-ping.exe', '.'), ('bin/nbt.exe', '.')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='FLS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , uac_admin=True)
