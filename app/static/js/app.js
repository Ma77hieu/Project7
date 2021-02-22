$(function () {

    const answer_zone = $('#answer');

    class message {
        constructor(author, content) {
            let contentString = (content);
            if (author == 'user') {
                this.contentString = "Vous: " + contentString;
            }
            else {
                this.contentString = "GrandPyBot: " + contentString;
            }
            // return contentString;
        }

    }

    let button = $('#button');

    button.on('click', function () {
        let userInput = $('#userQuestion').val();
        alert(userInput);
        let messages = new message('user', userInput);
        let userMessage = ("<div class='userMessage'>" + messages.contentString + "</div>");
        answer_zone.append(userMessage);
    })
})