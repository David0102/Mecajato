function clientes_servicos(tipo) {
    if (tipo == '1') {
        window.location.href = "/clientes/"

    } else if (tipo == '2') {
        window.location.href = "/servicos/"

    } else if (tipo == '3') {
        window.location.href = "/usuarios/cadastro"

    } else {
        window.location.href = "/usuarios/logout"
    }
}