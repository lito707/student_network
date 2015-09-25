$('#follow_btn').click(function(){
  var topicid;
  topicid = $(this).attr("data-topicid");
  $.get('/topics/follow/', { topic_id: topicid}, function(data){
    $()

  })



})
