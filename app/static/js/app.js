$(function () {

    const answer_zone = $('#answer');

    class message {
        constructor(author, content) {
            let contentString = (content);
            if (author == 'user') {
                this.contentString = "Vous: " + contentString;
            }
            else {
                parsing(content);
                this.contentString = "GrandPyBot: " + contentString;
            }
        }

    }

    let button = $('#button');

    button.on('click', function (e) {
        e.preventDefault();
        let userInput = $('#userQuestion').val();
        let messages = new message('user', userInput);
        let userMessage = ("<div class='userMessage'>" + messages.contentString + "</div>");
        answer_zone.css('display', 'block')
        answer_zone.append(userMessage);
    });

    let map;

    function initMap() {
        map = new google.maps.Map(document.getElementById("map"), {
            center: { lat: -34.397, lng: 150.644 },
            zoom: 8,
        });
    }


    // function parsing(textToParse) {
    //     $.ajax({
    //         url: 'http://127.0.0.1:5000/parser/',
    //         data: textToParse,
    //         type: 'POST',
    //         success: function (response) {
    //             console.log("worked");
    //         },
    //         error: function (error) {
    //             console.log(error);
    //         }
    //     });
    // }

    // let a = parsing("Test text to be parsed");
    // let apiResponse = ("<div class='apiResponse'>" + a + "</div>");
    // answer_zone.append(apiResponse);
});
