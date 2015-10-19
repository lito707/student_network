$(document).ready(function() {


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

$('button.add-resource').on('click',null,function(e){
    e.preventDefault();
    $button = $(this);
    $button.hide();
    topicid = $button.attr("data-topicid");
    $button.next('.add-resource-form').show();
    // $('.add-resource-form').show();
});

$('#activities-container').load('/activities/recent/')
$('.add-resource-form').load('/resources/add/')


  
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






