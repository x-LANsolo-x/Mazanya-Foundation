import os

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MAZANYA Foundation | {TITLE}</title>
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
  <!-- Custom Cursor -->
  <div class="cursor-dot"></div>
  <div class="cursor-ring"></div>

  <!-- Header -->
  <header>
    <a href="index.html" class="nav-logo">
      <img src="assets/mazanya_logo_primary-2.png" alt="Mazanya Logo">
    </a>
    <nav class="nav-links">
      <a href="about.html">About</a>
      <a href="programs.html">Programs</a>
      <a href="volunteer.html">Volunteer</a>
      <a href="research.html">Research</a>
      <a href="survey.html">Survey</a>
      <a href="contact.html">Contact</a>
    </nav>
    <a href="donate.html" class="nav-cta">Donate Now</a>
  </header>

  <!-- Hero Section -->
  <section class="hero container" style="min-height: 50vh; padding-top: 150px; justify-content: flex-start;">
    <h1 class="reveal-text">
      <span class="hero-line">{PAGE_TITLE}</span>
    </h1>
    <p class="hero-desc">{PAGE_DESC}</p>
  </section>

  <!-- CONTENT -->
  {CONTENT}

  <footer style="text-align: center; padding: 4rem; color: var(--ink);">
    <p>&copy; 2026 MAZANYA Foundation. All rights reserved.</p>
  </footer>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <script src="https://unpkg.com/@studio-freight/lenis@1.0.32/dist/lenis.min.js"></script>
  <script src="js/app.js"></script>
</body>
</html>"""

pages = {
    "about.html": {
        "TITLE": "About Us",
        "PAGE_TITLE": "Our <span class='highlight'>Story</span>",
        "PAGE_DESC": "We believe communities thrive when women are empowered, girls are educated, and children receive opportunities to grow and succeed.",
        "CONTENT": """
  <section class="bento-section container">
    <div class="bento-grid">
      <div class="bento-box bento-large bg-indigo">
        <span class="bento-tag">Vision</span>
        <h3 class="bento-title">A Future of Equality</h3>
        <p class="bento-desc">To create a world where every woman and child lives with dignity, opportunity, equality, and hope.</p>
      </div>
      <div class="bento-box bento-wide">
        <span class="bento-tag">Mission</span>
        <h3 class="bento-title" style="font-size: 2rem;">Empower, Educate, Strengthen</h3>
        <p class="bento-desc">To empower women, educate girls, support children, and strengthen communities through education, health, entrepreneurship, leadership development, and social awareness initiatives.</p>
      </div>
      <div class="bento-box">
        <span class="bento-tag" style="color: var(--coral);">Core Value</span>
        <h3 class="bento-title">Compassion</h3>
        <p class="bento-desc">Serving communities with empathy and respect.</p>
      </div>
      <div class="bento-box">
        <span class="bento-tag" style="color: var(--indigo);">Core Value</span>
        <h3 class="bento-title">Integrity</h3>
        <p class="bento-desc">We maintain transparency and accountability.</p>
      </div>
      <div class="bento-box bg-dark">
        <span class="bento-tag">Core Value</span>
        <h3 class="bento-title">Equality</h3>
        <p class="bento-desc">Equal opportunities regardless of background.</p>
      </div>
      <div class="bento-box bg-coral">
        <span class="bento-tag">Core Value</span>
        <h3 class="bento-title">Innovation</h3>
        <p class="bento-desc">Creative solutions for social challenges.</p>
      </div>
    </div>
  </section>
"""
    },
    "programs.html": {
        "TITLE": "Our Programs",
        "PAGE_TITLE": "Our <span class='coral'>Initiatives</span>",
        "PAGE_DESC": "Seven programs. One purpose. Targeted, community-driven initiatives creating sustainable and measurable change.",
        "CONTENT": """
  <section class="bento-section container">
    <div class="bento-grid" style="grid-template-columns: repeat(3, 1fr);">
      <div class="bento-box bg-indigo">
        <span class="bento-tag">Education</span>
        <h3 class="bento-title">Nanaki Jyot</h3>
        <p class="bento-desc">Lighting Every Girl’s Future. Focuses on promoting quality education, digital literacy, mentorship, and learning opportunities for girls from all backgrounds.</p>
      </div>
      <div class="bento-box">
        <span class="bento-tag" style="color: var(--coral);">Leadership</span>
        <h3 class="bento-title">Dhiyaan Di Udaan</h3>
        <p class="bento-desc">Every Daughter Deserves Wings. Dedicated to nurturing leadership, confidence, creativity, and future readiness among young girls.</p>
      </div>
      <div class="bento-box bg-dark">
        <span class="bento-tag">Health</span>
        <h3 class="bento-title">Swasth Nari</h3>
        <p class="bento-desc">Healthy Women. Strong Communities. Promotes awareness regarding women’s physical, mental, reproductive, and nutritional health.</p>
      </div>
      <div class="bento-box bento-wide">
        <span class="bento-tag" style="color: var(--indigo);">Empowerment</span>
        <h3 class="bento-title" style="font-size: 2.5rem;">Project Shakti</h3>
        <p class="bento-desc">Empowered Women Empower Nations. Supports women through skill development, financial literacy, leadership training, and community engagement initiatives.</p>
      </div>
      <div class="bento-box bg-coral">
        <span class="bento-tag">Enterprise</span>
        <h3 class="bento-title">Her Enterprise</h3>
        <p class="bento-desc">From Ideas to Independence. Encourages women entrepreneurship through mentorship, business development support, and market access opportunities.</p>
      </div>
      <div class="bento-box bg-dark">
        <span class="bento-tag">Rights</span>
        <h3 class="bento-title">Nari Samman</h3>
        <p class="bento-desc">Dignity is Every Woman’s Right. Works toward promoting awareness of women’s rights, equality, safety, and social dignity.</p>
      </div>
      <div class="bento-box bento-wide bg-indigo">
        <span class="bento-tag">Child Welfare</span>
        <h3 class="bento-title" style="font-size: 2.5rem;">Project Muskaan</h3>
        <p class="bento-desc">Every Child Matters. Focuses on child welfare, education support, nutrition awareness, and holistic child development.</p>
      </div>
    </div>
  </section>
"""
    },
    "volunteer.html": {
        "TITLE": "Volunteer",
        "PAGE_TITLE": "Become a <span class='highlight'>Founding</span> Volunteer",
        "PAGE_DESC": "Mazanya Foundation is building a network of passionate changemakers committed to creating positive social impact. Whether you are a student, educator, healthcare professional, entrepreneur, researcher, designer, or social worker, your contribution can make a difference.",
        "CONTENT": """
  <section class="bento-section container">
    <div class="bento-grid">
      <div class="bento-box bento-large bg-coral">
        <span class="bento-tag">Join Us</span>
        <h3 class="bento-title">Opportunities</h3>
        <p class="bento-desc">Campus Ambassador, Community Volunteer, Research Volunteer, Content Creator, Graphic Designer, Social Media Volunteer, Fundraising Volunteer, Event Volunteer.</p>
      </div>
      <div class="bento-box">
        <span class="bento-tag" style="color: var(--indigo);">Benefits</span>
        <h3 class="bento-title">Certificate</h3>
        <p class="bento-desc">Certificate of Contribution & Recommendation Letter (Performance Based).</p>
      </div>
      <div class="bento-box bg-dark">
        <span class="bento-tag">Benefits</span>
        <h3 class="bento-title">Network</h3>
        <p class="bento-desc">Leadership Development & Professional Networking.</p>
      </div>
    </div>
  </section>
"""
    },
    "donate.html": {
        "TITLE": "Donate",
        "PAGE_TITLE": "Support <span class='coral'>Change.</span> Empower Futures.",
        "PAGE_DESC": "Your support helps us create opportunities for women, girls, and children. Every contribution helps us move closer to a society where dignity, education, health, and empowerment are accessible to all.",
        "CONTENT": """
  <section class="bento-section container">
    <div class="bento-grid">
      <div class="bento-box bento-large bg-dark">
        <span class="bento-tag">Make an Impact</span>
        <h3 class="bento-title">Why Donate?</h3>
        <p class="bento-desc">• Support Girl Child Education<br>• Support Women Leadership Programs<br>• Support Health Awareness Campaigns<br>• Support Entrepreneurship Development<br>• Support Community Outreach Activities<br>• Support Research and Social Innovation</p>
      </div>
      <div class="bento-box bento-large bg-indigo">
        <span class="bento-tag">Our Promise</span>
        <h3 class="bento-title">Transparency Commitment</h3>
        <p class="bento-desc">Mazanya Foundation is committed to transparency, accountability, and responsible utilization of resources. All donations will be managed ethically and used in alignment with the organization’s mission and objectives.</p>
      </div>
      <div class="bento-box bento-wide">
        <form style="display:flex; flex-direction:column; gap:1.5rem; justify-content:center; height:100%;">
          <input type="number" placeholder="Donation Amount (₹)" style="padding:1.5rem; border-radius:1rem; border:1px solid var(--glass-border); background:rgba(255,255,255,0.8); font-family:var(--font-main); font-size:1.2rem; width:100%;">
          <button class="nav-cta" style="border:none; cursor:pointer; width:100%; text-align:center; padding:1.5rem; background:var(--coral); color:#fff;">Donate Now</button>
        </form>
      </div>
    </div>
  </section>
"""
    },
    "research.html": {
        "TITLE": "Research & Knowledge",
        "PAGE_TITLE": "Knowledge for <span class='highlight'>Social Change</span>",
        "PAGE_DESC": "Mazanya Foundation believes that meaningful social impact must be supported by evidence, research, and community understanding. Through research, surveys, publications, and knowledge sharing, we aim to identify challenges and develop informed solutions.",
        "CONTENT": """
  <section class="bento-section container">
    <div class="bento-grid">
      <div class="bento-box bento-large bg-dark">
        <span class="bento-tag">Areas</span>
        <h3 class="bento-title">Focus Areas</h3>
        <p class="bento-desc">Women Empowerment, Girl Child Education, Health and Nutrition, Child Development, Entrepreneurship, Gender Equality, Rural Development, Community Wellbeing, Social Innovation.</p>
      </div>
      <div class="bento-box bento-wide bg-indigo">
        <span class="bento-tag">Join Us</span>
        <h3 class="bento-title" style="font-size: 2.5rem;">Research Collaborations</h3>
        <p class="bento-desc">Researchers, academicians, students, professionals, and institutions are invited to collaborate with Mazanya Foundation in generating knowledge that drives positive change.</p>
      </div>
    </div>
  </section>
"""
    },
    "survey.html": {
        "TITLE": "Surveys",
        "PAGE_TITLE": "Community <span class='coral'>Insights</span> for Better Impact",
        "PAGE_DESC": "Understanding communities is the first step toward creating sustainable solutions. Mazanya Foundation conducts surveys and assessments to identify challenges, understand needs, and develop effective interventions.",
        "CONTENT": """
  <section class="bento-section container">
    <div class="bento-grid">
      <div class="bento-box bento-large bg-coral">
        <span class="bento-tag">Surveys</span>
        <h3 class="bento-title">Survey Areas</h3>
        <p class="bento-desc">• Women’s Health Survey<br>• Girl Child Education Survey<br>• Women Entrepreneurship Survey<br>• Community Development Survey<br>• Child Wellbeing Survey<br>• Leadership Development Survey</p>
      </div>
      <div class="bento-box bento-wide">
        <span class="bento-tag" style="color: var(--indigo);">Your Voice</span>
        <h3 class="bento-title" style="font-size: 2.5rem;">Participate</h3>
        <p class="bento-desc">Your voice matters. By participating in our surveys, you contribute to building data-driven solutions that support communities and inform future initiatives.</p>
      </div>
    </div>
  </section>
"""
    },
    "contact.html": {
        "TITLE": "Contact",
        "PAGE_TITLE": "Let’s <span class='highlight'>Connect</span>",
        "PAGE_DESC": "We welcome conversations, collaborations, ideas, and opportunities to work together. Whether you are a volunteer, donor, researcher, educational institution, healthcare professional, corporate organization, or community member, we would love to hear from you.",
        "CONTENT": """
  <section class="bento-section container">
    <div class="bento-grid">
      <div class="bento-box bento-tall bg-dark">
        <span class="bento-tag">Reach Out</span>
        <h3 class="bento-title">Contact Info</h3>
        <p class="bento-desc" style="margin-top: 2rem;"><strong>Email</strong><br>info@mazanyafoundation.org</p>
        <p class="bento-desc"><strong>Phone</strong><br>+91 XXXXX XXXXX</p>
        <p class="bento-desc"><strong>Address</strong><br>[Registered Office Address]</p>
        <p class="bento-desc"><strong>Working Hours</strong><br>Monday – Saturday<br>9:00 AM – 6:00 PM</p>
      </div>
      <div class="bento-box bento-large">
        <form style="display:flex; flex-direction:column; gap:1.5rem; justify-content:center; height:100%;">
          <input type="text" placeholder="Your Name" style="padding:1rem; border-radius:1rem; border:1px solid var(--glass-border); background:rgba(255,255,255,0.8); font-family:var(--font-main); font-size:1.1rem; width:100%;">
          <input type="email" placeholder="Your Email" style="padding:1rem; border-radius:1rem; border:1px solid var(--glass-border); background:rgba(255,255,255,0.8); font-family:var(--font-main); font-size:1.1rem; width:100%;">
          <textarea placeholder="Your Message" rows="5" style="padding:1rem; border-radius:1rem; border:1px solid var(--glass-border); background:rgba(255,255,255,0.8); font-family:var(--font-main); font-size:1.1rem; width:100%; resize:none;"></textarea>
          <button class="nav-cta" style="border:none; cursor:pointer; width:100%; text-align:center; padding:1.2rem; background:var(--indigo); color:#fff;">Send Message</button>
        </form>
      </div>
    </div>
  </section>
"""
    }
}

for filename, data in pages.items():
    html_content = TEMPLATE.format(
        TITLE=data["TITLE"],
        PAGE_TITLE=data["PAGE_TITLE"],
        PAGE_DESC=data["PAGE_DESC"],
        CONTENT=data["CONTENT"]
    )
    with open(f"portal-2/{filename}", "w") as f:
        f.write(html_content)
        
print("Generated all pages in portal-2")
