import wave,struct
source = wave.open("result1.wav", mode="rb")
result = wave.open("resuk3.wav", mode="wb")
print("vvedite tip iskajeniya  zatem ego stepen")
c=str(input())
k=int(input())
params = source.getparms()
result.steparams(params)
nawdata=[]
nframs = sourse.getparams()
n2frames = source.getnframs()
n2frames=[]
data = struct.unoack("<"+str(nframes)+"h", source.readfames(nframes))
if c=="zamedlit":
    for frame in data :
        for j in  range  (k):
            nawdata.append(frame)
newframes =struct.park("<" + str (nframes*k) + "h" , *nawdata)
restult.writeframs(newframes)
s=="uskorit"
for i in range (0,len(data),k):
    nawdata.sppend(data[1])
newframes =struct.park("<" + str (nframes/k) + "h" , *nawdata)
restult.writeframs(newframes)   
    
