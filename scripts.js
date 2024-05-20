
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
