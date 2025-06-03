from model.bayes_model import calcular_probabilidade_doenca

class BayesController:
    def __init__(self, view):
        self.view = view

    def calcular(self):
        prevalencia = self.view.prevalencia.get()
        sensibilidade = self.view.sensibilidade.get()
        especificidade = self.view.especificidade.get()
        resultado_teste = self.view.resultado_teste.get()

        probabilidade = calcular_probabilidade_doenca(
            prevalencia,
            sensibilidade,
            especificidade,
            resultado_teste
        )

        resultado_formatado = f"Probabilidade calculada: {probabilidade*100:.2f}%"
        self.view.mostrar_resultado(resultado_formatado)