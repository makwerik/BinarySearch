class BinarySearch:
    """Бинарный поиск"""

    def __init__(self, array, target):
        self.array = sorted(array)
        self.target = target

    def search(self):
        """Метод для поиска таргета"""
        left, right = 0, len(self.array) - 1

        while left <= right:
            # Поиск середины массива
            mid = (left + right) // 2
            # Если середина массива равна искомому значению, возвращаем индекс
            if array[mid] == self.target:
                return mid
            # Если искомое значение больше середины массива, сдвигаем левую границу вправо
            elif array[mid] < self.target:
                left = mid + 1
            # В противном случае сдвигаем правую границу влево
            else:
                right = mid - 1

        # Если искомое значение не найдено
        return -1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 10

    binary_search = BinarySearch(array, target)
    result = binary_search.search()

    assert result == 9
