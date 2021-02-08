//Ocultar mensagem de erro
function ocultarErro(){
    
    //Alterando as características CSS do H1
    var exibirErro = document.getElementsByTagName("h1")[0].style.display="none";
    
}

//Validar
function validar(){
    
    //Obter os objetos
    var username = document.getElementById("username");
    var password = document.getElementById("password");
    var exibirErro = document.getElementsByTagName("h1")[0];
    
    //Validação
    if(username.value == ""){
        exibirErro.innerHTML = "O campo Username não pode estar vazio.";
        exibirErro.style.display = "block";
        nome.focus;
        return false;
        
    }else if(username.value.length < 3){
        exibirErro.innerHTML = "O campo Username deve ter pelo menos três caracteres.";
        exibirErro.style.display = "block";
        nome.focus;
        return false;

    }if(password.value == ""){
        exibirErro.innerHTML = "O campo Senha não pode estar vazio.";
        exibirErro.style.display = "block";
        nome.focus;
        return false;

    }else if(password.value.length < 3){
        exibirErro.innerHTML = "O campo Senha deve ter pelo menos três caracteres.";
        exibirErro.style.display = "block";
        nome.focus;
        return false;

    }  
    
}