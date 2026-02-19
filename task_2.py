import queue, datetime

tasks_list = [["task_" + str(i)] for i in range(1,10) ]

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now().strftime("%H:%M:%S")
        result = func(*args, **kwargs)
        end = datetime.datetime.now().strftime("%H:%M:%S")
        time_control = f"Время начала выполнения: {start}, время окончания выполнения: {end}"

        return result, time_control
    return wrapper

@timeit
def task_run(task):
    number = task[0]
    task.clear()
    for i in range(1,10):
        task.append(i)
    task_dict = {number:task}
    delay = 0
    for i in range(1,100000000):
        delay += i
    return task_dict
#Создали очередь
queue = queue.Queue()
#Заполнили очередь
for task in tasks_list:
    queue.enqueue(task)

log_text = ""
#Запустили выполнение задач
for i in range(1,queue.q_size()):
    task_result, time_control = task_run(queue.dequeue())
    log_text += f"{task_result}, {time_control}\n"

print(log_text)
