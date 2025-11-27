from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    form_data = {'gender': 'male', 'height_father': '', 'height_mother': ''}

    if request.method == 'POST':
        form_data = {
            'gender': request.form.get('gender', 'male'),
            'height_father': request.form.get('height_father', ''),
            'height_mother': request.form.get('height_mother', '')
        }

        try:
            height_father, height_mother = map(float, (form_data['height_father'], form_data['height_mother']))
            for h, p in [(height_father, "ayah"), (height_mother, "ibu")]:
                if not (55 <= h <= 280):
                    raise ValueError(f"Tinggi {p} harus antara 55 cm dan 280 cm.")

            avg = (height_father + height_mother + (13 if form_data['gender'] == 'male' else -13)) / 2
            result = f"Perkiraan tinggi anak adalah {round(avg-7.5,1)} cm sampai dengan {round(avg+7.5,1)} cm"

        except ValueError as e:
            result = {'error': 'Masukkan angka yang valid untuk tinggi badan.' if "could not convert" in str(e) else str(e)}

    return render_template('index.html', result=result, form=form_data)

if __name__ == '__main__':
    app.run(debug=True)