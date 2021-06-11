from flask import Flask,jsonify,request

app=Flask(__name__)

students=[{
        'name':'NylaHussein',
        'course':'Computer sceince',
        'session':'Evening' ,
         'Faculty':[]
    },
    {
        'name':'NassiwaNasrah',
        'course':'Information Technology',
        'session':'Day' ,
        'Faculty':[]
    }
    ]
@app.route('/student')
def show_stdnts():
    return jsonify(students)
@app.route('/student/<string:name>')
def View_astudent(name):
    for student in students:
        if student['name']==name:
            return jsonify(student)

@app.route('/student/<string:name>/Faculty', methods=['POST'])
def create_fac(name):
    Req=request.get_json()
    for student in students:
        if student['name']==name:
            faclty=[{
                'name':Req['name'],
                'codinator':Req['codinator']
             }]
            student['Faculty'].append(faclty)
            return jsonify(student)       
app.run()