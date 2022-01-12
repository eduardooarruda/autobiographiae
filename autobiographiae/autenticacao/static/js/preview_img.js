function previewImagem() {
    var imagem = document.querySelector("#foto").files[0];
    var preview = document.querySelector("#img");
    document.querySelector("#img").style.width = "200px";

    var reader = new FileReader();
    reader.onloadend = function () {
        preview.src = reader.result;
    };
    if (imagem) {
        reader.readAsDataURL(imagem);
    } else {
        preview.src =
            "{{ url_for('autenticacao.static', filename='img/foto_usuario.png') }}";
        document.querySelector("#img").style.width = "150px";
    }
}
