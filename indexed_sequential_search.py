def indexed_sequential_search(arr, index, target, ascending=True):
    result = ""
    if not ascending:
        arr = arr[::-1]
        index = index[::-1]
    
    comparison_count = 0
    
    for i in range(len(index) - 1):
        comparison_count += 1
        result += f"\nBloque {i + 1}:\n¿Es {index[i]} menor o igual que {target} y menor que {index[i + 1]}?\n"
        if index[i] <= target and target < index[i + 1]:
            start = arr.index(index[i])
            end = arr.index(index[i + 1])
            result += f"Si, el rango es desde la posición {start} hasta la posición {end}.\nComparación {comparison_count}.\n"

            for j in range(start, end):
                comparison_count += 1
                result += f"\n¿Es {arr[j]} igual que {target}?\n"
                if arr[j] == target:
                    result += f"Si, y está en la posición {j}.\nComparación {comparison_count}\n"
                    return result
                else:
                    result += f"No, {arr[j]} diferente que {target}. \nComparación {comparison_count}\n"
            else: 
                result += f"\nElemento no encontrado en el bloque.\nBloque: {i + 1}; Comparación: {comparison_count}\nSiguiente bloque...\n"
                continue
        else:
            result += f"No, continuar con el siguiente bloque.\nComparación {comparison_count}.\n"
    result += f"\nElemento no encontrado.\nTotal de comparaciones: {comparison_count}\n"
    return result


def create_arr(elements_list):
    arr = [int(x) for x in elements_list.split(',')]
    return arr


def create_index(arr, block_size):
    index = []
    for i in range(0, len(arr), block_size):
        index.append(arr[i]) 
    return index