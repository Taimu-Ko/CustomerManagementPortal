function deleteCard(cardId) {
    if(confirm("Are you sure you want to delete this card?")) {
        fetch('/cards/delete', {
            method: 'POST',
            body: JSON.stringify({cardId: cardId}),
        }).then((_res) => {
            window.location.href = "/cards";
        });
    }
}

function viewCard(cardId, edit) {
    window.location.href = "/cards/id=" + cardId + '&canEdit=' + edit;
}

function editCard(cardId, edit) {
    window.location.href = "/cards/id=" + cardId + '&canEdit=' + edit;
}

function addCard() {
    window.location.href = "/cards/add";
}

function generateCardNumber() {
    return '6312542452452457636'
}

function generateExpiryDate() {
    return '2026-01-01'
}

function viewInvoice(id) {
    window.location.href = "/invoices/id=" + id;
}

function deleteUser(userId) {
    if(confirm("Are you sure you want to delete this user?")) {
        fetch('/admin/delete', {
            method: 'POST',
            body: JSON.stringify({userId: userId}),
        }).then((_res) => {
            window.location.href = "/admin";
        });
    }   
}

function unlockLockUser(userId) {
    if(confirm("Are you sure you want to unlock/lock this user?")) {
        fetch('/admin/lock', {
            method: 'POST',
            body: JSON.stringify({userId: userId}),
        }).then((_res) => {
            window.location.href = "/admin";
        });
    }     
}