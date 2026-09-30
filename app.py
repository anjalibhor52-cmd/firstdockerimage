from flask import Flask
app = Flask(__name__) 

@app.route("/") 
def home():
    return "Hello World!" 

@app.route("/anju")
def Anjali():
    return "Anjali is samrt girl!"
@app.route("/anu")
def Anushka():
    return "Anushka is good girl!"
    
if __name__ == "__main__": 
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000) 
