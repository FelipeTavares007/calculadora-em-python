# 🧮 Calculadora em Python (Tkinter)

Calculadora desktop simples com interface gráfica, desenvolvida em Python usando a biblioteca **Tkinter**. O projeto foi criado para praticar lógica de programação, funções, variáveis globais, tratamento de erros e construção de interfaces gráficas.

## ✨ Funcionalidades

- Soma, subtração, multiplicação e divisão
- Números decimais (com proteção contra mais de um ponto no mesmo número)
- Botão **⌫** para apagar o último dígito
- Botão **C** para limpar o visor
- Tratamento de entrada vazia ou inválida nas operações (com `try/except`)
- Interface com visor alinhado à direita e botões organizados em grade

## 🖼️ Layout

| Botão | Função |
|-------|--------|
| `0-9` | Inserem dígitos no visor |
| `.` | Insere o ponto decimal |
| `➕` `➖` `✖` `➗` | Operações matemáticas |
| `🟰` | Calcula o resultado |
| `⌫` | Apaga o último caractere |
| `C` | Limpa o visor |

## 🛠️ Tecnologias

- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (já incluso na instalação padrão do Python)


## 🧠 Como funciona

1. Ao clicar em uma operação, o número digitado é guardado em uma variável (`num1`), a operação escolhida é salva em `operacao` e o visor é limpo.
2. O usuário digita o segundo número.
3. Ao clicar em `🟰`, a função `igual()` lê o segundo número, aplica a operação guardada e exibe o resultado no visor.

## 📌 Possíveis melhorias

- Tratar divisão por zero
- Permitir encadear várias operações sem apertar `=` entre elas
- Adicionar suporte ao teclado
- Melhorar o visual (cores, fontes e tamanho dos botões)
- Organizar o código em funções menores para evitar repetição

## 👤 Autor

**Felipe Tavares**
GitHub: [@FelipeTavares007](https://github.com/FelipeTavares007)
