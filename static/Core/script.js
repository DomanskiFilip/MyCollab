// function updates the year in the footer

function updateYear(){
    let year = document.getElementById("year");
    let date = new Date();
    year.innerHTML = date.getFullYear();
  }

  updateYear();