document.addEventListener('DOMContentLoaded', function() {
    const dnarId = document.querySelector('#idField');
    const feedbackArea = document.querySelector('.invalid-feedback');
    const emailField = document.querySelector('#emailField')
    const emailFeedbackArea = document.querySelector('.email-feedback');
    const idSuccessOutput = document.querySelector('.idSuccessOutput');

    emailField.addEventListener('keyup', (e) => {
        const emailVal = e.target.value;
        

        emailField.classList.remove("is-invalid");
        emailFeedbackArea.style.display = 'none';

        if (emailVal.length > 0) {
            fetch('/auth/validate-email', {
                body: JSON.stringify({ email: emailVal }),
                method: "POST",
            })
            .then(res => res.json())
            .then(data => {
                console.log("data", data);
                if (data.email_error) {
                    emailField.classList.add("is-invalid");
                    emailFeedbackArea.style.display = 'block';
                    emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`;
                }
            });
        }
    });

    dnarId.addEventListener("keyup", (e) => {
        const dnarIdVal = e.target.value;
        idSuccessOutput.textContent=`Checking ${dnarIdVal}`;

        dnarId.classList.remove("is-invalid");
        feedbackArea.style.display = 'none';

        if (dnarIdVal.length > 0) {
            fetch('/auth/validate-id', {
                    body: JSON.stringify({ dnarId: dnarIdVal }),
                    method: "POST",
                })
                .then(res => res.json())
                .then(data => {
                    idSuccessOutput.style.display='none'
                    console.log("data", data);
                    if (data.dnarid_error) {
                        dnarId.classList.add("is-invalid");
                        feedbackArea.style.display = 'block';
                        feedbackArea.innerHTML = `<p>${data.dnarid_error}</p>`;
                    }
                }
            );
        }
    });
});
