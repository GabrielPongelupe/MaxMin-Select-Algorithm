def find_min_max(arr, start, end):
    # Caso base: um único elemento
    if start == end:
        return arr[start], arr[start]
    
    # Caso base: dois elementos
    if end == start + 1:
        if arr[start] < arr[end]:
            return arr[start], arr[end]
        else:
            return arr[end], arr[start]
    
    # Divide o array ao meio
    mid = (start + end) // 2
    min_left, max_left = find_min_max(arr, start, mid)
    min_right, max_right = find_min_max(arr, mid + 1, end)
    
    # Combina os resultados
    return min(min_left, min_right), max(max_left, max_right)
