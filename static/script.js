document.addEventListener("DOMContentLoaded", () => {
    loadTables();
});

function loadTables() {
    fetch('/tables')
        .then(response => response.json())
        .then(data => {
            const tableList = document.getElementById('tableList');
            tableList.innerHTML = ''; // 清空当前选项
            data.forEach(table => {
                const option = document.createElement('option');
                option.value = table;
                option.textContent = table;
                tableList.appendChild(option);
            });
            if (data.length > 0) {
                loadTableEntries(); // 自动加载第一个表的内容
            }
        })
        .catch(error => console.error('Error loading tables:', error));
}

function createTable() {
    const tableName = document.getElementById('tableName').value;
    fetch('/tables', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ table_name: tableName }),
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
            loadTables(); // 重新加载表列表
        })
        .catch(error => console.error('Error creating table:', error));
}

function deleteTable() {
    const tableName = document.getElementById('tableList').value;
    fetch(`/tables/${tableName}`, {
        method: 'DELETE',
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
            loadTables(); // 重新加载表列表
        })
        .catch(error => console.error('Error deleting table:', error));
}

function loadTableEntries() {
    const tableName = document.getElementById('tableList').value;
    fetch(`/tables/${tableName}/entries`)
        .then(response => response.json())
        .then(data => {
            const entryList = document.getElementById('entryList');
            entryList.innerHTML = ''; // 清空当前条目
            data.forEach(entry => {
                const li = document.createElement('li');
                li.textContent = entry.text;

                // 创建删除按钮
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.onclick = () => deleteEntry(tableName, entry.id);

                li.appendChild(deleteButton);
                entryList.appendChild(li);
            });
        })
        .catch(error => console.error('Error loading entries:', error));
}

function addEntry() {
    const tableName = document.getElementById('tableList').value;
    const entryText = document.getElementById('entryText').value;
    fetch(`/tables/${tableName}/entries`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: entryText }),
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
            loadTableEntries(); // 重新加载条目
        })
        .catch(error => console.error('Error adding entry:', error));
}

function deleteEntry(tableName, entryId) {
    fetch(`/tables/${tableName}/entries/${entryId}`, {
        method: 'DELETE',
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
            loadTableEntries(); // 重新加载条目
        })
        .catch(error => console.error('Error deleting entry:', error));
}

function deleteAllEntries() {
    const tableName = document.getElementById('tableList').value;
    fetch(`/tables/${tableName}/entries`, {
        method: 'DELETE',
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
            loadTableEntries(); // 重新加载条目
        })
        .catch(error => console.error('Error deleting entries:', error));
}

function queryEntries() {
    const tableName = document.getElementById('tableList').value;
    const queryText = document.getElementById('queryText').value;
    fetch(`/tables/${tableName}/query`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: queryText }),
    })
        .then(response => response.json())
        .then(data => {
            const queryResultList = document.getElementById('queryResultList');
            queryResultList.innerHTML = ''; // 清空当前查询结果
            if (data.message) {
                const li = document.createElement('li');
                li.textContent = data.message;
                queryResultList.appendChild(li);
            } else {
                data.forEach(result => {
                    const li = document.createElement('li');
                    li.textContent = `${result.text} (Similarity: ${result.similarity.toFixed(2)})`;
                    queryResultList.appendChild(li);
                });
            }
        })
        .catch(error => console.error('Error querying entries:', error));
}

function splitAndAddEntry() {
    const tableName = document.getElementById('tableList').value;
    const entryText = document.getElementById('semanticEntryText').value;
    fetch('/split_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: entryText }),
    })
        .then(response => response.json())
        .then(chunks => {
            chunks.forEach(chunk => {
                fetch(`/tables/${tableName}/entries`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ text: chunk }),
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data.message);
                        loadTableEntries(); // 重新加载条目
                    })
                    .catch(error => console.error('Error adding split entry:', error));
            });
        })
        .catch(error => console.error('Error splitting text:', error));
}
