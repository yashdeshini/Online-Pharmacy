document.addEventListener('DOMContentLoaded', function () {
    const cartTable = document.querySelector('.cart-table');
    cartTable.addEventListener('change', function (event) {
        if (event.target.classList.contains('quantity-select')) {
            const row = event.target.closest('tr');
            const price = parseFloat(event.target.dataset.price);
            const quantity = parseInt(event.target.value, 10);
            const total = price * quantity;
            row.querySelector('.total-price').textContent = `$${total.toFixed(2)}`;
            updateSummary();
        }
    });

    cartTable.addEventListener('click', function (event) {
        if (event.target.classList.contains('remove')) {
            const row = event.target.closest('tr');
            const itemId = row.dataset.itemId;
            removeItem(itemId);
            row.remove();
            updateSummary();
        }
    });

    function updateSummary() {
        let totalItems = 0;
        let totalPrice = 0;
        document.querySelectorAll('.quantity-select').forEach(selectElement => {
            const quantity = parseInt(selectElement.value, 10);
            totalItems += quantity;
            const row = selectElement.closest('tr');
            const total = parseFloat(row.querySelector('.total-price').textContent);
            totalPrice += total;
        });
        document.getElementById('total-items').textContent = totalItems;
        document.getElementById('total-price').textContent = `$${totalPrice.toFixed(2)}`;
    }

    function removeItem(itemId) {
        console.log('Remove item:', itemId);
        // Add AJAX or form submission logic here to handle item removal on the server.
    }

    updateSummary(); // Initial cart summary update.
});
