//alert when user has any ticket
(function(){
    $(document).ready(function(){
        var transfer_click = $('.data').data("userTicket");
        var $transfer = $('#transfer');

        $('#transfer').on('click',function(event){
            if (transfer_click <= 0){
                alert("현재 보유 중이신 티켓의 갯수가 부족하여 양도 받으실 수 없습니다.");
            }
        });
    });
})();

//Load comment used ajax
(function(){

    var comments_section = $("#comment");
    var item_slug = $("#comment").data("item-slug");
  
    var api_url = "/api/"+ item_slug + "/comments/";

    $.ajax ({
        url:api_url,
        method:"GET"
    }).success(function(comments){

    for (var i=0; i<comments.length; i++){
        var comment = comments[i];
        comments_section.append(
            "<p>"+comment.user+" : "+comment.content+"</p>"
            );
        }
    });

})();

//input comment used ajax
(function(){
   
   var comment_content = $("#input_comment");
   var comment_list = $("#comment");

   var item_slug = $("#comment").data("item-slug");

   var comment_create_url = "/api/"+ item_slug +"/comments/";

    //BUTTON CLICK
   $('#input_comment_button').on('click',function(event){   

        comment = comment_content.val();
        
        console.log(comment);
        console.log(comment_content);
        console.log(item_slug);
        console.log(comment_create_url);

        // Get csrf_token 
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
        
            
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        }); 

 
        $.ajax({
            type:'POST',
            url:comment_create_url,
            data:{
            comment: comment,
            slug: item_slug,
            },
            success:function(input_comment){

                console.log(input_comment);
                console.log(input_comment.comment_id);
                comment_dic = jQuery.parseJSON(input_comment.comment_id);
                console.log(comment_dic.user_id);

                comment_user = comment_dic.user_id
                comment_list.append(
                    "<p>"+comment_user+" : "+comment+"</p>"
                )
                comment_content.val(""); 
            }
        }); 
    });

})();


(function(){

})();
