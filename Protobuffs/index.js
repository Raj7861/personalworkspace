
const fs = require("fs")

const employee = []
aAyesh
const Ayesha = {
    "name": "Ayesha",
    "salary": 30000,
    "id": 1002
}

employee.push(Ayesha)
employee.push()

fs.writeFileSync("jsondata.json", JSON.stringify(employee))
console.log(JSON.stringify(employee))
Ayesha