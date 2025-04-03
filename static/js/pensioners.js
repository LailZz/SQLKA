document.addEventListener('DOMContentLoaded', function() {
    // Search functionality
    const searchInput = document.getElementById('search-input');
    const searchBtn = document.getElementById('search-btn');
    const tableRows = document.querySelectorAll('tbody tr');

    if (searchInput && searchBtn) {
        searchBtn.addEventListener('click', function() {
            const searchTerm = searchInput.value.toLowerCase();
            
            tableRows.forEach(row => {
                const cells = row.querySelectorAll('td');
                let matches = false;
                
                cells.forEach(cell => {
                    if (cell.textContent.toLowerCase().includes(searchTerm)) {
                        matches = true;
                    }
                });
                
                if (matches) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });

        searchInput.addEventListener('keyup', function(e) {
            if (e.key === 'Enter') {
                searchBtn.click();
            }
        });
    }

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

                if (!valid) {
                    e.preventDefault();
                    alert('Будь ласка, заповніть всі обов\'язкові поля');
                }
            });
        }
    });
});