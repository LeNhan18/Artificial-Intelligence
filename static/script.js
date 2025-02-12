document.getElementById("email-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  if (!email) {
    document.getElementById("result").innerHTML =
      '<span class="error">Vui lòng nhập nội dung email!</span>';
    return;
  }

  try {
    // Gửi yêu cầu POST đến API Flask
    const response = await fetch("http://127.0.0.1:5000/nhanle", {
      method: "POST"
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email }),
    });

    if (!response.ok) {
      throw new Error(`Lỗi HTTP: ${response.status}`);
    }

    // Nhận dữ liệu JSON từ phản hồi
    const data = await response.json();

    if (data["Ket Qua dự đoán"]) {
      // Hiển thị kết quả dự đoán
      const label = data["Ket Qua dự đoán"] === "spam" ? "Thư rác" : "Thư thường";
      document.getElementById("result").innerHTML =
        `<span>Kết quả: ${label}</span>`;
    } else if (data.error) {
      // Hiển thị lỗi từ server nếu có
      document.getElementById("result").innerHTML =
        `<span class="error">${data.error}</span>`;
    } else {
      document.getElementById("result").innerHTML =
        '<span class="error">Kết quả không xác định!</span>';
    }
  } catch (error) {
    console.error(error);
    document.getElementById("result").innerHTML =
      '<span class="error">Đã xảy ra lỗi. Vui lòng thử lại!</span>';
  }
});
