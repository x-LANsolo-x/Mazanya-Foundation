import os

with open("index.html", "r") as f:
    html = f.read()

header_end = html.find("</header>") + 9
footer_start = html.find("<footer>")

header = html[:header_end]
footer = html[footer_start:]

h = header.replace("<title>MAZANYA Foundation | Building a Resilient Future</title>", "<title>Our Programs - MAZANYA Foundation</title>")
h = h.replace('nav-item active"><a href="index.html"', 'nav-item"><a href="index.html"')
h = h.replace('nav-item"><a href="programs.html"', 'nav-item active"><a href="programs.html"')

programs_content = """
  <!-- Page Hero Details -->
  <section class="page-hero">
    <div class="container">
      <h1>Our Programs</h1>
      <div class="breadcrumbs">
        <a href="index.html">Home</a> &nbsp;/&nbsp; <span>Our Programs</span>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="text-center section-intro">
        <span class="handwritten">Creating Impact</span>
        <h2 class="accent-title center">Empowering Through Action</h2>
        <p>Our initiatives are designed to address the root causes of social inequality by providing education, healthcare, economic independence, and advocacy.</p>
      </div>

      <div class="grid grid-2">
        <!-- Program 1 -->
        <div class="pillar-card" id="nanaki-jyot">
          <div class="pillar-icon"><i class="fa-solid fa-book-open-reader"></i></div>
          <h3>Nanaki Jyot</h3>
          <h4 style="color: var(--color-primary); margin-bottom: 0.5rem;">Lighting Every Girl’s Future</h4>
          <p>Nanaki Jyot focuses on promoting quality education, digital literacy, mentorship, and learning opportunities for girls from all backgrounds.</p>
        </div>

        <!-- Program 2 -->
        <div class="pillar-card" id="dhiyaan-di-udaan">
          <div class="pillar-icon"><i class="fa-solid fa-dove"></i></div>
          <h3>Dhiyaan Di Udaan</h3>
          <h4 style="color: var(--color-primary); margin-bottom: 0.5rem;">Every Daughter Deserves Wings</h4>
          <p>Dhiyaan Di Udaan is dedicated to nurturing leadership, confidence, creativity, and future readiness among young girls.</p>
        </div>

        <!-- Program 3 -->
        <div class="pillar-card" id="swasth-nari">
          <div class="pillar-icon"><i class="fa-solid fa-heart-pulse"></i></div>
          <h3>Swasth Nari</h3>
          <h4 style="color: var(--color-primary); margin-bottom: 0.5rem;">Healthy Women. Strong Communities.</h4>
          <p>Swasth Nari promotes awareness regarding women’s physical, mental, reproductive, and nutritional health.</p>
        </div>

        <!-- Program 4 -->
        <div class="pillar-card" id="project-shakti">
          <div class="pillar-icon"><i class="fa-solid fa-bolt"></i></div>
          <h3>Project Shakti</h3>
          <h4 style="color: var(--color-primary); margin-bottom: 0.5rem;">Empowered Women Empower Nations</h4>
          <p>Project Shakti supports women through skill development, financial literacy, leadership training, and community engagement initiatives.</p>
        </div>

        <!-- Program 5 -->
        <div class="pillar-card" id="her-enterprise">
          <div class="pillar-icon"><i class="fa-solid fa-briefcase"></i></div>
          <h3>Her Enterprise</h3>
          <h4 style="color: var(--color-primary); margin-bottom: 0.5rem;">From Ideas to Independence</h4>
          <p>Her Enterprise encourages women entrepreneurship through mentorship, business development support, and market access opportunities.</p>
        </div>

        <!-- Program 6 -->
        <div class="pillar-card" id="nari-samman">
          <div class="pillar-icon"><i class="fa-solid fa-scale-balanced"></i></div>
          <h3>Nari Samman</h3>
          <h4 style="color: var(--color-primary); margin-bottom: 0.5rem;">Dignity is Every Woman’s Right</h4>
          <p>Nari Samman works toward promoting awareness of women’s rights, equality, safety, and social dignity.</p>
        </div>

        <!-- Program 7 -->
        <div class="pillar-card" id="project-muskaan" style="grid-column: 1 / -1; max-width: 600px; margin: 0 auto;">
          <div class="pillar-icon"><i class="fa-solid fa-children"></i></div>
          <h3>Project Muskaan</h3>
          <h4 style="color: var(--color-primary); margin-bottom: 0.5rem;">Every Child Matters</h4>
          <p>Project Muskaan focuses on child welfare, education support, nutrition awareness, and holistic child development.</p>
        </div>
      </div>
    </div>
  </section>
"""

full_html = h + "\n" + programs_content + "\n" + footer
with open("programs.html", "w") as f:
    f.write(full_html)
print("Updated programs.html")
