from flask import Flask, jsonify, request
import util

app=Flask(__name__)

@app.route('/classify_image',methods=['GET','POST'])
def classify_image():
    image_data=request.form['image_data']

    response=jsonify(util.classify_image(image_data))
    response.headers.add('Acess-Allow-Control-Origin','*')

    return response




@app.route('/hello')
def hello():
    return 'Hi'


if __name__=='__main__':
    print('Starting Flask Server for Image Classification')
    util.load_saved_artifacts()
    app.run(debug=True)




# one can send the image to the backend server from UI via., an aws-s3 bucket link or via., a base64 encoded string(https://www.base64-image.de)..
# the server is the place where the classification process occurs.. 