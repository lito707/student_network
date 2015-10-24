$(document).ready(function() {
// $('.reply-resource-form').load('/resources/add/')

$('button.add-resource').on('click',function(e){
    e.preventDefault();
    $button = $(this);
    $button.hide();
    topicid = $button.attr("data-topicid");

    $.get('/resources/add_resource/'+topicid ,function(data){
    id = 'resource-form-'+topicid
    
    $("#"+id).show();
        // alert(data);
    //     // $(this).next('.reply-resource-form').show();
    //     // $(this).parent().next('.reply-resource-form').css("display", "block");
    //     // $('#add-resource ').attr('data-topicid', topicid);
    //     // $(this).parent().next('.resource-form').show();
    //     // $('#add-resource ').show();
    //     // $('#resource-form').slideToggle();        
    //     // $('#resource-form').show();


    });
    
    // $('.reply-resource-form').show();
});

// $('.resource-form').load('/resources/add/')

})
