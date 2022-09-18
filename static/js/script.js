
var table = document.getElementById("table_container");
var this_row = table.getElementsByClassName("table_row");

var btn_skip= document.getElementById("skip");
var btn_send_dialog= document.getElementById("send_dialog");
var btn_send= document.getElementById("send");

var current = document.getElementsByClassName("active");
for (var i = 0; i < this_row.length; i++) {
    this_row[i].addEventListener("click", function() {
    if (current.length > 0) { 
        current[0].className = current[0].className.replace(" active", "");
    }
    this.className += " active";
    });
}

btn_skip.addEventListener("click",function(){
    current[0].style.display = "none";
})
function mySent() {
    var i = "get_" + current[0].id
    document.getElementById(i).submit();
}


var players = document.getElementById("box_player");
var players_name = players.getElementsByClassName("player_name");

var btn_disables= document.getElementById("disable");

var current_player = document.getElementsByClassName("active1");
for (var i = 0; i < players_name.length; i++) {
    players_name[i].addEventListener("click", function() {
    if (current_player.length > 0) { 
        current_player[0].className = current_player[0].className.replace(" active1", "");
    }
    this.className += " active1";
    });
}

function myDisable() {
    var i = "disable_" + current_player[0].id
    document.getElementById(i).submit();
}
