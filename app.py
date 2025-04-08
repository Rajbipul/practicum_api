from flask import Flask, render_template

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
def web():
    return render_template('index.html')  # ✅ Corrected here

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
