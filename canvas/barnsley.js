document.addEventListener("DOMContentLoaded", function () {
    const canvas = document.getElementById("barnsleyCanvas");
    const ctx = canvas.getContext("2d");

    const width = canvas.width;
    const height = canvas.height;

    let x = 0;
    let y = 0;

    for (let i = 0; i < 50000; i++) {
        const r = Math.random();
        let newX, newY;

        if (r < 0.01) {
            newX = 0;
            newY = 0.16 * y;
        } else if (r < 0.86) {
            newX = 0.85 * x + 0.04 * y;
            newY = -0.04 * x + 0.85 * y + 1.6;
        } else if (r < 0.93) {
            newX = 0.2 * x - 0.26 * y;
            newY = 0.23 * x + 0.22 * y + 1.6;
        } else {
            newX = -0.15 * x + 0.28 * y;
            newY = 0.26 * x + 0.24 * y + 0.44;
        }

        x = newX;
        y = newY;

        const plotX = Math.round(width / 2 + x * width / 8);
        const plotY = Math.round(height - y * height / 12);

        ctx.fillStyle = "#006400";
        ctx.fillRect(plotX, plotY, 2, 2);
    }
});
