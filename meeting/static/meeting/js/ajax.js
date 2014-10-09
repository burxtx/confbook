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
    $(document).on("click", ".delete", function(){
        if (!confirm('确认删除会议室?')) { return; }
        var id = $(this).attr("id");
        var item = $(this).parents(".blog-post");
        // var url = $(this).attr("href");
        var url = '/meetingrooms/delete/'+id;
        $.post(url, {
            'id': id,
            'csrfmiddlewaretoken': csrftoken
            },
            function(){
            item.fadeOut();
        });
    });
});