from PIL import Image,ImageDraw
import random
import colorsys

def highlight(answers):
    img = Image.open('assets/grid.png').convert('RGBA')
    overlay = Image.new('RGBA',img.size,(255,255,255,0))
    draw = ImageDraw.Draw(overlay)
    for a in answers:
        if a[2] < 4:
            x = [min(a[0][0],a[0][2],a[1][0],a[1][2]),min(a[0][1],a[0][3],a[1][3],a[1][1])]
            y = [max(a[0][0],a[0][2],a[1][0],a[1][2]),max(a[0][1],a[0][3],a[1][3],a[1][1])]
            h = random.random()
            s = random.uniform(0.5, 1.0)
            l = random.uniform(0.5, 0.6)
            r,g,b = colorsys.hls_to_rgb(h, l, s)
            r,g,b = int(r * 255),int(g * 255),int(b * 255)
            draw.rectangle([x,y],fill=(r,g,b,150),outline=None,width=1)
    outpt = Image.alpha_composite(img,overlay)
    outpt.save('assets/output.png')       
