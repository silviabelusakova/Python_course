from flask import Flask, request, send_file, render_template

app = Flask(__name__)

@app.route('/home', methods=['GET','POST'])
def home():


    if request.method =='POST':

        name = request.form['name']
        message = request.form['message']
        return f'{name} says: {message}'
    
    if request.method =='GET':

        return render_template('index.html')

    # username = request.args.get('name', 'Guest')
    # return render_template('index.html', name=username)


# @app.route('/greet', methods=['GET'])
# def greet():

#     name = request.args.get('name', 'Guest')
#     msg = f'Hello {name}'

#     return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


# curl localhost:5000/greet?name=Peter
# curl 127.0.0.1:5000/greet?name=Peter
# Hello Peter

# curl localhost:5000/greet
# Hello Guest



#image return from flask 


# @app.route('/get_image')
# def get_img():

#     filename ='sid.jpg'

#     return send_file(filename, mimetype='image/jpg')


