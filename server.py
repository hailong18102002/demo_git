from machinetranslation import translator
from flask import Flask, render_template, request,send_file
import json

app = Flask("Web Translator")
   
@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    textTranslate=translator.englishToFrench(textToTranslate)
    return "Translated text to French" + textTranslate

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    textTranslate=translator.frenchToEnglish(textToTranslate)
    return "Translated text to English"+textTranslate

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return send_file('index.html') 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
