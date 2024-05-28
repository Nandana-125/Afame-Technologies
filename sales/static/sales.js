document.getElementById('salesForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const tvExpense = document.getElementById('tvExpense').value;
    const radioExpense = document.getElementById('radioExpense').value;
    const newspaperExpense = document.getElementById('newspaperExpense').value;

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            tvExpense: tvExpense,
            radioExpense: radioExpense,
            newspaperExpense: newspaperExpense
        })
    });

    const result = await response.json();
    document.getElementById('result').innerText = result.sales.toFixed(2);
});
