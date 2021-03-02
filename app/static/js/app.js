
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
    let marker
    const answer_zone = $('#answer');


    function initMap(myPos) {

        map = new google.maps.Map(document.getElementById("map"), {
            center: myPos,
            zoom: 16
        });
        marker = new google.maps.Marker({
            position: myPos,
            map,
        });
    }

    $('form').on('submit', function (e) {
        e.preventDefault();
        let myPos = { lat: 48.004375739116036, lng: 0.20389941900651232 };
        initMap(myPos); //careful with the quota
        console.log('toto');

        // console.log($('#userQuestion').val());
        // let textToParse = $('#userQuestion').val();

        // let userInput = $('#user#userQ).val();
        // let messages = new message('user', userInput);

        $.ajax({
            url: 'parser',
            type: "POST",
            // data: textToParse,
            success: function (responseJSON) {
                console.log(responseJSON)
                let userQuestion = responseJSON.userMessage
                let parsedTextDisplayed = responseJSON.apiAnswer
                console.log(userQuestion)
                console.log(parsedTextDisplayed)
                let userMessage = ("<div class='userMessage'>" + userQuestion + "</div>");
                let apiResponse = ("<div class='apiResponse'>" + parsedTextDisplayed + "</div>");
                answer_zone.css('display', 'block')
                answer_zone.append(userMessage);
                answer_zone.append(apiResponse);
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
