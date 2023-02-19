import os
from flask import Flask, request, jsonify, render_template, send_from_directory

diretorio = "C:\\Users\\anderson.bispo\\PycharmProjects\\API Flask Up_Arquivos\\output"

api = Flask(__name__)

@api.route("/arquivos", methods=["GET"])
def lista_arquivos():
    arquivos = []
    # Listar cada arquivo dentro do diretorio
    for nome_do_arquivo in os.listdir(diretorio):
        # puxa o endereço dos arquivos (path)
        endereco_do_arquivo = os.path.join(diretorio, nome_do_arquivo)
        # Verificar se é um arquivo ou um diretorio e se for um arquivo adiciona na lista
        if(os.path.isfile(endereco_do_arquivo)):
            arquivos.append(nome_do_arquivo)


    return jsonify(arquivos)

@api.route("/arquivos/<nome_do_arquivo>", methods=["GET"])
def get_arquivo(nome_do_arquivo):
    return send_from_directory(diretorio, nome_do_arquivo, as_attachment=True)
    #as_attachement = True baixa o arquivo pro computador / False ele abre uma page html com o arquivo

@api.route("/arquivos", methods=["POST"])
def post_arquivos():
    arquivo = request.files.get("meuArquivo") #Busca pelo id do arquivo

    print(arquivo)
    nome_do_arquivo = arquivo.filename # identifica qual o nome do arquivo
    arquivo.save(os.path.join(diretorio, nome_do_arquivo))
    # salva dentro do diretorio e com o nome do arquivo

    return '', 201

if __name__ == "__main__":
    api.run(debug=True, port=8000)