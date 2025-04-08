from flask import Flask

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
    global ans
    ans = str(n)
    return 'okay'

@app.route("/")
def wlcome():
    return "Hi! Flask server is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
