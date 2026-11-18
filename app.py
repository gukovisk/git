from flask import Flask, render_template

# Inicializa o aplicativo web
app = Flask(__name__)

# Rota principal do site
@app.route('/')
def home():
    # Retorna a nossa página HTML quando alguém entrar no site
    return render_template('index.html')

if __name__ == '__main__':
    # Roda o servidor localmente
    app.run(debug=True)