import * as bootstrap from "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js";
window.bootstrap = bootstrap;  

/*Declare constants for comment function*/
const editButtons = document.getElementsByClassName("edit-button");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

/*Declare constants for delete function*/
const deleteModal = window.$('#deleteModal').modal();
const deleteButtons = document.getElementsByClassName("delete-button");
const closeModal = document.getElementById('closeModal');
const deleteConfirm = document.getElementById("deleteConfirm");


/*Function to allow editing of comments*/
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

/*Function for allowing deletion of comments*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}