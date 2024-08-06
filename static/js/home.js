// Function to show popup
document.getElementById('add_data').addEventListener('click', function() {
    document.getElementById('myPopup').style.display = 'block';
});

// Function to hide popup when close button is clicked
document.getElementById('closePopup').addEventListener('click', function() {
    document.getElementById('myPopup').style.display = 'none';
});

// Function to hide popup when clicking outside the popup
window.addEventListener('click', function(event) {
    if (event.target == document.getElementById('myPopup')) {
        document.getElementById('myPopup').style.display = 'none';
    }
});

// Function to validate Aadhaar number
function validateAadhar(aadharNumber) {
    const aadharRegex = /^\d{12}$/; // Regex for exactly 12 digits
    return aadharRegex.test(aadharNumber);
}

// Function to validate Mobile number
function validateMobile(mobileNumber) {
    const mobileRegex = /^\d{10}$/; // Regex for exactly 10 digits
    return mobileRegex.test(mobileNumber);
}

// For animated text
document.addEventListener("DOMContentLoaded", function() {
    const textElement = document.getElementById('text');
    const text = textElement.textContent;
    textElement.textContent = ''; 

    let index = 0;
    const speed = 80; 

    function type() {
        if (index < text.length) {
            textElement.textContent += text.charAt(index);
            index++;
            setTimeout(type, speed);
        } else {
            setTimeout(erase, speed * 2); 
        }
    }

    function erase() {
        if (index > 0) {
            textElement.textContent = text.substring(0, index - 1);
            index--;
            setTimeout(erase, speed);
        } else {
            setTimeout(type, speed); 
        }
    }

    type(); 
});

// Login Popup

