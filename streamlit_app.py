import streamlit as st

st.title("🎈 My new app")
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game Flappy Bird Simpel</title>
    <style>
        body {
            background-color: #222;
            color: #fff;
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        h1 { margin-bottom: 5px; }
        #score-board { font-size: 24px; margin-bottom: 15px; font-weight: bold; color: #ffeb3b; }
        canvas {
            border: 4px solid #fff;
            background-color: #70c5ce; /* Warna langit */
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
        }
        .info { margin-top: 10px; color: #ccc; }
    </style>
</head>
<body>

    <h1>Flappy Kotak 🐦</h1>
    <div id="score-board">Skor: 0</div>
    <canvas id="gameCanvas" width="400" height="500"></canvas>
    <div class="info">Tekan <b>SPASI</b> atau <b>KLIK MOUSE</b> untuk Melompat!</div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const scoreBoard = document.getElementById("score-board");

        // Karakter Burung (Kotak Kuning)
        let birdY = 250;
        let birdX = 50;
        let birdSize = 20;
        let gravity = 0.4;
        let velocity = 0;
        let jump = -7;

        // Pipa (Rintangan)
        let pipes = [];
        let pipeWidth = 50;
        let pipeGap = 130; // Jarak celah atas bawah
        let pipeSpeed = 2;
        let frameCount = 0;

        let score = 0;
        let gameOver = false;

        // Fungsi mereset game saat mulai/kalah
        function resetGame() {
            birdY = 250;
            velocity = 0;
            pipes = [];
            score = 0;
            frameCount = 0;
            gameOver = false;
            scoreBoard.innerText = "Skor: " + score;
            loop();
        }

        // Membuat pipa baru secara acak
        function spawnPipe() {
            let minHeight = 50;
            let maxHeight = canvas.height - pipeGap - minHeight;
            let height = Math.floor(Math.random() * (maxHeight - minHeight + 1)) + minHeight;

            pipes.push({
                x: canvas.width,
                top: height,
                bottom: canvas.height - height - pipeGap,
                passed: false
            });
        }

        // Loop Utama Game
        function loop() {
            if (gameOver) {
                alert("Game Over! Skor Akhir Kamu: " + score);
                resetGame();
                return;
            }

            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // 1. Logika & Gravitasi Burung
            velocity += gravity;
            birdY += velocity;

            // Gambar Burung
            ctx.fillStyle = "#ffeb3b"; // Warna kuning burung
            ctx.fillRect(birdX, birdY, birdSize, birdSize);

            // Cek jika burung jatuh ke dasar atau terbang terlalu tinggi
            if (birdY + birdSize > canvas.height || birdY < 0) {
                gameOver = true;
            }

            // 2. Logika Pipa
            if (frameCount % 100 === 0) {
                spawnPipe();
            }
            frameCount++;

            for (let i = pipes.length - 1; i >= 0; i--) {
                pipes[i].x -= pipeSpeed;

                // Gambar Pipa Atas
                ctx.fillStyle = "#4caf50"; // Warna hijau pipa
                ctx.fillRect(pipes[i].x, 0, pipeWidth, pipes[i].top);

                // Gambar Pipa Bawah
                ctx.fillRect(pipes[i].x, canvas.height - pipes[i].bottom, pipeWidth, pipes[i].bottom);

                // Hitung Skor jika berhasil melewati pipa
                if (!pipes[i].passed && pipes[i].x + pipeWidth < birdX) {
                    score++;
                    scoreBoard.innerText = "Skor: " + score;
                    pipes[i].passed = true;
                }

                // Deteksi Tabrakan Burung dengan Pipa
                if (
                    birdX < pipes[i].x + pipeWidth &&
                    birdX + birdSize > pipes[i].x &&
                    (birdY < pipes[i].top || birdY + birdSize > canvas.height - pipes[i].bottom)
                ) {
                    gameOver = true;
                }

                // Hapus pipa yang sudah keluar layar biar memori tidak penuh
                if (pipes[i].x + pipeWidth < 0) {
                    pipes.splice(i, 1);
                }
            }

            requestAnimationFrame(loop);
        }

        // Kontrol Lompat (Bisa pakai Spasi atau Klik Mouse)
        function flap() {
            if (!gameOver) {
                velocity = jump;
            }
        }

        window.addEventListener("keydown", function(e) {
            if (e.code === "Space") flap();
        });

        canvas.addEventListener("mousedown", flap);

        // Mulai game pertama kali
        resetGame();
    </script>
</body>
</html>
