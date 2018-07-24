# -*- mode: python -*-

block_cipher = None


a = Analysis(['robot.py', 'lottery.py', 'window.py', 'backend.py'],
             pathex=['D:\\大三下\\小机器人\\抽卡'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='robot',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
