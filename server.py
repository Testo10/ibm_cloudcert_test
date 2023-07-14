import machinetranslation
from flask import Flask

app = Flask(__name__)

@app.route('/translate/english-to-french/<text>')
def translate_english_to_french(text):
    translated_text = machinetranslation.english_to_french(text)
    return translated_text

@app.route('/translate/french-to-english/<text>')
def translate_french_to_english(text):
    translated_text = machinetranslation.french_to_english(text)
    return translated_text

if __name__ == '__main__':
    app.run()
