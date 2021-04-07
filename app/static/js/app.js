
$(document).ready(function () {
    let map;
    let marker;




    function escape(inputString) {
        var toReplace = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;'
        };
        for (let charac in toReplace) {
            inputString = inputString.replace(charac, toReplace[charac])
        }
        return inputString
    };



    function initMap(myPos) {
        const lastmap = document.getElementsByClassName("map")[0];
        map = new google.maps.Map(lastmap, {
            center: myPos,
            zoom: 16
        });
        marker = new google.maps.Marker({
            position: myPos,
            map,
        });
    }

    $('form').on('submit', function (e) {
        // const lastMessagesApi = $('.apiResponse')[0]
        // const lastMessagesUser = $('.userMessage')[0]
        // lastMessagesApi.remove()
        // lastMessagesUser.remove()
        // mapDiv.empty()
        const answerZone = $('#answerZone');
        answerZone.prepend("<div class='map'></div><div class='answer'></div>");
        // const row = answerZone.insertBefore(newRow, null);
        const loader = $('#loader');


        e.preventDefault();
        let questionNoXss = escape($('#userInput').val())
        loader.show();

        $.ajax({
            url: 'parser',
            type: "POST",
            data: {
                "question": questionNoXss
            },
            success: function (responseJSON) {
                const mapDiv = $(".map:first");
                const answer = $(".answer:first");
                console.log(responseJSON)
                console.log(responseJSON.location)
                let itemLat = responseJSON.latitude
                let itemLon = responseJSON.longitude
                let userQuestion = responseJSON.userMessage
                let parsedTextDisplayed1 = responseJSON.apiAnswer1
                let parsedTextDisplayed2 = responseJSON.apiAnswer2
                let userMessage = ("<div class='userMessage'>" + userQuestion + "</div>");
                let apiResponse1 = ("<div class='apiResponse'>" + parsedTextDisplayed1 + "</div>");
                answer.css('display', 'block')
                answer.append(userMessage);
                answer.append(apiResponse1);
                if (parsedTextDisplayed2 != "") {
                    let apiResponse2 = ("<div class='apiResponse'>" + parsedTextDisplayed2 + "</div>");
                    answer.append(apiResponse2);
                }
                if (responseJSON.location == true) {
                    let myPos = { lat: itemLat, lng: itemLon };
                    initMap(myPos);
                }
                else {
                    mapDiv.css({
                        "display": "flex",
                        "flex-direction": "column",
                        "justify-content": "center",
                        "align-items": "center",
                        "color": "red"
                    })
                    mapDiv.html("<p>Pas de géolocalisation disponible</p>")
                }

            },
            error: function () {
                console.log('oops, something went wrong');
            }
        }).done(function () {
            loader.hide();
            mapDiv.show();
            answer.show();
        })
    })
})
