def displayMenu():
    print('tradutor de expressões')
    print('='*13)
    print('Menu: ')
    print('     Mercúrio')
    print('     Plutão')
    print('     Jupiter')



textSpeakDictionary = {
    'Mercurio' : '91700000',
    'Plutão' : '5 bilhões',
    'Jupiter' : '628 milhões',

}
 

running = True

displayMenu()
ordem = input('Digite um planeta: ')
while running == True:

    menuChoice = input('>_').lower()

    if menuChoice == 'Mercurio':
        print('Mercurio está a 91700000km da Terra')

    