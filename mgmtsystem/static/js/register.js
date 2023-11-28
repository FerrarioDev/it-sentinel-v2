const dnarId=document.querySelector('#idField');
const feedbackArea=document.querySelector('.invalid_feedback')
dnarId.addEventListener("keyup", (e) => {
    const dnarIdVal = e.target.value;
    
    dnarId.classList.remove("is-invalid");
    feedbackArea.style.display = 'none';
                
    
    if(dnarIdVal.length > 0) {
        fetch( '/auth/validate=id',{
            body: JSON.stringify({ dnarId: dnarIdVal }),
            method: "POST",
            })
            .then(res =>res.json()
            .then(data => {
                console.log("data", data);
                if (data.dnarid_error){
                    dnarId.classList.add("is-invalid");
                    feedbackArea.style.display = 'block';
                    feedbackArea.innerHTML = `<p>${data.dnarId_error}<p>`;
                }
            })
        );
    }
})
