var swiper = new Swiper(".swiperImg", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    loop:true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 150,
      modifier: 2.5,
      slideShadows: true,
    },
    breakpoints: {
      // when window width is >= 760px
      760: {
        // slidesPerView: 2,
        // spaceBetween: 20
      },
      // when window width is >= 1050px
      1050: {
        // slidesPerView: 3,
        // spaceBetween: 30
      }
    }
    
  });


var swiper2 = new Swiper(".swiperCubic", {
  effect: "cube",
  grabCursor: true,
  cubeEffect: {
    shadow: true,
    slideShadows: true,
    shadowOffset: 20,
    shadowScale: 0.94,
  },
  pagination: {
    el: ".swiper-pagination",
  },
  breakpoints: {
    // when window width is >= 760px
    760: {
      // slidesPerView: 2,
      // spaceBetween: 20
    },
    // when window width is >= 1050px
    1050: {
      // slidesPerView: 3,
      // spaceBetween: 30
    }
  }
});

var swiper2b = new Swiper(".swiperCubic2", {
  effect: "cube",
  grabCursor: true,
  cubeEffect: {
    shadow: true,
    slideShadows: true,
    shadowOffset: 20,
    shadowScale: 0.94,
  },
  pagination: {
    el: ".swiper-pagination",
  },
  breakpoints: {
    // when window width is >= 760px
    760: {
      // slidesPerView: 2,
      // spaceBetween: 20
    },
    // when window width is >= 1050px
    1050: {
      // slidesPerView: 3,
      // spaceBetween: 30
    }
  }
});

var swiper3 = new Swiper(".swiperReview", {
  // parallax: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  loop:true,
  autoplay:{
  
    delay:3000,
    disableOnInteraction:false,
  }
});
