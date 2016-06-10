function exemplo_ajax_cep(){

    // criacao do objeto ajax
    var req = new XMLHttpRequest();

    // trecho que trata da resposta
    req.onreadystatechange = function() {
        if (req.readyState == 4 && req.status == 200) {            
            var objeto = JSON.parse(req.responseText);
            alert(req.responseText);            
            //alert(objeto.bairro);
            //document.getElementById('myDiv').innerHTML = "username:"+response.username + " <br> Secret:"+response.secret;            
            //document.getElementById('myDiv').innerHTML = req.responseText;
        } else if (req.status == 404){
            alert("ops....deu xabum....");
        }
    }    

    // trecho que trata da requisicao e do envio de parametros para o flask (servidor)
    req.open('GET', 'https://baconipsum.com/api/?type=meat-and-filler')
    //req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    //var un = document.getElementById('scname').value;
    //var sec = document.getElementById('secret').value;
    //var postVars = 'username='+un+'&secret='+sec;
    req.send(); 
}


function exemplo_ajax() {
    // criacao do objeto ajax
    var req = new XMLHttpRequest();

    // trecho que trata da resposta
    req.onreadystatechange = function() {
        if (req.readyState == 4 && req.status == 200) {
            var response = JSON.parse(req.responseText);
            document.getElementById('myDiv').innerHTML = "username:"+response.username + " <br> Secret:"+response.secret;            
            //document.getElementById('myDiv').innerHTML = req.responseText;
        } else if (req.status == 404){
            alert("ops....deu xabum....");
        }
    }    

    // trecho que trata da requisicao e do envio de parametros para o flask (servidor)
    req.open('POST', '/ajax')
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    var un = document.getElementById('scname').value;
    var sec = document.getElementById('secret').value;
    var postVars = 'username='+un+'&secret='+sec;
    req.send(postVars);        

    // retorno
    return false
}