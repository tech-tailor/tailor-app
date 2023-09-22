const smallImages = document.querySelectorAll('.small-image');
const bigImage = document.getElementById('large-image');

smallImages.forEach((smallImage) => {
  smallImage.addEventListener('click', () => {
    // Get the data-src attribute of the clicked small image
    const largeImageSrc = smallImage.getAttribute('data-src');

    // Update the source of the big image with the clicked small image's source
    bigImage.setAttribute('src', largeImageSrc);
  });
});
