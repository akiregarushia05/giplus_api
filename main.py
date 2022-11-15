from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf import Form
from wtforms.fields import DateField

# para instalar mysqldb
# necesito instalar previamente:
# mysql (instala descargando mysql / mysql workbench)
# mysqlclient (MacOS y linux)
# si tienen instalado mysql workbench, no es necesario instalar mysqlclient

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'us-east.connect.psdb.cloud'
app.config['MYSQL_USER'] = '6jcu49gsz7tb5qqf920q'
app.config['MYSQL_PASSWORD'] = 'pscale_pw_2o523jxZkxoC2dz3my59Gt89opRLLKgkdhNp1nFHsGl'
app.config['MYSQL_DB'] = 'database1'
#app.config['MYSQL_SSL'] = 'fake_flag_to_enable_tls'

mysql = MySQL(app)

@app.route('/')
def form():
    cursor = mysql.connection.cursor()
    cursor.execute(''' select IdTercero, TipoIdentificacionFK, NumIdentificacion, 
    Nombres, Apellidos, Telefono, Celular, Email, Ciudad, Departamento, 
    Direccion, TipoUsuarioFK, ClaveUsuario
    from tbl_Tercero;''')
    data = cursor.fetchall()
    print(data)
    cursor.close()
    return render_template('index.html', data=data)


@app.route('/tercero', methods=['POST', 'GET'])
def tercero():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(''' select IdTercero, TipoIdentificacionFK, NumIdentificacion, Nombres, Apellidos, Telefono, 
        Celular, Email, Ciudad, Departamento, Direccion, TipoUsuarioFK, ClaveUsuario
        from tbl_Tercero;''')
        data = cursor.fetchall()
        print(data)
        cursor.close()
        return render_template('index.html', data=data)

    if request.method == 'POST':
        IdTercero : int =request.form['IdTercero']
        TipoIdentificacionFK: int = request.form['TipoIdentificacionFK']
        NumIdentificacion : str = request.form['NumIdentificacion']
        Nombres: str = request.form['Nombres']
        Apellidos: str = request.form['Apellidos']
        Telefono: str = request.form['Telefono']
        Celular: str = request.form['Celular']
        Email: str = request.form['Email']
        Ciudad: str = request.form['Ciudad']
        Departamento: str = request.form['Departamento']
        Direccion: str = request.form['Direccion']
        TipoUsuarioFK : int = request.form['TipoUsuarioFK']
        ClaveUsuario : str = request.form['ClaveUsuario']

        try:
            try:
                cursor = mysql.connection.cursor()
                cursor.execute('''INSERT INTO tbl_Tercero(IdTercero, TipoIdentificacionFK, NumIdentificacion, 
                Nombres, Apellidos, Telefono, Celular, Email, Ciudad, Departamento, Direccion, 
                TipoUsuarioFK, ClaveUsuario) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                               (IdTercero, TipoIdentificacionFK, NumIdentificacion, Nombres, Apellidos, Telefono,
                                Celular, Email, Ciudad, Departamento, Direccion, TipoUsuarioFK, ClaveUsuario))
            except TypeError as e:
                print(e)
                return None
            try:
                mysql.connection.commit()
            except TypeError as e:
                print(e)
                return None
        finally:
            cursor.close()
        return redirect(url_for('tercero'))





@app.route("/eliminarTercero", methods=["POST"])
def delete():
    numIdentificacion : str = request.form.get("numIdentificacion")
    print(numIdentificacion)
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE FROM tbl_Tercero WHERE NumIdentificacion LIKE %s''', (numIdentificacion,))
    mysql.connection.commit()
    cursor.close()
    return redirect("/")

'''@app.route('/doctor')
def doctor(): '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')












