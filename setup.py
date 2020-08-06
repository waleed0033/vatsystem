from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql10358905:PIfY7MdFuy@sql10.freesqldatabase.com:3306/sql10358905?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/customer')
def show_customer():
    return render_template('customer.html',Customer=Customer)

@app.route('/customer/<int:customer_id>')
def test(customer_id):
    return render_template('customer_id.html',Customer=Customer.get_Customer(customer_id))

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone_number = db.Column(db.String(24))
    address = db.Column(db.String(256))
    vat_id = db.Column(db.String(24))
    orders = db.relationship('Order', backref='OrderBy', lazy='dynamic')

    def __repr__(self):
        return '<Customer {}>'.format(self.id)

    def get_Customers():
        return Customer.query.all()

    def get_Customer(id):
        return Customer.query.get(id)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_data = db.Column(db.Date())
    total_amount = db.Column(db.Integer)
    vat_amount = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    items = db.relationship('Item', backref='Item', lazy='dynamic')

    def __repr__(self):
        return '<Order {}>'.format(self.id)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64))
    item_quantity = db.Column(db.Integer)
    item_amount = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

    def __repr__(self):
        return '<Item {}>'.format(self.id)

if __name__ == '__main__':
    app.run(debug=True,host= '0.0.0.0')