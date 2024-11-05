
$(document).ready(function () {

        $("#form").submit(function (event) {
            event.preventDefault();


            $.ajax({
                type: "POST",
                url: "/basic",
                data: {
                          type:$('.type:checked').val(),
                          loc: $('#loc').val()
                 },

                dataType: 'json',
                success: function (data) {
                    $("#kloc").text(data.kloc);
                    $("#effort").text(data.effort +" "+"PMs");
                    $("#time").text(data.time+" "+"months");
                    $("#persons").text(data.persons+" "+"persons");
                    $("#productivity").text(data.productivity+" "+"KLOC / PM");

                }
            });
        });
});




$(document).ready(function () {

        $("#form2").submit(function (event) {
            event.preventDefault();

            var formvalues = $(this).serialize();


            $.ajax({
                type: "POST",
                url: "/intermediate",
                data: formvalues,
                dataType: 'json',
                success: function (data) {
                    $("#eaf").text(data.eaf);
                    $("#kloc").text(data.kloc);
                    $("#effort").text(data.effort +" "+"PMs");
                    $("#timeee").text(data.time+" "+"months");
                    $("#persons").text(data.persons+" "+"persons");
                    $("#productivity").text(data.productivity+" "+"KLOC / PM");

                }
            });
        });
});




function select(valuetype) {
       var attName = $(valuetype).data('value');
       document.getElementById(attName).innerText = valuetype.innerText;
       $('[name="' + attName + '"]').val(valuetype.innerText);
    }




