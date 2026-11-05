import sys
import json
from weather import (
    safe_fetch, count_values, find_key, max_depth,
    summarize, classify, filter_hot_days, count_by_label
)

def main():
    # INPUT
    if "--offline" in sys.argv:
        with open("sample_response.json", "r") as f:
            data = json.load(f)
    else:
        # MODO EN VIVO (Latitud y longitud por defecto)
        data = safe_fetch(20.97, -89.62)
        if data is None:
            print("No se pudo conectar a la API. Se detiene la ejecucion limpiamente.")
            return

    # PROCESS
    valores = count_values(data)
    profundidad = max_depth(data)
    
    # Extraer los dos valores de temperature_2m_max
    busqueda_temp = find_key(data, "temperature_2m_max")
    unidades = busqueda_temp[0]
    temperaturas = busqueda_temp[1]
    
    min_t, max_t, avg_t = summarize(temperaturas)
    dias_calurosos = filter_hot_days(temperaturas)
    conteo_categorias = count_by_label(temperaturas)
    clasificacion_maxima = classify(max_t)

    # OUTPUT
    print(f"Valores: {valores}")
    print(f"Profundidad: {profundidad}")
    print(f"Unidades encontradas: {unidades}")
    print(f"Minimo: {min_t}")
    print(f"Maximo: {max_t}")
    print(f"Promedio: {avg_t}")
    print(f"Dias calurosos: {dias_calurosos}")
    print(f"Por categoria: {conteo_categorias}")
    print(f"Clasificacion del maximo: {clasificacion_maxima}")

if __name__ == "__main__":
    main()