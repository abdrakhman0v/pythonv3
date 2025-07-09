import json

class CreateMixin:
    def create(self, new_product):
        with open('db_mix.json') as f:
            products = json.load(f)
        products.append(new_product)
        with open('db_mix.json', 'w') as f:
            json.dump(products, f, indent=4)
        print('Товар успешно добавлен!')

class ReadMixin:
    def read(self, id):
        with open('db_mix.json') as f:
            products = json.load(f)
            for product in products:
                if product['id'] == id:
                    print(f"Товар - {product['title']}. Цена - {product['price']}$")
                    break
            else:
                print('Неверный ID')
                return

class ReadAllMixin:
    def read_all(self):
        with open('db_mix.json') as f:
            products = json.load(f)
            print('=======Список всех товаров=======')
            for product in products:
                print(f"ID:{product['id']} Товар - {product['title']}. Цена - {product['price']}$")

class UpdateMixin:
    def update(self, id, key, new):
        with open('db_mix.json') as f:
            products = json.load(f)
            for product in products:
                if product['id'] == id:
                    product[key] = new
                    break
            else:
                print('Неверный ID')
                return
        with open('db_mix.json', 'w') as f:
            json.dump(products,f,indent=4)
        print(f"Товар - {product['title']} обновлен!")

class DeleteMixin:
    def delete(self, id):
        with open('db_mix.json') as f:
            products = json.load(f)
            for product in products:
                if product['id'] == id:
                    print(f"Товар - {product['title']} - удален!")
                    products.remove(product)
                    break
            else:
                print('Неверный ID')
                return
        with open('db_mix.json','w') as f:
            json.dump(products,f,indent=4)
        
        

class Products(CreateMixin,ReadMixin,ReadAllMixin,UpdateMixin,DeleteMixin):
    ...

products = Products()
# products.create({'id':1,'title':'Toyota','price':12000})
# products.create({'id':2,'title':'Subaru','price':8000})
# products.create({'id':3,'title':'BMW','price':6500})
# products.create({'id':4,'title':'Mustang','price':40000})
# products.read(1)
products.read_all()
# products.update(1,'price',11500)
# products.delete(4)