# main.py
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Таблица с треугольниками</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <table id="main-table">
        <tr>
            <th>№</th>
            <th>Город</th>
            <th>Страна</th>
        </tr>
        <tr>
            <td>1</td>
            <td class="city">
                Москва
                <div class="triangle triangle-left" onclick="toggleTable(this, 'up')"></div>
                <div class="triangle triangle-right" onclick="toggleTable(this, 'down')"></div>
                <div class="triangle triangle-middle" onclick="toggleTable(this, 'middle')"></div>
            </td>
            <td>Россия</td>
        </tr>
        <tr>
            <td>2</td>
            <td class="city">
                Париж
                <div class="triangle triangle-left" onclick="toggleTable(this, 'up')"></div>
                <div class="triangle triangle-right" onclick="toggleTable(this, 'down')"></div>
                <div class="triangle triangle-middle" onclick="toggleTable(this, 'middle')"></div>
            </td>
            <td>Франция</td>
        </tr>
        <tr>
            <td>3</td>
            <td class="city">
                Нью-Йорк
                <div class="triangle triangle-left" onclick="toggleTable(this, 'up')"></div>
                <div class="triangle triangle-right" onclick="toggleTable(this, 'down')"></div>
                <div class="triangle triangle-middle" onclick="toggleTable(this, 'middle')"></div>
            </td>
            <td>США</td>
        </tr>
        <tr>
            <td>4</td>
            <td class="city">
                Токио
                <div class="triangle triangle-left" onclick="toggleTable(this, 'up')"></div>
                <div class="triangle triangle-right" onclick="toggleTable(this, 'down')"></div>
                <div class="triangle triangle-middle" onclick="toggleTable(this, 'middle')"></div>
            </td>
            <td>Япония</td>
        </tr>
        <tr>
            <td>5</td>
            <td class="city">
                Берлин
                <div class="triangle triangle-left" onclick="toggleTable(this, 'up')"></div>
                <div class="triangle triangle-right" onclick="toggleTable(this, 'down')"></div>
                <div class="triangle triangle-middle" onclick="toggleTable(this, 'middle')"></div>
            </td>
            <td>Германия</td>
        </tr>
        <tr>
            <td>6</td>
            <td class="city">
                Рим
                <div class="triangle triangle-left" onclick="toggleTable(this, 'up')"></div>
                <div class="triangle triangle-right" onclick="toggleTable(this, 'down')"></div>
                <div class="triangle triangle-middle" onclick="toggleTable(this, 'middle')"></div>
            </td>
            <td>Италия</td>
        </tr>
    </table>
    <script src="scripts.js"></script>
</body>
</html>
"""

css_content = """
table {
    width: 70%;
    border-collapse: collapse;
    margin: 50px auto;
}
th, td {
    border: 1px solid #dddddd;
    text-align: center;
    padding: 8px;
}
.city {
    position: relative;
    cursor: pointer;
}
.triangle {
    width: 0;
    height: 0;
    border-style: solid;
    position: absolute;
}
.triangle-left {
    border-width: 0 10px 10px 0;
    border-color: transparent #007bff transparent transparent;
    left: -15px;
    top: 0;
}
.triangle-right {
    border-width: 10px 0 0 10px;
    border-color: transparent transparent transparent #007bff;
    right: -15px;
    bottom: 0;
}
.triangle-middle {
    border-width: 10px 10px 0 0;
    border-color: #007bff transparent transparent transparent;
    left: 50%;
    top: -15px;
    transform: translateX(-50%);
}
"""

js_content = """
function toggleTable(element, direction) {
    const cityCell = element.parentElement;
    const row = cityCell.parentElement;
    const table = document.getElementById('main-table');
    const index = row.rowIndex;
    const notificationRows = [
        '<tr class="notification-row"><td colspan="3">Уведомления</td></tr>',
        '<tr class="notification-row"><td colspan="3">Осмотр</td></tr>',
        '<tr class="notification-row"><td colspan="3">ТО</td></tr>',
        '<tr class="notification-row"><td colspan="3">СТО</td></tr>',
        '<tr class="notification-row"><td colspan="3">Перегруз</td></tr>',
        '<tr class="notification-row"><td colspan="3">Перегрев</td></tr>'
    ];
    const scheduleRows = [
        '<tr class="schedule-row"><td colspan="3">Планируемое время заезда</td></tr>',
        '<tr class="schedule-row"><td colspan="3">Планируемое время выезда</td></tr>'
    ];
    const additionalRows = [
        '<tr class="additional-row"><td colspan="3">Дополнительная информация 1</td></tr>',
        '<tr class="additional-row"><td colspan="3">Дополнительная информация 2</td></tr>'
    ];

    if (direction === 'up') {
        toggleRows(notificationRows, table, index);
    } else if (direction === 'down') {
        toggleRows(scheduleRows, table, index + 1);
    } else if (direction === 'middle') {
        toggleRows(additionalRows, table, index + notificationRows.length + 1);
    }
}

function toggleRows(rows, table, index) {
    const existingRows = Array.from(table.rows).slice(index + 1, index + 1 + rows.length);
    if (existingRows.every(row => row.classList.contains('notification-row') || row.classList.contains('schedule-row') || row.classList.contains('additional-row'))) {
        existingRows.forEach(row => table.deleteRow(row.rowIndex));
    } else {
        rows.forEach((row, i) => {
            table.insertRow(index + i + 1).outerHTML = row;
        });
    }
}
"""

# Функция для записи содержимого в файл
def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

# Запись содержимого в соответствующие файлы
write_to_file('index.html', html_content)
write_to_file('styles.css', css_content)
write_to_file('scripts.js', js_content)

print("Файлы index.html, styles.css и scripts.js успешно созданы.")
