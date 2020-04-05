# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['path/BLE_LED_Display/GUI_/LED_GUI.py'],
             pathex=['path'],
             binaries=[],
             datas=[("path/BLE_LED_Display/GUI_/connect.sh","."),
("path/BLE_LED_Display/GUI_/LED.png","."),
("path/BLE_LED_Display/GUI_/LEDoff.png", "."),
("path/BLE_LED_Display/GUI_/LEDon.png","."),
("path/BLE_LED_Display/GUI_/script2.sh","."),
("path/BLE_LED_Display/GUI_/theWrite.sh","."),
("path/BLE_LED_Display/GUI_/write.sh","."),
("path/BLE_LED_Display/GUI_/write2.sh","."),
("path/BLE_LED_Display/GUI_/writeArray.sh",".")],
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
          [],
          exclude_binaries=True,
          name='LED_GUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='LED_GUI')
