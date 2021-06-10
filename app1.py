from flask import Flask, jsonify

app=Flask(__name__)

students=[{
        'name':'Nyla Hussein',
        'course':'Computer sceince',
        'session':'Evening',
        'Faculty':[]

    },
    {
        'name':'Nassiwa Nasrah',
        'course':'Information Technology',
        'session':'Day' ,
        'Faculty':[]
    }
    ]
@app.route('/student')
def return_students():
    return jsonify({'students': students})

app.run()