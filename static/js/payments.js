document.addEventListener('DOMContentLoaded', function() {
    // Delete confirmation for all delete buttons
    const deleteForms = document.querySelectorAll('form.inline-form');
    deleteForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!confirm('Ви впевнені, що хочете видалити цей запис?')) {
                e.preventDefault();
            }
        });
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        if (form.id !== 'filter-form') {
            form.addEventListener('submit', function(e) {
                let valid = true;
                const requiredInputs = form.querySelectorAll('input[required], select[required], textarea[required]');
                
                requiredInputs.forEach(input => {
                    if (!input.value.trim()) {
                        valid = false;
                        input.style.borderColor = 'red';
                    } else {
                        input.style.borderColor = '';
                    }
                });

                // Additional validation for amounts
                const amountInput = form.querySelector('input[name="amount"]');
                if (amountInput && parseFloat(amountInput.value) <= 0) {
                    valid = false;
                    amountInput.style.borderColor = 'red';
                    alert('Сума виплати повинна бути більше нуля');
                }

                if (!valid) {
                    e.preventDefault();
                    if (amountInput && parseFloat(amountInput.value) > 0) {
                        alert('Будь ласка, заповніть всі обов\'язкові поля');
                    }
                }
            });
        }
    });

    // Auto-calculate total amount
    const amountInput = document.querySelector('input[name="amount"]');
    const additionalInput = document.querySelector('input[name="additional_payment"]');
    const totalDisplay = document.createElement('div');
    totalDisplay.className = 'total-amount';
    
    if (amountInput && additionalInput) {
        amountInput.insertAdjacentElement('afterend', totalDisplay);
        
        function calculateTotal() {
            const amount = parseFloat(amountInput.value) || 0;
            const additional = parseFloat(additionalInput.value) || 0;
            const total = amount + additional;
            totalDisplay.textContent = `Загальна сума: ${total.toFixed(2)} грн`;
        }
        
        amountInput.addEventListener('input', calculateTotal);
        additionalInput.addEventListener('input', calculateTotal);
        calculateTotal();
    }
});