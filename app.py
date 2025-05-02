from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
items = []

# Create
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item = {
        'id': len(items) + 1,
        'name': data['name'],
        'description': data.get('description', '')
    }
    items.append(item)
    return jsonify(item), 201

# Read all
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# Read one
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item), 200

# Update
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])
    return jsonify(item), 200

# Delete
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

# New feature: Search 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)