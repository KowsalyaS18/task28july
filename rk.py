from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc,desc,func
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
class emplFam(db.Model):
    __tablename__ = 'employeefam'
    emp_id = db.Column('emp_id', db.Integer, primary_key=True)
    f_name = db.Column(db.String(100))
    m_name = db.Column(db.String(50))
    m_status= db.Column(db.String(200))
    ann_inc = db.Column(db.Integer)
    def __init__(self,emp_id,f_name,m_name,m_status,ann_inc):
        self.emp_id = emp_id
        self.f_name = f_name
        self.m_name=m_name
        self.m_status=m_status
        self.ann_inc=ann_inc

@app.route('/join',methods=['GET'])
def join():
    det = db.session.query(emplDet).join(emplFam, emplFam.emp_id == emplDet.emp_id).filter(emplDet.place == "RK Nagar").with_entities(emplDet.emp_id,emplDet.emp_name,emplFam.f_name,emplFam.m_name,emplFam.m_status,emplFam.ann_inc).limit(10).all()
    res = []
    for row in det:
        row_as_dict = dict(row)
        res.append(row_as_dict)
    return jsonify(res)

#db.create_all()
#db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
