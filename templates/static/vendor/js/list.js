function ver_contato(id) {
    console.log(id);
    fetch('/contatos/detalhes/' + id)
        .then(response => response.text())
        .then(html => {
        $('#exampleModal').modal('show');
            document.querySelector('.modal-body').innerHTML = html;
        });
}


