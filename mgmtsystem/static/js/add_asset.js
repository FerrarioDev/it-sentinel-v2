document.addEventListener('DOMContentLoaded', function () {
    // Function to show/hide fields based on the selected category
    function toggleFields() {
        var selectedCategory = document.getElementById('id_asset_category').value;
        var computerId = document.getElementById('computer_id');
        var driveSerialnumber = document.getElementById('drive_serialnumber');

        if (selectedCategory === 'Computer') {
            computerId.style.display = 'block';
            driveSerialnumber.style.display = 'block';

        } else {
            computerId.style.display = 'none';
            driveSerialnumber.style.display = 'none';
        }
    }

    // Initial call to toggleFields to set the initial state
    toggleFields();

    // Attach an event listener to the category dropdown to call toggleFields on change
    document.getElementById('id_asset_category').addEventListener('change', function () {
        toggleFields();
    });
});