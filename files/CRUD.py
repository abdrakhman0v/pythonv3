import json

def create_product(new_product, file):
    try:
        with open(file) as f:
            products = json.load(f)       
    except FileNotFoundError:
        print(f"{file} - не найден. Создаю новый файл.")
        products = []
    products.append(new_product)

    with open(file, "w") as f:
        json.dump(products, f, indent=4)
    print("Вы успешно добавили товар!")

create_product({"id":1, "title":"nike", "price":1200},"shop_db.json")
create_product({"id":2, "title":"iPhone", "price":30000},"shop_db.json")
create_product({"id":3, "title":"adidas", "price":500},"shop_db.json")
create_product({"id":4, "title":"Samsung", "price":20000},"shop_db.json")

def read_products(file):
    with open(file) as f:
        products = json.load(f)
        for product in products:
            print(f"Товар: {product['title']}, цена - {product['price']}$")

read_products("shop_db.json")

def read_product(id,file):
    with open(file) as f:
        products = json.load(f)
        product = next((p for p in products if p["id"] == id), "Неверный id")
        print(f"Товар - {product['title']}. Цена - {product["price"]}$")

read_product(2,"shop_db.json")
        
        

def update_product(id,key,new,file):
    with open(file) as f:
        products = json.load(f)
    for product in products:
        if product["id"] == id:
            product[key] = new
            break
    else:
        print("Неверный id")
        return   
    with open(file, "w") as f:
        json.dump(products, f, indent=4)
    print(f"Товар - {product['title']} обновлен")
        
update_product(1,"price", 500,"shop_db.json")
update_product(3,"title", "ps","shop_db.json")

def delete_product(id,file):
    with open(file) as f:
        products = json.load(f)
    for product in products:
        if product["id"] == id:
            products.remove(product)
            break
    else:
        print("Неверный id")
        return
    with open(file,"w") as f:
        json.dump(products,f,indent=4)
    print(f"Товар - {product['title']} удален!")

delete_product(1,"shop_db.json")
