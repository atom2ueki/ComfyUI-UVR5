// loadAudioFromPath.js

const fs = require('fs');
const path = require('path');

function loadAudioFromPath(audioFileName) {
    const audioDirectory = '/app/ComfyUI/audios';

    // Construct the full path to the audio file
    const audioFilePath = path.join(audioDirectory, audioFileName);

    if (!fs.existsSync(audioFilePath)) {
        throw new Error(`Audio file not found: ${audioFilePath}`);
    }

    // Read the audio file
    const audioData = fs.readFileSync(audioFilePath);

    // Prepare the output type (based on uploadAudio.js)
    return {
        name: audioFileName,
        data: audioData.toString('base64'), // Convert to base64 for transmission if required
        mimeType: 'audio/mpeg', // Adjust the MIME type if needed
    };
}

module.exports = loadAudioFromPath;