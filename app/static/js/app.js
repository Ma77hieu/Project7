$(function () {

    const answer_zone = document.querySelector('#answer');

    class message {
        constructor(author, content) {
            let contentString = (content);
            if (author == 'user') {
                contentString = "Vous: " + contentString;
                alert(contentString);
            }
            else {
                messageDisplayed.insertBefore('GrandPyBot: ');
                messageDisplayed.style.textAlign = "right";
            }
        }

    }

    let button = $('#button');

    button.on('click', function () {
        let messages = new message('user', "ma réponse");

        answer_zone.append(messages);
    })
})