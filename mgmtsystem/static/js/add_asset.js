document.addEventListener('DOMContentLoaded', function () {
    function toggleFields() {
        var selectedCategory = document.querySelector('#id_asset_category').value;
        var computerId = document.querySelector('#computer_id');
        var driveSerialnumber = document.querySelector('#drive_serialnumber');

        if (selectedCategory === 'Computer') {
            computerId.style.display = 'block';
            driveSerialnumber.style.display = 'block';
        } else {
            computerId.style.display = 'none';
            driveSerialnumber.style.display = 'none';
        }
    }

    toggleFields();

    document.querySelector('#id_asset_category').addEventListener('change', function () {
        toggleFields();
    });
});