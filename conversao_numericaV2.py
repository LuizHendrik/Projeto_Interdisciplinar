import easygui

def converter_para_decimal(numero, base):
    try:
        # Convertendo o número para decimal
        decimal = int(numero, base)
        return decimal
    except ValueError:
        return None

def mostrar_informacoes():
    info = "Nome: Hendrik Mariano\nRGM: 31175163\nCurso: Analise e desenvolvimento de Sistemas\nDisciplinas: Organizacao e Arquitetura de Computadores, Programacao de Computadores\n\n" + \
           "---------------------------------------------\n\n" + \
           "Nome: Alex Gobbo\nRGM: 12345\nCurso: Analise e desenvolvimento de Sistemas\nDisciplinas: Organizacao e Arquitetura de Computadores, Programacao de Computadores\n\n" + \
           "---------------------------------------------\n\n" + \
           "Nome: Victor Araujo\nRGM: 32186673\nCurso: Analise e desenvolvimento de Sistemas\nDisciplinas: Organizacao e Arquitetura de Computadores, Programacao de Computadores"
    easygui.msgbox(info, title="Informações do Aluno")



def mostrar_manual():
    manual = "Este é um manual básico de uso:\n\n1. Digite o número que deseja converter.\n2. Selecione a base do número digitado.\n3. Clique em 'Converter'.\n4. Os resultados serão exibidos nas caixas de texto.\n\nDivirta-se convertendo!"
    easygui.msgbox(manual, title="Manual do Usuário")

def main():
    while True:
        # Exibindo o menu principal
        choices = ["Converter Número", "Informações do Aluno", "Manual do Usuário", "Sair"]
        choice = easygui.buttonbox("Selecione uma opção:", choices=choices)

        # Verificando a escolha do usuário
        if choice == "Converter Número":
            numero = easygui.enterbox("Digite o número que deseja converter:")
            if numero is not None:
                base = easygui.choicebox("Selecione a base do número:", choices=["BINÁRIO", "OCTAL", "DECIMAL", "HEXADECIMAL"])
                if base is not None:
                    base = base.lower()
                    if base == "binário":
                        base = 2
                    elif base == "octal":
                        base = 8
                    elif base == "decimal":
                        base = 10
                    elif base == "hexadecimal":
                        base = 16

                    # Convertendo o número para decimal
                    decimal = converter_para_decimal(numero, base)
                    if decimal is not None:
                        easygui.msgbox(f"Decimal: {decimal}", title="Resultado")
                    else:
                        easygui.msgbox("Número inválido!", title="Erro")
        elif choice == "Informações do Aluno":
            mostrar_informacoes()
        elif choice == "Manual do Usuário":
            mostrar_manual()
        elif choice == "Sair":
            break

if __name__ == "__main__":
    main()
