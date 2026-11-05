def count_values(obj):
    if isinstance(obj, dict):
        return sum(count_values(v) for v in obj.values())
    elif isinstance(obj, list):
        return sum(count_values(item) for item in obj)
    return 1

def find_key(obj, key):
    """
    Explicación:
    Al buscar 'temperature_2m_max', devuelve dos resultados porque la llave existe
    en dos niveles del JSON: en 'daily_units' guardando la unidad ('C') y 
    en 'daily' guardando la lista con los valores numéricos.
    """
    results = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                results.append(v)
            results.extend(find_key(v, key))
    elif isinstance(obj, list):
        for item in obj:
            results.extend(find_key(item, key))
    return results

def max_depth(obj):
    if isinstance(obj, dict):
        if not obj:
            return 1
        return 1 + max([max_depth(v) for v in obj.values()] + [0])
    elif isinstance(obj, list):
        if not obj:
            return 1
        return 1 + max([max_depth(item) for item in obj] + [0])
    return 0