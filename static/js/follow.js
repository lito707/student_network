$(document).ready(function() {
  $('.follow-btn').click(function(){
    var topicid;
    topicid = $(this).attr("data-topicid");
    $.get('/activities/follow_topic/', { topic_id: topicid } ,function() {

    } 
    )

  })

  $('#activities').load('/activities/recent/')



  
})

// $(document).ready(function(){
// 	$('#activities').load(function(){
// 		$.get('activities/recent',function(){
// 			alert("success");
// 		})


// 	}
// 		)

// })



