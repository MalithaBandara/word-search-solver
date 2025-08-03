from PIL import Image,ImageDraw
import random
import colorsys

def highlight(answers):
    img = Image.open('assets/grid.png').convert('RGBA')
    overlay = Image.new('RGBA',img.size,(255,255,255,0))
    draw = ImageDraw.Draw(overlay)
    for a in answers:
        h = random.random()
        s = random.uniform(0.5,1.0)
        l = random.uniform(0.5,0.6)
        r,g,b = colorsys.hls_to_rgb(h,l,s)
        r,g,b = int(r*255),int(g*255),int(b*255)
        p = int((a[0][2]-a[0][0])/2)
        q = int((a[0][3]-a[0][1])/2)
        if a[2] < 4:
            x = [min(a[0][0],a[0][2],a[1][0],a[1][2]),min(a[0][1],a[0][3],a[1][3],a[1][1])]
            y = [max(a[0][0],a[0][2],a[1][0],a[1][2]),max(a[0][1],a[0][3],a[1][3],a[1][1])]
            draw.rectangle([x,y],fill=(r,g,b,150),outline=None,width=1)
        elif a[2] < 6:
            x = [min(a[0][0],a[0][2],a[1][0],a[1][2]),max(a[0][1],a[0][3],a[1][3],a[1][1])]
            y = [max(a[0][0],a[0][2],a[1][0],a[1][2]),min(a[0][1],a[0][3],a[1][3],a[1][1])]
            draw.polygon([(x[0]-p,x[1]-q/2),(x[0]+p/2,x[1]+q),(y[0]+p/2,y[1]+q),(y[0]-p,y[1]-q/2)],fill=(r,g,b,150),outline=None)

        else:
            x = [min(a[0][0],a[0][2],a[1][0],a[1][2]),min(a[0][1],a[0][3],a[1][3],a[1][1])]
            y = [max(a[0][0],a[0][2],a[1][0],a[1][2]),max(a[0][1],a[0][3],a[1][3],a[1][1])]
            draw.polygon([(x[0]+p,x[1]-q/2),(x[0]-p/2,x[1]+q),(y[0]-p,y[1]+q/2),(y[0]+p/2,y[1]-q)],fill=(r,g,b,150),outline=None)
        
    outpt = Image.alpha_composite(img,overlay)
    outpt.save('assets/output.png')       
