def bubble_sort(arr, n):
    for i in range(n):
## iterando de 0 a n-i-1 ya que los últimos i elementos ya están ordenados
        for j in range(n - i - 1):
## comprobando el siguiente elemento
            if arr[j] > arr[j + 1]:
## intercambiando los elementos adyacentes
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

## inicialización del array
arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
bubble_sort(arr, 9)
## imprimiendo el array
print(str(arr))