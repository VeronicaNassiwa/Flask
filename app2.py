from flask import Flask ,jsonify,request

app=Flask(__name__)
students=[{
        'name':'Nyla Hussein',
        'course':'Computer sceince'
    },
    {
        'name':'Nassiwa Nasrah',
        'course':'Information Technology'
    }
    ]

@app.route('/school', methods=['POST'])
def sending_info():
    user_data=request.get_json()

    new_student={
        'name':user_data['name'],
        'subjects':[]
    }

    students.append(new_student)
    return jsonify(new_student)
    

app.run()    
