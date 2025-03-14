from flask import Flask, render_template

app = Flask(__name__)

# Список товаров (в реальном приложении данные будут из базы данных)
products = [
    {'id': 1, 'name': 'Товар 1', 'price': 10.99, 'image': 'negr.jfif', 'description': 'Описание товара 1'},
    {'id': 2, 'name': 'Товар 2', 'price': 25.50, 'image': 'negr 2.jfif', 'description': 'Описание товара 2'},
    {'id': 3, 'name': 'Товар 3', 'price': 5.75, 'image': 'negr 3.jfif', 'description': 'Описание товара 3'},
    # ... добавить больше товаров
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
