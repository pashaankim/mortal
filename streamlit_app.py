import streamlit as st
st.title("🎈 My new app")
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Game Tebak Angka Simpel</title>
    <style>
        body {
            background-color: #f0f2f5;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 50px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            display: inline-block;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
        input {
            padding: 10px;
            font-size: 16px;
            width: 60px;
            text-align: center;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover { background-color: #0056b3; }
        #pesan { margin-top: 20px; font-weight: bold; font-size: 18px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🎲 Game Tebak Angka 🎲</h2>
        <p>Aku sedang memikirkan angka antara <b>1 sampai 10</b>.</p>
        <p>Coba tebak angka berapa itu?</p>
        
        <input type="number" id="tebakanInput" min="1" max="10">
        <button onclick="cekTebakan()">Tebak!</button>

        <p id="pesan" style="color: #333;"></p>
    </div>
    <script>
        // Komputer memilih angka acak antara 1 sampai 10 saat game dimulai
        let angkaRahasia = Math.floor(Math.random() * 10) + 1;
        let jumlahTebakan = 0;

        function cekTebakan() {
            let input = document.getElementById("tebakanInput").value;
            let pesan = document.getElementById("pesan");
            
            // Validasi jika input kosong
            if (input === "") {
                pesan.innerHTML = "Masukkan angka dulu ya!";
                pesan.style.color = "red";
                return;
            }
            let tebakan = Number(input);
            jumlahTebakan++;

            if (tebakan === angkaRahasia) {
                pesan.innerHTML = `🎉 BENAR! Angkanya adalah ${angkaRahasia}.<br>Kamu berhasil menebak dalam ${jumlahTebakan} kali percobaan!`;
                pesan.style.color = "green";
                
                // Reset game otomatis setelah 3 detik
                setTimeout(() => {
                    angkaRahasia = Math.floor(Math.random() * 10) + 1;
                    jumlahTebakan = 0;
                    pesan.innerHTML = "Game di-reset! Silakan tebak angka baru.";
                    pesan.style.color = "#333";
                    document.getElementById("tebakanInput").value = "";
                }, 4000);

            } else if (tebakan < angkaRahasia) {
                pesan.innerHTML = "❌ Terlalu KECIL! Coba angka yang lebih besar.";
                pesan.style.color = "blue";
            } else {
                pesan.innerHTML = "❌ Terlalu BESAR! Coba angka yang lebih kecil.";
                pesan.style.color = "orange";
            }
        }
    </script>
</body>
</html>
