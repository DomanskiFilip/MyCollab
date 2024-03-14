function clearPreview() {
    for (let i = 0; i < 3; i++) {
        let previews = document.querySelectorAll(`#preview${i}`);
        previews.forEach(preview => {
            preview.innerHTML = '';
        });
    }
    
    let fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(fileInput => {
        fileInput.value = '';
    });
}