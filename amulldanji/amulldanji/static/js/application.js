(function(){
    $(document).ready(function(){
        var transfer_click = $('.data').data("userTicket");
        var $transfer = $('#transfer');
        
        $('#transfer').on('click',function(event){
            event.preventDefault();
            if (transfer_click <= 0){
                alert("현재 보유 중이신 티켓의 갯수가 부족하여 양도 받으실 수 없습니다.");
            }
        });
    });
})();
