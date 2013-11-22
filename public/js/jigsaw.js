$(document).ready(function(){
    function replaceAll(s1,s2,s3){
        var r = new RegExp(s2.replace(/([\(\)\[\]\{\}\^\$\+\-\*\?\.\"\'\|\/\\])/g,"\\$1"),"ig");
        return s1.replace(r,s3);
    }

    $("body div").each(function(i) {
        var id = $(this).attr("id");
        var type = $(this).attr("type");
        var data = $(this).attr("data");
 
        var height = $(this).attr("height");
        if (!height){
            height = '500px';
        }

        var width = $(this).attr("width");
        if (!width){
            width = '1333px';
        }


        if (id && type){
            // static data
            if (data) {
               if (type == 'line' || type == 'column'){
                    url = '/ajax/line';
               }
               else if (type == 'pie'){
                    url = '/ajax/pie';
               }
               else if (type == 'map'){
                    url = '/ajax/map';
               }
               $.getJSON(url+"?id="+id+"&type="+type+"&data="+data+"&callback=?",  function(data){
                  console.log(data);
                  $("#"+replaceAll(id, "|", "\\|")).css("height", height); 
                  $("#"+replaceAll(id, "|", "\\|")).css("width", width);
                  $("#"+replaceAll(id, "|", "\\|")).html(data.js);
               });
            }
        }
    });
});
