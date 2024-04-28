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
    document.querySelectorAll('.carousel-slide').forEach(slide => {
        slide.querySelectorAll('input[type="text"], input[type="radio"]:checked, input[type="range"]').forEach(input => {
            formData.append(input.name, input.value);
        });
    });

    console.log(Array.from(formData.entries())); // Debugging: See what's collected
    alert('Form submitted! Check console for data.'); // Placeholder: Replace with actual submission logic
}

prevBtn.addEventListener('click', () => {
    currentSlide = Math.max(0, currentSlide - 1);
    updateCarousel();
});

updateCarousel(); // Initialize the view
