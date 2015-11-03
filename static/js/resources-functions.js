/* Functions to add resources */
$(document).ready(function() {

/* Add resource button makes the request to add resource and load respective div 
    with the response from the request.
*/
$('button.add-resource').on('click',function(e){
    e.preventDefault();
    $button = $(this);
    $button.hide();
    topicid = $button.attr("data-topicid");
    id = 'resource-form-' + topicid
    $.get('/resources/add_resource/'+topicid ,function(data){
        $("#"+id).empty();
        $("#"+id).append(data);
    });
    $button.unbind();

});

/* Submit a form to add a resource to a topic using a POST request, load 
    respective div with the response from the request.
*/
$("input[id^='add-submit-']").click( function(e) {
    topicid = $(this).attr("data-topicid");
    id = 'resource-form-' + topicid;

    $.post( '/resources/add_resource/'+topicid +"/", 
                    $('form#form-'+topicid).serialize(), function(data) {
        $("#"+id).empty();
        $("#"+id).append(data);
        }
    );
    $(this).unbind
    e.preventDefault();
});

})


    
    

