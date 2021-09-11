function addelement(cam, link ){
    const new_col= document.createElement("div");
    new_col.className = "col-lg-6 m-b-3";
    const new_card = document.createElement("div");
    new_card.className= "card";
    const new_card_body  = document.createElement("div");
    new_card_body.className= "card-body";
    const new_row  = document.createElement("div");
    new_row.className= "row";
    new_row.innerHTML= cam ;
    const ifrm = document.createElement("iframe");
    ifrm.setAttribute("src", link  );
    ifrm.style.width = "640px";
    ifrm.style.height = "320px";
    document.body.appendChild(ifrm);
    document.getElementById('video').appendChild(new_col);
    new_col.appendChild(new_card);
    new_card.appendChild(new_card_body);
    new_card_body.appendChild(new_row);
    new_row.appendChild(ifrm);
    
    


}