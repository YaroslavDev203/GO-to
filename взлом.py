import wave,struct 
source = wave.open ('secret.wav', mode = 'rb') 
result = wave.open ('resolt233.wav', mode = 'wb') 
source2 = wave.open ('key.wav', mode = 'rb') 
params = source.getparams() 
result.setparams(params) 
params = source.getparams() 
nframes = source.getnframes() 
nframes2 = source2.getnframes() 
data = struct.unpack('<'+str(nframes)+'h', source.readframes(nframes)) 
data2 = struct.unpack('<'+str(nframes2)+'h', source2.readframes(nframes2)) 
newdata = [] 
for i in range (len(data)): 
    newdata.append(data[i]^data2[i]) 
newframes = struct.pack ('<'+str(nframes) + 'h',*newdata) 
result.writeframes(newframes)
