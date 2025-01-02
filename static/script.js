document.getElementById("email-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    if (!email) {
        document.getElementById("result").innerHTML = '<span class="error">Vui lòng nhập nội dung email!</span>';
        return;
    }

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email: email }),
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();
        document.getElementById("result").innerHTML =
            `<span>Kết quả: ${data.KetQua === "spam" ? "Thư rác" : "Thư thường"}</span>`;
    } catch (error) {
        console.error(error);
        document.getElementById("result").innerHTML =
            '<span class="error">Đã xảy ra lỗi. Vui lòng thử lại!</span>';
    }
});
