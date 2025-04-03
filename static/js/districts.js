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
        if (form.id !== 'search-form') {
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

                if (!valid) {
                    e.preventDefault();
                    alert('Будь ласка, заповніть всі обов\'язкові поля');
                }
            });
        }
    });

    // Additional JavaScript for districts page
    console.log('Districts page loaded');
});