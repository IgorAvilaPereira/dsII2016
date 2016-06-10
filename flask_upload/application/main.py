import os
from flask import Flask #para
from flask import render_template #templates
from flask import request #requisicoes e formularios
from flask import redirect #redirecionamento
from flask import url_for #redirecionamento
from flask import flash # mensagens
from flask import jsonify #json
from werkzeug.utils import secure_filename

# diretorio onde os arquivos serao armazenados
UPLOAD_FOLDER = './arquivos/'

# extensoes permitidas
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

# para usar sessoes e usar as mensagens flash
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# tamanho maximo dos arquivos (exemplo - no maximo 1 mb)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Formulario sem o input file...')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            
            #print "Antes do Secure:"+file.filename
            filename = secure_filename(file.filename)            
            print "Depois do Secute:"+filename
            
            # se quiser manter o nome original
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            # se quiser colocar outro nome no arquivo
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "igor."+ filename.rsplit('.', 1)[1]))
            
            flash('Upload realizado com sucesso')                                      
            return redirect(url_for('upload_file'))
    return render_template('upload_file.html')

# ===========================================================================

# EXEMPLO AJAX

@app.route('/teste_ajax')
def index():
    return render_template("teste_ajax.html")        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():
    username = request.form['username']
    secret = request.form['secret']
    #return str(secret) + "eh muito ruim"
    return jsonify(username=username, secret = secret)    
# ===============================================================================


if __name__ == '__main__':    
    app.debug = True
    app.run()