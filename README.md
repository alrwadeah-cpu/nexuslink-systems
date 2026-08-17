# NexusLink Systems - Employee Login Portal
بوابة موظفي نيكسوس لينك سيستمز لتقنية المعلومات

A premium, modern, bilingual (English/Arabic) employee login portal designed specifically for a secure enterprise IT environment.

---

## 🚀 How to Run the Website (كيفية التشغيل)

### 1. Active Live Server (Currently Running!)
A lightweight local server has been started for you automatically:
👉 **[http://localhost:8000/](http://localhost:8000/)**

Simply click the link above or copy-paste it into your web browser (Chrome, Edge, Firefox, Safari) to interact with the login portal.

### 2. Manual Alternative (Direct File Access)
If the local server is closed or you wish to run it offline:
1. Navigate to the project directory: `C:\Users\DA\Desktop\site\`
2. Double-click the **[index.html](index.html)** file to open it directly in any web browser.

### 3. Running with Uvicorn (بايثون و Uvicorn)
You can run the project as an ASGI application using Python and Uvicorn:
1. Make sure `uvicorn` is installed:
   ```bash
   pip install uvicorn
   ```
2. Run the application in the project directory using:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   Then open: **[http://localhost:8000/](http://localhost:8000/)**

---

## 🎨 Design Features (مميزات التصميم)

*   **Split-Screen Layout (تقسيم الشاشة المزدوج)**:
    *   **Branding & Network Visual (اليسار)**: Includes an interactive **HTML5 Canvas Particle Network** showing nodes and connection links (symbolizing networks and databases) along with pulsing background glowing beams.
    *   **Secure Authentication Form (اليمين)**: A dark-themed glassmorphism form card (`backdrop-filter`) with floating input label transitions.
*   **Bilingual Translation & RTL Support (دعم ثنائي اللغة ولغات RTL)**:
    *   Dynamic toggle in the top-right header switches instantly between English and Arabic.
    *   Layout elements (icons, borders, floating labels, checkbox, form grid) automatically mirror direction using CSS Logical Properties (`dir="rtl"` / `dir="ltr"`).
*   **Form Validation & Feedback (التحقق الفوري من البيانات)**:
    *   Live validation for corporate emails (`name@nexuslink.com`) or Employee IDs (`EMP-XXXXX`).
    *   Live validation checking that the security password is at least 8 characters long.
    *   Eye icon button to toggle security password visibility (show/hide).
*   **Mock LDAP/AD Authentication (محاكاة خادم الشركة)**:
    *   Submitting the form shows a loading sequence simulating a connection to corporate LDAP/AD servers, followed by an "Access Granted" success overlay.
*   **SSO Badge Option**: Support for hardware authentication keys (e.g. YubiKey).

---

## 📁 File Structure (هيكل الملفات)

*   **[index.html](index.html)**: Semantic HTML5 document containing the core layout structure and inline SVG icon paths.
*   **[style.css](style.css)**: Modern CSS stylesheet containing typography (Outfit & Cairo fonts), layout grid rules, micro-animations, theme variables, and logical properties.
*   **[script.js](script.js)**: Logic for multi-language translation dictionaries, input listeners, password visibility toggle, server progress indicators, and the canvas particles networking logic.
*   **[README.md](README.md)**: This documentation guide.
