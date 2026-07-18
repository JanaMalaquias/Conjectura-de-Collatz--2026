# Conjectura de Collatz

## 📖 Descrição

Este projeto foi desenvolvido para resolver o desafio da **Conjectura de Collatz**, um famoso problema matemático que afirma que, para qualquer número inteiro positivo, ao aplicar repetidamente as seguintes regras, sempre será possível chegar ao número 1:

- Se o número for **par**, divida-o por 2.
- Se o número for **ímpar**, multiplique-o por 3 e some 1.

O programa recebe um número inteiro positivo informado pelo usuário, calcula a sequência de Collatz, exibe todos os números gerados e informa a quantidade de passos necessários para chegar ao número 1.

---

## 🚀 Funcionalidades

- Recebe um número inteiro positivo.
- Calcula a sequência da Conjectura de Collatz.
- Exibe a sequência completa.
- Informa a quantidade de passos até chegar ao número 1.
- Valida se o número informado é positivo.

---

## 🛠️ Tecnologias Utilizadas

- Python 3

---

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

3. Execute o programa:

```bash
python main.py
```

Caso o comando acima não funcione, utilize:

```bash
python3 main.py
```

---

## 💻 Exemplo de execução

Entrada:

```
Digite um número inteiro positivo: 6
```

Saída:

```
Sequência:
6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

Quantidade de passos: 8
```

---

## 📂 Estrutura do Projeto

```
.
├── main.py
└── README.md
```

---

## 📚 Conceitos Aplicados

- Estruturas de repetição (`while`)
- Estruturas condicionais (`if` / `else`)
- Funções
- Listas
- Tratamento de exceções (`try` / `except`)
- Entrada e saída de dados

---

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e aprendizado.