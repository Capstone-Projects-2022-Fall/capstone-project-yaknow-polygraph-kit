//
const bodyParser = require("body-parser")
const ejs = require("ejs")
const session = require("express-session")
const express = require("express")
const path = require("path")
const cookieParser = require("cookie-parser")
const mysql = require("mysql2")
const app = express()
const port = process.env.PORT || 8000

var urlencodedParser = bodyParser.urlencoded({ extended: false })

const connection = mysql.createConnection({
  host: "173.255.232.150",
  user: "cis4398",
  password: "dNC=IK~9)7",
  database: "users",
})
connection.connect(function (error) {
  if (!!error) console.log(error)
  else console.log("Database Successful")
})

app.set("views", path.join(__dirname, "views"))
app.set("view engine", "ejs")
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(cookieParser("secret"))
app.use(
  "/css",
  express.static(path.join(__dirname, "node_modules/bootstrap/dist/css"))
)
app.use(
  "/js",
  express.static(path.join(__dirname, "node_modules/bootstrap/dist/js"))
)
app.use(
  session({
    secret: "secret",
    resave: true,
    saveUninitialized: true,
  })
)
let sess
function checkUserSession(req, res, next) {
  if (req.session.loggedin) {
    next()
  } else {
    res.redirect("/")
  }
}
app.get("/", function (req, res) {
  sess = req.session
  if (sess.loggedin) {
    return res.redirect("/dashboard")
  }
  if (req.query.logout) {
    return res.redirect("/")
  }
  res.render("login", { title: "Login" })
})
app.post("/", (req, res) => {
  sess = req.session
  const username = req.body.username
  const password = req.body.password

  if (username !== "keshav" && password !== "admin1234") {
    res.render("login", {
      title: "Login",
    })
  } else {
    if (username === "keshav") {
      if (password === "admin1234") {
        sess.username = username
        sess.password = password
        sess.loggedin = true
        res.redirect("/dashboard")
      } else {
        res.render("login", { title: "Login" })
      }
    } else {
      console.log("Username Wrong")
      res.render("login", { title: "Login" })
    }
  }
})
app.get("/dashboard", checkUserSession, async (req, res) => {
  sess = req.session
  sess.loggedin = true
  res.render("dashboard", {
    title: "dashboard",
    loggedin: sess.loggedin,
  })
})
app.get("/user", checkUserSession, async (req, res) => {
  sess = req.session
  sess.loggedin = true

  let sql = "SELECT * FROM user"
  let query = connection.query(sql, (err, rows) => {
    if (err) throw err
    res.render("user", {
      title: "Table",
      users: rows,
    })
  })
})
app.get("/add", (req, res) => {
  res.render("user_add", {
    title: "Add Data",
  })
})
app.post("/update", (req, res) => {
  const userId = req.body.id
  let sql =
    "update user SET f_name='" +
    req.body.f_name +
    "',  username='" +
    req.body.username +
    "',  password='" +
    req.body.password +
    "' where id =" +
    userId
  let query = connection.query(sql, (err, results) => {
    if (err) throw err
    res.redirect("/user")
  })
})
app.post("/save", (req, res) => {
  let data = {
    f_name: req.body.f_name,
    username: req.body.username,
    password: req.body.password,
  }
  let sql = "INSERT INTO user SET ?"
  let query = connection.query(sql, data, (err, results) => {
    if (err) throw err
    res.redirect("/user")
  })
})
app.get("/user/edit/:userId", (req, res) => {
  sess = req.session
  sess.loggedin = true

  const userId = req.params.userId
  let sql = `Select * from user where id = ${userId}`
  let query = connection.query(sql, (err, result) => {
    if (err) throw err
    res.render("user_edit", {
      title: "Edit Tabel",
      user: result[0],
    })
  })
})
app.get("/user/delete/:userId", (req, res) => {
  const userId = req.params.userId
  let sql = `DELETE from user where id = ${userId}`
  let query = connection.query(sql, (err, result) => {
    if (err) throw err
    res.redirect("/user")
  })
})

app.get("/logout", (req, res) => {
  res.redirect("/?logout=true")
  req.session.destroy((err) => {
    if (err) {
      return console.log(err)
    }
  })
})

app.listen(port, function (err) {
  if (err) console.log(err)
  console.log("Server Running On http://localhost:8000")
})
