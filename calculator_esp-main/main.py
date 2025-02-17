from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def result_calculate(size, lights, device):
    """Calcula el consumo energético (función de utilidad)."""
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    return size * home_coef + lights * light_coef + device * devices_coef

# --- Rutas ---

@app.route('/')
def index():
    """Página de inicio."""
    return render_template('index.html')

@app.route('/<size>')
def lights(size):
    """Página para seleccionar la cantidad de luces."""
    return render_template('lights.html', size=size)

@app.route('/<size>/<lights>')
def electronics(size, lights):
    """Página para seleccionar la cantidad de dispositivos."""
    return render_template('electronics.html', size=size, lights=lights)

@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    """Página de resultados de la calculadora."""
    result = result_calculate(int(size), int(lights), int(device))
    return render_template('end.html', result=result)

@app.route('/form')
def form():
    """Página del formulario."""
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    """Procesa el envío del formulario, guarda los datos y redirige."""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        date = request.form['date']

        # --- aqui se guardan los datos con form.txt (con UTF-8) ---
        try:
            with open('form.txt', 'a', encoding='utf-8') as f:  # <--- encoding='utf-8'
                f.write(f"Nombre: {name}\n")
                f.write(f"Email: {email}\n")
                f.write(f"Dirección: {address}\n")
                f.write(f"Fecha: {date}\n")
                f.write("-" * 20 + "\n")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")
            return "Error al guardar los datos", 500

        # Redirige a form_result.html y pasa los datos
        return render_template('form_result.html', name=name, email=email, address=address, date=date)

if __name__ == '__main__':
    app.run(debug=True)