const carousel = document.getElementById('carousel');
const progressBar = document.querySelector('.progress');
const slides = document.querySelectorAll('.carousel-slide');
const totalSlides = slides.length;
let currentSlide = 0;

function updateCarousel() {
  const slideWidth = slides[0].offsetWidth;
  carousel.style.transform = `translateX(${-slideWidth * currentSlide}px)`;
  progressBar.style.width = `${((currentSlide + 1) / totalSlides) * 100}%`;

  // Update slide indicator text
  const indicator = document.getElementById('slideIndicator');
  indicator.textContent = `Page ${currentSlide + 1} of ${totalSlides}`;
}

document.querySelector('.prev-btn').addEventListener('click', () => {
  currentSlide = Math.max(0, currentSlide - 1);
  updateCarousel();
});

document.querySelector('.next-btn').addEventListener('click', () => {
  currentSlide = Math.min(slides.length - 1, currentSlide + 1);
  updateCarousel();
});

updateCarousel(); // Initialize the view