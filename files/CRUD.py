import json

def create_product(new_product, file):
    with open(file) as f:
        products = json.load(f)
        products.append(new_product)
    with open(file, "w") as f:
        json.dump(products, f, indent=4)
    print("Вы успешно добавили товар!")

# create_product({"id":1, "title":"nike", "price":1200},"shop_db.json")
# create_product({"id":2, "title":"iPhone", "price":30000},"shop_db.json")

def read_products(file):
    with open(file) as f:
        products = json.load(f)
        for product in products:
            print(f"Товар: {product["title"]}, цена - {product["price"]} ")

# read_products("shop_db.json")

def read_product(id,file):
    with open(file) as f:
        products = json.load(f)
        product = next((p for p in products if p["id"] == id), "Неверный id")
        print(product)

# read_product(2,"shop_db.json")
        
        

def update_product(id,file):
    with open(file) as f:
        products = json.load(f)
        for product in products:
            product[key] = new
    with open(file, "w") as f:
        json.dump(product, f)

update_product("title","mouse","shop_db.json")

def delete_product(id, file):
    ...