import time
chave = False
f = 440
t = 1/f
i = 0
for i in range (0, 1000):
    if chave == True:
        print('Ligado')
        time.sleep(t/2)
        chave = False
    else:
        print('Desligado')
        time.sleep(t/2)
        chave = True
