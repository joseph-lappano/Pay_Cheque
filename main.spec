# main.spec

from PyInstaller.utils.hooks import collect_all
from PyInstaller.building.build_main import Analysis, PYZ, EXE

project_dir = r"C:\Users\Joeyl\Desktop\To be EXEd"

# Collect all pandas data, binaries, and hidden imports
datas, binaries, hiddenimports = collect_all('pandas')

# Your additional data files (PNGs and TTF)
additional_datas = [
    ('icon.png', '.'),     # source, destination folder inside exe
    ('number.png', '.'),
    ('search.png', '.'),
    ('times.ttf', '.'),
]

# Combine pandas datas with your own
datas += additional_datas

a = Analysis(
    ['main.py'],        # your main script
    pathex=['C:\\Users\\Joeyl\\Desktop\\To be EXEd'],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Pay Cheque',
    debug=False,
    strip=False,
    upx=True,
    console=True,         # False = no console window (windowed app)
    icon='icon.ico'        # your icon file, make sure you have icon.ico here
)
