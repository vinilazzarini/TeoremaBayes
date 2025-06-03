# Sistema de Cálculo de Probabilidade com o Teorema de Bayes

## 🎯 Descrição

Este sistema calcula a probabilidade de uma pessoa ter uma doença com base no resultado de um teste, utilizando o Teorema de Bayes. 

O sistema apesar de simples, foi feito na arquitetura MVC, no model temos a responsabilidade de realizar o calcular, na view a de exibição do layout e dos dados, e o controller de realizar a comunição entre a view e o model. As formulas utilizadas aparecem ao iniciar a aplicação, tanto no layout quanto em um png que gerará automaticamente na mesma pasta do executavel apos o inicio da aplicação.

---

## 🛠️ Tecnologias utilizadas

- Python 3.x
- Tkinter
- TtkBootstrap
- Matplotlib
- Pillow

---

## 🖥️ Como usar

1. Informe os valores:
   - Prevalência (0 a 1)
   - Sensibilidade (0 a 1)
   - Especificidade (0 a 1)

2. Escolha o resultado do teste: "positivo" ou "negativo".

3. Clique em "Calcular".

O sistema exibirá a probabilidade calculada e mostrará a fórmula do Teorema de Bayes.

---

### ✅ Importante:

- Ao rodar o executável, ele criará automaticamente o arquivo formula.png no diretório.
- Execute sempre no mesmo diretório dos arquivos do projeto.
- Ao iniciar o executavel o app minimizar.

---

Feito por: Vinícius Lazzarini Fernandes Torquato
