import os

with open("index.html", "r") as f:
    html = f.read()

header_end = html.find("</header>") + 9
footer_start = html.find("<footer>")

header = html[:header_end]
footer = html[footer_start:]

h = header.replace("<title>MAZANYA Foundation | Building a Resilient Future</title>", "<title>About Us - MAZANYA Foundation</title>")
h = h.replace('nav-item active"><a href="index.html"', 'nav-item"><a href="index.html"')
h = h.replace('nav-item"><a href="about.html"', 'nav-item active"><a href="about.html"')

about_content = """
  <!-- Page Hero Details -->
  <section class="page-hero">
    <div class="container">
      <h1>About Us</h1>
      <div class="breadcrumbs">
        <a href="index.html">Home</a> &nbsp;/&nbsp; <span>About Us</span>
      </div>
    </div>
  </section>

  <!-- Our Story Section -->
  <section class="section">
    <div class="container">
      <div class="about-intro-grid">
        <div>
          <span class="handwritten">Our Story</span>
          <h2>A Vision for Empowerment</h2>
          <p>
            <strong>Mazanya Foundation</strong> was established with a simple yet powerful vision—to create a future where every woman, girl, and child can realize their full potential.
          </p>
          <p>
            The foundation was born from the belief that communities thrive when women are empowered, girls are educated, and children receive opportunities to grow and succeed.
          </p>
          <p>
            As a young organization, we are committed to building impactful programs, meaningful partnerships, and sustainable solutions that address social challenges through innovation, collaboration, and compassion.
          </p>
        </div>
        <div>
          <div style="background-color: var(--color-accent-light); padding: 3rem; border-radius: 8px; border: 1px solid var(--color-border); box-shadow: var(--shadow-sm);">
            <h3 style="color: var(--color-primary); border-bottom: 2px solid var(--color-border); padding-bottom: 0.75rem; margin-bottom: 1rem;"><i class="fa-solid fa-bullseye"></i> Vision & Mission</h3>
            <p><strong>Vision:</strong> To create a world where every woman and child lives with dignity, opportunity, equality, and hope.</p>
            <p><strong>Mission:</strong> To empower women, educate girls, support children, and strengthen communities through education, health, entrepreneurship, leadership development, and social awareness initiatives.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Core Values -->
  <section class="section section-bg">
    <div class="container">
      <div class="text-center section-intro">
        <span class="handwritten">What Guides Us</span>
        <h2>Our Core Values</h2>
      </div>

      <div class="grid grid-3">
        <div class="pillar-card text-center">
          <h3>Compassion</h3>
          <p>We believe in serving communities with empathy and respect.</p>
        </div>
        <div class="pillar-card text-center">
          <h3>Integrity</h3>
          <p>We maintain transparency and accountability in everything we do.</p>
        </div>
        <div class="pillar-card text-center">
          <h3>Equality</h3>
          <p>We promote equal opportunities regardless of background.</p>
        </div>
        <div class="pillar-card text-center">
          <h3>Innovation</h3>
          <p>We embrace creative solutions for social challenges.</p>
        </div>
        <div class="pillar-card text-center">
          <h3>Collaboration</h3>
          <p>We believe lasting change is achieved together.</p>
        </div>
        <div class="pillar-card text-center">
          <h3>Sustainability</h3>
          <p>We focus on long-term impact and community empowerment.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Founder Message Section -->
  <section class="section">
    <div class="container">
      <div class="text-center section-intro">
        <span class="handwritten">Founder's Note</span>
        <h2>Message from the Founder</h2>
      </div>
      <div style="max-width: 800px; margin: 0 auto; text-align: center; font-size: 1.1rem; line-height: 1.8;">
        <p><em>"Every great movement begins with a vision. Mazanya Foundation was established with the aspiration of creating opportunities for women, girls, and children to learn, lead, and thrive."</em></p>
        <p>We invite volunteers, institutions, researchers, professionals, and organizations to join us in building a future rooted in dignity, equality, and empowerment. Together, we can transform lives and communities.</p>
        <p class="mt-2"><strong>— Dr. Priya Sharma</strong><br><span style="font-size: 0.9rem; color: var(--color-gray-dark);">Founder, Mazanya Foundation</span></p>
      </div>
    </div>
  </section>
"""

full_html = h + "\n" + about_content + "\n" + footer
with open("about.html", "w") as f:
    f.write(full_html)
print("Updated about.html")
