  function checkCholesterol() {
    const value = parseFloat(document.getElementById("total_cholesterol").value);
    const output = document.getElementById("cholesterol_category");
    if (isNaN(value)) {
      output.textContent = "";
      return;
    }
    if (value < 200) {
      output.textContent = "Category: Normal";
      output.style.color = "green";
    } else {
      output.textContent = "Category: High";
      output.style.color = "red";
    }
  }

  function checkSysBP() {
    const value = parseFloat(document.getElementById("sysBP").value);
    const output = document.getElementById("sysbp_category");
    if (isNaN(value)) {
      output.textContent = "";
      return;
    }
    if (value >= 90 && value <= 120) {
      output.textContent = "Category: Normal";
      output.style.color = "green";
    } else if (value < 90) {
      output.textContent = "Category: Low";
      output.style.color = "orange";
    } else {
      output.textContent = "Category: High";
      output.style.color = "red";
    }
  }

  function checkDiaBP() {
    const value = parseFloat(document.getElementById("diaBP").value);
    const output = document.getElementById("diabp_category");
    if (isNaN(value)) {
      output.textContent = "";
      return;
    }
    if (value >= 60 && value <= 80) {
      output.textContent = "Category: Normal";
      output.style.color = "green";
    } else if (value < 60) {
      output.textContent = "Category: Low";
      output.style.color = "orange";
    } else {
      output.textContent = "Category: High";
      output.style.color = "red";
    }
  }

  function checkBMI() {
    const value = parseFloat(document.getElementById("bmi").value);
    const output = document.getElementById("bmi_category");
    if (isNaN(value)) {
      output.textContent = "";
      return;
    }
    if (value >= 18.5 && value <= 24.9) {
      output.textContent = "Category: Normal";
      output.style.color = "green";
    } else if (value < 18.5) {
      output.textContent = "Category: Underweight";
      output.style.color = "orange";
    } else if (value <= 29.9) {
      output.textContent = "Category: Overweight";
      output.style.color = "red";
    } else {
      output.textContent = "Category: Obese";
      output.style.color = "darkred";
    }
  }

  function checkHeartRate() {
    const value = parseFloat(document.getElementById("heart_rate").value);
    const output = document.getElementById("heartrate_category");
    if (isNaN(value)) {
      output.textContent = "";
      return;
    }
    if (value >= 60 && value <= 100) {
      output.textContent = "Category: Normal";
      output.style.color = "green";
    } else if (value < 60) {
      output.textContent = "Category: Bradycardia (Low)";
      output.style.color = "orange";
    } else {
      output.textContent = "Category: Tachycardia (High)";
      output.style.color = "red";
    }
  }

  function checkGlucose() {
    const value = parseFloat(document.getElementById("glucose").value);
    const output = document.getElementById("glucose_category");
    if (isNaN(value)) {
      output.textContent = "";
      return;
    }
    if (value >= 70 && value <= 100) {
      output.textContent = "Category: Normal (Fasting)";
      output.style.color = "green";
    } else if (value < 70) {
      output.textContent = "Category: Low";
      output.style.color = "orange";
    } else {
      output.textContent = "Category: High";
      output.style.color = "red";
    }
  } 
