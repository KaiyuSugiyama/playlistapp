"""Driver for Web server"""

from views import app

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=False,host='192.168.1.182',port=5000)
