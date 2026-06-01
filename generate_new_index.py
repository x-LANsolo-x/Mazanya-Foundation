import os

# Completely new structural HTML for the index page
new_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Mazanya Foundation is dedicated to empowering women, educating girls, and strengthening communities for a resilient future.">
  <title>MAZANYA Foundation | Empowering Women & Educating Girls</title>
  
  <link rel="icon" type="image/png" href="mazanya_logo_icon-2.png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="css/style.css?v=3">
</head>
<body class="modern-body">

  <!-- Ambient Organic Background -->
  <div class="organic-bg">
    <div class="blob blob-1"></div>
    <div class="blob blob-2"></div>
    <div class="blob blob-3"></div>
  </div>

  <!-- Header Navigation -->
  <header class="glass-header animate-on-scroll fade-down">
    <div class="container nav-container">
      <a href="index.html" class="logo-block">
        <img src="mazanya_logo_icon-2.png" alt="MAZANYA Logo">
        <span class="logo-text">MAZANYA</span>
      </a>
      
      <ul class="nav-menu">
        <li class="nav-item active"><a href="index.html" class="nav-link">Home</a></li>
        <li class="nav-item"><a href="about.html" class="nav-link">About Us</a></li>
        <li class="nav-item"><a href="programs.html" class="nav-link">Programs</a></li>
        <li class="nav-item"><a href="research.html" class="nav-link">Research</a></li>
        <li class="nav-item"><a href="volunteer.html" class="nav-link">Volunteer</a></li>
        <li class="nav-item"><a href="contact.html" class="nav-link">Contact</a></li>
      </ul>
      
      <div class="nav-actions">
        <a href="donate.html" class="btn btn-primary magnetic-btn">Donate Now</a>
      </div>
    </div>
  </header>

  <!-- Dynamic Hero Section -->
  <section class="creative-hero">
    <div class="container">
      <div class="hero-content stagger-group">
        <span class="hero-label animate-on-scroll fade-up">Welcome to Mazanya Foundation</span>
        <h1 class="huge-title animate-on-scroll fade-up">Building a<br><span class="italic-serif text-primary">Resilient</span><br>Future Together.</h1>
        <p class="hero-desc animate-on-scroll fade-up">Empowering Women, Educating Girls, Supporting Children, and Strengthening Communities.</p>
        <div class="hero-actions animate-on-scroll fade-up">
          <a href="about.html" class="btn btn-primary magnetic-btn">Discover Our Vision</a>
          <a href="programs.html" class="btn btn-outline magnetic-btn">Explore Programs</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Marquee -->
  <div class="marquee-section animate-on-scroll fade-in">
    <div class="marquee-content">
      <span>Women Empowerment</span>
      <span class="dot">•</span>
      <span>Girl Child Education</span>
      <span class="dot">•</span>
      <span>Health & Wellness</span>
      <span class="dot">•</span>
      <span>Skill Development</span>
      <span class="dot">•</span>
      <span>Community Strengthening</span>
      <span class="dot">•</span>
      <span>Women Empowerment</span>
      <span class="dot">•</span>
      <span>Girl Child Education</span>
      <span class="dot">•</span>
      <span>Health & Wellness</span>
    </div>
  </div>

  <!-- Bento Box: About Us Preview -->
  <section class="section bento-section">
    <div class="container">
      <div class="bento-grid">
        <div class="bento-box bento-large tilt-card animate-on-scroll slide-in-left">
          <div class="bento-inner">
            <span class="handwritten">Our Mission</span>
            <h2 class="bold-title">Investing in people for meaningful social change.</h2>
            <p>We work to create opportunities for women to lead, girls to learn, and children to thrive in a safe and supportive environment.</p>
            <a href="about.html" class="link-arrow mt-1">Read Our Story <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
        
        <div class="bento-box bento-small bento-accent tilt-card animate-on-scroll slide-in-right delay-1">
          <div class="bento-inner center-content">
            <i class="fa-solid fa-book-open-reader huge-icon"></i>
            <h3>Education</h3>
          </div>
        </div>
        
        <div class="bento-box bento-small bento-dark tilt-card animate-on-scroll slide-in-right delay-2">
          <div class="bento-inner center-content">
            <i class="fa-solid fa-briefcase huge-icon"></i>
            <h3>Independence</h3>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Our Initiatives: Asymmetrical Grid -->
  <section class="section programs-creative">
    <div class="container">
      <div class="section-header animate-on-scroll fade-up">
        <h2 class="huge-title-small">Our Initiatives</h2>
        <p>Targeted programs driving real impact across communities.</p>
      </div>

      <div class="asym-grid">
        <!-- Program 1 -->
        <a href="programs.html#nanaki-jyot" class="asym-card card-tall tilt-card animate-on-scroll fade-up">
          <div class="card-bg"></div>
          <div class="card-content">
            <div class="icon-wrap"><i class="fa-solid fa-graduation-cap"></i></div>
            <h3>Nanaki Jyot</h3>
            <p>Promoting quality education and digital literacy for girls.</p>
          </div>
        </a>

        <!-- Program 2 -->
        <a href="programs.html#swasth-nari" class="asym-card card-wide tilt-card animate-on-scroll fade-up delay-1">
          <div class="card-bg bg-accent"></div>
          <div class="card-content">
            <div class="icon-wrap"><i class="fa-solid fa-heart-pulse"></i></div>
            <h3>Swasth Nari</h3>
            <p>Advancing women's health, wellness, and nutritional awareness.</p>
          </div>
        </a>

        <!-- Program 3 -->
        <a href="programs.html#her-enterprise" class="asym-card card-wide tilt-card animate-on-scroll fade-up delay-2">
          <div class="card-bg bg-dark"></div>
          <div class="card-content">
            <div class="icon-wrap"><i class="fa-solid fa-chart-line"></i></div>
            <h3>Her Enterprise</h3>
            <p>Empowering women entrepreneurs with mentorship and skills.</p>
          </div>
        </a>
      </div>
      
      <div class="text-center mt-2 animate-on-scroll fade-up">
        <a href="programs.html" class="btn btn-primary magnetic-btn">View All 7 Programs</a>
      </div>
    </div>
  </section>

  <!-- CTA Section -->
  <section class="section creative-cta">
    <div class="container">
      <div class="cta-box tilt-card animate-on-scroll fade-up">
        <h2 class="huge-title-small text-white">Be the Catalyst for Change</h2>
        <p class="text-white-dim">Join us as a volunteer, partner, or donor to build a future rooted in dignity and equality.</p>
        <div class="cta-buttons">
          <a href="volunteer.html" class="btn btn-secondary magnetic-btn">Become a Volunteer</a>
          <a href="donate.html" class="btn btn-primary magnetic-btn">Make a Donation</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="creative-footer">
    <div class="container">
      <div class="footer-top">
        <div class="brand">
          <h2>MAZANYA</h2>
          <p>Empowering Women. Educating Girls.</p>
        </div>
        <div class="socials">
          <a href="#" class="social-link"><i class="fa-brands fa-linkedin-in"></i></a>
          <a href="#" class="social-link"><i class="fa-brands fa-twitter"></i></a>
          <a href="#" class="social-link"><i class="fa-brands fa-instagram"></i></a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Mazanya Foundation. All rights reserved.</p>
        <div class="legal-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="js/animations.js"></script>
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(new_html)

print("Successfully replaced index.html with the new creative layout.")
