from decimal import *
import decimal
from numeros_base import *

def unidade_dezena_centena(terno):
    numero_extenso = ''
    termos = len(terno)
    digito = terno[0]
    if termos == 3:
        if digito != 0:
            if terno[1:] == [0, 0]:
                if digito == 1:
                    numero_extenso += CENTENAS[0]
                else:
                    numero_extenso += CENTENAS[digito]
            else:
                numero_extenso += CENTENAS[digito] + ' e '
                numero_extenso += unidade_dezena_centena(terno[1:])
        else:
            numero_extenso += unidade_dezena_centena(terno[1:])
    if termos == 2:
        if digito != 0:
                if terno[1] == 0:
                    numero_extenso += DEZENAS[digito]
                elif digito == 1:
                    numero_extenso += DEZENA_ESPECIAL[terno[1]]
                else:
                    numero_extenso += DEZENAS[digito] + ' e ' + unidade_dezena_centena(terno[1:])
        else:
            numero_extenso += unidade_dezena_centena(terno[1:])
    elif termos == 1:
        numero_extenso += UNIDADES[digito]

    return numero_extenso


def milhares(ternos):
    numero_extenso = ''
    termos = len(ternos)
    terno = ternos[0]
    
    if termos >= 3:
        if terno != [0, 0, 0]:
            if terno == [0, 0, 1] or terno == [1]:
                numero_extenso += 'um ' + MILHAR[termos - 3][0]
            else:
                numero_extenso += unidade_dezena_centena(terno) + ' ' + MILHAR[termos - 3][1]

            if ternos[1:] == [[0, 0, 0],[0, 0, 0]]:
                return numero_extenso
            else:
                numero_extenso += ' ' + milhares(ternos[1:])
        else:
            numero_extenso += milhares(ternos[1:])

    if termos == 2:
        if terno != [0, 0, 0]: 
            numero_extenso += unidade_dezena_centena(terno) + ' mil' 
            if ternos[1] == [0, 0, 0]:
                return numero_extenso
            elif ternos[1][0]:
                numero_extenso += ' ' + milhares(ternos[1:])
            else:
                numero_extenso += ' e ' + milhares(ternos[1:])
        else:
            numero_extenso += ' ' + milhares(ternos[1:])
        
    elif termos == 1:
        if terno != [0, 0, 0]:
            numero_extenso += unidade_dezena_centena(terno)

    return numero_extenso



def separar_casas(numero):
    digitos = list(str(numero))
    tamanho = len(digitos)

    casa = tamanho % 3
    casas = []
    terno = []
    for i in range(tamanho):
        terno.append(int(digitos[i]))
        if (i + 1) % 3 == casa:
            casas.append(terno)
            terno = []
    return casas

def validar_tamanho(inteiro: int, decimal:str):
    max_algarismo_inteiro = 63
    max_algarismo_decimal = 36
    # A parte inteira  pode ter no maximo 33 algarismos
    if inteiro > int(max_algarismo_inteiro * '9'):
        raise ValueError('Valor muito grande')

    # A parte inteira  pode ter no maximo 33 algarismos
    if len(decimal) > max_algarismo_decimal:
        raise ValueError('Valor decimal muito grande')

def formatar_numero(numero:int or float or str):
    '''
    Função que formata um número real e retorna a parte inteira e a decimal.
    :param numero: Número real a ser formatado. Caso a entrada seja uma string, ela deverá estar no formato numérico brasileiro. Ex.: '1.000,00' ou '1000,00' ou '1000'
    return: (inteiro: int, decimal: str)
    '''
    
    if isinstance(numero, int):
        return (numero, '0')
    elif isinstance(numero, str):
        # remove os pontos
        numero = numero.replace('.', '')
        # Substitui a vírgula por ponto
        numero = numero.replace(',', '.')

        # verifica se o número é um float
        try:
            float(numero)
        except ValueError:
            raise TypeError('Número não formatado corretamente')

        partes = numero.split('.')
        inteiro = int(partes[0])
        if len(partes) == 1:
            decimal = '0'
        elif len(partes) == 2:
            decimal = partes[1]
        else:
            raise Exception('Número inválido')

        validar_tamanho(inteiro, decimal)
        return (inteiro, decimal)
        
    
    # se não for nenhum dos tipos acima, é porque o número não é um inteiro ou float.
    if numero == int(numero):
        return (int(numero), '0')

    inteiro = int(numero)
    decimal = numero - int(numero)
    decimal = str(decimal).split('.')[1]

    validar_tamanho(inteiro, decimal)
    
    return (inteiro, decimal)

def real(numero:float or str):
    '''
    Função que recebe um número real e retorna o número por extenso.
    :param numero: Número real a ser formatado.
    '''

    inteiro, decimal = formatar_numero(numero)
    extenso = milhares(separar_casas(inteiro))
    
    if int(decimal) != 0:
        ordem = len(str(decimal)) - 1
        decimal = int(decimal)
        
        
        if ordem > 11:
            ordem = 7 + ordem // 3 
    
        if inteiro == 0:
            extenso = ''
        elif inteiro == 1:
            extenso += ' inteiro e '
        else:
            extenso += ' inteiros e '

        if decimal == 1:
            plural = 0
        else:
            plural = 1

        extenso += milhares(separar_casas(decimal)) + ' ' + DECIMAIS[ordem][plural]
        
    return extenso

def monetario(numero:float or str):
    inteiro, decimal = formatar_numero(str(numero))
    extenso = milhares(separar_casas(inteiro))

    if inteiro == 0:
            extenso = ''
    elif inteiro == 1:
        extenso += ' real'
    else:
        extenso += ' reais'

    
    if decimal != None and int(decimal) != 0:
        ordem = len(decimal)
        if ordem == 1:
            decimal += '0'
            ordem = 2
        elif ordem > 11:
            ordem = 7 + ordem // 3
    
        if inteiro == 0:
            extenso = ''
        elif inteiro == 1:
            extenso += ' e '
        else:
            extenso += ' e '

        decimal = int(decimal)
        if decimal == 1:
            plural = 0
        else:
            plural = 1
        
        extenso += milhares(separar_casas(decimal))
        if decimal == 1:
            if ordem < 3:
                extenso += ' centavo'
            else:
                extenso +=' ' + DECIMAIS[ordem - 3][plural] + ' de centavo'
        elif decimal < 100:
            extenso +=' centavos'
        else:
            extenso +=' ' + DECIMAIS[ordem - 3][plural] + ' de centavo'
        
    return extenso

if __name__ == '__main__':
    
    while True:
        
        # numero = input('Digite um número real: ')
        numero = 0.02
        print(numero)
        extenso = real(numero)
        print(numero, extenso)
