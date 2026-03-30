from flask import Flask, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Task Dashboard</title>

<style>
body {
    font-family: Arial;
    margin: 0;
    background: #eef2f7;
}

.header {
    background: #2c3e50;
    color: white;
    padding: 15px;
    text-align: center;
    font-size: 24px;
}

.container {
    padding: 20px;
}

.form {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
}

input, select {
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

button {
    padding: 10px;
    background: #3498db;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #2980b9;
}

table {
    width: 100%;
    border-collapse: collapse;
    background: white;
}

th {
    background: #34495e;
    color: white;
    padding: 10px;
}

td {
    padding: 10px;
    border-bottom: 1px solid #ddd;
    text-align: center;
}

.done {
    text-decoration: line-through;
    color: gray;
}

.action {
    cursor: pointer;
    margin: 0 5px;
}

.filter {
    margin-bottom: 15px;
}
</style>
</head>

<body>

<div class="header">Task Tracker Dashboard</div>

<div class="container">

<div class="form">
    <input id="taskInput" placeholder="Enter task">
    <input type="date" id="dateInput">
    <button onclick="addTask()">Add</button>
</div>

<div class="filter">
    <label>Filter by Month:</label>
    <input type="month" id="monthFilter" onchange="filterTasks()">
</div>

<table>
    <thead>
        <tr>
            <th>Task</th>
            <th>Date</th>
            <th>Status</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody id="taskTable"></tbody>
</table>

</div>

<script>
let tasks = [];

function addTask() {
    const text = document.getElementById("taskInput").value;
    const date = document.getElementById("dateInput").value;

    if (!text || !date) return;

    tasks.push({text, date, done: false});
    renderTasks();

    document.getElementById("taskInput").value = "";
}

function renderTasks(filtered = null) {
    const data = filtered || tasks;
    const table = document.getElementById("taskTable");
    table.innerHTML = "";

    data.forEach((task, index) => {
        const row = `
        <tr>
            <td class="${task.done ? 'done' : ''}">${task.text}</td>
            <td>${task.date}</td>
            <td>${task.done ? "✔ Done" : "Pending"}</td>
            <td>
                <span class="action" onclick="toggleDone(${index})">✔</span>
                <span class="action" onclick="deleteTask(${index})">❌</span>
            </td>
        </tr>
        `;
        table.innerHTML += row;
    });
}

function deleteTask(i) {
    tasks.splice(i, 1);
    renderTasks();
}

function toggleDone(i) {
    tasks[i].done = !tasks[i].done;
    renderTasks();
}

function filterTasks() {
    const month = document.getElementById("monthFilter").value;

    if (!month) {
        renderTasks();
        return;
    }

    const filtered = tasks.filter(t => t.date.startsWith(month));
    renderTasks(filtered);
}
</script>

</body>
</html>
"""

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect('/')

@app.route('/done/<int:index>')
def done(index):
    tasks[index] = "✔ " + tasks[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)