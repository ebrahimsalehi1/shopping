from app import db, Customer, Order
from sqlalchemy import func

customer1 = Customer(name='hamid hamidi', code=1293)
customer2 = Customer(name='bagher bagheri', code=1283)
customer3 = Customer(name='saeid saeidi', code=1273)


order1 = Order(date=func.date('2022-09-14'), customer_id=1)
order2 = Order(date=func.date('2022-09-15'), customer_id=3)
order3 = Order(date=func.date('2022-09-15'), customer_id=2)


db.session.add_all([customer1, customer2, customer3])
db.session.add_all([order1, order2, order3])
# Just for testing stuffs


# Commit must be done
db.session.commit()
