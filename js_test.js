<script type="text/javascript">
    function list_rooms(){
        var date = $("#input_date").val();
        var time_slot = 0;
        var url = $("a").attr("href");
        var params = "?date=" + date + "&time_slot=" + time_slot;
        $.get(url+params)
    }
</script>

<a class="book_meeting" onclick="redir('{{mid}}')" href="{% url 'meeting:new_reservation' %}?mid={{meetingroom}}&date={{request.GET.date}}&lote={{request.GET.lote}}" role="button" 
                class="btn btn-warning btn-book" type="submit">预定</a>