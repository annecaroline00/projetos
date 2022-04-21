def par (num):
    return num % 2 == 0


def digi_tres (num):
    return num >= 100 and num <= 999


if __name__ == "__main__":
    num = int(input().strip())

    d1 = num//100 #392//100 = 3
    d2 = (num//10)%10 #392//10 = 39 %10 = 3
    d3 = num % 10  #392%10 = 39

    qtdpar = 0
    if (digi_tres(num) and par(d1)):
        qtdpar = qtdpar + 1
    if (digi_tres(num) and par(d2)):
        qtdpar = qtdpar + 1
    if (digi_tres(num) and par(d3)):
        qtdpar = qtdpar + 1
    print(qtdpar)