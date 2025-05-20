class User:
    _all_users = []  # Общий список всех пользователей (статический атрибут)

    def __init__(self, user_id, name):
        self._id = user_id
        self._name = name
        self._access_level = 'user'
        User._all_users.append(self)  # Добавляем нового пользователя в общий список

    # Статические методы без использования декораторов
    def get_all_users():
        return list(User._all_users)  # Возвращаем копию списка

    def find_user_by_id(user_id):
        for user in User._all_users:
            if user.get_id() == user_id:
                return user
        return None

    # Геттеры для доступа к защищенным атрибутам
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Сеттер для изменения имени
    def set_name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f"Сотрудник(ID: {self._id}, Имя: {self._name}, Статус: {self._access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, user_id, name):
        # Проверяем, нет ли пользователя с таким ID
        existing_user = User.find_user_by_id(user_id)
        if existing_user is None:
            User(user_id, name)  # Создаем нового пользователя
            return True
        return False

    def remove_user(self, user_id):
        user_to_remove = User.find_user_by_id(user_id)
        # Нельзя удалить администратора или несуществующего пользователя
        if user_to_remove and user_to_remove.get_access_level() != 'admin':
            User._all_users.remove(user_to_remove)
            return True
        return False

    def __str__(self):
        return f"Сотрудник(ID: {self._id}, Имя: {self._name}, Статус: {self._access_level})"


# Пример использования
if __name__ == "__main__":
    # Создаем администратора
    admin = Admin(100, "Алексей Админов")

    # Администратор добавляет пользователей
    admin.add_user(1, "Иван Петров")
    admin.add_user(2, "Мария Сидорова")

    # Выводим всех пользователей
    print("Все пользователи в системе:")
    for user in User.get_all_users():
        print(f"- {user}")

    # Администратор удаляет пользователя
    admin.remove_user(1)

    print("\nПосле удаления:")
    for user in User.get_all_users():
        print(f"- {user}")
