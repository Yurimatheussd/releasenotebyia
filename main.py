import google.generativeai as genai
import pyperclip
import os
from dotenv import load_dotenv

# Variáveis globais para armazenar os dados
text_problem_global = ""
text_solution_global = ""

def main():
    load_dotenv()
    #crie um arquivo .env na raiz com sua chave
    api_key = os.getenv('GENAI_API_KEY')
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-pro')

    global text_problem_global
    global text_solution_global

    while True:
        if not text_problem_global:
            text_problem_global = input('Digite o problema da sua issue: ')
            print('\n')
        if not text_solution_global:
            text_solution_global = input('Digite a solução sugerida da sua issue:')
            print('\n')
        
        text_param_text_problem =\
            'A seguir vou te passar o texto de um problema de um release note'\
            ', preciso que o texto fique no passado.'\
            ' Corrija erros de portugues, não altere o conteudo,'\
            'deixe mais simples para um cliente ler, substituindo nome de tabelas e campos do banco.'\
            'Formate o texto em poucas linhas.'\
            ' (Este não um campo para apresntar solução).Subistitua termo como Cliente disse, Foi informado pelo clente, para Foi identificado '
            
        response_problem = model.generate_content(f'{text_param_text_problem} {text_problem_global}')

        text_param_text_solution = \
            'A seguir vou te passar o texto de uma solução de um release note'\
            ', preciso que ele fique no presente.'\
            'Corrija erros de portugues, não altere o conteudo,  deixe mais simples para um cliente ler'\
            ', substituindo nome de tabelas e campos do banco.'\
            ' Formate o texto em poucas linhas (Este não um campo para apresntar solução)'
            
        response_solution = model.generate_content(f'{text_param_text_solution} {text_solution_global}')

        # Copiar para area de transferencia
        pyperclip.copy('PROBLEMA: ' + response_problem.text + '\n' + 'SOLUÇÃO: ' + response_solution.text)
        print('\n')
        # Imprimir o problema e a solução gerados
        print('PROBLEMA: ' + response_problem.text +'\n')
        print('SOLUÇÃO: ' + response_solution.text +'\n')

        choice = input("Escolha uma opção:\n1. Nova Consulta\n2. Refresh na resposta\n3. Sair\n").strip()

        if choice == '1':
            # Limpar os dados globais
            text_problem_global = ""
            text_solution_global = ""
            continue
        elif choice == '2':
            # Dar refresh na resposta
            print('\n')
            continue
        elif choice == '3':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

   # input("Pressione Enter para fechar o console...")

if __name__ == "__main__":
    main()
