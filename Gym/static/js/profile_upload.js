// Profile Picture Upload JavaScript
function uploadProfilePicture(userId) {
    const fileInput = document.getElementById('profile-image-input');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select an image file first.');
        return;
    }
    
    // Validate file type
    const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/webp'];
    if (!allowedTypes.includes(file.type)) {
        alert('Invalid file type. Please upload JPEG, PNG, GIF, or WebP images.');
        return;
    }
    
    // Validate file size (5MB limit)
    if (file.size > 5 * 1024 * 1024) {
        alert('File too large. Please upload images smaller than 5MB.');
        return;
    }
    
    // Create FormData object
    const formData = new FormData();
    formData.append('image', file);
    formData.append('user_id', userId);
    
    // Show loading indicator
    const uploadBtn = document.getElementById('upload-btn');
    const originalText = uploadBtn.textContent;
    uploadBtn.textContent = 'Uploading...';
    uploadBtn.disabled = true;
    
    // Make AJAX request
    fetch('/upload_profile_image/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update the profile image on the page
            const profileImg = document.getElementById('profile-image');
            if (profileImg) {
                profileImg.src = data.image_url + '?t=' + new Date().getTime(); // Add timestamp to prevent caching
            }
            alert(data.message || 'Profile picture updated successfully!');
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while uploading the image.');
    })
    .finally(() => {
        // Reset button
        uploadBtn.textContent = originalText;
        uploadBtn.disabled = false;
        // Clear file input
        fileInput.value = '';
    });
}

// Preview image before upload
function previewImage(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const preview = document.getElementById('image-preview');
            if (preview) {
                preview.src = e.target.result;
                preview.style.display = 'block';
            }
        };
        reader.readAsDataURL(input.files[0]);
    }
}

// Initialize event listeners when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('profile-image-input');
    if (fileInput) {
        fileInput.addEventListener('change', function() {
            previewImage(this);
        });
    }
});
