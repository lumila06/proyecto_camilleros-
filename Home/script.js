let currentSlide = 0;

function moveSlide(step) {
    const slides = document.querySelectorAll('.banner-image');
    const totalSlides = slides.length;
    currentSlide = (currentSlide + step + totalSlides) % totalSlides;
    const offset = -100 * currentSlide;
    document.querySelector('.banner-carousel').style.transform = `translateX(${offset}%)`;
}

// Optionally, you can set an interval to automatically move the slides
setInterval(() => moveSlide(1), 10000); // Change slide every 5 seconds

