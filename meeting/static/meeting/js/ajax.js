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
    // $(document).on("click", ".delete", function(){
    //     if (!confirm('拒绝后该请求会被删除，确认拒绝?')) { return; }
    //     var id = $(this).attr("id");
    //     var item = $(this).parents(".blog-post");
    //     // var url = $(this).attr("href");
    //     var url = '/meetingrooms/delete/'+id;
    //     $.post(url, {
    //         'id': id,
    //         'csrfmiddlewaretoken': csrftoken
    //         },
    //         function(){
    //         item.fadeOut();
    //     });
    // });
    $(document).on("click", ".book_meeting", function(){
        var m = $(this).siblings()[0];
        var meetingroom = m.textContent;
        var mid = m.id;
        var date = $("#input_date").val();
        var time_slot = $("#input_time_slot").val();
        var params = "?date=" + date + "&time_slot=" + time_slot + "&mid=" + mid + "&meetingroom=" + meetingroom;
        location.href = $(".book_meeting").attr("action")+params;
    });
    
    // $(".confirm").click(function(){
    //     // var room = $(".room").text();
    //     // var date = $(".date").text();
    //     // var time = parseInt($(".time_slot").text());
    //     // var vip = $(".vip").text();
    //     // var count = parseInt($(".count").text());
    //     // var dept = $(".dept").text();
    //     // var phone = parseInt($(".phone").text());
    //     var id = $(".confirm").attr('id');
    //     var url = $(".confirm").attr('action');
    //     var data = {
    //         // 'book_date': date,
    //         // 'book_time': time,
    //         // 'room': room,
    //         // 'vip': vip,
    //         // 'count': count,
    //         // 'dept': dept,
    //         // 'phone': phone,
    //         'id': id,
    //         'status': 2,
    //         'csrfmiddlewaretoken':csrftoken
    //         };
    //     $.post(url, data,
    //         function(){
    //             window.location.assign(url)
    //     });
    // });
    // $.fn.checkRequired=function(inputArg){
    //     if (inputArg.required) {
    //         if($(this).is("input") || $(this).is("textarea")){
    //             $(this).bind("focus", function(){
    //                 if(inputArg.onFocus!=undefined)

    //             })
    //         })
    //     }
    // }
});

