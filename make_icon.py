# Pixel art ikon generátor (nem kell hozzá külső csomag): python3 tools/make_icon.py
import math,zlib,struct
N=64
def hs(n):
    n=math.sin(n*127.1+311.7)*43758.5453;return n-math.floor(n)
def mix(a,b,t):return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
g=[[(0,0,0)]*N for _ in range(N)]
def put(x,y,c):
    if 0<=x<N and 0<=y<N:g[int(y)][int(x)]=c
for y in range(N):
    for x in range(N):
        t=min(1,int(y/44*6)/6);g[y][x]=mix((70,150,222),(208,238,252),t)
def disc(cx,cy,r,c):
    for y in range(-r,r+1):
        for x in range(-r,r+1):
            if x*x+y*y<=r*r:put(cx+x,cy+y,c)
disc(50,12,9,(255,245,190));disc(50,12,6,(255,226,110));disc(49,11,3,(255,250,210))
def cloud(x,y):
    for dx,dy,w in((0,0,12),(2,-2,8),(4,-3,4)):
        for i in range(w):put(x+dx+i,y+dy,(250,252,255))
    for i in range(12):put(x+i,y+1,(190,205,225))
cloud(6,10);cloud(34,5)
for x in range(N):
    h=int(40+math.sin(x*.12+1)*3+math.sin(x*.3)*1);
    for y in range(h,50):put(x,y,mix((60,130,110),(90,160,100),(x%7)/7*.4))
for x in range(N):
    h=int(44+math.sin(x*.2+3)*2)
    for y in range(h,50):put(x,y,(60,140,70))
for y in range(50,N):
    for x in range(N):
        d=(y-50)/14;r=hs(x*1.7+y*31.3)
        base=mix((128,92,58),(84,58,38),d);k=int((r-.5)*22)
        put(x,y,tuple(max(0,min(255,c+k)) for c in base))
for x in range(N):
    put(x,50,(110,200,80));put(x,51,(70,150,60))
    if hs(x*3.1)>.55:put(x,49,(150,225,100))
# gyökerek
for ang,ln in((.25,16),(.45,12),(.65,10),(.85,14),(1.05,11),(1.25,15),(1.45,9),(.15,9)):
    for s in range(ln):
        for sg in(1,-1):
            put(32+sg*math.cos(ang)*s*1.1+(0 if sg>0 else 0),52+math.sin(ang)*s*.8+(s>6)*0,(216,178,124))
# törzs
for y in range(24,50):
    f=(50-y)/26;w=int(3.5-f*1.2)
    for x in range(-w,w+1):
        put(32+x,y,(58,36,18) if x<=-w else (154,106,62) if x>=w else (107,68,38))
# ágak
def branch(x0,y0,x1,y1,c):
    n=int(max(abs(x1-x0),abs(y1-y0)))+1
    for i in range(n+1):put(x0+(x1-x0)*i/n,y0+(y1-y0)*i/n,c)
for b in((32,34,20,26),(32,32,44,24),(32,28,24,18),(32,27,41,17),(32,24,32,14)):branch(*b,(90,56,32))
PAL=[(31,90,42),(47,125,50),(76,175,61),(139,216,78)]
def blob(cx,cy,r,o):
    for y in range(-r,r+1):
        for x in range(-r,r+1):
            if x*x+y*y>r*r:continue
            l=max(0,min(.999,(-x*.5-y)/r*.5+.5+(hs((x+cx)*7.3+(y+cy)*13.1+o)-.5)*.55+(.04 if (x+y)&1 else -.04)))
            c=PAL[0] if (r>2 and y>0 and x*x+y*y>(r-1.5)**2) else PAL[int(l*4)]
            put(cx+x,cy+y,c)
for cx,cy,r,o in((19,28,8,1),(45,28,8,2),(24,19,10,3),(40,19,10,4),(32,12,11,5),(32,21,11,6),(15,22,6,7),(49,21,6,8)):blob(cx,cy,r,o)
# virágok a fűben
for x,c in((8,(255,107,139)),(16,(255,209,102)),(48,(184,140,255)),(56,(248,244,255)),(22,(255,209,102))):
    put(x,48,(63,143,58));put(x,47,c);put(x+1,47,c)
def png(path,k):
    rows=[[px for px in row for _ in range(k)] for row in g for _ in range(k)]
    raw=b''.join(b'\x00'+b''.join(bytes(c) for c in r) for r in rows)
    ch=lambda t,d:struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
    open(path,'wb').write(b'\x89PNG\r\n\x1a\n'+ch(b'IHDR',struct.pack('>IIBBBBB',N*k,N*k,8,2,0,0,0))+ch(b'IDAT',zlib.compress(raw))+ch(b'IEND',b''))
png('icon-512.png',8)
# 192: 64*3
png('icon-192.png',3)
