from flask import Flask, jsonify

app=Flask(__name__)

new_student=[{
        'name':'Nyla Hussein',
        'course':'Computer sceince'
    },
    {
        'name':'Nassiwa Nasrah',
        'course':'Information Technology'
    }
    ]
@app.route('/school')
def student():
    return jsonify({'new_student': new_student})

app.run()