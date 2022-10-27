var mysql = require("mysql")
var app = express()

var connection = mysql.createConnection({
  host: "localhost",
  port: 3306,
  user: "user",
  password: "password",
  database: "mydb",
})

const buttonBeginElement = document.getElementById("button-begin")
const buttonCollectElement = document.getElementById("button-collect")
const formElement = document.getElementById("form")

function button_clicked() {
  console.log("Button Clicked")
}

function upload(event) {
  event.preventDefault()

  const userFile = document.getElementById("file").files[0]

  const formData = new FormData()
  formData.append("data", userFile, "user-data")

  fetch("http://httpbin.org/post", {
    method: "POST",
    body: formData,
  })
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch((err) => console.log(err))

  var fileReader = new FileReader()
  fileReader.onload = function () {
    const csv = fileReader.result
    const array = csv.split("\r\n").map((line) => {
      return line.split(",")
    })
    document.getElementById("output").textContent = array
  }

  fileReader.readAsText(userFile)
}

buttonBeginElement.addEventListener("click", button_clicked)
buttonCollectElement.addEventListener("click", button_clicked)
formElement.addEventListener("submit", upload)
