# Sistema de Cálculo de Probabilidade com o Teorema de Bayes

## 🎯 Descrição

Este sistema calcula a probabilidade de uma pessoa ter uma doença com base no resultado de um teste, utilizando o Teorema de Bayes. A aplicação possui uma interface gráfica (GUI) moderna feita com TtkBootstrap.

---

## 🛠️ Tecnologias utilizadas

- Python 3.x
- Tkinter
- TtkBootstrap
- Matplotlib
- Pillow

---

## ⚙️ Instalação de dependências

Antes de executar, instale as seguintes bibliotecas:

pip install matplotlib pillow ttkbootstrap

---

## 🚀 Como executar a aplicação

1. Baixe ou clone os arquivos do projeto.

2. Estrutura de pastas:

.
├── main.py
├── controller
│   └── bayes_controller.py
├── model
│   └── bayes_model.py
└── view
    └── bayes_view.py

3. No terminal, execute:

python main.py

A interface será aberta automaticamente.

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

## 📦 Como compilar para executável (.exe)

### 1. Instale o PyInstaller:

pip install pyinstaller

---

### 2. Compile com:

pyinstaller --onefile --noconsole main.py

O executável será gerado na pasta:

./dist/main.exe

---

### ✅ Importante:

- Ao rodar o executável, ele criará automaticamente o arquivo formula.png no diretório.
- Execute sempre no mesmo diretório dos arquivos do projeto.

---

## (Opcional) Arquivo .spec personalizado

Se quiser customizar ainda mais o executável, gere o arquivo .spec:

pyinstaller --onefile --noconsole --name="TeoremaBayes" main.py

Depois, compile com:

pyinstaller TeoremaBayes.spec

---

## ✅ Dúvidas

- Pode rodar o Python diretamente ou usar o executável.
- Se ocorrer erro relacionado ao formula.png, execute no mesmo diretório ou ajuste o caminho no código.
- Não altere os nomes das pastas: controller, model e view.

---

Feito por: Vinícius Lazzarini Fernandes Torquato
