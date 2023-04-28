function exibir_form_servico(tipo) {

    add_servico = document.getElementById('form_servico')

    if (tipo == "1") {
        add_servico.style.display = "block"
    }

    if (tipo == "2") {
        window.location.href = "/servicos/lista_servicos/"
    }

}