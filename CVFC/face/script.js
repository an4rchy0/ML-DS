// Variabel global
let emotionModel;
let video;
let canvas;
let ctx;
let isDetecting = false;
let detectionInterval;

// Daftar emosi yang akan dideteksi
const emotions = ['marah', 'jijik', 'takut', 'senang', 'netral', 'sedih', 'terkejut'];

// Fungsi untuk memuat model
async function loadModels() {
    try {
        // Memuat model deteksi wajah dan landmark dari face-api.js
        await faceapi.nets.tinyFaceDetector.loadFromUri('https://justadudewhohacks.github.io/face-api.js/models');
        await faceapi.nets.faceLandmark68Net.loadFromUri('https://justadudewhohacks.github.io/face-api.js/models');
        await faceapi.nets.faceExpressionNet.loadFromUri('https://justadudewhohacks.github.io/face-api.js/models');
        
        console.log('Semua model berhasil dimuat');
        document.getElementById('startButton').disabled = false;
    } catch (err) {
        console.error('Gagal memuat model:', err);
        alert('Gagal memuat model. Lihat konsol untuk detailnya.');
    }
}

// Fungsi untuk memulai kamera
async function startVideo() {
    try {
        video = document.getElementById('video');
        canvas = document.getElementById('canvas');
        ctx = canvas.getContext('2d');
        
        const stream = await navigator.mediaDevices.getUserMedia({ 
            video: { width: 640, height: 480 } 
        });
        video.srcObject = stream;
        
        return new Promise((resolve) => {
            video.onloadedmetadata = () => {
                video.play();
                resolve(video);
            };
        });
    } catch (err) {
        console.error('Error accessing camera:', err);
        alert('Tidak dapat mengakses kamera. Pastikan Anda memberikan izin.');
        throw err;
    }
}

// Fungsi untuk mendeteksi emosi
async function detectEmotion() {
    if (!isDetecting) return;
    
    try {
        // Deteksi wajah dan ekspresi menggunakan face-api.js
        const detections = await faceapi.detectAllFaces(video, 
            new faceapi.TinyFaceDetectorOptions())
            .withFaceLandmarks()
            .withFaceExpressions();
        
        if (detections && detections.length > 0) {
            // Gambar deteksi ke canvas
            const displaySize = { width: video.width, height: video.height };
            faceapi.matchDimensions(canvas, displaySize);
            
            const resizedDetections = faceapi.resizeResults(detections, displaySize);
            faceapi.draw.drawDetections(canvas, resizedDetections);
            faceapi.draw.drawFaceLandmarks(canvas, resizedDetections);
            
            // Ambil ekspresi dengan confidence tertinggi
            const expressions = detections[0].expressions;
            const sorted = Object.entries(expressions)
                .sort((a, b) => b[1] - a[1]);
            const [emotion, confidence] = sorted[0];
            
            // Tampilkan hasil
            document.getElementById('emotionResult').innerHTML = 
                `Emosi: ${translateEmotion(emotion)} <br> 
                Tingkat Kepercayaan: ${(confidence * 100).toFixed(2)}%`;
            
            // Gambar label emosi
            const box = detections[0].detection.box;
            const text = `${translateEmotion(emotion)} (${(confidence * 100).toFixed(1)}%)`;
            const drawOptions = {
                anchorPosition: 'BOTTOM_LEFT',
                backgroundColor: 'rgba(0, 0, 0, 0.5)'
            };
            new faceapi.draw.DrawTextField(
                [text],
                { x: box.x, y: box.y + box.height },
                drawOptions
            ).draw(canvas);
        } else {
            document.getElementById('emotionResult').innerHTML = 'Tidak ada wajah yang terdeteksi';
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
    } catch (err) {
        console.error('Error detecting emotion:', err);
        document.getElementById('emotionResult').innerHTML = 'Error saat mendeteksi emosi';
    }
    
    // Lanjutkan deteksi
    if (isDetecting) {
        detectionInterval = requestAnimationFrame(detectEmotion);
    }
}

// Fungsi untuk menerjemahkan emosi ke Bahasa Indonesia
function translateEmotion(emotion) {
    const translations = {
        'angry': 'Marah',
        'disgusted': 'Jijik',
        'fearful': 'Takut',
        'happy': 'Senang',
        'neutral': 'Netral',
        'sad': 'Sedih',
        'surprised': 'Terkejut'
    };
    return translations[emotion] || emotion;
}

// Event listeners
document.addEventListener('DOMContentLoaded', async () => {
    // Nonaktifkan tombol sampai model dimuat
    document.getElementById('startButton').disabled = true;
    document.getElementById('stopButton').disabled = true;
    
    // Setup canvas
    canvas = document.getElementById('canvas');
    ctx = canvas.getContext('2d');
    canvas.width = 640;
    canvas.height = 480;
    
    // Mulai memuat model
    await loadModels();
    
    // Setup tombol
    document.getElementById('startButton').addEventListener('click', async () => {
        try {
            await startVideo();
            isDetecting = true;
            document.getElementById('startButton').disabled = true;
            document.getElementById('stopButton').disabled = false;
            detectEmotion();
        } catch (err) {
            console.error('Error starting video:', err);
        }
    });
    
    document.getElementById('stopButton').addEventListener('click', () => {
        isDetecting = false;
        cancelAnimationFrame(detectionInterval);
        document.getElementById('startButton').disabled = false;
        document.getElementById('stopButton').disabled = true;
        document.getElementById('emotionResult').innerHTML = 'Deteksi dihentikan';
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    });
});