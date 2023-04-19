function add_carro(){

    container = document.getElementById('form-carro')

    html = "<br><div class='row'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro' required></div> <div class='col-md'><input type='text' placeholder='Placa' class='form-control' name='placa' required> </div> <div class='col-md'><input type='number' placeholder='Ano' class='form-control' name='ano' required> </div></div>"

    container.innerHTML += html


}

function exibir_form(tipo){

    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att-cliente')

    if(tipo == "1"){
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"
    }

    if(tipo == "2"){
        add_cliente.style.display = "none"
        att_cliente.style.display = "block"
    }

}