# 1 leiviskä on 20 naulaa
# 1 naula on 32 luotia
# 1 luoti on 13.3 grammaa

#naula = 425.6
#leiviska = 8512
#luoti= 13.3



leiviska_string = input('Anna leiviskät: ')
naula_string = input('Anna naulat: ')
luoti_string = input('Anna luodit: ')

leiviska = float(leiviska_string) * 8512
naula = float(naula_string) * 425.6
luoti = float(luoti_string) * 13.3

massa = leiviska + naula + luoti
yhteispaino = massa / 1000
yhteispaino_int = int(yhteispaino)
ylijaama = int((yhteispaino - int(yhteispaino)) * 1000)

print('Massa nykymittojen mukaan on ' + str(yhteispaino_int) + ' kilogrammaa ja ' + str(ylijaama) + ' grammaa.')