import random
import time


def generate_array(size):
    """Генерирует случайный массив из size элементов"""
    return [random.randint(0, 100) for _ in range(size)]


def is_sorted(array):
    """Проверяет, отсортирован ли массив по возрастанию"""
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True


def bubble_sort(array):
    """Сортирует массив по возрастанию методом пузырька"""
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # Обмен элементов
                array[j], array[j + 1] = array[j + 1], array[j]


num_runs = 100
array_size = 100

total_time_bubble = 0
total_time_sort = 0

array = generate_array(array_size)
for _ in range(num_runs):
    random.shuffle(array)
    start_time_bubble = time.time()
    bubble_sort(array)
    end_time_bubble = time.time()

    total_time_bubble += end_time_bubble - start_time_bubble
    array1 = array
    start_time_sort = time.time()
    array1.sort()
    end_time_sort = time.time()

    total_time_sort += end_time_sort - start_time_sort

average_time_bubble = total_time_bubble / num_runs
average_time_sort = total_time_sort / num_runs
print("Отсортированный массив пузырьком:", array)
print("Время одной сортировки пузырьком:", average_time_bubble)
print("Отсортированный массив стандартной сортировкой:", array1)
print("Время одной стандартной сортировки:", average_time_sort)
