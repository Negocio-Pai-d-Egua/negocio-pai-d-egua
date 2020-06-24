from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)
cardapio={
    "combinado_1":{
        "prato":"Frango Assado","preco":"12.00","src":"../static/image/alimento_1.jpg","descricao":"Frango, batata frita, salada e molho de tomate para acompanhar"
    },
"combinado_2":{
        "prato":"Doce de Cupuaçu","preco":"8.00","src":"../static/image/Aperitivo1.png","descricao":"Mistura de doce de cupuaçu com leite e outros acompanhamentos.."
    },
"combinado_3":{
        "prato":"Bolinho de Carne","preco":"5.00","src":"../static/image/Aperitivo2.png","descricao":"Bolinho de carne com torta de maçã."
    },
"combinado_4":{
        "prato":"Tortilha","preco":"4.00","src":"../static/image/Aperitivo3.png","descricao":"Tortilha de varios sabores."
    },
"combinado_5":{
        "prato":"Camarões","preco":"11.00","src":"../static/image/Aperitivo4.png","descricao":"Camarões empanados,fritos e assados servidos em um balde."
    },
"combinado_6":{
        "prato":"Pratos da Região","preco":"12.00","src":"../static/image/Aperitivo5.png","descricao":"Pratos exóticos e regionais."
    }
}

carr=[]
pedidos_clientes=[]
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/combinado",methods= ["post"])
def combinado():
    combinado=request.form["prato"]
    preco = cardapio[combinado]["preco"]
    src= cardapio[combinado]["src"]
    descricao= cardapio[combinado]["descricao"]
    combinado = cardapio[combinado]["prato"]
    return render_template("Comida/combinado_1.html",combinado=combinado,preco=preco,src=src,descricao=descricao)

@app.route("/validacao_compra",methods= ["post"])
def validacao_compra():
    pedido=request.form.to_dict()
    carr.append(pedido)
    return redirect(url_for("home"))

@app.route("/carrinho")
def carrinho():
    total=0.0
    for produto in carr:
        total+= float(produto["preco"])
    return render_template("carrinho.html", carrinho=carr, total=total)

@app.route("/formulario", methods= ["post"])
def formulario():
    return render_template("formulario.html")

@app.route("/pedido_finalizado", methods= ["post"])
def pedido_finalizado():
    cliente=request.form.to_dict()
    pratos=carr
    pedidoatual={cliente["mesa"]:{"cliente":cliente,"pedido": pratos}}
    pedidos_clientes.append(pedidoatual)
    arquivo = open("mesa_"+cliente["mesa"]+'.txt', 'w')
    arquivo.writelines('informacoes cliente: \n')
    arquivo.writelines("nome: "+cliente["nome"]+"\n")
    arquivo.writelines("forma de pagamento: " + cliente["forma_pagamento"]+ "\n")
    arquivo.writelines("pedido: \n")
    total=0.0
    for p in carr:
        arquivo.writelines(p["prato"]+" "+p["preco"]+"\n")
        total += float(p["preco"])
    arquivo.writelines("Total:  " + str(total) + "\n")
    arquivo.close()
    carr.clear()
    return render_template("pedido_finalizado.html")

@app.route("/ver_pedido")
def ver_pedido():
    pedidos={"pedidos":pedidos_clientes}
    return pedidos



if __name__=="__main__":
    app.run(debug=True)