from flask import Flask ,jsonify,request

app=Flask(__name__)
students=[{
        'name':'Nyla Hussein',
        'course':'Computer sceince',
        'session':'Evening' ,
        'courseUnits':[]
    },
    {
        'name':'Nassiwa Nasrah',
        'course':'Information Technology',
        'session':'Day' ,
        'courseUnits':[]
    }
    ]

@app.route('/student', methods=['POST'])
def sending_info():
    user_data=request.get_json()

    new_student={
        'name':user_data['name'],
        'course':'Computer sceince',
        'session':'Evening' ,
        'Faculty':[]
    }

    students.append(new_student)
    return jsonify(new_student)
    

app.run()    
