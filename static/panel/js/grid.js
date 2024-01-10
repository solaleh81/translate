$(document).ready(function() {
    $(".sidebar-toggler").each(function(index) {
        $(this).on("click", function() {
            $('.sidebar-toggle-close').each(function(index, item) {
                if (item.classList.contains('d-inline')) {
                    item.classList.remove('d-inline');
                    item.classList.add('d-none');
                    $('#panel-sidebar').fadeOut(250);
                    $('#panel-main').animate({ width: '100%', padding: '2rem 1.3rem' }, 50);
                } else {
                    item.classList.add('d-inline');
                    item.classList.remove('d-none');
                    $('#panel-sidebar').fadeIn(250);
                    if ($(window).width() > 1199.98) {
                        $('#panel-main').animate({ width: 'calc(100% - 13rem)', padding: '2rem 4rem 1rem 1.3rem' }, 50);
                    }
                }
            });
            $('.sidebar-toggle-bar').each(function(index, item) {
                if (item.classList.contains('d-none')) {
                    item.classList.add('d-inline');
                    item.classList.remove('d-none');
                    $('#panel-sidebar').fadeOut(250);
                    $('#panel-main').animate({ width: '100%', padding: '2rem 1.3rem' }, 50);
                } else {
                    item.classList.remove('d-inline');
                    item.classList.add('d-none');
                    item.classList.remove('d-inline');
                    $('#panel-sidebar').fadeIn(250);
                    if ($(window).width() > 1199.98) {
                        $('#panel-main').animate({ width: 'calc(100% - 13rem)', padding: '2rem 4rem 1rem 1.3rem' }, 50);
                    }
                }
            });
        });
    });


    $('#body-header-toggler').click(function() {
        $('#body-header').toggle(250);
    })
})