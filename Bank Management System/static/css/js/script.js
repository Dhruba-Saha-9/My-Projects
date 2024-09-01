document.getElementById('create-account-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const initialDeposit = document.getElementById('initialDeposit').value;
    const response = await fetch('/create-account', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, initialDeposit })
    });
    const result = await response.json();
    document.getElementById('result').innerText = result.message || result.error;
});

document.getElementById('deposit-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const accountId = document.getElementById('depositAccountId').value;
    const amount = document.getElementById('depositAmount').value;
    const response = await fetch('/deposit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ accountId, amount })
    });
    const result = await response.json();
    document.getElementById('result').innerText = result.message || result.error;
});

document.getElementById('withdraw-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const accountId = document.getElementById('withdrawAccountId').value;
    const amount = document.getElementById('withdrawAmount').value;
    const response = await fetch('/withdraw', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ accountId, amount })
    });
    const result = await response.json();
    document.getElementById('result').innerText = result.message || result.error;
});

document.getElementById('check-balance-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const accountId = document.getElementById('balanceAccountId').value;
    const response = await fetch(`/check-balance?accountId=${accountId}`);
    const result = await response.json();
    document.getElementById('result').innerText = result.balance !== undefined ? `Balance: $${result.balance}` : result.error;
});
