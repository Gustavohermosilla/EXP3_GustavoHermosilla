$(document).ready(function(){

    $("#enviar").click(function(){

        $.get("https://apis.digital.gob.cl/fl/feriados/2023",function(data){

            $.each(data ,function(i,item)
                {
                    $("#categorias").append("<tr><td>"+ item.nombre +
                    "</td><td>"+ item.fecha +
                    "</td><td>"+ item.irrenunciable +
                    "</td><td>"+ item.tipo +"</td></tr>");
                  
                });


        });
    });
});

function MostrarFecha() 
        {   document.getElementById('demo').innerHTML = Date();
         
        }

