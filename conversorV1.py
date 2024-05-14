def convert_binario(n):
     decimal = n
     if n == 0:
          return print('0')
     else:
          binario = ''
          while n > 1:
               resto = n%2
               n = int(n/2)
               binario += str(resto)
          binario += '1'
          return print('''    ******************************************************************************
                       A conversão do número decimal''',decimal,'''para binário é''', binario[-1::-1])
     

def convert_hexadecimal(n):
     tabela = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.upper().split()
     resto =[]
     n = int(n)
     while n > 0:
          resto.append(tabela[(n%16)])
          n = n // 16
          
     resto.reverse()
     return print( '''        *******************************************************************************
                                 A  conversão do número decimal ''',decimal,'''para o hexadecimal é = ''', ''.join(resto))



def conversao_para_octal(n):
     if n == 0:
          return '0'
     else:
          octal = ''
          while n > 0:
               resto = n%8
               n = int(n/8)
               octal += str(resto)
          return print('''  ************************************************************************************
                            A  conversão do número decimal ''',decimal ,''' para o octal é = ''', octal [-1::-1])

	
def detalhesPrograma():
     print('''
          ***********DETALHES DO SISTEMA******************
              CURSO: ANALISE E DESENVOLVIMENTO DE SISTEMA
              ALUNO: Hendrik Mariano
              RGM  : 31175163
              TURMA :4B
              DICIPLINAS ENVOVIDAS :
              ARQUITETURA DE COMPUTADORES
              PROGRAMAÇÃO DE COMPUTADORES
              VERSÃO DO PROGRAMA :1.0
           ''')
def fecharPrograma():
     exit()
     
     
while True:
     print('''  
                     APÓS SELECIONAR UMA OPÇÃO APERTE A TECLA ENTER          
                 *******************************************************''')
     opcoes = int (input('''
                  
                              *EXCOLHA UMA OPÇAO DO MENU*
                 *******************************************************
                  [1] CONVERSÃO PARA BINARIO
                  [2] CONVERSÃO PARA HEXADECIMAL
                  [3] CONVERSÃO PARA OCTAL
                  [4] DETALHES DO PROGRAMA
                  [5] Sair \n
                  '''))
     if opcoes == 1:
         
          decimal = int(input('''            Informe o número decimal que você gostaria de converter para binário: '''))
          convert_binario(decimal)
         
               
     elif opcoes == 2:
         
          decimal = int(input('              Informe o número decimal que você gostaria de converter para hexadecimal:'))
          
          convert_hexadecimal(decimal)

        
     elif opcoes == 3:
       
          decimal = int(input('              Informe o número decimal que você gostaria de converter para octal: '))
          conversao_para_octal(decimal)
          
     elif opcoes == 4:
         
          detalhesPrograma()

     elif opcoes == 5:
          fecharPrograma()
     else:
       print('                     OPÇÃO INVALIDA!')
