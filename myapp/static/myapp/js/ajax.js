$(document).ready(function() {
    $('.like-form').submit(function(e) {
        e.preventDefault();
        const video_id = $('.like-btn').val()
        const token = $('input[name=csrfmiddlewaretoken]').val()
        const url = $(this).attr('action')
        $.ajax({
            method: "POST",
            url: url,
            headers: { 'X-CSRFToken': token },
            data: {
                'video_id': video_id
            },
            success: function(response) {
                if (response.like == true) {
                    $('#thumbup').addClass(response.btnlike)
                    $('#like-count').text(response.likes_count)

                } else {
                    $('#thumbup').addClass(response.btnlike)
                    $('#like-count').text(response.likes_count)
                }
            }
        })
    })



})