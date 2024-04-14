def calculate_sequence(n):
    try:
        if not isinstance(n, int) or n <= 0:
            raise Exception("Введите положительное целое число.")

        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            sequence.append(n)

        peak = max(sequence)

        return sequence, len(sequence), peak

    except Exception as e:
        return f"Ошибка: {str(e)}"


number = 13
result = calculate_sequence(number)
print(f"Последовательность: {result[0]}")
print(f"Количество элементов в последовательности: {result[1]}")
print(f"Пик последовательности: {result[2]}")