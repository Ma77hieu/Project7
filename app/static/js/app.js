
$(document).ready(function () {
    let map;
    let marker
    const answer_zone = $('#answer');
    const loader = $('#loader');
    const mapDiv = ($('#map'))

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
        console.log($('#userInput').val());
        loader.show();
        $.ajax({
            url: 'parser',
            type: "POST",
            data: {
                "question": $('#userInput').val()
            },
            success: function (responseJSON) {
                console.log(responseJSON)
                console.log(responseJSON.location)
                let itemLat = responseJSON.latitude
                // console.log(itemLat)
                let itemLon = responseJSON.longitude
                // console.log(itemLon)
                // let locationFound = responseJSON.location
                let userQuestion = responseJSON.userMessage
                let parsedTextDisplayed = responseJSON.apiAnswer
                // console.log(userQuestion)
                // console.log(parsedTextDisplayed)
                let userMessage = ("<div class='userMessage'>" + userQuestion + "</div>");
                let apiResponse = ("<div class='apiResponse'>" + parsedTextDisplayed + "</div>");
                answer_zone.css('display', 'block')
                answer_zone.append(userMessage);
                answer_zone.append(apiResponse);
                // console.log('ca marche');
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
            answer_zone.show();
        })
    })
})
