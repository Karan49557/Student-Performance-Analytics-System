# Student Performance Analytics System

An interactive, web-based student performance and grade analytics dashboard designed to help educators and institutions track student scores, compute statistical distributions, and visualize academic performance in real-time.

---

## 🚀 Features

* **Automated Statistical Metrics:** Instantly calculates total students, class average, median score, pass rate, highest/lowest range, and standard deviation.
* **Interactive Visualizations:** Powered by **Chart.js** to render dynamic Score Distribution bar charts and Grade Breakdown doughnut charts.
* **Advanced Search & Filtering:** Search students instantly by name and monitor performance status at a glance.
* **Print-Ready Reporting:** Features optimized print styling for generating clean hard-copy or PDF academic reports directly from the browser.
* **RESTful Backend Integration:** Built with Python and Flask to handle data requests and manage records seamlessly.

---

## 🛠️ Technologies Used

* **Backend:** Python 3.x, Flask (WSGI framework)
* **Frontend:** HTML5, Tailwind CSS, JavaScript (ES6+)
* **Data Visualization:** Chart.js, FontAwesome
* **Data Processing:** Python standard libraries & numeric routines

---

## 📂 Project Structure

```text
student-analytics/
│
├── app.py                 # Python Flask Backend Server
├── templates/
│   └── index.html         # Frontend Dashboard (HTML, Tailwind CSS, JS)
└── README.md              # Project Documentation
