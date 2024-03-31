from models import Restaurant, db
restaurant = db.query(Restaurant).all()
for i in restaurant:
    print(i.id)