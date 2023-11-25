function getPrice(){
    const milk=document.querySelector('[name=milk]').Checked;
    const sugar=document.querySelector('[name=sugar]').Checked;
    const drink=document.querySelector('[name=drink]:checked').value;

    const obj={
        'method':'get-price',
        'params':{
            drink:drink,
            milk:milk,
            sugar:sugar
        }
    }

    fetch('/lab7/api',{
        method:'POST', 
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify(obj)
    })
    .then (function(resp){
        return resp.json();
    })
    .then (function(data){
        document.querySelector('#price').innerHTML = 'Цена напитка:${data.result} rub'
    })

}