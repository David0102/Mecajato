function exibir_form_servico(tipo) {

    add_servico = document.getElementById('form_servico')
    list_servicos = document.getElementById('teste')

    if (tipo == "1") {
        add_servico.style.display = "block"
        list_servicos.style.display = "none"
    }

    if (tipo == "2") {
        add_servico.style.display = "none"
        list_servicos.style.display = "block"
    }

}