
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



$(document).ready(function () {
    let map;
    const answer_zone = $('#answer');
    // let button = $('#button');

    function initMap() {
        map = new google.maps.Map(document.getElementById("map"), {
            center: { lat: -34.397, lng: 150.644 },
            zoom: 8
        });
    }


    $('form').on('submit', function (e) {
        e.preventDefault();
        // initMap(); //careful with the quota
        console.log('toto');

        // console.log($('#userQuestion').val());
        // let textToParse = $('#userQuestion').val();

        // let userInput = $('#user#userQ).val();
        // let messages = new message('user', userInput);

        $.ajax({
            url: 'parser',
            type: "POST",
            // data: textToParse,
            success: function () {
                // let userMessage = ("<div class='userMessage'>" + userQuestion + "</div>");
                // let apiResponse = ("<div class='apiResponse'>" + parsedTextDisplayed + "</div>");
                // answer_zone.css('display', 'block')
                // answer_zone.append(userMessage);
                // answer_zone.append(apiResponse);
                console.log
                console.log('ca marche');

            },
            error: function () {
                console.log('oops');
            }
        })

    });


    // initMap();


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
