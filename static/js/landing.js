window.addEventListener('scroll', () => {
    const moreContent = document.getElementById('more-content');
    const windowHeight = window.innerHeight;
    const elementTop = moreContent.getBoundingClientRect().top;
  
    // Check if the element's top is within the window
    if (elementTop < windowHeight) {
      moreContent.classList.add('visible');
      moreContent.classList.remove('hidden');
    }
  });

  