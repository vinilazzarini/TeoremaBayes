def calcular_probabilidade_doenca(prevalencia, sensibilidade, especificidade, resultado_teste):
    p_doente = prevalencia
    p_saudavel = 1 - prevalencia

    if resultado_teste == "positivo":
        p_positivo = (sensibilidade * p_doente) + ((1 - especificidade) * p_saudavel)
        p_doente_dado_positivo = (sensibilidade * p_doente) / p_positivo
        return p_doente_dado_positivo
    else:
        p_negativo = ((1 - sensibilidade) * p_doente) + (especificidade * p_saudavel)
        if p_negativo == 0:
            return 0
        p_doente_dado_negativo = ((1 - sensibilidade) * p_doente) / p_negativo
        return p_doente_dado_negativo