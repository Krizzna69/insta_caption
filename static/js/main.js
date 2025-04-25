document.addEventListener('DOMContentLoaded', function() {
    // Image preview
    const imageUpload = document.getElementById('imageUpload');
    const preview = document.getElementById('preview');
    const imagePreview = document.getElementById('imagePreview');
    
    imageUpload.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                preview.src = e.target.result;
                imagePreview.classList.remove('d-none');
            }
            reader.readAsDataURL(file);
        }
    });
    
    // Form submission
    const uploadForm = document.getElementById('uploadForm');
    const generateBtn = document.getElementById('generateBtn');
    const resultsSection = document.getElementById('resultsSection');
    const generatedCaption = document.getElementById('generatedCaption');
    const generatedHashtags = document.getElementById('generatedHashtags');
    
    uploadForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (!imageUpload.files[0]) {
            alert('Please select an image to upload.');
            return;
        }
        
        const formData = new FormData(uploadForm);
        generateBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Generating...';
        generateBtn.disabled = true;
        
        fetch('/generate', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            generatedCaption.textContent = data.caption;
            generatedHashtags.textContent = data.hashtags;
            resultsSection.classList.remove('d-none');
            
            // Scroll to results
            resultsSection.scrollIntoView({ behavior: 'smooth' });
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error generating caption. Please try again.');
        })
        .finally(() => {
            generateBtn.innerHTML = 'Generate Caption';
            generateBtn.disabled = false;
        });
    });
});

// Copy to clipboard function
function copyToClipboard(elementId) {
    const element = document.getElementById(elementId);
    const text = element.textContent;
    
    navigator.clipboard.writeText(text).then(() => {
        // Create temporary element to show "Copied!" message
        const tempBtn = document.createElement('span');
        tempBtn.textContent = ' ✓ Copied!';
        tempBtn.classList.add('text-success', 'ms-2');
        
        // Add it after the button
        const btn = document.activeElement;
        btn.parentNode.insertBefore(tempBtn, btn.nextSibling);
        
        // Remove after 2 seconds
        setTimeout(() => {
            tempBtn.remove();
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
}