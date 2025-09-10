document.addEventListener('DOMContentLoaded', () => {
    // Basic function to fetch data and update UI
    async function fetchData(endpoint, elementId) {
        try {
            const response = await fetch(`/api/${endpoint}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            document.getElementById(elementId).textContent = JSON.stringify(data, null, 2);
        } catch (error) {
            document.getElementById(elementId).textContent = `Error: ${error.message}`;
        }
    }

    // Call functions to load initial data
    const location = { lat: 28.7041, lon: 77.1025 }; // Example: Delhi
    fetchData(`weather?lat=${location.lat}&lon=${location.lon}`, 'weatherAlerts');
    fetchData(`mandi?commodity=Tomato&state=Delhi`, 'mandiPrices');

    // Voice recording logic
    const recordButton = document.getElementById('recordButton');
    const voiceStatus = document.getElementById('voiceStatus');
    const audioPlayback = document.getElementById('audioPlayback');

    let mediaRecorder;
    let audioChunks = [];

    recordButton.addEventListener('mousedown', async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            mediaRecorder = new MediaRecorder(stream);
            audioChunks = [];
            
            mediaRecorder.ondataavailable = event => {
                audioChunks.push(event.data);
            };
            
            mediaRecorder.onstop = async () => {
                const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' }); // Adjust type if needed
                const formData = new FormData();
                formData.append('file', audioBlob, 'audio.mp3');
                
                voiceStatus.textContent = 'Transcribing...';
                
                const response = await fetch('/api/voice/asr', {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();
                voiceStatus.textContent = `Transcript: "${result.text}"`;

                // Now, get the TTS response for the transcribed text
                const ttsResponse = await fetch('/api/voice/tts', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text: result.text })
                });
                const ttsResult = await ttsResponse.json();
                audioPlayback.src = ttsResult.audio_url;
            };
            
            mediaRecorder.start();
            voiceStatus.textContent = 'Recording...';
        } catch (error) {
            voiceStatus.textContent = `Error: ${error.message}. Please enable microphone access.`;
        }
    });

    recordButton.addEventListener('mouseup', () => {
        if (mediaRecorder && mediaRecorder.state === 'recording') {
            mediaRecorder.stop();
        }
    });

    // Pest image upload logic
    const uploadPestButton = document.getElementById('uploadPest');
    const pestImageInput = document.getElementById('pestImage');
    const pestStatus = document.getElementById('pestStatus');

    uploadPestButton.addEventListener('click', async () => {
        if (pestImageInput.files.length === 0) {
            pestStatus.textContent = 'Please select a file first.';
            return;
        }

        const formData = new FormData();
        formData.append('file', pestImageInput.files[0]);

        pestStatus.textContent = 'Uploading...';

        try {
            const response = await fetch('/api/pest/submit', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            pestStatus.textContent = `Upload successful! Ticket ID: ${result.ticket_id}. Expected review SLA: ${result.sla}.`;
        } catch (error) {
            pestStatus.textContent = `Error uploading file: ${error.message}`;
        }
    });
});