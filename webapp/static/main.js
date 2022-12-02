function showComp() {
    var x = document.getElementById("comp");
    var y = document.getElementById("completion");
    var z = document.getElementById("open");
    if (x.style.display === "none") {
      x.style.display = "block";
      y.style.display = "none";
      z.style.display = "none";
    } else if (x.style.display === "block") {
      x.style.display = "block";
      y.style.display = "none";
      z.style.display = "none";
    } else {
      x.style.display = "none";
      y.style.display = "none";
      z.style.display = "none";
    }
  }

  function showCompletion() {
    var x = document.getElementById("comp");
    var y = document.getElementById("completion");
    var z = document.getElementById("open");
    if (y.style.display === "none") {
      x.style.display = "none";
      y.style.display = "block";
      z.style.display = "none";
    } else if (y.style.display === "block") {
      x.style.display = "none";
      y.style.display = "block";
      z.style.display = "none";
    } else {
      x.style.display = "none";
      y.style.display = "none";
      z.style.display = "none";
    }
  }
  
  function showOpen() {
    var x = document.getElementById("comp");
    var y = document.getElementById("completion");
    var z = document.getElementById("open");
    if (z.style.display === "none") {
      x.style.display = "none";
      y.style.display = "none";
      z.style.display = "block";
    } else if (z.style.display === "block") {
      x.style.display = "none";
      y.style.display = "none";
      z.style.display = "block";
    } else {
      x.style.display = "none";
      y.style.display = "none";
      z.style.display = "none";
    }
  }

  function showLeaders() {
    var x = document.getElementById("addmembership")
    var y = document.getElementById("clubleaders")
    var z = document.getElementById("clubmembers")
    if (y.style.display === "none") {
        x.style.display = "none";
        y.style.display = "block";
        z.style.display = "none";
    }
  }

  function showMembers() {
    var x = document.getElementById("addmembership")
    var y = document.getElementById("clubleaders")
    var z = document.getElementById("clubmembers")
    if (z.style.display === "none") {
        x.style.display = "none";
        y.style.display = "none";
        z.style.display = "block";
    }
  }

  function showInfo() {
    var x = document.getElementById("addmembership")
    var y = document.getElementById("clubleaders")
    var z = document.getElementById("clubmembers")
    if (x.style.display === "none") {
        x.style.display = "block";
        y.style.display = "none";
        z.style.display = "none";
    }
  }
  