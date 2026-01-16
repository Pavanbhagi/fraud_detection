// DOM Elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');
const previewImage = document.getElementById('previewImage');
const removeImageBtn = document.getElementById('removeImage');
const detectBtn = document.getElementById('detectBtn');
const resultsSection = document.getElementById('resultsSection');
const resultsContainer = document.getElementById('resultsContainer');
const resultsCount = document.getElementById('resultsCount');
const toast = document.getElementById('toast');
const toastMessage = document.getElementById('toastMessage');

let selectedFile = null;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
    checkHealth();
});

// Setup Event Listeners
function setupEventListeners() {
    // Upload area click
    uploadArea.addEventListener('click', () => fileInput.click());
    
    // File input change
    fileInput.addEventListener('change', handleFileSelect);
    
    // Drag and drop
    uploadArea.addEventListener('dragover', handleDragOver);
    uploadArea.addEventListener('dragleave', handleDragLeave);
    uploadArea.addEventListener('drop', handleDrop);
    
    // Remove image
    removeImageBtn.addEventListener('click', removeImage);
    
    // Detect button
    detectBtn.addEventListener('click', detectCard);
}

// Check API Health
async function checkHealth() {
    try {
        const response = await fetch('/health');
        const data = await response.json();
        if (data.status === 'healthy') {
            console.log('API is healthy');
        }
    } catch (error) {
        console.error('Health check failed:', error);
        showToast('API connection failed', 'error');
    }
}

// Handle File Select
function handleFileSelect(e) {
    const file = e.target.files[0];
    if (file) {
        processFile(file);
    }
}

// Handle Drag Over
function handleDragOver(e) {
    e.preventDefault();
    e.stopPropagation();
    uploadArea.classList.add('dragover');
}

// Handle Drag Leave
function handleDragLeave(e) {
    e.preventDefault();
    e.stopPropagation();
    uploadArea.classList.remove('dragover');
}

// Handle Drop
function handleDrop(e) {
    e.preventDefault();
    e.stopPropagation();
    uploadArea.classList.remove('dragover');
    
    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
        processFile(file);
    } else {
        showToast('Please upload an image file', 'error');
    }
}

// Process File
function processFile(file) {
    // Validate file size (16MB max)
    if (file.size > 16 * 1024 * 1024) {
        showToast('File size must be less than 16MB', 'error');
        return;
    }
    
    // Validate file type
    if (!file.type.startsWith('image/')) {
        showToast('Please upload an image file', 'error');
        return;
    }
    
    selectedFile = file;
    
    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        imagePreview.style.display = 'block';
        detectBtn.disabled = false;
    };
    reader.readAsDataURL(file);
}

// Remove Image
function removeImage() {
    selectedFile = null;
    fileInput.value = '';
    imagePreview.style.display = 'none';
    detectBtn.disabled = true;
    hideResults();
}

// Detect Card
async function detectCard() {
    if (!selectedFile) {
        showToast('Please select an image first', 'warning');
        return;
    }
    
    // Show loading state
    detectBtn.classList.add('loading');
    detectBtn.disabled = true;
    hideResults();
    
    try {
        // Create form data
        const formData = new FormData();
        formData.append('file', selectedFile);
        
        // Send request
        const response = await fetch('/detect', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Detection failed');
        }
        
        const data = await response.json();
        displayResults(data);
        showToast(`Successfully detected ${data.num_cards_detected} card(s)`, 'success');
        
    } catch (error) {
        console.error('Detection error:', error);
        showToast(error.message || 'Failed to detect credit card', 'error');
    } finally {
        detectBtn.classList.remove('loading');
        detectBtn.disabled = false;
    }
}

// Display Results
function displayResults(data) {
    resultsContainer.innerHTML = '';
    
    if (data.num_cards_detected === 0) {
        resultsContainer.innerHTML = `
            <div class="card-result">
                <div class="card-header">
                    <div class="card-title">No Cards Detected</div>
                </div>
                <div class="card-info">
                    <div class="info-item">
                        <div class="info-label">Message</div>
                        <div class="info-value">No credit cards were found in the image. Please try a different image with better lighting and focus.</div>
                    </div>
                </div>
            </div>
        `;
    } else {
        data.cards.forEach((card, index) => {
            const cardElement = createCardElement(card, index + 1);
            resultsContainer.appendChild(cardElement);
        });
    }
    
    resultsCount.textContent = `${data.num_cards_detected} card(s) detected`;
    resultsSection.style.display = 'block';
    
    // Smooth scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Create Card Element
function createCardElement(card, index) {
    const cardDiv = document.createElement('div');
    cardDiv.className = 'card-result';
    
    // Format card number
    const cardNumber = card.card_number 
        ? formatCardNumber(card.card_number) 
        : '<span class="not-found">Not found</span>';
    
    // Validation badge
    const validationBadge = card.card_number
        ? `<span class="card-badge ${card.is_valid ? 'badge-valid' : 'badge-invalid'}">
            ${card.is_valid ? '✓ Valid' : '✗ Invalid'}
           </span>`
        : '';
    
    // Confidence badge
    const confidenceBadge = card.detection_confidence
        ? `<span class="card-badge badge-confidence">
            ${Math.round(card.detection_confidence * 100)}% Confidence
           </span>`
        : '';
    
    cardDiv.innerHTML = `
        <div class="card-header">
            <div class="card-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20 4H4C2.89 4 2.01 4.89 2.01 6L2 18C2 19.11 2.89 20 4 20H20C21.11 20 22 19.11 22 18V6C22 4.89 21.11 4 20 4ZM20 18H4V12H20V18ZM20 8H4V6H20V8Z" fill="currentColor"/>
                </svg>
                Card ${index}
            </div>
            <div style="display: flex; gap: 0.5rem;">
                ${validationBadge}
                ${confidenceBadge}
            </div>
        </div>
        <div class="card-info">
            <div class="info-item">
                <div class="info-label">Card Number</div>
                <div class="info-value card-number">${cardNumber}</div>
            </div>
            <div class="info-item">
                <div class="info-label">Cardholder Name</div>
                <div class="info-value">${card.cardholder_name || '<span class="not-found">Not found</span>'}</div>
            </div>
            <div class="info-item">
                <div class="info-label">Expiry Date</div>
                <div class="info-value">${card.expiry_date || '<span class="not-found">Not found</span>'}</div>
            </div>
            <div class="info-item">
                <div class="info-label">Detection Confidence</div>
                <div class="info-value">${card.detection_confidence ? Math.round(card.detection_confidence * 100) + '%' : 'N/A'}</div>
            </div>
            <div class="info-item">
                <div class="info-label">Bounding Box</div>
                <div class="bbox-info">
                    <span>X: ${card.bbox[0]}</span>
                    <span>Y: ${card.bbox[1]}</span>
                    <span>Width: ${card.bbox[2] - card.bbox[0]}</span>
                    <span>Height: ${card.bbox[3] - card.bbox[1]}</span>
                </div>
            </div>
            ${card.all_text && card.all_text.length > 0 ? `
            <div class="info-item">
                <div class="info-label">All Detected Text</div>
                <div class="info-value" style="font-size: 0.9rem; line-height: 1.8;">
                    ${card.all_text.map(text => 
                        `<div style="margin-bottom: 0.25rem;">
                            "${text.text}" <span style="color: var(--text-muted); font-size: 0.8rem;">(${Math.round(text.confidence * 100)}%)</span>
                        </div>`
                    ).join('')}
                </div>
            </div>
            ` : ''}
        </div>
    `;
    
    return cardDiv;
}

// Format Card Number
function formatCardNumber(number) {
    // Add spaces every 4 digits
    return number.replace(/(\d{4})(?=\d)/g, '$1 ');
}

// Hide Results
function hideResults() {
    resultsSection.style.display = 'none';
    resultsContainer.innerHTML = '';
}

// Show Toast
function showToast(message, type = 'success') {
    toastMessage.textContent = message;
    toast.className = `toast ${type} show`;
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Prevent default drag behaviors on window
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    window.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
    });
});
