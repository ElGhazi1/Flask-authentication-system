  // Keep the carousel running when mouse hovers over it
  var carouselElement = document.querySelector('#carouselExampleDark');

  carouselElement.addEventListener('mouseenter', function () {
      // Pause the carousel when mouse enters
      carouselElement.carousel('pause');
  });

  carouselElement.addEventListener('mouseleave', function () {
      // Resume the carousel when mouse leaves
      carouselElement.carousel('cycle');
  });

