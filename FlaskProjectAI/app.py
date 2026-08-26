from flask import Flask, render_template_string, request, jsonify
import requests
import json
from datetime import datetime
import urllib.parse

app = Flask(__name__)

# HTML Template with embedded CSS and JavaScript
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>AI Voice Assistant</title>
    <style>
        .container {
            max-width: 600px;
            margin: 50px auto;
            text-align: center;
        }
        h1 { font-size: 2em; }
        #assistant, .status { margin-bottom: 20px; }
        #listening, #processing {
            display: inline-block;
            margin-right: 10px;
        }
        #output {
            margin-top: 20px;
            text-align: left;
        }
        #output p { margin-bottom: 10px; }
        input[type="text"] {
            width: 70%;
            padding: 10px;
            margin-right: 10px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            margin-top: 10px;
        }
        button {
            padding: 10px 20px;
            cursor: pointer;
            flex-shrink: 0;
        }
        button:hover { background-color: #ddd; }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/annyang/2.6.1/annyang.min.js"></script>
</head>
<body>
    <div class="container">
        <h1>AI Voice Prototype</h1>
        <input id="inputtext" type="text">
        <button id="start">🎙️</button>
        <button id="speak">🔈</button>
        <div id="output"></div>
    </div>
    <script>
        // Sanitization function to prevent XSS
        function sanitizeInput(input) {
            const div = document.createElement('div');
            div.textContent = input;
            return div.innerHTML;
        }

        // Safe URL encoding function
        function safeUrlEncode(input) {
            return encodeURIComponent(input).replace(/[!'()*]/g, function(c) {
                return '%' + c.charCodeAt(0).toString(16).toUpperCase();
            });
        }

        // Elements
        const startBtn = document.getElementById("start");
        const speakBtn = document.getElementById("speak");
        const inputText = document.getElementById("inputtext");
        const outputDiv = document.getElementById("output");

        // Speech recognition setup
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();

        // Get current weather using Flask backend
        async function getCurrentWeather() {
            try {
                const response = await fetch('/get_weather');
                const data = await response.json();

                if (data.success) {
                    return data.message;
                } else {
                    return data.message;
                }
            } catch (error) {
                console.error("Weather fetch error:", error);
                return 'Sorry, I could not fetch the weather data at the moment.';
            }
        }

        // Get current time using Flask backend
        async function getCurrentTime() {
            try {
                const response = await fetch('/get_time');
                const data = await response.json();
                return data.message;
            } catch (error) {
                console.error("Time fetch error:", error);
                return 'Sorry, I could not get the current time.';
            }
        }

        // Arrays of possible commands
        const commands = {
            greeting: ["hello", "hi", "hey", "hi pva", "hey pva", "hello pva", "hi there pva", "hello there pva", "hey there pva"],
            pvaDefinition: ["what does pva stand for", "what is pva", "pva is", "pva"],
            time: ["what time is it", "what is the time", "the time now is"],
            weather: ["what is the weather", "what's the weather", "tell me the weather", "what is the current weather", "the weather is", "what is the weather like today"],
            youtube: ["open youtube"],
            search: ["search for", "look for"],
            research: ["lets do some research", "time to research", "research", "look it up", "look it up on google scholar", "research time", "research articles", "open research articles", "open google scholar"],
            play: ["play"],
            other: ["open chatgpt", "open studysmarter", "open w3schools", "open pdf summarizer", "open google scholar"],
            help: ["what can you do", "give me a list of commands", "how can you help me", "commands"],
            joke: ["tell me a joke", "say something funny", "make me laugh","open joke generator"],
            summarize: ["sum this up", "summarize", "open quilbot"],
            plagiarism: ["is there any plagiarism", "scan for plagiarism", "open zerogpt", "plagiarism"],
            amazonCourse: ["open amazon course", "open cloud computing course", "open amazon cloud computing course", "open cloud computing", "run cloud foundations", "run cloud computing", "open cloud course"],
            checkMarks: ["results", "results?", "check academic results", "what are my marks", "results for ca test", "results for exam", "academic record", "open academic record", "open ienabler"],
            php: ["run php script", "run php code", "open php", "run the php", "run this php script", "run script"],
            whatsapp: ["open whatsapp", "open whatsapp web", "run whatsapp"],
            Mathpapa: ["open mathpapa", "run mathpapa", "calculate for me","compute","calculate"],
            Drawio: ["open draw.io","run draw.io","draw for me","design for me"]
        };

        // Recognize command by matching against an array of possible commands
        function recognizeCommand(command, possibleCommands) {
            return possibleCommands.some(possibleCommand => 
                command.toLowerCase().includes(possibleCommand.toLowerCase())
            );
        }

        // Function to speak out text
        function readOut(message) {
            const speech = new SpeechSynthesisUtterance(sanitizeInput(message));
            speech.volume = 1;
            speech.voice = speechSynthesis.getVoices().find(voice => voice.name === 'Google UK English Male');
            window.speechSynthesis.speak(speech);
        }

        // Function to handle voice triggers and process commands
        async function processCommand(command) {
            // Sanitize the input command
            command = sanitizeInput(command.toLowerCase());
            let response = "";

            if (recognizeCommand(command, commands.greeting)) {
                response = "Hi there, I am PVA, how can I help you?";
            } else if (recognizeCommand(command, commands.pvaDefinition)) {
                response = "PVA stands for Prototype Virtual Assistant";
            } else if (recognizeCommand(command, commands.youtube)) {
                response = "Opening YouTube, Sir";
                window.open("https://www.youtube.com/");
            } else if (recognizeCommand(command, commands.time)) {
                response = await getCurrentTime();
            } else if (recognizeCommand(command, commands.weather)) {
                response = await getCurrentWeather();
            } else if (recognizeCommand(command, commands.search)) {
                let searchTerm = command.replace(/search for|look for/i, "").trim();
                response = `Searching for ${sanitizeInput(searchTerm)}`;
                window.open(`https://www.google.com/search?q=${safeUrlEncode(searchTerm)}`);
            } else if (recognizeCommand(command, commands.play)) {
                let song = command.replace(/play/i, "").trim();
                response = `Playing ${sanitizeInput(song)} on YouTube Music, Sir`;
                window.open(`https://music.youtube.com/search?q=${safeUrlEncode(song)}`);
            } else if (command.includes("open chatgpt")) {
                response = "Opening ChatGPT, Sir";
                window.open("https://chat.openai.com/");
            } else if (command.includes("open gemini")) {
                response = "Opening Gemini, Sir";
                window.open("https://gemini.google.com/");
            } else if (command.includes("open blackbox")) {
                response = "Opening Blackbox, Sir";
                window.open("https://www.blackbox.ai/");
            } else if (command.includes("open claude ")) {
                response = "Opening Claude AI, Sir";
                window.open("https://claude.ai/new");
            } else if (command.includes("open studysmarter")) {
                response = "Opening StudySmarter, Sir";
                window.open("https://app.studysmarter.de/home");
            } else if (command.includes("open w3schools")) {
                response = "Opening W3Schools, Sir";
                window.open("https://www.w3schools.com/");
            } else if (command.includes("open pdf summarizer")) {
                response = "Opening PDF Summarizer, Sir";
                window.open("https://smallpdf.com/ai-pdf");
            } else if (recognizeCommand(command, commands.research)) {
                response = "Opening Google Scholar, Sir";
                window.open("https://scholar.google.com/");
            } else if (recognizeCommand(command, commands.help)) {
                response = "Here is a list of commands I can recognize: \\n" +
                    "1. Greetings\\n2. Ask about PVA\\n3. Get the time\\n4. Get the weather\\n" +
                    "5. Open YouTube\\n6. Search Google\\n7. Play a song\\n8. Tell a joke\\n" +
                    "9. Open various websites\\n10. Check academic results\\n11. Run PHP scripts\\n" +
                    "12. Open Amazon cloud computing course\\n13. Open WhatsApp Web\\n14. Open mathpapa";
            } else if (recognizeCommand(command, commands.joke)) {
                response = "Opening joke generator";
                window.open("jokegenerator.html");
            } else if (recognizeCommand(command, commands.amazonCourse)) {
                response = "Opening Amazon course Sir";
                window.open("https://awsacademy.instructure.com/courses/79868/modules/items/7215080");
            } else if (command.includes("open gmail")) {
                response = "Opening gmail Sir";
                window.open("https://mail.google.com/mail/u/0/?ogbl#inbox");
            } else if (recognizeCommand(command, commands.summarize)) {
                response = "Opening quilbot for you Sir";
                window.open("https://quillbot.com/paragraph-rewriter?msockid=00eb042c2c1a604b168316992de7611b");
            } else if (recognizeCommand(command, commands.plagiarism)) {
                response = "Opening zeroGPT Sir";
                window.open("https://www.zerogpt.com/");
            } else if (command.includes("open google")) {
                response = "Opening Google Sir";
                window.open("https://www.google.co.za/?gws_rd=ssl");
            } else if (command.includes("open moodle")) {
                response = "Opening Moodle Sir";
                window.open("https://learning.richfield.ac.za/HET/login/index.php");
            } else if (recognizeCommand(command, commands.checkMarks)) {
                response = "Opening Richfield iEnabler Sir";
                window.open("https://rgitie.richfield.ac.za/pls/rgitp/w99pkg.mi_login");
            } else if (recognizeCommand(command, commands.php)) {
                response = "Running php now for you Sir";
                window.open("http://localhost/hello.php");
            } else if(command.includes("open brilliant")){
                response ="Opening Brilliant Sir ";
                window.open("https://brilliant.org/home/");
            } else if(command.includes("open afrihost")){
                response ="Opening afrihost Sir ";
                window.open("https://clientzone.afrihost.com/en/login");
            } else if(command.includes("open poe ai")){
                response ="Opening Poe AI Sir ";
                window.open("https://poe.com/");
            } else if(command.includes("open onedrive")){
                response = "Opening OneDrive";
                window.open("https://studentspctrainingedu-my.sharepoint.com/");
            } else if(recognizeCommand(command, commands.whatsapp)) {
                response = "Opening WhatsApp Web, Sir";
                window.open("https://web.whatsapp.com/");
            } else if(recognizeCommand(command, commands.Mathpapa)) {
                response = "Opening mathpapa, Sir";
                window.open("https://www.mathpapa.com/algebra-calculator.html");
            }
            else if(recognizeCommand(command, commands.Drawio)) {
                response = "Opening draw.io, Sir";
                window.open("https://app.diagrams.net/");
            } else {
                response = "I didn't quite catch that, please try again.";
            }

            readOut(response);
            outputDiv.innerHTML += `<p>${response.replace(/\\n/g, '<br>')}</p>`;
        }

        // Event listeners
        recognition.onstart = () => console.log("VR active");
        recognition.onresult = (event) => {
            let transcript = sanitizeInput(event.results[event.resultIndex][0].transcript);
            inputText.value = transcript;
            processCommand(transcript);
        };
        recognition.onend = () => console.log("VR deactivated");

        startBtn.addEventListener("click", () => recognition.start());
        speakBtn.addEventListener("click", () => readOut("Hi there, I am PVA, designed by Mr. Sewnarain. How may I be of service?"));
        inputText.addEventListener("keydown", (event) => {
            if (event.key === 'Enter') {
                let sanitizedInput = sanitizeInput(inputText.value);
                processCommand(sanitizedInput);
                inputText.value = '';
            }
        });
    </script>
</body>
</html>
'''


@app.route('/')
def index():
    return render_template_string(html_template)


# API endpoint to get current weather
@app.route('/get_weather', methods=['GET'])
def get_weather():
    api_key = '8f2751d8f8683d4abfc8076553e81b54'
    city = 'Durban'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote(city)}&units=metric&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return jsonify({
                'success': True,
                'message': f"The current weather in {city} is {data['weather'][0]['description']} with a temperature of {data['main']['temp']:.1f}°C."
            })
        else:
            return jsonify({
                'success': False,
                'message': f"Sorry, I could not fetch the weather data. Error: {data.get('message', 'Unknown error')}"
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Sorry, I could not fetch the weather data at the moment.'
        })


# API endpoint to get current time
@app.route('/get_time', methods=['GET'])
def get_time():
    now = datetime.now()
    hours = now.hour
    minutes = now.minute
    period = 'PM' if hours >= 12 else 'AM'
    hours = hours % 12 or 12

    time_string = f"It is {hours}:{minutes:02d} {period} right now."
    return jsonify({'message': time_string})


if __name__ == '__main__':
    app.run(debug=True)