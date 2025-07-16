let currentTheme = "dark";

function createStars() {
  const starsContainer = document.getElementById("stars");
  const numStars = 100;

  for (let i = 0; i < numStars; i++) {
    const star = document.createElement("div");
    star.className = "star";
    star.style.left = Math.random() * 100 + "%";
    star.style.top = Math.random() * 100 + "%";
    star.style.animationDelay = Math.random() * 3 + "s";
    star.style.animationDuration = Math.random() * 2 + 3 + "s";
    starsContainer.appendChild(star);
  }
}

function createParticles() {
  const particlesContainer = document.getElementById("particles");
  const numParticles = 50;

  for (let i = 0; i < numParticles; i++) {
    const particle = document.createElement("div");
    particle.className = "particle";
    particle.style.left = Math.random() * 100 + "%";
    particle.style.animationDelay = Math.random() * 15 + "s";
    particle.style.animationDuration = Math.random() * 10 + 15 + "s";

    const colors =
      currentTheme === "light"
        ? ["#2563eb", "#7c3aed", "#3b82f6", "#1e293b"]
        : ["#4a9eff", "#8b5cf6", "#60a5fa", "#ffffff"];

    const color = colors[Math.floor(Math.random() * colors.length)];
    particle.style.background = color;
    particle.style.boxShadow = `0 0 10px ${color}`;

    particlesContainer.appendChild(particle);
  }
}

function updateParticleColors() {
  const particles = document.querySelectorAll(".particle");
  const colors =
    currentTheme === "light"
      ? ["#2563eb", "#7c3aed", "#3b82f6", "#1e293b"]
      : ["#4a9eff", "#8b5cf6", "#60a5fa", "#ffffff"];

  particles.forEach((particle) => {
    const color = colors[Math.floor(Math.random() * colors.length)];
    particle.style.background = color;
    particle.style.boxShadow = `0 0 10px ${color}`;
  });
}

function detectSystemTheme() {
  if (
    window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches
  ) {
    return "dark";
  }
  return "light";
}

function initializeTheme() {
  const systemTheme = detectSystemTheme();
  currentTheme = systemTheme;
  const body = document.body;
  const themeToggle = document.getElementById("themeToggle");

  if (systemTheme === "light") {
    body.setAttribute("data-theme", "light");
    themeToggle.checked = true;
  } else {
    body.removeAttribute("data-theme");
    themeToggle.checked = false;
  }
}

createStars();
createParticles();
initializeTheme();

const themeToggle = document.getElementById("themeToggle");
const body = document.body;

themeToggle.addEventListener("change", function () {
  if (this.checked) {
    body.setAttribute("data-theme", "light");
    currentTheme = "light";
  } else {
    body.removeAttribute("data-theme");
    currentTheme = "dark";
  }
  updateParticleColors();
});

window
  .matchMedia("(prefers-color-scheme: dark)")
  .addEventListener("change", function (e) {
    const newTheme = e.matches ? "dark" : "light";
    currentTheme = newTheme;
    body.setAttribute("data-theme", newTheme);
    themeToggle.checked = newTheme === "light";
    updateParticleColors();
  });
