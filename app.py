from flask import Flask, render_template, request

app = Flask(__name__)

# District-wise dialect dictionary (replace/add more as needed)
dialects = {
    "Kottayam": {
        "how are you": "സുഖമാണോ മച്ചാ",
        "what are you doing": "എന്താ പണിയുന്നു മച്ചാ",
        "where are you going": "എവിടെയാ പോവുന്നേ",
        "i am fine": "എനിക്ക് സുഖമാണ്",
    },
    "Idukki": {
        "how are you": "സുഖമാണോ സൈപ്പേ",
        "what are you doing": "എന്താ ചെയ്യുന്നു സൈപ്പേ",
        "where are you going": "എവിടെയാ പോവുന്നേ സൈപ്പേ",
        "i am fine": "എനിക്ക് സുഖമാണെ",
    },
    "Ernakulam": {
        "how are you": "സുഖമാണോ ചേട്ടാ",
        "what are you doing": "എന്താ ചെയ്യുന്നു ചേട്ടാ",
        "where are you going": "എവിടെയാ പോവുന്നേ ചേട്ടാ",
        "i am fine": "എനിക്ക് സുഖമാണു ചേട്ടാ",
    },
    "Malappuram": {
        "how are you": "സുഖമാണോ ചേട്ടാ",
        "what are you doing": "ചെയ്യുന്‌നെന്താ ചേട്ടാ",
        "where are you going": "പോകുന്‌നെവിടെ ചേട്ടാ",
        "i am fine": "എനിക്ക് സുഖമാണു ചേട്ടാ",
    },
    "Trivandrum": {
        "how are you": "സുഖമാണോ മച്ചാ",
        "what are you doing": "എന്ത് ചെയ്യുന്നു മച്ചാ",
        "where are you going": "എവിടെയാ പോകുന്നേ മച്ചാ",
        "i am fine": "എനിക്ക് സുഖമാണ് മച്ചാ",
    },
}

districts = list(dialects.keys())

standard_translation = {
    "how are you": "സുഖമാണോ",
    "what are you doing": "നീ എന്താണ് ചെയ്യുന്നത്",
    "where are you going": "നീ എവിടെയാണ് പോകുന്നത്",
    "i am fine": "എനിക്ക് സുഖമാണ്",
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    malayalam = ""
    if request.method == "POST":
        english = request.form.get("english", "").lower().strip()
        district = request.form.get("district")

        if english and district:
            malayalam = standard_translation.get(english, "")
            district_dialect = dialects.get(district, {})
            dialect_translation = district_dialect.get(english, "")

            if dialect_translation:
                result = dialect_translation
            else:
                result = "❌ Sorry, dialect not available for this phrase."
        else:
            result = "❌ Please enter a phrase and select a district."

    return render_template("index.html", result=result, malayalam=malayalam, districts=districts)

if __name__ == "__main__":
    app.run(debug=True)
