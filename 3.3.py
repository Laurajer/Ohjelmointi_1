#Kirjoita ohjelma, joka kysyy käyttäjän biologisen
# sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa,
# onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input('Anna sukupuoli: ')
if sukupuoli == 'mies':
    hemoglobiiniM = int(input('Anna hemoglobiini arvosi: '))
if hemoglobiiniM <= 134:
        print('Hemoglobiinisi on alhainen.')
if hemoglobiiniM >= 195:
        print('Hemoglobiinisi on korkea.')
if hemoglobiiniM >= 134 and hemoglobiiniM < 195:
            print('Hemoglobiinisi on normaali.')

if sukupuoli == 'nainen':
    hemoglobiiniN = int(input('Anna hemoglobiini arvosi: '))
if hemoglobiiniN <= 117:
        print('Hemoglobiinisi on alhainen.')
if hemoglobiiniN >= 175:
        print('Hemoglobiinisi on korkea.')
if hemoglobiiniN >= 117 and hemoglobiiniN < 175:
            print('Hemoglobiinisi on normaali.')
