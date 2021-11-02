function navbarfunction() {
    var x = document.getElementById("menu");
    if (x.style.display == "block") 
    {
        x.style.display = "none";
    }
    else {
        x.style.display = "block";
    };
}

function hidealert(){
  var alert = document.getElementById("alert")
 
  alert.classList.remove("show")  
  alert.classList.add("fade")  

  alert.remove()
  
}

