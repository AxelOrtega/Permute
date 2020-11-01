import os
import sys
import time
import string
import argparse
import itertools

'''sys.setdefaultencoding('utf-8')'''


def createWordList(chrs, min_longitud, max_longitud, salida):

    if min_longitud > max_longitud:
    	print ("[!] El rango minimo tiene que ser menor o igual al rango maximo")
    	sys.exit()
        
    if os.path.exists(os.path.dirname(salida)) == False:
        os.makedirs(os.path.dirname(salida))

    print ('[+] Creando diccionario en `%s`...' % salida)
    print ('[i] Inicio: %s' % time.strftime('%H:%M:%S'))

    salida = open(salida, 'w')

    for n in range(min_longitud, max_longitud + 1):
        for xs in itertools.product(chrs, repeat=n):
            caracteres = ''.join(xs)
            salida.write("%s\n" % caracteres)
            sys.stdout.write('\r[+] Guardando Caracter `%s`' % caracteres)
            sys.stdout.flush()
    salida.close()

    print ('\n[i] Termino %s' % time.strftime('%H:%M:%S'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Generador de diccionarios')
    parser.add_argument(
        '-c', '--caracteres',
        default=None, help='Caracteres a usar')
    parser.add_argument(
        '-mn', '--min_longitud', type=int,
        default=1, help='Minimo de caracteres')
    parser.add_argument(
        '-mx', '--max_longitud', type=int,
        default=2, help='Maximo de caracteres')
    parser.add_argument(
        '-s', '--salida',
        default='salida/wordlist.txt', help='salida of wordlist file.')

    args = parser.parse_args()
    if args.caracteres is None:
        args.caracteres = string.printable.replace(' \t\n\r\x0b\x0c', '')
    createWordList(args.caracteres, args.min_longitud, args.max_longitud, args.salida)
