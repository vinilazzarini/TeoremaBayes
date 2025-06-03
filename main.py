from controller.bayes_controller import BayesController
from view.bayes_view import BayesView

if __name__ == "__main__":
    view = BayesView()
    controller = BayesController(view)
    view.configurar_calcular(controller.calcular)
    view.iniciar()