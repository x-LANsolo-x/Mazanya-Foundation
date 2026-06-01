// Wait for DOM to load
document.addEventListener("DOMContentLoaded", () => {
  
  // 1. Initialize Lenis for Smooth Scrolling
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    direction: 'vertical',
    gestureDirection: 'vertical',
    smooth: true,
    mouseMultiplier: 1,
    smoothTouch: false,
    touchMultiplier: 2,
    infinite: false,
  });

  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);

  // Register GSAP ScrollTrigger
  gsap.registerPlugin(ScrollTrigger);

  // Sync GSAP with Lenis
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add((time)=>{
    lenis.raf(time * 1000);
  });
  gsap.ticker.lagSmoothing(0, 0);

  // 2. Custom Cursor
  const dot = document.querySelector('.cursor-dot');
  const ring = document.querySelector('.cursor-ring');
  
  if (dot && ring) {
    let mouseX = 0, mouseY = 0;
    let ringX = 0, ringY = 0;
    
    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      
      // Dot follows instantly
      gsap.set(dot, { x: mouseX, y: mouseY });
    });
    
    // Ring follows with easing
    gsap.ticker.add(() => {
      ringX += (mouseX - ringX) * 0.15;
      ringY += (mouseY - ringY) * 0.15;
      gsap.set(ring, { x: ringX, y: ringY });
    });

    // Hover effect on links and bento boxes
    const hoverables = document.querySelectorAll('a, button, .bento-box');
    hoverables.forEach(el => {
      el.addEventListener('mouseenter', () => {
        ring.classList.add('hovered');
      });
      el.addEventListener('mouseleave', () => {
        ring.classList.remove('hovered');
      });
    });
  }

  // 3. Hero Animations
  const tl = gsap.timeline();

  // Reveal hero text lines
  tl.fromTo(".hero-line", 
    { y: 150 },
    { y: 0, duration: 1.2, stagger: 0.15, ease: "power4.out", delay: 0.2 }
  );

  // Fade in hero desc
  tl.fromTo(".hero-desc",
    { opacity: 0, y: 30 },
    { opacity: 1, y: 0, duration: 1, ease: "power3.out" },
    "-=0.8"
  );

  // 4. Bento Box Scroll Reveal
  const bentoBoxes = document.querySelectorAll('.bento-box');
  
  bentoBoxes.forEach((box, i) => {
    gsap.fromTo(box, 
      { opacity: 0, y: 100, scale: 0.95 },
      {
        opacity: 1,
        y: 0,
        scale: 1,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: {
          trigger: box,
          start: "top 85%", // when top of box hits 85% of viewport
          toggleActions: "play none none reverse"
        }
      }
    );
  });

});
