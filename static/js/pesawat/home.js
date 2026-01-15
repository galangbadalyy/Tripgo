// Show/hide return date
document.querySelectorAll('input[name="trip_type"]').forEach(radio => {
    radio.addEventListener('change', (e) => {
        const returnField = document.getElementById('return-date-field');
        if (e.target.value === 'round-trip') {
            returnField.classList.remove('hidden');
        } else {
            returnField.classList.add('hidden');
        }
    });
});

// Swap location
document.querySelector('.swap-btn').addEventListener('click', (e) => {
    e.preventDefault();
    const from = document.querySelector('input[name="asal"]');
    const to = document.querySelector('input[name="tujuan"]');
    const temp = from.value;
    from.value = to.value;
    to.value = temp;
});