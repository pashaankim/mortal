import streamlit as st

st.title("🎈 My new app")
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game Ular Seru & Mudah</title>
    <style>
        body {
            background-color: #1e1e24;
            color: #fff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        h1 {
            margin-bottom: 10px;
        }
        #score-board {
            font-size: 24px;
            margin-bottom: 20px;
            font-weight: bold;
            color: #4caf50;
        }
        canvas {
            border: 4px solid #fff;
            background-color: #111;
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
        }
        .info {
            margin-top: 15px;
            color: #aaa;
            font-size: 14px;
        }
    </style>
</head>
<body>

    <h1>Game Ular 🐍</h1>
    <div id="score-board">Skor: 0</div>
    <canvas id="gameCanvas" width="400" height="400"></canvas>
    <div class="info">Gunakan tombol PANAH di keyboard untuk bergerak!</div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const scoreBoard = document.getElementById("score-board");

        const gridSize = 20;
        const tileCount = canvas.width / gridSize;

        // Posisi awal ular
        let snake = [{x: 10, y: 10}];
        // Posisi awal makanan
        let food = {x: 15, y: 7};
        
        // Kecepatan & arah gerak (mulai dengan diam)
        let dx = 0;
        let dy = 0;
        
        let score = 0;
        let gameSpeed = 100; // Semakin kecil angkanya, semakin cepat jalannya game

        // Loop utama game
        function main() {
            if (hasGameEnded()) {
                alert("Game Over! Skor Akhir Kamu: " + score);
                document.location.reload();
                return;
            }

            setTimeout(function onTick() {
                clearCanvas();
                drawFood();
                moveSnake();
                drawSnake();
                main();
            }, gameSpeed);
        }

        // Jalankan game pertama kali
        main();

        // Menggambar background hitam canvas
        function clearCanvas() {
            ctx.fillStyle = "#111";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }

        // Menggambar ular
        function drawSnake() {
            snake.forEach((part, index) => {
                // Kepala ular warna hijau terang, badannya hijau biasa
                ctx.fillStyle = index === 0 ? "#81c784" : "#4caf50";
                ctx.fillRect(part.x * gridSize, part.y * gridSize, gridSize - 2, gridSize - 2);
            });
        }

        // Menggerakkan ular
        function moveSnake() {
            const head = {x: snake[0].x + dx, y: snake[0].y + dy};
            snake.unshift(head);

            // Cek apakah ular makan buah
            const hasEatenFood = snake[0].x === food.x && snake[0].y === food.y;
            if (hasEatenFood) {
                score += 10;
                scoreBoard.innerText = "Skor: " + score;
                generateFood();
            } else {
                snake.pop(); // Hapus ekor jika tidak makan buah
            }
        }

        // Memunculkan makanan secara acak
        function generateFood() {
            food.x = Math.floor(Math.random() * tileCount);
            food.y = Math.floor(Math.random() * tileCount);
            
            // Pastikan makanan tidak muncul di badan ular
            snake.forEach(part => {
                if (part.x === food.x && part.y === food.y) generateFood();
            });
        }

        // Menggambar makanan (warna merah)
        function drawFood() {
            ctx.fillStyle = "#ff5722";
            ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);
        }

        // Deteksi tabrakan (Game Over)
        function hasGameEnded() {
            // Tabrak dinding kiri/kanan/atas/bawah
            const hitLeftWall = snake[0].x < 0;
            const hitRightWall = snake[0].x >= tileCount;
            const hitToptWall = snake[0].y < 0;
            const hitBottomWall = snake[0].y >= tileCount;

            if (hitLeftWall || hitRightWall || hitToptWall || hitBottomWall) return true;

            // Tabrak badan sendiri
            for (let i = 4; i < snake.length; i++) {
                if (snake[i].x === snake[0].x && snake[i].y === snake[0].y) return true;
            }
            return false;
        }

        // Membaca input keyboard tombol panah
        window.addEventListener("keydown", changeDirection);

        function changeDirection(event) {
            const keyPressed = event.keyCode;
            const LEFT_KEY = 37;
            const UP_KEY = 38;
            const RIGHT_KEY = 39;
            const DOWN_KEY = 40;

            const goingUp = dy === -1;
            const goingDown = dy === 1;
            const goingRight = dx === 1;
            const goingLeft = dx === -1;

            if (keyPressed === LEFT_KEY && !goingRight) { dx = -1; dy = 0; }
            if (keyPressed === UP_KEY && !goingDown) { dx = 0; dy = -1; }
            if (keyPressed === RIGHT_KEY && !goingLeft) { dx = 1; dy = 0; }
            if (keyPressed === DOWN_KEY && !goingUp) { dx = 0; dy = 1; }
        }
    </script>
</body>
</html>
