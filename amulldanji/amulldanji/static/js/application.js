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
            "<p>"+comment.content+"@"+comment.user+"</p>"
            );
    }
    });

})();

(function(){

})();
