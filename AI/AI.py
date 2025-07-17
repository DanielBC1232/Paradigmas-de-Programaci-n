def generar_interpretacion(resumen, correlacion, clusters):
    # Simulación simple
    num_clusters = len(set(clusters))
    texto = f"""
    🔍 Análisis automático:
    El sistema detectó {num_clusters} agrupaciones principales en los datos.

    Según la matriz de correlaciones y el resumen, podrías enfocarte en variables con alta varianza o fuerte correlación.

    Recomendación: revisar aquellas con r > 0.8 o outliers significativos.
    """
    return texto.strip()
