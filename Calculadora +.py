import numpy as np 
import os
os.system ('cls')
import colorama
from colorama import Fore,Back,Style
colorama.init()
    
print(Fore.LIGHTCYAN_EX+'===========================================')
print(Fore.LIGHTGREEN_EX +'Seja bem vindo a sua super calculadora! ')                               #Quando eu for colocar o outro while eu tenho que colocar os IF's
print(Fore.LIGHTCYAN_EX+'===========================================')                              # juntos obviamente!

#Esse é o menu inicial
historico_de_contas=[]       
while True:                                                     
        opção=input(Fore.LIGHTCYAN_EX+'''
             O que você deseja Calcular?    
          
          (1) Contas ordinárias    
          (2) Fahrenheit e celsius                  
          (3) Juros
          (4) Histórico
          (5) Sair
           ===>  ''')
        if opção not in ['1','2','3','4','5']:
            print(Fore.LIGHTRED_EX+'Essa opção não existe!')
            input( Fore.LIGHTWHITE_EX+'Pressione enter para voltar ao menu!')     
        if opção == '1':
            while True:
                print(Fore.LIGHTCYAN_EX+'='*43)
                contas_ordinárias=input(Fore.CYAN+'''
                    (1) Adição
                    (2) Subtração
                    (3) Multiplicação
                    (4) Divisão
                    (5) Potencialização
                    (6) Sair
                    ===> ''')
                    #Menu dentro do menu, próprio para as contas ordinárias!

                                      
                if contas_ordinárias =='1':                                                               
                        try:
                            numero1=int (input (Fore.LIGHTGREEN_EX+'Digite um número: '))
                            numero2=int (input(Fore.LIGHTGREEN_EX+'Digite um número: '))
                        except ValueError:
                            print(Fore.LIGHTRED_EX+"Nesse campos só é permitido números")
                            input(Fore.LIGHTWHITE_EX+'Pressione enter para voltar ao menu!')
                            continue    
                        adição= numero1 + numero2
                        historico_de_contas.append(adição)  #tentar adicionar na lista
                        print(Fore.LIGHTGREEN_EX+'====================================')
                        print(Fore.LIGHTGREEN_EX+  f'O resultado dessa adição é {adição}')
                        print(Fore.LIGHTGREEN_EX+'====================================')
                        input(Fore.LIGHTWHITE_EX+'Pressione enter para voltar ao menu!') 
                elif contas_ordinárias =='2':
                        try:
                            numero1=int (input(Fore.LIGHTGREEN_EX+'Digite um número: '))
                            numero2=int (input(Fore.LIGHTGREEN_EX+'Digite um número: '))
                        except ValueError:
                            print(Fore.LIGHTRED_EX+' Nesse campos só é permitido números')
                            input( Fore.LIGHTWHITE_EX+'Pressione enter para voltar!') 
                            continue
                        subtração= numero1 - numero2
                        print(Fore.LIGHTGREEN_EX+'====================================')
                        print(Fore.LIGHTGREEN_EX+  f'O resultado dessa subtração é {subtração}')
                        print(Fore.LIGHTGREEN_EX+'====================================')
                elif contas_ordinárias =='3':
                        try:
                            numero1=int (input(Fore.LIGHTGREEN_EX+'Digite um número: '))
                            numero2=int (input(Fore.LIGHTGREEN_EX+'Digite um número: '))
                        except ValueError:
                            print(Fore.LIGHTRED_EX+"Nesse campos só é permitido números")  
                            input( Fore.LIGHTWHITE_EX+'Pressione enter para voltar!')
                            continue
                        multiplicação= numero1 * numero2
                        print(Fore.LIGHTGREEN_EX+'====================================')
                        print(Fore.LIGHTGREEN_EX+  f'O resultado dessa multiplicação é {multiplicação}')
                        print(Fore.LIGHTGREEN_EX+'====================================')
                        input( Fore.LIGHTWHITE_EX+'Pressione enter para voltar!')    
                elif contas_ordinárias =='4':
                            try:
                                numero1=int (input(Fore.LIGHTGREEN_EX+'Digite um número: '))
                                numero2=int (input(Fore.LIGHTGREEN_EX+'Digite um número: '))
                            except ValueError:
                                print(Fore.LIGHTRED_EX+'Nesse campo só é permitido números! ')
                                input( Fore.LIGHTWHITE_EX+'Pressione enter para voltar!')
                                continue
                            try:    
                                divisão= numero1 / numero2
                                
                            except ZeroDivisionError:
                                print(Fore.RED+'Não existe divisão por zero!')
                                input(Fore.LIGHTWHITE_EX+'Pressione enter para voltar!')                  #Esses try, e excepts são para controlar todos os possiveis erros cometidos
                            else:                                                                           #pelo usuário!
                                print(Fore.LIGHTGREEN_EX+'====================================')
                                print(Fore.LIGHTGREEN_EX+  f'O resultado dessa Divisão é {divisão}')
                                print(Fore.LIGHTGREEN_EX+'====================================')
                                input( Fore.LIGHTWHITE_EX+'Pressione enter para voltar!')    
                elif contas_ordinárias == '5':
                            try:
                                numero1= int (input(Fore.LIGHTGREEN_EX+'Digite um número: '))
                                numero2=int (input(Fore.LIGHTGREEN_EX+'Digite um número: '))
                            except ValueError:
                                print(Fore.LIGHTRED_EX+'Nesse campo só é permitido números! ')
                                input( Fore.LIGHTWHITE_EX+'Pressione enter para voltar!')
                                continue
                            potencialização= numero1 ** numero2
                            print(Fore.LIGHTGREEN_EX+'====================================')
                            print(Fore.LIGHTGREEN_EX+  f'O resultado dessa potencialização é {potencialização}')
                            print(Fore.LIGHTGREEN_EX+'====================================')
                            input( Fore.LIGHTWHITE_EX+'Pressione enter para voltar!')
                elif contas_ordinárias not in ['1', '2', '3','4,','5','6']:                     #Coloquei o controle de danos aqui, funciona na mesma maneira!
                    print(Fore.LIGHTRED_EX+'Essa opção não existe')
                    input(Fore.LIGHTWHITE_EX+'Pressione enter para voltar ao menu')
                elif contas_ordinárias == '6':
                        print(Fore.LIGHTWHITE_EX+'Você voltou para o inicio!')   
                        break
        elif opção =='2':
            print('Aqui você vai calcular a temperatura!')                                  #Menu de celcius
            try:
                celsius=float(input(Fore.LIGHTCYAN_EX+'Informe a temperatura em C° '))
            except ValueError:
                print(Fore.LIGHTRED_EX+'Nesse campo só é permitido números!')
                input(Fore.LIGHTWHITE_EX+'Pressione enter para voltar ao menu')
            else:
                fahrenheit=(9* celsius / 5) + 32
                print(Fore.LIGHTGREEN_EX+'='*60)
                print(Fore.LIGHTGREEN_EX+'A temperatura de {} celsius corresponde a {} fahrenheit'.format(celsius,fahrenheit))
                print(Fore.LIGHTGREEN_EX+'='*60)
        elif opção =='3':
            print('aqui você irar calcular juros! ') #aqui onde calcula a Bhaskara
            try:
                juros_para_calculo=float(input('Digite o numero do juros!'))
            except ValueError:
                print('Nesse campo só é permitido números!')
        elif opção =='4':
            print(Fore.LIGHTCYAN_EX+'='*50)
            print(Fore.LIGHTWHITE_EX+'essa é as contas que você realizou anteriormente ==>',  historico_de_contas)
            print(Fore.LIGHTCYAN_EX+'='*50)
        
        elif opção =='5':
            print(Fore.LIGHTWHITE_EX+'Fim do programa!')
            break  
       

           