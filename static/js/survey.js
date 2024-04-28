const carousel = document.getElementById('carousel');
const progressBar = document.querySelector('.progress');
const slides = document.querySelectorAll('.carousel-slide');
const totalSlides = slides.length;
let currentSlide = 0;

const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

function updateCarousel() {
    const slideWidth = slides[0].offsetWidth;
    carousel.style.transform = `translateX(${-slideWidth * currentSlide}px)`;
    progressBar.style.width = `${((currentSlide + 1) / totalSlides) * 100}%`;

    // Update slide indicator text
    const indicator = document.getElementById('slideIndicator');
    indicator.textContent = `Page ${currentSlide + 1} of ${totalSlides}`;

    // Hide 'Previous' button on the first slide and adjust 'Next' button on the last slide
    prevBtn.style.visibility = (currentSlide === 0) ? 'hidden' : 'visible';
    nextBtn.textContent = (currentSlide === slides.length - 1) ? 'Submit' : 'Next';
    nextBtn.onclick = handleNextButtonClick;  // Use a dedicated function for handling the click
}

function handleNextButtonClick() {
    const form = slides[currentSlide].querySelector('form');
    if (form.checkValidity()) {
        if (currentSlide === slides.length - 1) {
            submitForm();
        } else {
            moveToNextSlide();
        }
    } else {
        form.reportValidity();
    }
}

function moveToNextSlide() {
    currentSlide++;
    updateCarousel();
}

function submitForm() {
    const formData = new FormData();
    let weight = null;
    let height = null;
    const results = []; // Array to store the calculated BMI values

    // Collect all input values and store them in FormData
    document.querySelectorAll('.carousel-slide').forEach(slide => {
        slide.querySelectorAll('input[type="text"], input[type="radio"]:checked, input[type="range"]').forEach(input => {
            formData.append(input.name, input.value);
            // Capture weight and height specifically for BMI calculation
            if (input.name === "weight") {
                weight = parseFloat(input.value);
            } else if (input.name === "height") {
                height = parseFloat(input.value);
            }
        });
    });

    // Calculate BMI if weight and height are available and append directly to results array
    if (weight && height) {
        let bmi = weight / ((height / 100) ** 2); // Assumes height is in cm, converts to meters in calculation
        bmi = Math.round(bmi);
        formData.append('BMI', bmi.toFixed(2)); // Append the label 'BMI' and calculated value to the results array
    }

    const jsonObject = {};
    formData.forEach((value, key) => {
        jsonObject[key] = value;
    });

    console.log('Sending:', jsonObject);
    // POST request using fetch API
    fetch('/api/params', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonObject)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        window.location.href = './go-result/user-data/'+data.+'';
    })
    .catch(error => console.error('Error:', error));
}

prevBtn.addEventListener('click', () => {
    currentSlide = Math.max(0, currentSlide - 1);
    updateCarousel();
});

updateCarousel(); // Initialize the view
