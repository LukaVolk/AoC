const fs = require('fs');

fs.readFile('2023/dan8/i.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    
    const lines = data.split('\n');
    console.log(lines);
    console.log(lines[0]);
    let dict = {};
    for (let i = 2; i < lines.length; i++) {
        const line = lines[i];
        const parts = line.split(' = ');
        const key = parts[0];
        const value = parts[1];
        dict[key] = value;
    }
    console.log(dict);

});

