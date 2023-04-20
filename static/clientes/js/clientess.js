function add_carro() {

    container = document.getElementById('form-carro')

    html = "<br><div class='row'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro' required></div> <div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='placa' required> </div> <div class='col-md'><input type='number' placeholder='Ano' class='form-control' name='ano' required> </div></div>"

    container.innerHTML += html

}

function exibir_form(tipo) {

    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att-cliente')

    if (tipo == "1") {
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"
    }

    if (tipo == "2") {
        add_cliente.style.display = "none"
        att_cliente.style.display = "block"
    }

}

function exibir_form(tipo) {

    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att-cliente')

    if (tipo == "1") {
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"
    }

    if (tipo == "2") {
        add_cliente.style.display = "none"
        att_cliente.style.display = "block"
    }

}

function dados_cliente() {
    cliente = document.getElementById('cliente-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_cliente = cliente.value

    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data
    }).then(function (result) {
        return result.json()

    }).then(function (data) {

        document.getElementById('form-att-cliente').style.display = "block"
        document.getElementById('nome').value = data['cliente']['nome']
        document.getElementById('sobrenome').value = data['cliente']['sobrenome']
        email = document.getElementById('email').value = data['cliente']['email']
        cpf = document.getElementById('cpf').value = data['cliente']['cpf']

        div_carros = document.getElementById('carros')
        div_carros.innerHTML = ""

        for (i = 0; i < data['carros'].length; i++) {

            div_carros.innerHTML += "<form action='/clientes/update_carro/" + data['carros'][i]['id'] + "' method='POST'>\
                <div class='row'>\
                    <div class='col-md'>\
                        <input type='text' class='form-control' name='carro' value='" + data['carros'][i]['fields']['carro'] + "'>\
                    </div>\
                    <div class='col-md'>\
                        <input type='text' class='form-control' name='placa' value='" + data['carros'][i]['fields']['placa'] + "'>\
                    </div>\
                    <div class='col-md'>\
                        <input type='text' class='form-control' name='ano' value='" + data['carros'][i]['fields']['ano'] + "'>\
                    </div>\
                    <div class='col-md'>\
                        <input type='submit' class='btn btn-success' value='Salvar'>\
                    </div>\
                </div><br>"

        }

    })
}