# UAS PAK CAN (MYSQL - LOGIN - CRUD)
aplikasi pendaftaran <b>sesuai kriteria UAS</b> kecuali No.2

dibuat dengan :
- Node JS
- Express JS
- MySql

fitur aplikasi :
- login
- Create
- Read
- Update
- Delete

## Demo Akun
username : fathon
password : admin1234

## Cara Instalasinya gmna boi?
ikutin langkah - langkahnya yaa :)

### 1) Clone Repository atau Download ZIP
```
https://github.com/betonk26/mysql-login.git
```

### 2) Masuk Directorynya
cara masuknya ke bagian atas vs code -> new terminal kemudian
```
cd mysql-login
```

### 3) Install Dependencies
jalanin di terminal kalau mau coba
```
npm install express mysql bootstrap express-session ejs body-parser cookie-parser path morgan env
```
atau
```
npm install
```

### 4) Setting Project
ubah database kalian atau bisa juga pakai database bawaan
```js
const connection = mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'',
    database:'UBAH DATABASE KALIAN' // bawaan 'test_node'
});
```

ubah akun loginnya
```js
if (username !== 'USERNAME KALIAN' && password !== 'PASSWORD KALIAN') //if (username !== 'fathon' && password !== 'admin1234')
```
dan juga ganti untuk check akunnya
```
if (username === "fathon") {
        if (password === "admin1234") {
```


### 5) Jalanin Servernya (aplikasi)
ada 2 cara yaitu menggunakan
```
npm start
```
atau
```
nodemon app
```
note : untuk nodemon harus sudah terinstall secara global
```
npm install -g nodemon
```

Aplikasi kamu berjalan pada port : http://localhost:8000

## Catatan
Ini adalah Project Free & Open Source, Jika Kalian Ingin Menggunakannya Untuk Kepentingan Pribadi / Komersil, Boleh Saja

## CREDITS
- Ahmad Fathon Nurhidayat

## Donate For Support This Project :)
`nambahin buat bayar makrab` 6801038643 no rek BCA AHMAD FATHON <br>
`biar bikin templatenya makin niat` <a href="https://saweria.co/fathon" target='_blank'>click here!</a>
