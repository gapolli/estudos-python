import winsound
freq = 400
dur = 100
for x in range(0,100):
    winsound.Beep(freq,dur)
    freq = freq+10
