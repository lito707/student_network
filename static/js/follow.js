$(document).ready(function() {
  $('#follow-btn').click(function(){
    // var topicid=1;
    
    var topicid;
    topicid = $(this).attr("data-topicid");
    $.get('/topics/follow_topic/', { topic_id: topicid } ,function() {
      // $('#follow')

    } )

  })

})
