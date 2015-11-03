/*Functions to handle topic events*/
$(document).ready(function() {


/* Follow a topic that is not being followed, on click change to following*/
$('button.followButton').on('click', null,function(e){
    e.preventDefault();
    $button = $(this);
    if($button.hasClass('following')){
        
        var topicid;
    	topicid = $button.attr("data-topicid");
    	unfollow_topic(topicid);
        
        
        $button.removeClass('following');
        $button.removeClass('unfollow');
        $button.text('Follow');
    } else {
        
        var topicid;
    	topicid = $button.attr("data-topicid");
    	follow_topic(topicid);
        
        $button.addClass('following');
        $button.text('Following');
    }
});

/* For a following topic unfollow if clicked and return to a follow button*/
$('button.followButton').hover(function(){
    $button = $(this);
    if($button.hasClass('following')){
        $button.addClass('unfollow');
        $button.text('Unfollow');
    }
}, function(){
    if($button.hasClass('following')){
        $button.removeClass('unfollow');
        $button.text('Following');
    }
});

$('button.delete-topic').click(function(){
    var topicid;
        topicid = $(this).attr("data-topicid");
        delete_topic(topicid);
    $(this).unbind();

})



$('#activities-container').load('/activities/recent/')

  
})

// Functions to be called
function follow_topic (topicid) { 
	$.get('/topics/follow_topic/', { topic_id: topicid } ,function() {
    });
}

function unfollow_topic (topicid) { 
    $.get('/topics/unfollow_topic/', { topic_id: topicid } ,function() {
    })
}

function delete_topic (topicid) { 
    id = 'topic-' + topicid
    $.get('/topics/delete/'+topicid ,function(data) {
        $("#"+id).empty();
        $("#"+id).append(data);
    })
}





