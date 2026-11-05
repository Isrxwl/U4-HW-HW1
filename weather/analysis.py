import collections

def summarize(temperatures):
    # Retorna mínimo, máximo y promedio en un solo return
    return min(temperatures), max(temperatures), round(sum(temperatures) / len(temperatures), 2)

def classify(temperature):
    if temperature >= 32:
        return "muy caluroso"
    if temperature >= 28:
        return "caluroso"
    if temperature >= 20:
        return "templado"
    return "fresco"

def filter_hot_days(temperatures, threshold=30):
    return list(filter(lambda x: x >= threshold, temperatures))

def count_by_label(temperatures):
    labels = [classify(t) for t in temperatures]
    # Retorna los elementos contados y ordenados
    return sorted(list(collections.Counter(labels).items()))