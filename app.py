import pymssql

server = 'myserver.database.windows.net'
database = 'dmhngh'
user_name = 'dmjhjbjn'
password = 'kjkjgjfyrdr46ryfe#14'

########################################################################

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def home():
    result = []
    columns = []

    if request.method=="POST":
        user_question = request.form["query"]
        if not user_question.lower().startswith("select"):
            return "You Can Only Search your request. cant Modify."
        
        try:
            now_connect = pymssql.connect(server=server, user= user_name, password= password, database= database)
            cursor = now_connect.cursor()
            cursor.execute(user_question)
            result = cursor.fetchall()

            columns = [column[0] for column in cursor.description]
            now_connect.close()

        except:
            return "Please Provide correct Code"
        
    return render_template("index.html", result=result, columns=columns)

if __name__=="__main__":
    app.run(debug=True)
