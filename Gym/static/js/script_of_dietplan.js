const mainImage = document.getElementById('mainImage');
const zoomInButton = document.getElementById('zoomIn');
const zoomOutButton = document.getElementById('zoomOut');
const downloadLink = document.getElementById('downloadLink');
const controls = document.querySelector('.controls');

let currentScale = 1;

zoomInButton.addEventListener('click', () => {
  currentScale += 0.1;
  mainImage.style.transform = `scale(${currentScale})`;
});

zoomOutButton.addEventListener('click', () => {
  if (currentScale > 0.1) {
    currentScale -= 0.1;
    mainImage.style.transform = `scale(${currentScale})`;
  }
});

downloadLink.addEventListener('click', () => {
  downloadLink.href = mainImage.src;
});

// Detect if image overlaps with controls and slide controls down if necessary
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.intersectionRatio < 1) {
      controls.style.bottom = `-${controls.offsetHeight + 20}px`; // Slide controls down
    } else {
      controls.style.bottom = '20px'; // Bring controls back up
    }
  });
});

observer.observe(mainImage);
