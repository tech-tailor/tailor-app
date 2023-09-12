console.log(5);
const slider = document.querySelector(".slider-container");
const slides = document.querySelectorAll(".slide");
let currentIndex = 0;

function moveSlider(index) {
    slides.forEach((slide, i) => {
        slide.style.transform = `translateX(${100 * (i - index)}%)`;
    });
}

// Move to the next slide
function nextSlide() {
    console.log(5);
    currentIndex = (currentIndex + 1) % slides.length;
    moveSlider(currentIndex);
}

// Move to the previous slide
function prevSlide() {
    console.log(10);
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    moveSlider(currentIndex);
}

// Handle user interaction (e.g., clicking arrows)
const nextButton = document.querySelector(".next-button");
const prevButton = document.querySelector(".prev-button");

nextButton.addEventListener("click", nextSlide);
prevButton.addEventListener("click", prevSlide);

// Optionally, you can add automatic slide transition using setInterval
// setInterval(nextSlide, 3000); // Auto slide every 3 seconds
