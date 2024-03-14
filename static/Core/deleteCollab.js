function confirmDelete(collabId) {
    let deleteCollabModal = document.getElementById("deleteCollabModal");
    deleteCollabModal.style.display = "flex";

    let deleteBtn = document.getElementById("deleteBtn");
    deleteBtn.style.opacity = "0";
    
    let editBtn = document.getElementById("editBtn");
    editBtn.style.borderTopRightRadius = "10px";
    editBtn.style.borderBottomRightRadius = "10px";

    let cancelDeleteBtn = document.getElementById("cancelDeleteBtn");
    cancelDeleteBtn.addEventListener("click", function() {
        deleteCollabModal.style.display = "none";
        deleteBtn.style.opacity = "1";
        editBtn.style.borderTopRightRadius = "initial";
        editBtn.style.borderBottomRightRadius = "initial";
    });

    window.onclick = function(event) {
        if (event.target == deleteCollabModal) {
            deleteCollabModal.style.display = "none";
        }
    };
}