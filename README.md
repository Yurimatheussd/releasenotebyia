# **Gerador de Release Notes Simplificado**

## **Visão Geral do Projeto**

Este projeto simplifica a criação de release notes, focando em entradas de problema e solução. Ele utiliza a API do Google Generative AI para gerar texto com base nas entradas do usuário.

### **Pré-requisitos**

- Você deve possuir uma chave de API válida para acessar o Google Generative AI. Esta chave deve ser fornecida no arquivo `.env` localizado na raiz do projeto.

### **Instalação**

1. Clone o repositório para o seu ambiente local.
2. Instale as dependências necessárias executando o comando `pip install -r requirements.txt`.
3. Crie um arquivo `.env` na raiz do projeto e insira sua chave de API do Google Generative AI no formato `GENAI_API_KEY=sua_chave_api_aqui`.

### **Uso**

1. Execute o script `main.py`.
2. O programa solicitará que você insira o problema e a solução relacionados à sua issue.
3. Após inserir as informações, o programa gerará uma versão simplificada e gramaticalmente correta do problema e da solução.
4. O texto gerado será copiado para a área de transferência e exibido no console.
5. Você pode escolher entre fazer uma nova consulta, atualizar a resposta ou sair do programa.

### **Observações**

- Este projeto tem como objetivo simplificar a geração de texto em linguagem natural para problemas e soluções em release notes.
- Certifique-se de seguir as instruções e diretrizes ao inserir as informações para obter resultados precisos e úteis.
- Para qualquer problema encontrado ou sugestão de melhoria, sinta-se à vontade para abrir uma issue neste repositório.

### **Autor**

Este projeto foi desenvolvido por [Yurimatheussd].

