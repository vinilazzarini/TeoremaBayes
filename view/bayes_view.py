import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import StringVar, DoubleVar

class BayesView:
    def __init__(self):
        self.root = tb.Window(themename="flatly")
        self.root.title("Sistema de Detecção de Doença - Teorema de Bayes")
        self.root.geometry("1000x800")

        self.prevalencia = DoubleVar()
        self.sensibilidade = DoubleVar()
        self.especificidade = DoubleVar()
        self.resultado_teste = StringVar(value="positivo")
        self.resultado = StringVar()

        self._generate_formula_image()
        self._setup_widgets()

    def _generate_formula_image(self):
        formula = (
            r"$P(\text{Doença} | \text{Teste}) = \frac{P(\text{Teste}|\text{Doença}) \times P(\text{Doença})}{P(\text{Teste})}$" "\n\n"
            r"Para resultado POSITIVO: P(Positivo | Doente) = sensibilidade -- P(Positivo | Saudável) = 1 - especificidade" "\n"
            r"$\frac{Sensibilidade \times Prevalência}{(Sensibilidade \times Prevalência) + (1 - Especificidade) \times (1 - Prevalência)}$" "\n\n"
            r"Para resultado NEGATIVO: P(Negativo | Doente) = 1 - sensibilidade -- P(Negativo | Saudável) = especificidade" "\n"
            r"$\frac{(1 - Sensibilidade) \times Prevalência}{(1 - Sensibilidade) \times Prevalência + Especificidade \times (1 - Prevalência)}$"
        )

        plt.figure(figsize=(6, 3))
        plt.text(0.01, 0.8, formula, fontsize=12, va='top')
        plt.axis('off')

        plt.savefig("formula.png", bbox_inches='tight')
        plt.close()

    def _setup_widgets(self):
        tb.Label(self.root, text="Sistema de Detecção de Doença - Teorema de Bayes").pack(pady=10)
        tb.Label(self.root, text="Saber se uma pessoa esta doente conforme o resultado do teste").pack(pady=10)
        tb.Label(self.root, text="Vinícius Lazzarini Fernandes Torquato RA: 2409922").pack(pady=10)

        img = Image.open("formula.png")
        self._generate_formula_image = ImageTk.PhotoImage(img)
        
        label_img = tb.Label(self.root, image=self._generate_formula_image)
        label_img.pack(pady=20)

        valores = [f"{x/100:.2f}" for x in range(0, 101)]

        tb.Label(self.root, text="Prevalência da Doença (P | Doença) (0-1):").pack(pady=5)
        tb.Spinbox(self.root, textvariable=self.prevalencia, values=valores).pack()

        
        tb.Label(self.root, text="Sensibilidade (0-1):").pack(pady=5)
        tb.Spinbox(self.root, textvariable=self.sensibilidade, values=valores).pack()

        tb.Label(self.root, text="Especificidade (0-1):").pack(pady=5)
        tb.Spinbox(self.root, textvariable=self.especificidade, values=valores).pack()

        tb.Label(self.root, text="Resultado do Teste:").pack(pady=5)
        tb.Combobox(self.root, textvariable=self.resultado_teste, values=["positivo", "negativo"]).pack()

        # O botão vai ser criado dinamicamente, depois
        self.botao_calcular = tb.Button(self.root, text="Calcular")
        self.botao_calcular.pack(pady=10)

        tb.Label(self.root, textvariable=self.resultado, wraplength=350).pack(pady=10)

    def configurar_calcular(self, funcao_calcular):
        self.botao_calcular.config(command=funcao_calcular)

    def mostrar_resultado(self, resultado_formatado):
        self.resultado.set(resultado_formatado)

    def iniciar(self):
        self.root.mainloop()
