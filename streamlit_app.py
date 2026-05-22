import streamlit as st

st.title("🎈 My new app")

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game 2048 Simpel</title>
    <style>
        body {
            background-color: #faf8ef;
            color: #776e65;
            font-family: "Clear Sans", "Helvetica Neue", Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        h1 { font-size: 48px; margin: 0; }
        #score-container {
            background: #bbada0;
            padding: 10px 20px;
            color: white;
            font-weight: bold;
            border-radius: 3px;
            margin-bottom: 20px;
        }
        #grid {
            background: #bbada0;
            width: 340px;
            height: 340px;
            padding: 10px;
            border-radius: 6px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-gap: 10px;
        }
        .cell {
            background: rgba(238, 228, 218, 0.35);
            border-radius: 3px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
            color: #776e65;
        }
        /* Warna untuk angka-angka khusus */
        .cell[data-value="2"] { background: #eee4da; }
        .cell[data-value="4"] { background: #ede0c8; }
        .cell[data-value="8"] { background: #f2b179; color: #f9f6f2; }
        .cell[data-value="16"] { background: #f59563; color: #f9f6f2; }
        .cell[data-value="32"] { background: #f67c5f; color: #f9f6f2; }
        .cell[data-value="64"] { background: #f65e3b; color: #f9f6f2; }
        .cell[data-value="128"] { background: #edcf72; color: #f9f6f2; font-size: 20px; }
        .cell[data-value="256"] { background: #edcc61; color: #f9f6f2; font-size: 20px; }
        .cell[data-value="512"] { background: #ebd846; color: #f9f6f2; font-size: 20px; }
        .cell[data-value="1024"] { background: #e2ba13; color: #f9f6f2; font-size: 16px; }
        .cell[data-value="2048"] { background: #ecc400; color: #f9f6f2; font-size: 16px; }
    </style>
</head>
<body>

    <h1>2048</h1>
    <div id="score-container">Skor: <span id="score">0</span></div>
    <div id="grid"></div>

    <script>
        const gridDisplay = document.getElementById('grid');
        const scoreDisplay = document.getElementById('score');
        const width = 4;
        let squares = [];
        let score = 0;

        // Membuat papan permainan 4x4
        function createBoard() {
            for (let i = 0; i < width * width; i++) {
                const cell = document.createElement('div');
                cell.classList.add('cell');
                cell.innerHTML = '';
                gridDisplay.appendChild(cell);
                squares.push(cell);
            }
            generateNumber();
            generateNumber();
        }
        createBoard();

        // Memunculkan angka 2 secara acak di kotak yang kosong
        function generateNumber() {
            let numZeroes = squares.filter(cell => cell.innerHTML === '');
            if (numZeroes.length > 0) {
                let randomSquare = numZeroes[Math.floor(Math.random() * numZeroes.length)];
                randomSquare.innerHTML = 2;
                randomSquare.setAttribute('data-value', 2);
                checkForGameOver();
            }
        }

        // Logika menggeser ke kanan
        function moveRight() {
            for (let i = 0; i < 16; i++) {
                if (i % 4 === 0) {
                    let totalOne = squares[i].innerHTML;
                    let totalTwo = squares[i+1].innerHTML;
                    let totalThree = squares[i+2].innerHTML;
                    let totalFour = squares[i+3].innerHTML;
                    let row = [Number(totalOne), Number(totalTwo), Number(totalThree), Number(totalFour)];

                    let filteredRow = row.filter(num => num);
                    let missing = 4 - filteredRow.length;
                    let zeros = Array(missing).fill('');
                    let newRow = zeros.concat(filteredRow);

                    squares[i].innerHTML = newRow[0];
                    squares[i+1].innerHTML = newRow[1];
                    squares[i+2].innerHTML = newRow[2];
                    squares[i+3].innerHTML = newRow[3];
                }
            }
            updateStyles();
        }

        // Logika menggeser ke kiri
        function moveLeft() {
            for (let i = 0; i < 16; i++) {
                if (i % 4 === 0) {
                    let totalOne = squares[i].innerHTML;
                    let totalTwo = squares[i+1].innerHTML;
                    let totalThree = squares[i+2].innerHTML;
                    let totalFour = squares[i+3].innerHTML;
                    let row = [Number(totalOne), Number(totalTwo), Number(totalThree), Number(totalFour)];

                    let filteredRow = row.filter(num => num);
                    let missing = 4 - filteredRow.length;
                    let zeros = Array(missing).fill('');
                    let newRow = filteredRow.concat(zeros);

                    squares[i].innerHTML = newRow[0];
                    squares[i+1].innerHTML = newRow[1];
                    squares[i+2].innerHTML = newRow[2];
                    squares[i+3].innerHTML = newRow[3];
                }
            }
            updateStyles();
        }

        // Menggabungkan angka baris yang sama saat digeser
        function combineRow() {
            for (let i = 0; i < 15; i++) {
                if (squares[i].innerHTML === squares[i+1].innerHTML && squares[i].innerHTML !== '' && (i + 1) % 4 !== 0) {
                    let combinedTotal = Number(squares[i].innerHTML) + Number(squares[i+1].innerHTML);
                    squares[i].innerHTML = combinedTotal;
                    squares[i+1].innerHTML = '';
                    score += combinedTotal;
                    scoreDisplay.innerHTML = score;
                }
            }
            updateStyles();
        }

        // Logika menggeser ke bawah
        function moveDown() {
            for (let i = 0; i < 4; i++) {
                let totalOne = squares[i].innerHTML;
                let totalTwo = squares[i+width].innerHTML;
                let totalThree = squares[i+(width*2)].innerHTML;
                let totalFour = squares[i+(width*3)].innerHTML;
                let column = [Number(totalOne), Number(totalTwo), Number(totalThree), Number(totalFour)];

                let filteredColumn = column.filter(num => num);
                let missing = 4 - filteredColumn.length;
                let zeros = Array(missing).fill('');
                let newColumn = zeros.concat(filteredColumn);

                squares[i].innerHTML = newColumn[0];
                squares[i+width].innerHTML = newColumn[1];
                squares[i+(width*2)].innerHTML = newColumn[2];
                squares[i+(width*3)].innerHTML = newColumn[3];
            }
            updateStyles();
        }

        // Logika menggeser ke atas
        function moveUp() {
            for (let i = 0; i < 4; i++) {
                let totalOne = squares[i].innerHTML;
                let totalTwo = squares[i+width].innerHTML;
                let totalThree = squares[i+(width*2)].innerHTML;
                let totalFour = squares[i+(width*3)].innerHTML;
                let column = [Number(totalOne), Number(totalTwo), Number(totalThree), Number(totalFour)];

                let filteredColumn = column.filter(num => num);
                let missing = 4 - filteredColumn.length;
                let zeros = Array(missing).fill('');
                let newColumn = filteredColumn.concat(zeros);

                squares[i].innerHTML = newColumn[0];
                squares[i+width].innerHTML = newColumn[1];
                squares[i+(width*2)].innerHTML = newColumn[2];
                squares[i+(width*3)].innerHTML = newColumn[3];
            }
            updateStyles();
        }

        // Menggabungkan angka kolom yang sama saat digeser
        function combineColumn() {
            for (let i = 0; i < 12; i++) {
                if (squares[i].innerHTML === squares[i+width].innerHTML && squares[i].innerHTML !== '') {
                    let combinedTotal = Number(squares[i].innerHTML) + Number(squares[i+width].innerHTML);
                    squares[i].innerHTML = combinedTotal;
                    squares[i+width].innerHTML = '';
                    score += combinedTotal;
                    scoreDisplay.innerHTML = score;
                }
            }
            updateStyles();
        }

        // Mengupdate warna kotak sesuai dengan nilainya
        function updateStyles() {
            for (let i = 0; i < squares.length; i++) {
                if (squares[i].innerHTML === "0" || squares[i].innerHTML === "") {
                    squares[i].innerHTML = "";
                    squares[i].removeAttribute('data-value');
                } else {
                    squares[i].setAttribute('data-value', squares[i].innerHTML);
                }
            }
        }

        // Membaca input tombol panah keyboard
        function control(e) {
            if (e.keyCode === 39) { // Panah Kanan
                moveRight(); combineRow(); moveRight(); generateNumber();
            } else if (e.keyCode === 37) { // Panah Kiri
                moveLeft(); combineRow(); moveLeft(); generateNumber();
            } else if (e.keyCode === 38) { // Panah Atas
                moveUp(); combineColumn(); moveUp(); generateNumber();
            } else if (e.keyCode === 40) { // Panah Bawah
                moveDown(); combineColumn(); moveDown(); generateNumber();
            }
        }
        document.addEventListener('keyup', control);

        // Cek jika game over (tidak ada kotak kosong lagi)
        function checkForGameOver() {
            let zeros = 0;
            for (let i = 0; i < squares.length; i++) {
                if (squares[i].innerHTML === "") zeros++;
            }
            if (zeros === 0) {
                alert("Game Over! Papan sudah penuh.");
                document.location.reload();
            }
        }
    </script>
</body>
</html> 
