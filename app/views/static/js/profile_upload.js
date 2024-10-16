document.addEventListener('DOMContentLoaded', function() {
    var imageUpload = document.getElementById('image-upload');
    var profileImage = document.getElementById('profile-image');
    var uploadProgress = document.getElementById('upload-progress');
    var uploadMessage = document.getElementById('upload-message');

    imageUpload.addEventListener('change', function() {
        var file = this.files[0];
        var reader = new FileReader();

        reader.onload = function(event) {
            profileImage.src = event.target.result;
        };

        reader.readAsDataURL(file);
    });
});
