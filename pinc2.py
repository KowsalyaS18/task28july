from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kowsalya:Kowsi@localhost:5432/test1'
app.debug = True
db = SQLAlchemy(app)


class placeDet(db.Model):
    __tablename__ = 'placedet'
    place= db.Column(db.String(200))
    pincode = db.Column('pincode',db.Integer,primary_key=True)
    def __init__(self,place,pincode):
        self.place = place
        self.pincode = pincode
'''@app.route('/emp',methods=['POST'])
def emrec():
    ipt=request.get_json()
    #print(ipt)
    det=emplFam(emp_id=ipt['emp_id'],f_name=ipt['f_name'],m_name=ipt['m_name'],m_status=ipt['m_status'],ann_inc=ipt['ann_inc'])
    db.session.add(det)
    db.session.commit()
    return("successfully created")'''
db.create_all()
db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
