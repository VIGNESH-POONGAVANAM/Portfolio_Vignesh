document.addEventListener("DOMContentLoaded", function () {
    const texts = ["a Python Full Stack Developer", "a Web Developer", "a Problem Solver"];
    let index = 0;

    function updateText() {
        const element = document.getElementById("animated-part");
        element.textContent = texts[index];
        index = (index + 1) % texts.length;
    }

    setInterval(updateText, 2000);

    // Initialize ScrollMagic Controller
    const controller = new ScrollMagic.Controller();

    // Create a ScrollMagic Scene
    new ScrollMagic.Scene({
        triggerElement: ".animation-container",
        duration: "100%"
    })
        .setTween(gsap.fromTo(".animation-container", { opacity: 1 }, { opacity: 1, duration: 2 }))
        .addTo(controller);
});
