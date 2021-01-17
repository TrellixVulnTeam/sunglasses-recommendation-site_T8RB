$(function () {

    $(document).scroll(function () {
        
        let $leftSideJumbo = $("#left-side-jumbo-wrap");
        let $nav = $("#nav");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());

        let $getStartedBtn = $("#nav-get-started");
        $getStartedBtn.toggleClass('displayed', ($(this).scrollTop() - 150) > $leftSideJumbo.height());

    });

});