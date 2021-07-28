from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kowsalya:Kowsi@localhost:5432/test1'
app.debug = True
db = SQLAlchemy(app)


class emplDet(db.Model):
    __tablename__ = 'employee'
    emp_id = db.Column('emp_id', db.Integer, primary_key=True)
    emp_name = db.Column(db.String(100))
    place = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    age = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    d_join=db.Column(db.Date)
    def __init__(self,emp_id, emp_name,place, addr, pin,age,salary,d_join):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.place = place
        self.addr = addr
        self.pin = pin
        self.age=age
        self.salary=salary
        self.d_join=d_join


@app.route('/emp',methods=['POST'])
def emrec():
    ipt=request.get_json()
    #print(ipt)
    det=emplDet(emp_id=ipt['emp_id'],emp_name=ipt['emp_name'],place=ipt['place'],addr=ipt['addr'],pin=ipt['pin'],age=ipt['age'],salary=ipt['salary'],d_join=ipt['d_join'])
    db.session.add(det)
    db.session.commit()
    return("successfully created")
#db.create_all()
#db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
