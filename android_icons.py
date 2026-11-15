# Az Android indítóikon cseréje a játék ikonjára (a GitHub Actions futtatja az APK építésekor)
import os,shutil
from PIL import Image
src=Image.open('icon-512.png').convert('RGBA')
res='android/app/src/main/res'
for d,s in {'mdpi':48,'hdpi':72,'xhdpi':96,'xxhdpi':144,'xxxhdpi':192}.items():
    p=f'{res}/mipmap-{d}';os.makedirs(p,exist_ok=True)
    im=src.resize((s,s),Image.NEAREST)
    for n in('ic_launcher.png','ic_launcher_round.png','ic_launcher_foreground.png'):im.save(f'{p}/{n}')
shutil.rmtree(f'{res}/mipmap-anydpi-v26',ignore_errors=True)
print('Android ikonok kész')
