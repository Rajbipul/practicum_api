from flask import Flask, render_template,request,jsonify

app = Flask(__name__)
ans = '0'

# This will be read by the ESP32
@app.route("/status")
def status():
    global ans
    response = ans
    ans = '0'  # Reset after reading
    return response

@app.route("/rotate/<int:n>")
def rot(n):
    print(n)
    global ans
    ans = str(n)
    return 'okay'


@app.route("/x", methods=["POST"])
def x():
    data = request.get_json()

    # Mapping item keys to motor numbers
    item_map = {
        'item1': 1,  # Cold Drink
        'item2': 2,  # Chocolate Bar
        'item3': 3   # Chips
    }

    for item_key, motor_number in item_map.items():
        quantity = data.get(item_key, 0)
        for _ in range(quantity):
            rot(motor_number)

    print("✅ Rotation commands sent based on:", data)
    return jsonify({"status": "received", "data": data})


@app.route("/")
def web():
    return render_template('index.html')  # ✅ Corrected here

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
