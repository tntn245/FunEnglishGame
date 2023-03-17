var table = document.getElementById("table_container");
var this_row = table.getElementsByClassName("table_row");

var current_row = document.getElementsByClassName("active");
var index_row = this_row.length - 1;
if (index_row >= 0) {
    this_row[index_row].className += " active";
}

function Send() {
    var i = "get_" + current_row[0].id
    document.getElementById(i).submit();
}

function Send_all() {
    document.getElementById("send_all_dialog").submit();
}

function Skip() {
    var i = "skip_" + current_row[0].id
    document.getElementById(i).submit();
}

var players = document.getElementById("box_player");
var players_name = players.getElementsByClassName("player_name");

var current_player = document.getElementsByClassName("active1");
for (var i = 0; i < players_name.length; i++) {
    players_name[i].addEventListener("click", function () {
        if (current_player.length > 0) {
            current_player[0].className = current_player[0].className.replace(" active1", "");
        }
        this.className += " active1";
    });
}

function Disable() {
    var i = "disable_" + current_player[0].id
    document.getElementById(i).submit();
}

localStorage.setItem('ShowDialog', document.getElementById('show_New_Dialog').value);
if (localStorage.getItem('ShowDialog')) {
    document.getElementById('dialog_' + localStorage.getItem('ShowDialog')).selected = true;
}

$("#dialogs_list").on("change", function () {
    $("#show_dialog_btn").trigger("click");
});