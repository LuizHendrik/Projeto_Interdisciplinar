import tkinter #biblioteca usada para criar interfaces graficas (GUI) em python
from tkinter import * #biblioteca usada para criar interfaces graficas (GUI) em python
from tkinter import ttk #biblioteca usada para criar interfaces graficas (GUI) em python
import numpy as np #biblioteca usada para criar interfaces graficas (GUI) em python
#tkiunter é uma biblioteca usada para criar interfaces graficas (GUI) em python

#cores para o projeto (cores hexadecimais)

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca / white
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = '#e89613'  # laranja
co6 = "#8c8c8c"  # cinza
co7 = "#ff0000"  # vermelho
co8 = "#00ff00"  # verde
co9 = "#0000ff"  # azul
co10 = "#ffff00" # amarelo
co11 = "#ff00ff" # magenta
co12 = "#00ff00" # verde
co13 = "#800000" # marrom
co14 = "#008000" # verde escuro
co15 = "#000080" # azul escuro
co16 = "#808000" # oliva
co17 = "#800080" # roxo
co18 = "#008080" # teal
co19 = "#c0c0c0" # prata

#Mostrar informacoes da equipe do projeto

def mostrar_informacoes(): #função para mostrar as informações da equipe do projeto
    
# Defina as informações do aluno aqui
    
#Hendrik
    nome = "Hendrik Mariano"
    rgm = "31175163"
    
#Alex
    nome2 = "Alex Gobbo"
    rgm2 = "31433375"
    
#Victor
    nome3 = "Victor Araujo"
    rgm3 = "32186673"
    
# janela para exibir as informações da equipe
    
    info_janela = Toplevel(janela)  #cria a janela
    info_janela.title("Informações do Aluno")   #nome da janela
    info_janela.geometry("400x300")   #largura x altura da janela
    info_janela.configure(bg=co1)    #cor de fundo da janela
        
        
# Adicione os rótulos para exibir as informações da equipe
    
#Hendrik
    Label(info_janela, text="Nome: "        + nome, bg=co1).pack() #cria o label
    Label(info_janela, text="RGM: "         + rgm, bg=co1).pack()   #cria o label
       
    Label(info_janela, text="-------------------------------------------------------", bg="white").pack() #cria o label
#Alex
    Label(info_janela, text="Nome: "        + nome2, bg=co1).pack() #cria o label
    Label(info_janela, text="RGM: "         + rgm2, bg=co1).pack()
    
    Label(info_janela, text="-------------------------------------------------------", bg="white").pack()   #cria o label
#Victor
    Label(info_janela, text="Nome: "        + nome3, bg=co1).pack() #cria o label
    Label(info_janela, text="RGM: "         + rgm3, bg=co1).pack()   #cria o label

# Define a cor de fundo da tela principal (tela pai): co5

janela = Tk() #cria a janela principal
janela.title('CONVERSOR DE BASES NUMERICAS') #nome da janela

janela.geometry('400x400') #largura x altura da janela do programa
janela.configure(bg=co2) #cor de fundo da janela

# Separator para separar a barra de título da janela principal

style = ttk.Style() #define o estilo da janela
style.theme_use ('clam') #define o tema da janela

style.configure('TSeparator', background='#000000') #cor do separador da janela principal (barra de título) 
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1,ipadx=190) #cria o separador da janela principal (barra de título)

#Janelas de dois frames cima e baixo 

frame_cima = Frame(janela, width=400, height=60, bg=co1, pady=0, padx=0) #cria o frame cima
frame_cima.grid(row=1, column=0) #posiciona o frame cima na janela principal

frame_baixo = Frame(janela, width=400, height=300, bg=co1, pady=12, padx=20) #cria o frame baixo
frame_baixo.grid(row=2, column=0, sticky=NW) #posiciona o frame baixo na janela principal

#frame cima

app_nome = Label(frame_cima, text="Conversor de base numerica", relief=FLAT, anchor='center', font=('System 20'), bg=co2, fg=co1) #cria o label
app_nome.place(x=10, y=15) #posiciona o label na janela principal


# Lista global para armazenar o histórico das conversões
historico = [] #lista vazia para armazenar o histórico das conversões

# Função para adicionar uma conversão ao histórico
def adicionar_ao_historico(conversao): #função para adicionar uma conversão ao histórico
    historico.append(conversao) #adiciona a conversão ao espaço

# Função para mostrar o histórico das conversões
def mostrar_historico(): #função para mostrar o histórico das conversões
    historico_janela = Toplevel(janela) #cria a janela
    historico_janela.title("Histórico de Conversões") #nome da janela
    historico_janela.geometry("400x400") #largura x altura da janela
    historico_janela.configure(bg=co3) #cor de fundo da janela
    
    Label(historico_janela, text="Histórico de Conversões", bg=co1, font=("Verdana", 14)).pack(pady=20) #cria o label
    
    # Listabox para exibir o histórico
    historico_listbox = Listbox(historico_janela, width=60, height=15, font=('Verdana', 12)) #cria a listabox
    historico_listbox.pack(pady=20) #posiciona a listabox
    
    for conversao in historico: #percorre o histórico
        historico_listbox.insert(END, conversao) #insere a conversão na listabox


#Funcao converter para converter os valores de binario, octal, decimal e hexadecimal para decimal e mostrar na tela
def converter():
        
    def numero_para_decimal(numero, base): #função para converter os valores de binario, octal, decimal e hexadecimal para decimal e mostrar na tela
    
    # O número decimal correspondente a cada base é:
    # BINARIO ↔ 2
    # OCTAL ↔ 8
    # DECIMAL ↔ 10
    # HEXADECIMAL ↔ 16
        
        decimal     = int(numero, base) #converte o número para decimal
        binario     = bin(decimal) #converte o número decimal para binário
        octal       = oct(decimal) #converte o número decimal para octal
        hexadecimal = hex(decimal) #converte o número decimal para hexadecimal
        
# mostra os valores dentro das caixas de texto na tela 
        
        l_binario['text']     = str(binario[2:]) #mostra o número binário na caixa de texto
        l_octal['text']       = str(octal[2:])  #mostra o número octal na caixa de texto
        l_decimal['text']     = str(decimal)   #mostra o número decimal na caixa de texto
        l_hexadecimal['text'] = str(hexadecimal[2:].upper()) #mostra o número hexadecimal na caixa de texto
        
        
# Converte (int), (bin), (oct) e (hexa) para string para mostrar na tela 
    numero = e_valor.get() #pega o valor digitado pelo usuário
    base = combo.get() #pega a base selecionada
    
# definindo o valor da base a ser convertida para decimal (2,8,10,16)
    if base == 'BINARIO': #se a base for binário
        base = 2 #define a base como 2
    elif base == 'OCTAL': #se a base for octal
        base = 8 #define a base como 8
    elif base == "DECIMAL": #se a base for decimal
        base = 10 #define a base como 10
    else: #se a base for hexadecimal
        base = 16 #define a base como 16
    
# convertendo o número para decimal e mostrando na tela
    decimal = int(numero, base) #converte o número para decimal
    
# convertendo o número decimal para binário, hexadecimal e octal 
    binario = bin(decimal) #converte o número decimal para binário
    octal = oct(decimal) #converte o número decimal para octal
    hexadecimal = hex(decimal) #converte o número decimal para hexadecimal
    
# mostrando os valores nas caixas de texto na tela
    l_binario['text'] = str(binario[2:]) #mostra o número binário na caixa de texto
    l_octal['text'] = str(octal[2:]) #mostra o número octal na caixa de texto
    l_decimal['text'] = str(decimal) #mostra o número decimal na caixa de texto
    l_hexadecimal['text'] = str(hexadecimal[2:].upper()) #mostra o número hexadecimal na caixa de texto
    
#chamando funcao
    numero_para_decimal(numero, base) #chama a função para converter o número para decimal

# Adicionar conversão ao histórico
    conversao = f"{numero} ({base}) --> BIN: {binario[2:]}, OCT: {octal[2:]}, DEC: {decimal}, HEX: {hexadecimal[2:].upper()}" #cria a conversão
    adicionar_ao_historico(conversao) #chama a função para adicionar a conversão ao usuário
        
    
#frame baixo configurando o combobox e o entry 

bases = ['BINARIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL'] #cria uma lista com as bases
combo = ttk.Combobox(frame_baixo,width=12, justify=CENTER, font=('Ivy 12 bold')) #cria o combobox
combo['values'] = (bases) #coloca as bases dentro do combobox
combo.place(x=20, y=10) #posiciona o combobox
e_valor = Entry(frame_baixo, width=9, justify='center', font=("",13), highlightthickness=1, relief='solid') #cria o entry
e_valor.place(x=175, y=10) #posiciona o entry


#BOTOES NO FRAME BAIXO 
b_converter = Button(frame_baixo,command=converter, text="CONVERTER", relief=RAISED, overrelief= RIDGE, font=('Ivy 8 bold'), bg=co1, fg=co4) #cria o botão
b_converter.place(x=280, y=10) #posiciona o botão

b_info = Button(frame_baixo, text="Informaçôes dos Developers", command=mostrar_informacoes, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold'), bg=co1, fg=co4) #cria o botão
b_info.place(x=20, y=250) #posiciona o botão

b_historico = Button(frame_baixo, text="Histórico", command=mostrar_historico, relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold'), bg=co1, fg=co4) #cria o botão
b_historico.place(x=230, y=250) #posiciona o botão

l_binario = Label(frame_baixo, text="BINARIO",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co15, fg=co1) #cria o label
l_binario.place(x=35, y=60) #posiciona o label
l_binario = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4) #cria o label
l_binario.place(x=170, y=60) #posiciona o label

l_octal = Label(frame_baixo, text="OCTAL",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co14, fg=co1) #cria o label
l_octal.place(x=35, y=100) #posiciona o label
l_octal = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)   #cria o label
l_octal.place(x=170, y=100) #posiciona o label

l_decimal = Label(frame_baixo, text="DECIMAL",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co13, fg=co1) #cria o label
l_decimal.place(x=35, y=140) #posiciona o label
l_decimal = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4) #cria o label
l_decimal.place(x=170, y=140) #posiciona o label

l_hexadecimal = Label(frame_baixo, text="HEXADECIMAL    ",width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co5, fg=co1) #cria o label
l_hexadecimal.place(x=35, y=180) #posiciona o label
l_hexadecimal = Label(frame_baixo, text="",width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4) #cria o label
l_hexadecimal.place(x=170, y=180) #posiciona o label

#loop da janela principal 
janela.mainloop()

#Referencia da fonte para as cores
#Interface grafica e cores (https://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm, (https://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm), https://docs.python.org/pt-br/3/library/tk.html
#Referencia para os testes dos calculos de conversao das bases binario, octal, decimal e hexadecimal(https://www.calculadoraonline.com.br/conversao-bases)
#Referencia para o site que eu pesquisava sobre o conversor de bases  (https://wiki.python.org.br/Binary)
