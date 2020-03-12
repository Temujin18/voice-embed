from flask import Flask, render_template, flash, request
import os
import numpy as np
from utils.embed import audio2embed

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/embed', methods=['POST', 'GET'])
def embed():
    if request.method == 'POST':
        if request.files:

            audio_file = request.files['audio-file']

            local_audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
            audio_file.save(local_audio_path)
            voice_embed = audio2embed(local_audio_path)

            local_embed_path = os.path.join(app.config['EMBEDS_FOLDER'], audio_file.filename.split('.')[0])
            np.save(local_embed_path, voice_embed)
    return render_template('index.html', message='File is now being processed.')


if __name__ == "__main__":
    app.debug = True
    app.run()