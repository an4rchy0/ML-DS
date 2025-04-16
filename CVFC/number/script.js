// Inisialisasi canvas untuk menggambar
const canvas = document.getElementById('drawing-canvas');
const ctx = canvas.getContext('2d');
let isDrawing = false;

// Model dan variabel global
let model;
const MODEL_URL = 'https://storage.googleapis.com/tfjs-models/tfjs/mnist_transfer_cnn_v1/model.json';

// Inisialisasi canvas
function initCanvas() {
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 15;
    ctx.lineCap = 'round';
    
    // Event listeners untuk menggambar
    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDrawing);
    canvas.addEventListener('mouseout', stopDrawing);
    
    // Event listeners untuk touch devices
    canvas.addEventListener('touchstart', handleTouch);
    canvas.addEventListener('touchmove', handleTouch);
    canvas.addEventListener('touchend', stopDrawing);
    
    // Tombol clear
    document.getElementById('clear-btn').addEventListener('click', clearCanvas);
    
    // Tombol prediksi
    document.getElementById('predict-btn').addEventListener('click', predict);
}

// Fungsi untuk memuat model
async function loadModel() {
    try {
        model = await tf.loadLayersModel(MODEL_URL);
        console.log('Model loaded successfully');
    } catch (error) {
        console.error('Error loading model:', error);
    }
}

// Fungsi menggambar
function startDrawing(e) {
    isDrawing = true;
    draw(e);
}

function draw(e) {
    if (!isDrawing) return;
    
    // Dapatkan posisi mouse/touch
    let x, y;
    if (e.type.includes('touch')) {
        const rect = canvas.getBoundingClientRect();
        x = e.touches[0].clientX - rect.left;
        y = e.touches[0].clientY - rect.top;
    } else {
        x = e.offsetX;
        y = e.offsetY;
    }
    
    // Gambar di canvas
    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
}

function stopDrawing() {
    isDrawing = false;
    ctx.beginPath();
}

function handleTouch(e) {
    e.preventDefault();
    if (e.type === 'touchstart') {
        startDrawing(e);
    } else if (e.type === 'touchmove') {
        draw(e);
    }
}

// Bersihkan canvas
function clearCanvas() {
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    document.getElementById('prediction-output').textContent = 'Gambar digit terlebih dahulu';
    document.getElementById('confidence-bars').innerHTML = '';
}

// Prediksi digit
async function predict() {
    if (!model) {
        alert('Model belum dimuat. Silakan tunggu sebentar...');
        return;
    }
    
    // Dapatkan data gambar dari canvas dan praproses
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const processedData = preprocessImage(imageData);
    
    // Buat prediksi
    const predictions = model.predict(processedData).dataSync();
    
    // Tampilkan hasil
    displayPredictions(predictions);
}

// Praproses gambar untuk model
function preprocessImage(imageData) {
    return tf.tidy(() => {
        // Konversi ImageData ke tensor
        let tensor = tf.browser.fromPixels(imageData, 1);
        
        // Resize ke 28x28 (ukuran yang diharapkan model MNIST)
        tensor = tf.image.resizeBilinear(tensor, [28, 28]);
        
        // Normalisasi dan reshape untuk model
        tensor = tensor.toFloat().div(255.0);
        tensor = tensor.expandDims(0);
        
        return tensor;
    });
}

// Tampilkan hasil prediksi
function displayPredictions(predictions) {
    // Dapatkan prediksi terbaik
    const maxPrediction = Math.max(...predictions);
    const predictedDigit = predictions.indexOf(maxPrediction);
    
    // Update UI
    document.getElementById('prediction-output').textContent = `Digit: ${predictedDigit} (${(maxPrediction * 100).toFixed(1)}% confidence)`;
    
    // Buat confidence bars
    const barsContainer = document.getElementById('confidence-bars');
    barsContainer.innerHTML = '';
    
    predictions.forEach((confidence, digit) => {
        const percent = (confidence * 100).toFixed(1);
        
        // Buat container untuk bar
        const barContainer = document.createElement('div');
        barContainer.className = 'confidence-label';
        
        // Label digit
        const digitLabel = document.createElement('span');
        digitLabel.textContent = `${digit}:`;
        
        // Persentase
        const percentLabel = document.createElement('span');
        percentLabel.textContent = `${percent}%`;
        
        // Bar container
        const bar = document.createElement('div');
        bar.className = 'confidence-bar';
        
        // Fill bar
        const fill = document.createElement('div');
        fill.className = 'confidence-fill';
        fill.style.width = `${percent}%`;
        
        bar.appendChild(fill);
        barContainer.appendChild(digitLabel);
        barContainer.appendChild(percentLabel);
        barsContainer.appendChild(barContainer);
        barsContainer.appendChild(bar);
    });
}

// Jalankan saat halaman dimuat
window.onload = async function() {
    initCanvas();
    await loadModel();
};