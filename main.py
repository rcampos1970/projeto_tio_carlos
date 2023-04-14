from openpyxl import load_workbook
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])

def handle_data():
    while(1==1):
        
        name = request.form.get('nam')
        description = request.form.get('des')
        price = request.form.get('pri')
        print(name)
        print(description)
        print(price)
        #writing to a txt file
        file = open('results.txt','a')
        file.write(str(name))
        file.write(";")
        file.write(str(description))
        file.write(";")
        file.write(str(price))
        file.write(";")
        file.write("\n")
        return render_template("index.html")
    file.close()
if __name__ == "__main__":
    app.run()