$(document).on('submit', '#contactForm, #bookingForm', function(event) {
    event.preventDefault();

    if (event.target.id == 'bookingForm') {
        button = document.querySelector(".button-bookingForm");
        button.innerHTML = "Booking..";

        var clickedObj = $(".button-bookingForm");
    
        const csrf = document.getElementsByName("csrfmiddlewaretoken")
        var tag = "bookingForm";
        var name = $('.booking-form #name').val();
        var email = $('.booking-form #email').val();
        var phone = $('.booking-form #phone').val();
        var date = $('.booking-form #date').val();
        var time = $('.booking-form #time').val();
        var people = $('.booking-form #people').val();
        var message = $('.booking-form #message').val();

        var dataPost = new FormData();
        dataPost.append("csrfmiddlewaretoken", csrf[0].value);
        dataPost.append("tag", tag);
        dataPost.append("name", name);
        dataPost.append("email", email);
        dataPost.append("phone", phone);
        dataPost.append("date", date);
        dataPost.append("time", time);
        dataPost.append("people", people);
        dataPost.append("message", message);

        $.ajax({
            method: 'POST',
            url: '',
            data: dataPost,
            processData: false,
            contentType: false,
            dataType: 'json',
    
            success: function(response) {
                var msg = response['msg'];
                if (msg == 'valid') {
                    $( '#bookingForm' ).each(function(){
                        this.reset();
                    });
                    button.innerHTML = "Your booking request was sent. We will call back or send an Email to confirm your booking. Thank you!";
                    setTimeout(function(){
                        button.innerHTML = "Book a Chef";
                    }, 4000);
                } else {
                    button.innerHTML = "Error! Please check your details..";
                    setTimeout(function(){
                        button.innerHTML = "Book a Chef";
                    }, 4000);             
                }
            },
            error: function(error) {
                button.innerHTML = "Error! Please try again later..";
                setTimeout(function(){
                    button.innerHTML = "Book a Chef";
                }, 4000);               
            }
        })
    }
    else if (event.target.id == 'contactForm') {
        button = document.querySelector(".button-Contact");
        button.innerHTML = "Sending";
 
        var clickedObj = $(".button-Contact");
    
        const csrf = document.getElementsByName("csrfmiddlewaretoken")
        var tag = "contactForm";
        var name = $('.contact-form #name').val();
        var email = $('.contact-form #email').val();
        var subject = $('.contact-form #subject').val();
        var message = $('.contact-form #message').val();
    
        var dataPost = new FormData();
        dataPost.append("csrfmiddlewaretoken", csrf[0].value);
        dataPost.append("tag", tag);
        dataPost.append("name", name);
        dataPost.append("email", email);
        dataPost.append("subject", subject);
        dataPost.append("message", message);
    
        $.ajax({
            method: 'POST',
            url: '',
            data: dataPost,
            processData: false,
            contentType: false,
            dataType: 'json',
    
            success: function(response) {
                var msg = response['msg'];
                if (msg == 'valid') {
                    $( '#contactForm' ).each(function(){
                        this.reset();
                    });
                    button.innerHTML = "Message Sent, Thank you!"
                    setTimeout(function(){
                        button.innerHTML = "Send Message";
                    }, 4000);
                } else {
                    button.innerHTML = "Error! Please check your details..";
                    setTimeout(function(){
                        button.innerHTML = "Send Message";
                    }, 4000);             
                }
            },
            error: function(error) {
                button.innerHTML = "Error! Please try again later..";
                setTimeout(function(){
                    button.innerHTML = "Send Message";
                }, 4000);               
            }
        })
    }
});