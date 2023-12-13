def read_file(file_path):
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            numbers = file.read().split()
            return numbers
    except FileNotFoundError:
        print("Файл не найден.")
        return []

def create_queues(numbers):
    queues = []
    for number in numbers:
        queue_found = False
        for queue in queues:
            if number[0] == queue[0][0]:
                queue.append(number)
                queue_found = True
                break
        if not queue_found:
            queues.append([number])
    return queues

def merge_queues(queues):
    result = []
    while queues:
        for queue in queues:
            if queue:
                result.append(queue.pop(0))
        queues = [queue for queue in queues if queue]
    return result

file_path = "3.txt"
numbers = read_file(file_path)
queues = create_queues(numbers)
result = merge_queues(queues)
result1 = []
for i in result:
    if ',' in i:
        i = i.replace(',', '')
    result1.append(i)
print(",".join(result1))