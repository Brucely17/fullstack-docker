from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def run():
    if request.method == 'GET':
        
        return """
                <h1>Rioyich Tenkai - Domain Expansion (G)</h1>
                <br> 
                <h2>Gojo Sataraou</h2> <br><h2>Sukuna</h2>
                <br>
                <h2>Arigatho Osaimasu</h2>
                """
    elif request.method == 'POST':
        
        data = request.get_json()  
        if not data:
            return jsonify({"error": "No JSON data received"}), 400
        return jsonify({
            "message": "Data received successfully",
            "received_data": data
        }), 200

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
