
const fs = require("fs");

const Schema = require("./employee_pb");

const emp1 = new Schema.Employee()
const emp2 = new Schema.Employee()

const employees = new Schema.Employees()

emp1.setId(1001);
emp1.setName("Siraj")
emp1.setSalary(30000.00)

emp2.setId(1002);
emp2.setName("Shameel")
emp2.setSalary(24000.00)

employees.addEmployees(emp1)
employees.addEmployees(emp2)

// console.log("My name is " + emp1.getName())
//console.log("My salary is " + emp2.getSalary())

const bytes = employees.serializeBinary()
fs.writeFileSync("employeeBinary", bytes)
console.log("Binary " + bytes)

const employees2 = Schema.Employees.deserializeBinary(bytes);
obj = JSON.stringify(employees2.toObject());
console.log(obj)
