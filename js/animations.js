document.addEventListener('DOMContentLoaded', () => {

  // ══════════════════════════════════════
  // 1. HERO PARTICLE CANVAS
  // ══════════════════════════════════════
  const canvas = document.getElementById('heroCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let W, H, particles = [];
    const resize = () => { W = canvas.width = canvas.offsetWidth; H = canvas.height = canvas.offsetHeight; };
    resize(); window.addEventListener('resize', resize);

    class Particle {
      constructor() { this.reset(); }
      reset() {
        this.x = Math.random() * W;
        this.y = Math.random() * H;
        this.size = Math.random() * 2.5 + 0.5;
        this.vx = (Math.random() - 0.5) * 0.4;
        this.vy = (Math.random() - 0.5) * 0.4;
        this.life = Math.random();
        this.maxLife = Math.random() * 0.015 + 0.003;
        this.alpha = 0;
        this.rising = true;
      }
      update() {
        this.x += this.vx; this.y += this.vy;
        if (this.rising) { this.alpha = Math.min(this.alpha + this.maxLife, 0.6); if (this.alpha >= 0.6) this.rising = false; }
        else { this.alpha -= this.maxLife * 0.5; if (this.alpha <= 0) this.reset(); }
        if (this.x < 0 || this.x > W || this.y < 0 || this.y > H) this.reset();
      }
      draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(192,57,108,${this.alpha})`;
        ctx.fill();
      }
    }

    for (let i = 0; i < 80; i++) particles.push(new Particle());

    const animParticles = () => {
      ctx.clearRect(0, 0, W, H);
      // Draw connecting lines between nearby particles
      particles.forEach((p, i) => {
        particles.slice(i + 1).forEach(q => {
          const dx = p.x - q.x, dy = p.y - q.y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < 100) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y);
            ctx.strokeStyle = `rgba(192,57,108,${(1 - dist / 100) * 0.08})`;
            ctx.lineWidth = 0.5;
            ctx.stroke();
          }
        });
        p.update(); p.draw();
      });
      requestAnimationFrame(animParticles);
    };
    animParticles();
  }

  // ══════════════════════════════════════
  // 3. SCROLL REVEAL (Intersection Observer)
  // ══════════════════════════════════════
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('show'); });
  }, { threshold: 0.12 });
  document.querySelectorAll('.anim').forEach(el => io.observe(el));

  // ══════════════════════════════════════
  // 4. MAGNETIC BUTTONS
  // ══════════════════════════════════════
  document.querySelectorAll('.mag').forEach(btn => {
    btn.style.transition = 'transform .4s cubic-bezier(.16,1,.3,1), box-shadow .4s';
    btn.addEventListener('mousemove', e => {
      const r = btn.getBoundingClientRect();
      const x = (e.clientX - r.left - r.width / 2) * 0.38;
      const y = (e.clientY - r.top - r.height / 2) * 0.38;
      btn.style.transform = `translate(${x}px,${y}px)`;
    });
    btn.addEventListener('mouseleave', () => { btn.style.transform = ''; });
  });

  // ══════════════════════════════════════
  // 5. 3D TILT CARDS
  // ══════════════════════════════════════
  document.querySelectorAll('.tilt').forEach(card => {
    card.addEventListener('mousemove', e => {
      const r = card.getBoundingClientRect();
      const x = (e.clientY - r.top - r.height / 2) / (r.height / 2) * -9;
      const y = (e.clientX - r.left - r.width / 2) / (r.width / 2) * 9;
      card.style.transition = 'transform .06s linear, box-shadow .06s linear';
      card.style.transform = `perspective(900px) rotateX(${x}deg) rotateY(${y}deg) scale(1.025)`;
      card.style.boxShadow = '0 22px 55px rgba(18,8,16,.16)';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transition = 'transform .5s cubic-bezier(.16,1,.3,1), box-shadow .5s';
      card.style.transform = '';
      card.style.boxShadow = '';
    });
  });

  // ══════════════════════════════════════
  // 6. BUTTON RIPPLE EFFECT
  // ══════════════════════════════════════
  document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', e => {
      const r = btn.getBoundingClientRect();
      const ripple = document.createElement('span');
      ripple.className = 'ripple';
      const size = Math.max(r.width, r.height) * 2;
      ripple.style.cssText = `width:${size}px;height:${size}px;left:${e.clientX - r.left - size/2}px;top:${e.clientY - r.top - size/2}px`;
      btn.appendChild(ripple);
      setTimeout(() => ripple.remove(), 620);
    });
  });

  // ══════════════════════════════════════
  // 7. COUNTER ANIMATION
  // ══════════════════════════════════════
  const cio = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const el = e.target;
      const target = parseFloat(el.dataset.target);
      const suffix = el.dataset.suffix || '';
      let current = 0;
      const step = target / (1800 / 16);
      const timer = setInterval(() => {
        current = Math.min(current + step, target);
        el.textContent = (Number.isInteger(target) ? Math.floor(current) : current.toFixed(1)) + suffix;
        if (current >= target) clearInterval(timer);
      }, 16);
      cio.unobserve(el);
    });
  }, { threshold: 0.5 });
  document.querySelectorAll('.count-up').forEach(c => cio.observe(c));

  // ══════════════════════════════════════
  // 8. PROGRESS BAR ANIMATION
  // ══════════════════════════════════════
  const pbio = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.querySelector('.prog-bar-fill')?.classList.add('go');
        pbio.unobserve(e.target);
      }
    });
  }, { threshold: 0.5 });
  document.querySelectorAll('.prog-bar-wrap').forEach(w => pbio.observe(w));

  // ══════════════════════════════════════
  // 9. HEADER SCROLL EFFECT
  // ══════════════════════════════════════
  const hdr = document.querySelector('header');
  window.addEventListener('scroll', () => {
    hdr.style.boxShadow = window.scrollY > 60 ? '0 4px 30px rgba(18,8,16,.12)' : '';
  }, { passive: true });

  // ══════════════════════════════════════
  // 10. PARALLAX on scroll (subtle)
  // ══════════════════════════════════════
  const parallaxEls = document.querySelectorAll('.blob');
  window.addEventListener('scroll', () => {
    const sy = window.scrollY;
    parallaxEls.forEach((el, i) => {
      const speed = [0.08, 0.05, 0.12][i] || 0.07;
      el.style.transform = `translateY(${sy * speed}px)`;
    });
  }, { passive: true });

  // ══════════════════════════════════════
  // 11. ORBIT ITEMS — pause on hover
  // ══════════════════════════════════════
  document.querySelectorAll('.orbit-item').forEach(el => {
    el.addEventListener('mouseenter', () => el.style.animationPlayState = 'paused');
    el.addEventListener('mouseleave', () => el.style.animationPlayState = 'running');
  });

});

  // ══════════════════════════════════════
  // 12. SCROLL-DRIVEN CARD CAROUSEL
  // ══════════════════════════════════════
  const scTrack = document.getElementById('scTrack');
  const scRail  = document.getElementById('scRail');
  const scProgressFill  = document.getElementById('scProgress');
  const scLabel = document.getElementById('scLabel');

  if (scTrack && scRail) {
    const CARDS_COUNT = scRail.querySelectorAll('.sc-card').length;
    const CARD_W      = 360 + 32; // card width + gap (2rem)
    const VISIBLE_W   = window.innerWidth - 80; // viewport minus padding
    const MAX_SHIFT   = CARD_W * (CARDS_COUNT - Math.floor(VISIBLE_W / CARD_W));

    window.addEventListener('scroll', () => {
      const rect = scTrack.getBoundingClientRect();
      const trackH = scTrack.offsetHeight;
      const stickyH = window.innerHeight * 0.88; // sc-sticky height

      // How far we've scrolled into the track (0 → 1)
      const rawProgress = -rect.top / (trackH - stickyH);
      const progress = Math.max(0, Math.min(1, rawProgress));

      // Translate the rail
      const shift = progress * MAX_SHIFT;
      scRail.style.transform = `translateX(-${shift}px)`;

      // Update progress bar
      if (scProgressFill) scProgressFill.style.width = (progress * 100) + '%';

      // Update label — which card is "active" (centred in view)
      const activeIdx = Math.min(CARDS_COUNT - 1, Math.floor(progress * CARDS_COUNT));
      if (scLabel) scLabel.textContent = `${activeIdx + 1} / ${CARDS_COUNT}`;

      // Highlight active card
      scRail.querySelectorAll('.sc-card').forEach((c, i) => {
        c.style.opacity = Math.abs(i - activeIdx) <= 1 ? '1' : '0.55';
        c.style.transform = i === activeIdx ? 'scale(1.03) translateY(-8px)' : '';
      });
    }, { passive: true });
  }
