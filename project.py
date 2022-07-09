from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Name': 'jeem',
        'Contact': '135779914',
        'Done': 'false'
    },
    {
        'id': 2,
        'Name': 'john',
        'Contact': '122909209',
        'Done': 'false'
    },
    {
        'id': 3,
        'Name': 'jack',
        'Contact': '102926789',
        'Done': 'false'
    }
]

@app.route('/')
def index():
    return('My contacts')

@app.route('/contacts/add', methods=['POST'])
def add_contact():
    if(not request.form):
        return jsonify({'Status': "error", 'message':'Give data please :|'}, 400)
    contact = {
        'id': contacts[-1]['id']+1,
        'Name': request.form['Name'],
        'Contact': request.form['Contact'],
        'Done': 'false'
    }
    contacts.append(contact)
    return jsonify({"Status":'success', 'Message':'Contact added successfully'}, 201)

@app.route('/contacts')
def get_contacts():
    return jsonify({"Status":'success', 'data':contacts})

app.run()
