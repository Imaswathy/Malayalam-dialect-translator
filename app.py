from flask import Flask, render_template, request

app = Flask(__name__)

phrasebook = {
    "how are you": "സുഖമാണോ?",
    "what is your name": "നിന്റെ പേര് എന്താണ്?",
    "where are you going": "എവിടേക്കാണ് പോകുന്നത്?",
    "i am hungry": "എനിക്ക് വിശക്കുന്നു.",
    "what are you doing": "എന്താണ് ചെയ്യുന്നത്?",
    "i am going home": "ഞാൻ വീട്ടിലേക്ക് പോകുകയാണ്.",
    "come here": "ഇവിടെ വാ.",
    "what happened": "എന്താണ് സംഭവിച്ചത്?",
    "don't worry": "പൊറുതിയിരിക്കുക.",
    "thank you": "നന്ദി."
}

dialects = {
    "Thiruvananthapuram": {
        "സുഖമാണോ?": "സുഖമാണോ ?",
        "നിന്റെ പേര് എന്താണ്?": "പേരേന്താണു?",
        "എവിടേക്കാണ് പോകുന്നത്?": "എവിടെക്കാണു പോകുന്നത്?",
        "എനിക്ക് വിശക്കുന്നു.": "എനിക്ക് വിശക്കുന്നു.",
        "എന്താണ് ചെയ്യുന്നത്?": "എന്താ ചെയ്യുന്നത്?",
        "ഞാൻ വീട്ടിലേക്ക് പോകുകയാണ്.": "ഞാൻ വീട്ടേക്കു പോവുകയാണ്.",
        "ഇവിടെ വാ.": "ഇവിടെ വാ.",
        "എന്താണ് സംഭവിച്ചത്?": "എന്താ പറ്റി?",
        "പൊറുതിയിരിക്കുക.": "ശാന്തിയാകു.",
        "നന്ദി.": "നന്ദി."
    },
    "Kollam": {
        "സുഖമാണോ?": "സുഖമാണേടാ?",
        "നിന്റെ പേര് എന്താണ്?": "പേരേടാ എന്താണ്?",
        "എവിടേക്കാണ് പോകുന്നത്?": "പോകുന്നേടെ എവിടെ?",
        "എനിക്ക് വിശക്കുന്നു.": "വിശക്കുന്നു ടേ!",
        "എന്താണ് ചെയ്യുന്നത്?": "ചെയ്യുന്നത് എന്താടാ?",
        "ഞാൻ വീട്ടിലേക്ക് പോകുകയാണ്.": "ഞാൻ വീട്ടേക്കാണ് പോവുന്നത് ടേ.",
        "ഇവിടെ വാ.": "ഇവിടെ വാ ടേ!",
        "എന്താണ് സംഭവിച്ചത്?": "പറ്റിയേടാ എന്താ?",
        "പൊറുതിയിരിക്കുക.": "ഒരുക്കനെ ഇരിക്കെടാ!",
        "നന്ദി.": "നന്ദിയാ ടേ!"
    },
    # Add other districts here (you already have them; keep unchanged)
    # ...
    "Kasargod": {
        "സുഖമാണോ?": "സുഖമാണോ ?",
        "നിന്റെ പേര് എന്താണ്?": "പേരേന്താണേ?",
        "എവിടേക്കാണ് പോകുന്നത്?": "എവിടെ പോവുന്നേ?",
        "എനിക്ക് വിശക്കുന്നു.": "എനിക്ക് വിശക്കുന്നു കേളോ.",
        "എന്താണ് ചെയ്യുന്നത്?": "എന്താ ചെയ്യുന്നു കേളോ?",
        "ഞാൻ വീട്ടിലേക്ക് പോകുകയാണ്.": "ഞാൻ വീട്ടിലേക് പോവുന്നേ കേളോ.",
        "ഇവിടെ വാ.": "ഇവിടെ വാ കേളോ.",
        "എന്താണ് സംഭവിച്ചത്?": "എന്താ പറ്റി കേളോ?",
        "പൊറുതിയിരിക്കുക.": "ശാന്തിയായി ഇരിക്കേ കേളോ.",
        "നന്ദി.": "നന്ദി കേളോ."
    }
}

districts = list(dialects.keys())

def translate(english, district):
    mal = phrasebook.get(english.lower())
    if not mal:
        return None, "❌ Phrase not found."
    slang = dialects[district].get(mal, mal)
    return mal, slang

@app.route('/', methods=['GET', 'POST'])
def index():
    mal = result = None
    if request.method == 'POST':
        eng = request.form.get('english', '').strip()
        district = request.form.get('district', '')
        if eng and district:
            mal, result = translate(eng, district)
        else:
            result = "⚠️ Please enter a phrase and select a district."
    return render_template('index.html', districts=districts, malayalam=mal, result=result)

if __name__ == '__main__':
    app.run(debug=True)
