import os
from flask import Flask, request, render_template, send_file, redirect, url_for, flash
from werkzeug.utils import secure_filename
from steganography import encode_image, decode_image

app = Flask(__name__)
app.secret_key = "stegano_secret"
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    image = request.files['image']
    message = request.form['message']

    if not image or not message:
        flash("Image and message are required.")
        return redirect(url_for('index'))

    filename = secure_filename(image.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], 'input_' + filename)
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'encoded_' + filename)
    
    image.save(input_path)
    encode_image(input_path, message, output_path)

    return send_file(output_path, as_attachment=True)

@app.route('/decode', methods=['POST'])
def decode():
    image = request.files['stego_image']

    if not image:
        flash("Image is required for decoding.")
        return redirect(url_for('index'))

    filename = secure_filename(image.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], 'decode_' + filename)
    image.save(input_path)

    message = decode_image(input_path)
    return render_template('index.html', decoded_message=message)

if __name__ == '__main__':
    app.run(debug=True)
