/**
 * Created by konstantin on 29.11.16.
 */

$(document).ready(function () {


    $('.album-edit-link').click(function () {
        console.log('OK');
        $('#exampleModal').modal();
        $('.modal-body').load($(this).attr('href'));
        return false;
    });

    $(document).on('btn btn-primary', '.ajax-form', function () {
        var form = $(this);
        $.post(form.attr('action'), form.serialize(), function (data) {
            if (data == 'OK') {
                document.location.href = document.location.href;
            }
            form.html(data);
        });
        return false;
    });
});


