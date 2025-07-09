import json

class RegisterMixin:
    def register(self, name, password):
        with open('user.json') as f:
            users = json.load(f)

        if users:
            max_id = max(user['id'] for user in users)
        else:
            max_id = 0
        new_id = max_id + 1

        self.name = name
        self.password = password
        user = {'id':new_id,'name':name,'password':password}
        for u in users:
            if u['name'] == name:
                print('Такой пользователь уже сущетсвует!')
                return
            elif u['password'] == password:
                print('Такой пароль уже существует!')
                return
        if validate_password(password) == False:
            return
        else:
            users.append(user)
            with open('user.json', 'w') as f:
                json.dump(users, f, ensure_ascii=False, indent = 4)
            print(f"Пользователь {user['name']} успешно зарегистрирован!")

# Функция проверки пароля
def validate_password(password):
    if len(password) < 8:  
        print('Пароль слишком короткий! Минимум 8 символов.')
        return False
    if password.isalpha() == True or password.isdigit() == True:
        print('Пароль должен состоять и из букв, и из цифр!')
        return False
    return True


class LoginMixin:
    def login(self, name, password):
        with open('user.json') as f:
            users = json.load(f)

        user = next((u for u in users if u['name'] == name), None)
        
        if not user:
            print('Неверное имя пользователя!')
            return
        if user['password'] != password:
            print('Неверный пароль!')
            return
        print(f"Добро пожаловть {user['name']}!")


class ChangePasswordMixin:
    def change_password(self, name, old_password, new_password):
        if not validate_password(new_password):
            return
        
        with open('user.json') as f:
            users = json.load(f)

        user = next((u for u in users if u['name'] == name), None)
        if not user:
            print('Неверное имя пользователя!')
            return
        if user:
            password = next((p for p in users if p['password'] == old_password), None)
            if not password:
                print('Неверно указан старый пароль!')
                return   
        check_password = next((c for c in users if c['password'] == new_password), None) 
        if check_password:
            print('Данный пароль занят!')  
            return
        if not check_password:   
            password['password'] = new_password

        with open('user.json', 'w') as f:
            json.dump(users, f, ensure_ascii=False, indent=4)
        print("Пароль успешно изменен!")


class ChangeUsernameMixin:
    def change_username(self, old_name, new_name):
        with open('user.json') as f:
            users = json.load(f)  
        user = next((u for u in users if u['name'] == old_name), None)
        if not user:
            print('Неверное имя пользователя!')     
            return
        
        while any(u['name'] == new_name for u in users):
            new_name = input('Это имя уже занято! Попробуйте снова: ')
        
        user['name'] = new_name

        with open('user.json', 'w') as f:
            json.dump(users, f, ensure_ascii = False, indent = 4)
        print(f"Имя пользователя {old_name} изменен на {new_name}")
         

class User(RegisterMixin, LoginMixin, ChangePasswordMixin, ChangeUsernameMixin):
    ...

class CheckOwnerMixin:
    def check_owner(self, owner):
        with open('user.json') as f:
            users = json.load(f)
        check = next((o for o in users if o['name'] == owner), None)
        if not check:
            print('Неверное имя пользователя!')
            return
        if check:
            print('Объект успешно создан!')

class Post(CheckOwnerMixin):
    def __init__(self, title, description, price, quantity, owner):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.owner = owner


user = User()
post = Post('iPhone','Черный цвет; Масло', 120000, 5, 'Temirlan')
# user.register('Temirlan','basket12')
# user.register('Alisher','123123az')
# user.register('Nurislam','87654321h')
# user.register('Gosha','1236455h')
# user.login('Temirlan','basket12')
# user.login('Alisher','123123az')
# user.change_username('Alisher','Alish')
# user.change_username('j','Nurislam')
# user.change_password('Nurislam','87654321h','basket69')
post.check_owner('Gosha')
