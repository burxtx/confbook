function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$(document).ready(function(){
    $("#submit_pending").click(function(){
        var room = $("h1").text(),
            date = $('a.post-tag').map(function(){
                return this.text;
            }).get();
            time_slot = $()
            url = $("#submit_pending").attr('action');
        $.post(url, {'room': room,
                    'date': date,
                    'time_slot': time_slot,
                    'csrfmiddlewaretoken': csrftoken
                    },
                    function(){
                        window.location.assign(url)
                    });
    });    
});