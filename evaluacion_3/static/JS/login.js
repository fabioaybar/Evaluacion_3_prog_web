$(function(){
    $("#boton_registro").click(function(){

        var usuario1 = $("#id_usuario").val();
        var pass = $("#id_pass").val();

        if (usuario1 == "admin"){
            if(pass == 1234){
                alert("USUARIO CORRECTO")
                alert("BIENVENIDO!!")
                
            }
            else{
                alert("usuario o contraseña incorrecto")
                alert("ACCESO DENEGADO!!")
                
            }
        }
        else{
            alert("usuario o contraseña incorrecto")
            alert("ACCESO DENEGADO!!")
        }



    })
});