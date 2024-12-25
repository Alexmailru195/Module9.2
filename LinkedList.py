class Node:
    """Класс для представления узла в связанном списке."""

    def __init__(self, data, next_node=None):
        """
        Инициализация узла.

        :param data: Данные, хранящиеся в узле.
        :param next_node: Указатель на следующий узел.
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для представления связанного списка."""

    def __init__(self):
        """Инициализация пустого связанного списка."""
        self.head = None

    def insert_at_head(self, data):
        """
        Вставка узла в начало списка.

        :param data: Данные для нового узла.
        :return: Сообщение о добавлении узла.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        return f"Узел с данными {new_node.data} добавлен в начало списка"

    def insert_at_end(self, data):
        """
        Вставка узла в конец списка.

        :param data: Данные для нового узла.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен в конец списка"

    def remove_node_position(self, rm_position):
        """
        Удаление узла из списка по позиции.

        :param rm_position: Позиция узла для удаления.
        :return: Сообщение о результате удаления.
        """
        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.next_node
            return f"Удален узел с данными {removed_node.data} позиции {rm_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return "Ничего не удалено"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        return f"Удален узел с данными {removed_node.data} позиции {rm_position}"

    def insert_at_position(self, data, node_position):
        """
        Вставка узла на заданную позицию.

        :param data: Данные для нового узла.
        :param node_position: Позиция для вставки узла.
        :return: Сообщение о результате вставки.
        """
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_head(data)
            return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"

        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1

        if current_node is None:
            return None
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"

    def print_ll(self):
        """Вывод данных списка на экран."""
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return "Данные списка выведены"

    def get(self, data):
        """
        Поиск узла с заданными данными.

        :param data: Данные для поиска.
        :return: Кортеж (устремлен, узел) или (False, None), если не найдено.
        """
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True, current_node
            current_node = current_node.next_node
        return False, None

    def change_data(self, node_data, change_data):
        """
        Изменение данных в узле.

        :param node_data: Данные узла для изменения.
        :param change_data: Новые данные для узла.
        :return: Сообщение о результате изменения.
        """
        current_node = self.head
        current_node_position = 1
        while current_node:
            if current_node.data == node_data:
                current_node.data = change_data
                return f"Заменены данные в узле № {current_node_position}"
            current_node = current_node.next_node
            current_node_position += 1
        return "Данные не обнаружены"


class Queue:
    """Класс для представления очереди, работающей с символьными значениями."""

    def __init__(self, max_size):
        """
        Инициализация очереди.

        :param max_size: Максимальный размер очереди.
        """
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        """Проверка очереди на пустоту."""
        return len(self.queue) == 0

    def is_full(self):
        """Проверка очереди на заполненность."""
        return len(self.queue) == self.max_size

    def enqueue(self, value):
        """
        Добавление элемента в очередь.

        :param value: Элемент для добавления.
        :return: Результат операции.
        """
        if self.is_full():
            return "Очередь полна!"
        self.queue.append(value)
        return f"Элемент '{value}' добавлен в очередь."

    def dequeue(self):
        """
        Удаление элемента из очереди.

        :return: Удаленный элемент или сообщение, если очередь пуста.
        """
        if self.is_empty():
            return "Очередь пуста!"
        return f"Элемент '{self.queue.pop(0)}' удален из очереди."

    def show(self):
        """Отображение всех элементов очереди на экран."""
        return self.queue


def main():
    """Главная функция для взаимодействия с пользователем."""
    queue = Queue(max_size=5)
    while True:
        print("\n1. Добавить элемент в очередь")
        print("2. Удалить элемент из очереди")
        print("3. Показать очередь")
        print("4. Проверить, пуста ли очередь")
        print("5. Проверить, полна ли очередь")
        print("6. Выход")

        choice = input("Выберите операцию: ")

        if choice == '1':
            value = input("Введите элемент: ")
            print(queue.enqueue(value))
        elif choice == '2':
            print(queue.dequeue())
        elif choice == '3':
            print("Очередь:", queue.show())
        elif choice == '4':
            print("Очередь пуста:", queue.is_empty())
        elif choice == '5':
            print("Очередь полна:", queue.is_full())
        elif choice == '6':
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
1