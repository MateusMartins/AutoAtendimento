from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
empDB=[
 ]

@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):

    for item in [emp for emp in empDB if (emp['id'] == empId)]:
        x = item
    return jsonify(x)

@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId):
    em = [emp for emp in empDB if (emp['id'] == empId)]
    if 'name' in request.json :
        em[0]['name'] = request.json['name']
    return jsonify({'emp':em[0]})

@app.route('/empdb/employee',methods=['POST'])
def createEmp():
    dat = {
    'id':request.json['id'],
    'name':request.json['name']
    }
    empDB.append(dat)
    return jsonify(dat)

@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
       abort(404)
    empDB.remove(em[0])
    return jsonify({'response':'Success'})

if __name__ == '__main__':
 app.run()