from flask import Flask, render_template, request, redirect
from models import Restaurant, db
import templates.mape.mape_main as mape_main
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///templates/mape/restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
engine = db.create_engine('sqlite:///templates/mape/restaurant.db')


@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        with db.Session(autoflush=False, bind=engine) as session:
            new_item = Restaurant(name=request.form['name'],
                                  email=request.form['email'],
                                  total_seats=request.form['total_seats'],
                                  password=request.form['password'],
                                  adress=request.form['adress'],
                                  description=request.form['description'],
                                  free_seats=0)
            session.add(new_item)
            session.commit()
            print('Додано!')
        return redirect('/map')
    return render_template('register.html')


@app.route('/map')
def map():
    mape_main.main(path="templates/mape/")
    return render_template('mape/map.html')



@app.route('/profile/<user_id>', methods=['GET', 'POST'])
def profile(user_id):
    user_id = int(user_id[1])
    with db.Session(autoflush=False, bind=engine) as session:
        user = session.get(Restaurant, user_id)
        print(user.total_seats, user.free_seats)
        return render_template('sitepage.html', free_places=2,
                               taken_places=user.total_seats)



@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        with db.Session(autoflush=False, bind=engine) as session:
            all_user = session.query(Restaurant).all()
            for user in all_user:
                if user.email == request.form['email'] and user.password == request.form['password']:
                    user_id = user.id
                    print(user.email, user_id)
                    session.commit()
                    return redirect(f'/profile/<{user_id}>', user_id)
                else:
                    print('Return one more')
                    return redirect('/log_in')
    return render_template('log_in.html')


if __name__ == '__main__':
    app.run(debug=True)