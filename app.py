from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Créer la base de données et la table


def init_db():
    conn = sqlite3.connect('base_de_donnees.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS livres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            auteur TEXT NOT NULL,
            disponible BOOLEAN DEFAULT 1
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/livres')
def livres():
    conn = sqlite3.connect('base_de_donnees.db')
    c = conn.cursor()
    c.execute('SELECT * FROM livres')
    livres = c.fetchall()
    conn.close()
    return render_template('livres.html', livres=livres)


@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        conn = sqlite3.connect('base_de_donnees.db')
        c = conn.cursor()
        c.execute('INSERT INTO livres (titre, auteur) VALUES (?, ?)', (titre, auteur))
        conn.commit()
        conn.close()
        return redirect('/livres')
    return render_template('ajouter_livre.html')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
