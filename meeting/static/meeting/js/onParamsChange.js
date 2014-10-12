function onDateTimeChange () {
    var date = $("#input_date").val();
    var time_slot = $("#input_time_slot").val();
    var params = "?date=" + date + "&time_slot=" + time_slot;
    $(".meetingrooms_list").load(
        document.URL + encodeURIComponent(params)
    );
}

$(document).ready(function(){
    $("#input_date").change(onDateTimeChange);
    $("#input_time_slot").change(onDateTimeChange);
});