import os

css_additions = """
/* =========================================
   COMPLETE REDESIGN & ANIMATIONS (V3)
   ========================================= */

/* Organic Background */
.modern-body {
  position: relative;
  background-color: var(--color-bg);
  overflow-x: hidden;
}

.organic-bg {
  position: fixed;
  top: 0; left: 0; width: 100vw; height: 100vh;
  z-index: -2;
  pointer-events: none;
  overflow: hidden;
  background: var(--color-bg);
}

.blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.4;
  animation: float 20s infinite alternate ease-in-out;
}

.blob-1 {
  top: -10%; left: -10%;
  width: 50vw; height: 50vw;
  background-color: rgba(192, 57, 108, 0.3);
}

.blob-2 {
  bottom: -20%; right: -10%;
  width: 60vw; height: 60vw;
  background-color: rgba(92, 16, 51, 0.2);
  animation-delay: -5s;
}

.blob-3 {
  top: 40%; left: 60%;
  width: 40vw; height: 40vw;
  background-color: rgba(212, 82, 122, 0.2);
  animation-duration: 25s;
}

@keyframes float {
  0% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(-5%, 5%) scale(1.1); }
  100% { transform: translate(5%, -5%) scale(0.9); }
}

/* Glass Header overrides */
.glass-header {
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255,255,255,0.4);
}

/* Typography Overrides */
.huge-title {
  font-family: var(--font-heading);
  font-size: 5.5rem;
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.03em;
  color: var(--color-dark);
  margin-bottom: 1.5rem;
}

.huge-title-small {
  font-family: var(--font-heading);
  font-size: 3.5rem;
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 1rem;
}

.text-primary { color: var(--color-primary); }
.italic-serif { font-style: italic; font-weight: 400; }

/* Creative Hero Section */
.creative-hero {
  min-height: 90vh;
  display: flex;
  align-items: center;
  position: relative;
  z-index: 1;
}

.hero-content {
  max-width: 900px;
}

.hero-label {
  display: inline-block;
  padding: 0.5rem 1.5rem;
  background: rgba(192, 57, 108, 0.1);
  color: var(--color-primary);
  border-radius: 50px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 0.85rem;
  margin-bottom: 2rem;
}

.hero-desc {
  font-size: 1.5rem;
  color: var(--color-grey-dark);
  max-width: 700px;
  margin-bottom: 3rem;
}

.hero-actions {
  display: flex;
  gap: 1.5rem;
}

/* Infinite Marquee */
.marquee-section {
  background: var(--color-dark);
  color: var(--color-white);
  padding: 1.5rem 0;
  overflow: hidden;
  position: relative;
  z-index: 2;
  transform: rotate(-2deg) scale(1.05); /* Slight tilt for creativity */
  margin: 4rem 0;
}

.marquee-content {
  display: flex;
  white-space: nowrap;
  animation: marquee 20s linear infinite;
  font-family: var(--font-heading);
  font-size: 2rem;
  font-weight: 600;
  font-style: italic;
}

.marquee-content span { margin: 0 2rem; }
.marquee-content .dot { color: var(--color-primary); }

@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* Bento Box Layout */
.bento-section { z-index: 2; position: relative; }

.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(2, 250px);
  gap: 1.5rem;
}

.bento-box {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(15px);
  border-radius: 24px;
  border: 1px solid rgba(255,255,255,0.8);
  box-shadow: var(--shadow-soft);
  position: relative;
  overflow: hidden;
  padding: 3rem;
}

.bento-large {
  grid-column: 1 / 3;
  grid-row: 1 / 3;
}

.bento-small {
  grid-column: 3 / 4;
}

.bento-accent { background: var(--color-primary); color: white; }
.bento-dark { background: var(--color-dark); color: white; }

.bento-inner {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.center-content { align-items: center; text-align: center; }

.huge-icon {
  font-size: 4rem;
  margin-bottom: 1.5rem;
}

/* Asymmetrical Grid for Programs */
.asym-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 2rem;
  margin-top: 4rem;
}

.asym-card {
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  padding: 3rem;
  color: var(--color-dark);
  text-decoration: none;
  background: rgba(255,255,255,0.5);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.7);
}

.asym-card:hover { color: var(--color-dark); }

.card-tall {
  grid-column: 1 / 6;
  min-height: 400px;
}

.card-wide {
  grid-column: 6 / 13;
  min-height: 250px;
}

.card-content { position: relative; z-index: 2; }
.card-content h3 { font-size: 2rem; margin-top: 1.5rem; }

/* CTA Block */
.creative-cta .cta-box {
  background: var(--color-dark);
  border-radius: 30px;
  padding: 5rem;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.creative-cta .cta-box::before {
  content: '';
  position: absolute;
  top: -50%; left: -50%; width: 200%; height: 200%;
  background: radial-gradient(circle, rgba(192,57,108,0.2) 0%, transparent 60%);
}

.text-white { color: white; }
.text-white-dim { color: rgba(255,255,255,0.7); font-size: 1.25rem; max-width: 600px; margin: 0 auto 3rem auto; }

.cta-buttons { display: flex; justify-content: center; gap: 1.5rem; }

/* Scroll Animations */
.animate-on-scroll {
  opacity: 0;
  transition: opacity 1s cubic-bezier(0.16, 1, 0.3, 1), transform 1s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}

.fade-up { transform: translateY(40px); }
.fade-down { transform: translateY(-40px); }
.fade-in { transform: scale(0.95); }
.slide-in-left { transform: translateX(-60px); }
.slide-in-right { transform: translateX(60px); }

.is-visible {
  opacity: 1;
  transform: translate(0) scale(1) !important;
}

/* Stagger Delays */
.delay-1 { transition-delay: 0.15s; }
.delay-2 { transition-delay: 0.3s; }
.delay-3 { transition-delay: 0.45s; }

.stagger-group .animate-on-scroll:nth-child(1) { transition-delay: 0.1s; }
.stagger-group .animate-on-scroll:nth-child(2) { transition-delay: 0.2s; }
.stagger-group .animate-on-scroll:nth-child(3) { transition-delay: 0.3s; }
.stagger-group .animate-on-scroll:nth-child(4) { transition-delay: 0.4s; }
"""

with open("css/style.css", "a") as f:
    f.write(css_additions)
print("Successfully appended CSS additions to style.css")
