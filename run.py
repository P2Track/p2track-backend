from flask import Flask, jsonify, request
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, parent_dir)

from services.service import add_information, get_all_information, get_information

app = Flask(__name__)

@app.route('/post_package', methods=['POST'])
def add_information_route():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'message': 'Data is required'}), 400
        
        block = add_information(data)
        return jsonify({'message': 'Inoformation added succesfully', 'block': block.__dict__}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route("/get_package/<int:index>", methods=['GET'])
def get_information_route(index):
    try:
        data = get_information(index)
        return jsonify({'data': data}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/get_all_packages', methods=['GET'])
def get_all_information_route():
    try:
        all_data = get_all_information()
        return jsonify({'data': all_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
