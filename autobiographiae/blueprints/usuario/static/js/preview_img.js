function previewImagem() {
    var imagem = document.querySelector("#foto").files[0];
    var preview = document.querySelector("#imagem");
    document.querySelector("#imagem").style.width = "300px";

    var reader = new FileReader();
    reader.onloadend = function () {
        preview.src = reader.result;
    };
    if (imagem) {
        reader.readAsDataURL(imagem);
    } else {
        preview.src =
            "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png";
        document.querySelector("#imagem").style.width = "150px";
    }
}
