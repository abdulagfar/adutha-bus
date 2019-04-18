function add_more() {
  var x = document.getElementById("add_more");
  if (x.style.display === "none") {
    x.style.display = "block";
    document.getElementById("btn_add_more").style.display==="none";
  } else {
    x.style.display = "none";
  }
}
