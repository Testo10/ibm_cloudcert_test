from machinetranslation import translator, testes
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def translate():
    text = ''
    translation = None

    if request.method == 'POST':
        text = request.form['text']

        if request.form['translate'] == 'French':
            translation = translator.english_to_french(text)
        elif request.form['translate'] == 'English':
            translation = translator.french_to_english(text)

    return render_template('index.html', text=text, translation=translation)


if __name__ == "__main__":
    app.run(port=4926)

#@app.route('/translate/french-to-english/<text>')
#def translate_french_to_english(text):
 #   translated_text = machinetranslation.french_to_english(text)
  #  return translated_text

#if __name__ == '__main__':
 #   app.run()
