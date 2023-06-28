$(function(){
    $("#contactanos").validate({
        rules:{
            nom:{
                required:true
            },
            ape:{
                required:true
            },
            correo:{
                required:true,
                email:true
            },
            fono:{
                required:true,
                number:true
            },
            carta:{
                required:true
            }
        },//rules
        messages:{
            nom:{
                required:'Ingrese nombre de usuario',
                minlength:'Formato incorrecto de nombre (3)'
            },
            ape:{
                required:'Ingrese un apellido',
                minlength:'Formato incorrecto de apellido(3)'
            },
            correo:{
                required:'Ingrese correo de usuario',
                email: 'Formato de correo inválido'
            },
            fono:{
                required: 'Ingrese teléfono',
                minlength:'Cantidad de digitos insuficientes(9)'
            },
            carta:{
                required: 'Ingrese su descripcion detallada',
                minlength:'Cantidad de caracteres insuficientes(10)'
            },
            
        },//messages                
    })
});

function CambiaColor(a)
        {
            a.style.background = "yellow";
        }

        function CambiarMayusculas()
        {
            var a = document.getElementById('nom');
            a.value = a.value.toUpperCase();
        }