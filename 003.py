km = float(input('Quantos kms: '))
minutos = int(input('Quantos minutos: '))
segundos = int(input('Quantos segundos: '))
milhas = km/1.61
totalsegundos = (minutos * 60) + segundos
hora = totalsegundos/3600
velocidade = milhas/hora
print('a velocidade media foi de {:.2f} milhas por hora'.format(velocidade))