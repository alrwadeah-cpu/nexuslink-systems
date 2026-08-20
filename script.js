// Translation dictionary for login and dashboard pages
const translations = {
    en: {
        pageTitleLogin: "Employee Portal - NexusLink Systems",
        pageTitleDashboard: "NexusLink Operational Console",
        brandTitle: "Architecting the Future. Starting with Today.",
        brandDesc: "Securely access the NexusLink core workspace to log your daily attendance, sync with your team, and drive global IT innovation. Your presence shapes our progress.",
        systemStatus: "All Corporate Systems Operational",
        cardTitle: "Employee Portal",
        cardSubtitle: "Please authenticate to continue to your workspace",
        labelEmail: "Corporate Email / Employee ID",
        labelPassword: "Security Password",
        labelRemember: "Remember Device",
        forgotLink: "Forgot Password?",
        btnSubmit: "Authorize Session",
        ssoDivider: "or authenticate via",
        btnSSO: "Corporate SSO Security Key",
        footerText: "Need assistance? Contact ",
        linkSupport: "IT Support Desk",
        errorEmail: "Please enter a valid corporate email (name@nexuslink.com) or Employee ID (EMP-XXXXX)",
        errorPassword: "Password must be at least 8 characters long",
        loadingVerify: "Verifying Credentials...",
        loadingConnect: "Connecting to Secure LDAP Server",
        successTitle: "Access Granted",
        successDesc: "Redirecting to NexusLink Dashboard. Welcome back!",
        successReturn: "Return",
        alertForgot: "Please contact IT Support Desk to reset your password.",
        alertSupport: "Opening Support Desk Ticket System...",
        alertSSO: "Checking for USB Security Key (YubiKey)...",
        loginFailed: "Authentication failed. Please check your credentials.",
        cardTitleRegister: "Create Account",
        cardSubtitleRegister: "Register your credentials to access the workspace",
        labelName: "Full Name",
        btnSubmitRegister: "Create Account",
        toggleToRegister: "Don't have an account? Create one",
        toggleToLogin: "Already have an account? Log in",
        errorName: "Please enter your full name",
        emailExists: "Email is already registered!",
        registerSuccess: "Account created successfully! Redirecting to login...",
        registerFailed: "Registration failed. Please try again.",
        loadingRegister: "Creating Account...",
        successTitleRegister: "Account Created",
        successDescRegister: "Your account has been created successfully. Welcome!",
        
        // Dashboard
        logoConsole: "OPERATIONAL CONSOLE",
        clockTitle: "Time & Attendance Gateways",
        btnCheckin: "Check In",
        btnCheckout: "Check Out",
        logsTitle: "Historical Operational Logs",
        userLogsSub: "Detailed logs of your daily attendance, departure, and status",
        userExcuseNotificationsTitle: "Delay Excuses Status",
        thDate: "DATE",
        thIn: "CHECK-IN",
        thOut: "CHECK-OUT",
        thStatus: "STATUS",
        badgeRecorded: "• RECORDED",
        badgeAbsent: "• ABSENT",
        badgeEmpty: "No logs found",
        btnTerminate: "Terminate Session",
        userDisplayLoading: "Loading...",
        workspaceActivated: "Workspace Activated",
        goodMorning: "Good morning",
        goodAfternoon: "Good afternoon",
        goodEvening: "Good evening",
        
        // Navigation & Admin Header
        navTitle: "EXECUTIVE COMMAND",
        navOverview: "Overview",
        navLiveAudit: "Live Audit",
        navUserOps: "User & Log Ops ▾",
        navAiAssist: "AI HR Assist",
        adminHeaderTitle: "EXECUTIVE MASTER COMMAND CENTER",
        badgeRealtime: "⚡ REALTIME WAL DB",
        badgePolicy: "🛡️ POLICY GUARD ACTIVE",
        badgeNotif: "🔔 NOTIFICATION BELL ENABLED",

        // Admin & Tables
        adminTitle: "Admin Attendance Console",
        adminManualTitle: "Manually Log Attendance Record",
        adminEmailLabel: "Employee Email",
        adminNameLabel: "Employee Name (Optional)",
        adminTypeLabel: "Movement Type",
        adminSubmitBtn: "Submit",
        optCheckin: "Check In",
        optCheckout: "Check Out",
        adminThName: "EMPLOYEE NAME",
        adminThEmail: "EMAIL",
        adminThType: "MOVEMENT",
        adminThDate: "DATE",
        adminThTime: "TIME",
        statTotal: "Total Records",
        statPresent: "Present Today",
        statCheckin: "Check In Today",
        statCheckout: "Check Out Today",
        statLate15: "Late > 15 Mins",
        statAbsent: "Absent Today",
        filterAll: "All Movements",
        btnClear: "Clear",
        btnExport: "Export Master CSV",
        excuseNotificationsTitle: "Pending Lateness Requests",
        btnRefresh: "Refresh",
        latenessTitle: "Lateness Audit Table (After 09:00 AM)",
        latenessSub: "Accurate calculation in minutes of delay time after 09:00 AM and application of discounts according to policy.text",
        masterAuditTitle: "Master Live Audit Terminal",
        masterAuditSub: "Comprehensive real-time tracking of check-in, check-out, and absence times for all employees",
        btnFilterLateness: "Delay Filters & Sorting",
        btnFilterMaster: "Search & Movement Filters",
        lblSearch: "Search by Name or Email:",
        lblDateFilter: "Filter by Date:",
        lblStatusFilter: "Movement Type:",
        lblLatenessFilter: "Lateness Degree:",
        searchPlaceholder: "Search by employee name or email...",
        btnSubmitExcuse: "Submit Delay Excuse",
        adminThInTime: "CHECK-IN TIME",
        adminThLateness: "LATENESS (AFTER 09:00 AM)",
        adminThStatus: "STATUS & DEDUCTION (POLICY GUARD)",
        adminThActivity: "STATUS & ACTIVITY",
        optAllLate: "All Late Movements",
        optGrace: "Grace Period (15 Mins)",
        optLate: "Regular Delay (15 - 60 Mins)",
        optDeduction: "Severe Delay (>60 Mins)",
        aiChatTitle: "NexusLink AI Assistant",
        aiChatSub: "Policy & Attendance Bot",
        aiChatWelcome: "Welcome to the Admin Console! Select an option above or type your question directly:",
        aiChatPlaceholder: "Ask about attendance policies or your records...",
        btnSend: "Send",
        adminAddUserTitle: "1- Add New Employee Account",
        adminNewNameLabel: "Full Name",
        adminNewEmailLabel: "Employee Email",
        adminNewPassLabel: "Password",
        adminAddUserBtn: "Add Employee Account",
        adminManualSubmitBtn: "Submit Attendance Record",
        adminLogEmailLabel: "Employee Email",
        adminLogNameLabel: "Employee Name (Optional)",
        adminLogTypeLabel: "Movement Type",
        excuseModalTitle: "Submit Lateness Excuse",
        excuseModalSub: "Direct submission to HR & Management with AI-assisted verification",
        excusePolicyNotice: "💡 <strong>Proof Policy (policy.text):</strong> Traffic accident excuses require attaching a <strong>Kroka / accident photo</strong>, and medical emergencies require an <strong>official medical report</strong> for instant approval.",
        excuseQuickChipsLabel: "⚡ Quick Excuse Presets:",
        excuseChipVehicle: "🚗 Vehicle Breakdown",
        excuseChipMedical: "🏥 Medical Emergency",
        excuseChipWeather: "🌧️ Severe Weather",
        excuseChipFamily: "🕊️ Bereavement / Family",
        excuseReasonLabel: "Detailed Reason for Delay to Manager:",
        excuseReasonPlaceholder: "Type your excuse reason here (e.g., vehicle breakdown, health emergency, official paperwork...)",
        excuseAttachmentLabel: "📷 Attach Proof Document (Accident Kroka / Medical Report - Optional):",
        excuseDropzonePrompt: "Click or drag & drop proof document here",
        excuseDropzoneSub: "(Supports JPG, PNG, GIF, WebP, PDF - Max 10MB)",
        excuseDeleteProof: "✕ Remove",
        btnCancel: "Cancel",
        btnSubmitExcuseSubmit: "Submit Excuse to Manager 🚀",
        lightboxTitle: "Proof Document Preview (Kroka / Medical Report)",
        lightboxDownload: "⬇️ Download File",
        lightboxClose: "Close",
        myExcusesTitle: "Delay Excuses Status",
        btnSelectDate: "Select Date",
        btnToday: "Today",
        btnYesterday: "Yesterday",
        btnShowAll: "Show All",
        navAiReport: "AI Report & Summary",
        aiReportHeaderTitle: "EXECUTIVE AI COMPLIANCE REPORT",
        badgeGeminiAI: "⚡ Powered by Gemini AI Engine",
        badgeRealtimeAnalytics: "📊 Real-Time Analytics",
        btnGenerateAiReport: "Generate Executive AI Report 🚀",
        aiKpiDiscipline: "Overall Discipline Score",
        aiKpiWarnings: "Active Warnings & Penalties",
        aiKpiSevere: "Severe Delays (>60 Mins)",
        aiKpiOntime: "On-Time Attendance Rate",
        aiInsightsTitle: "AI Executive Tactical Insights & Recommendations",
        aiRiskMatrixTitle: "Employee Discipline Risk Matrix & Recommendations",
        thRating: "Discipline Rating",
        thWarningCount: "Warning Count",
        thAiDetails: "AI Analysis & Recommendations",
        lblAiTargetEmployee: "Individual Employee Dossier:",
        lblAiReportDate: "Report Date:",
        optAllEmployees: "👥 All Employees",
        btnRefreshReport: "Refresh AI Report",
        lblDossierHistory: "Total Recorded Movements",
        lblDossierLate15: "Lateness Cases > 15 Mins",
        lblDossierLate60: "Severe Delay (>60 Mins)",
        lblDossierAbsences: "Recorded Absence Days",
        lblDossierEvaluationTitle: "Individual Employee AI Assessment & Recommendations"
    },
    ar: {
        pageTitleLogin: "بوابة الموظفين - نيكسوس لينك سيستمز",
        pageTitleDashboard: "لوحة التحكم التشغيلية - نيكسوس لينك",
        brandTitle: "بناء المستقبل لتقنية المعلومات. يبدأ من اليوم.",
        brandDesc: "الوصول الآمن إلى بيئة العمل الرئيسية لشركة نيكسوس لينك لتسجيل الحضور اليومي، والتنسيق مع فريقك، وقيادة الابتكار التقني العالمي. وجودك يثري تقدمنا.",
        systemStatus: "جميع الأنظمة التشغيلية للشركة تعمل كالمعتاد",
        cardTitle: "بوابة الموظفين",
        cardSubtitle: "الرجاء تسجيل الدخول للمتابعة إلى بيئة العمل الخاصة بك",
        labelEmail: "البريد الإلكتروني للشركة / الرقم الوظيفي",
        labelPassword: "كلمة المرور الأمنية",
        labelRemember: "تذكر هذا الجهاز",
        forgotLink: "نسيت كلمة المرور؟",
        btnSubmit: "تفويض الجلسة",
        ssoDivider: "أو تسجيل الدخول بواسطة",
        btnSSO: "مفتاح الأمان المؤسسي الموحد (SSO)",
        footerText: "هل تحتاج للمساعدة؟ اتصل بـ ",
        linkSupport: "مكتب الدعم الفني وتقنية المعلومات",
        errorEmail: "الرجاء إدخال بريد إلكتروني صحيح (name@nexuslink.com) أو رقم وظيفي (EMP-XXXXX)",
        errorPassword: "يجب أن تتكون كلمة المرور من 8 خانات على الأقل",
        loadingVerify: "جاري التحقق من الهوية...",
        loadingConnect: "الاتصال بخادم LDAP الآمن للشركة",
        successTitle: "تمت الموافقة على الدخول",
        successDesc: "جاري توجيهك إلى لوحة التحكم لشركة نيكسوس لينك. مرحباً بعودتك!",
        successReturn: "العودة",
        alertForgot: "الرجاء التواصل مع مكتب الدعم الفني لإعادة تعيين كلمة المرور الخاصة بك.",
        alertSupport: "جاري فتح نظام تذاكر الدعم الفني...",
        alertSSO: "جاري البحث عن مفتاح الأمان USB (YubiKey)...",
        loginFailed: "فشل التحقق من الهوية. الرجاء التأكد من البيانات المدخلة.",
        cardTitleRegister: "إنشاء حساب",
        cardSubtitleRegister: "سجل بياناتك للوصول إلى بيئة العمل",
        labelName: "الاسم الكامل",
        btnSubmitRegister: "إنشاء حساب",
        toggleToRegister: "ليس لديك حساب؟ إنشاء حساب",
        toggleToLogin: "لديك حساب بالفعل؟ تسجيل الدخول",
        errorName: "الرجاء إدخال اسمك الكامل",
        emailExists: "البريد الإلكتروني مسجل بالفعل!",
        registerSuccess: "تم إنشاء الحساب بنجاح! جاري التوجيه لتسجيل الدخول...",
        registerFailed: "فشل تسجيل الحساب. الرجاء المحاولة مرة أخرى.",
        loadingRegister: "جاري إنشاء الحساب...",
        successTitleRegister: "تم إنشاء الحساب",
        successDescRegister: "تم إنشاء حسابك بنجاح. مرحباً بك!",
        
        // Dashboard
        logoConsole: "لوحة التحكم التشغيلية",
        clockTitle: "بوابات تسجيل الحضور والانصراف",
        btnCheckin: "تسجيل حضور",
        btnCheckout: "تسجيل انصراف",
        logsTitle: "سجل العمليات التاريخي",
        userLogsSub: "تفاصيل سجلات الحضور والانصراف اليومية والتاريخية الخاصة بك",
        userExcuseNotificationsTitle: "متابعة حالة أعذار التأخير",
        thDate: "التاريخ",
        thIn: "حضور",
        thOut: "انصراف",
        thStatus: "الحالة",
        badgeRecorded: "• مسجّل",
        badgeAbsent: "• غائب",
        badgeEmpty: "لا توجد سجلات",
        btnTerminate: "إنهاء الجلسة",
        userDisplayLoading: "جاري التحميل...",
        workspaceActivated: "تم تفعيل بيئة العمل",
        goodMorning: "صباح الخير",
        goodAfternoon: "طاب يومك",
        goodEvening: "مساء الخير",

        // Navigation & Admin Header
        navTitle: "القيادة التنفيذية",
        navOverview: "الرئيسية",
        navLiveAudit: "السجل المباشر",
        navUserOps: "عمليات المستخدمين والمسجل ▾",
        navAiAssist: "المساعد الذكي",
        adminHeaderTitle: "مركز القيادة الرئيسي للمدير التنفيذي",
        badgeRealtime: "⚡ قاعدة بيانات مباشرة REALTIME",
        badgePolicy: "🛡️ نظام حماية السياسات مفعّل",
        badgeNotif: "🔔 جرس الإشعارات مفعّل",
        
        // Admin
        adminTitle: "لوحة تحكم الحضور للمشرف",
        adminManualTitle: "2- تسجيل حركة حضور وانصراف يدوياً",
        adminEmailLabel: "البريد الإلكتروني للموظف",
        adminNameLabel: "اسم الموظف (اختياري)",
        adminTypeLabel: "نوع الحركة",
        adminSubmitBtn: "إرسال",
        optCheckin: "تسجيل حضور",
        optCheckout: "تسجيل انصراف",
        adminThName: "اسم الموظف",
        adminThEmail: "البريد الإلكتروني",
        adminThType: "الحركة",
        adminThDate: "التاريخ",
        adminThTime: "الوقت",
        statTotal: "إجمالي السجلات",
        statPresent: "حاضرون اليوم",
        statCheckin: "تسجيل الدخول اليوم",
        statCheckout: "تسجيل الخروج اليوم",
        statLate15: "المتأخرون > 15 دقيقة",
        statAbsent: "الغياب اليوم",
        filterAll: "كل الحركات",
        btnClear: "تفريغ",
        btnExport: "تصدير إلى إكسل",
        excuseNotificationsTitle: "طلبات أعذار التأخير المعلقة",
        btnRefresh: "تحديث",
        latenessTitle: "جدول متابعة تأخير الموظفين بعد 09:00 ص",
        latenessSub: "حساب دقيق بالدقائق لوقت التأخير بعد 09:00 ص وتطبيق الخصومات حسب policy.text",
        masterAuditTitle: "جدول السجل الشامل للحضور والانصراف",
        masterAuditSub: "متابعة تفصيلية شاملة لوقت تسجيل الدخول والخروج والغياب لجميع الموظفين",
        btnFilterLateness: "فلاتر وتصفية التأخير",
        btnFilterMaster: "فلاتر البحث والتصفية",
        lblSearch: "البحث بالإيميل أو الاسم:",
        lblDateFilter: "تاريخ التصفية (اليوم/الشهر/السنة):",
        lblStatusFilter: "نوع الحركة:",
        lblLatenessFilter: "درجة التأخير:",
        searchPlaceholder: "بحث باسم الموظف أو بريده...",
        btnSubmitExcuse: "تقديم عذر تأخير",
        adminThInTime: "وقت الدخول",
        adminThLateness: "التأخير بعد 09:00 ص",
        adminThStatus: "الحالة والخصم (Policy Guard)",
        adminThActivity: "الحالة والنشاط",
        optAllLate: "كل الحضور المتأخر",
        optGrace: "ضمن فترة السماح (15 دقيقة)",
        optLate: "تأخير عادي (15 - 60 دقيقة)",
        optDeduction: "تأخير شديد (خصم نصف يوم >60د)",
        aiChatTitle: "المساعد الذكي لنيكسوس لينك",
        aiChatSub: "بوت السياسات والحضور",
        aiChatWelcome: "مرحباً بك في لوحة تحكم الأدمن! اختر أحد الخيارات أعلاه أو اكتب استفسارك مباشرة:",
        aiChatPlaceholder: "اسأل عن سياسات الدوام أو حضورك...",
        btnSend: "إرسال",
        adminAddUserTitle: "1- إضافة حساب موظف جديد",
        adminNewNameLabel: "الاسم الكامل",
        adminNewEmailLabel: "البريد الإلكتروني للموظف",
        adminNewPassLabel: "كلمة المرور",
        adminAddUserBtn: "إضافة حساب الموظف",
        adminManualSubmitBtn: "تسجيل حركة الحضور",
        adminLogEmailLabel: "البريد الإلكتروني للموظف",
        adminLogNameLabel: "اسم الموظف (اختياري)",
        adminLogTypeLabel: "نوع الحركة",
        excuseModalTitle: "تقديم عذر تأخير عن الدوام",
        excuseModalSub: "تقديم مباشر لقسم الموارد البشرية والإدارة مع تدقيق ذكي",
        excusePolicyNotice: "💡 <strong>شرط الإثبات (policy.text):</strong> أعذار حوادث السير تتطلب إرفاق <strong>صورة الكروكة أو الحادث</strong>، والأعذار الصحية تتطلب إرفاق <strong>التقرير الطبي الرسمي</strong> للقبول الفوري.",
        excuseQuickChipsLabel: "⚡ خيارات سريعة للأعذار الشائعة:",
        excuseChipVehicle: "🚗 عطل مفاجئ بالمركبة",
        excuseChipMedical: "🏥 ظرف صحي طارئ",
        excuseChipWeather: "🌧️ أحوال جوية قاهرة",
        excuseChipFamily: "🕊️ حالة وفاة / عائلي",
        excuseReasonLabel: "سبب التأخير التفصيلي للمدير:",
        excuseReasonPlaceholder: "اكتب سبب التأخير هنا بالتفصيل (مثال: عطل طارئ بالمركبة، ظروف صحية طارئة، مواعيد رسمية...)",
        excuseAttachmentLabel: "📷 إرفاق وثيقة الإثبات (كروكة الحادث / التقرير الطبي - اختياري):",
        excuseDropzonePrompt: "اضغط هنا أو اسحب وأفلت وثيقة الإثبات",
        excuseDropzoneSub: "(يدعم صور JPG, PNG, GIF, WebP أو ملف PDF - حتى 10MB)",
        excuseDeleteProof: "✕ حذف",
        btnCancel: "إلغاء",
        btnSubmitExcuseSubmit: "إرسال العذر للمدير 🚀",
        lightboxTitle: "معاينة وثيقة الإثبات (الكروكة / التقرير الطبي)",
        lightboxDownload: "⬇️ تحميل الملف",
        lightboxClose: "إغلاق",
        myExcusesTitle: "متابعة حالة أعذار التأخير",
        btnSelectDate: "تاريخ الدوام",
        btnToday: "اليوم",
        btnYesterday: "الأمس",
        btnShowAll: "عرض الكل",
        navAiReport: "تقارير الذكاء الاصطناعي",
        aiReportHeaderTitle: "تقرير تحليلات وملخصات الذكاء الاصطناعي التنفيذي",
        badgeGeminiAI: "⚡ المحرك الذكي Gemini AI",
        badgeRealtimeAnalytics: "📊 تحليلات فورية مباشرة",
        btnGenerateAiReport: "توليد التقرير التنفيذي المباشر 🚀",
        aiKpiDiscipline: "معدل الانضباط العام",
        aiKpiWarnings: "الإنذارات والخصومات المستحقة",
        aiKpiSevere: "تأخير شديد يتجاوز 60د",
        aiKpiOntime: "نسبة الحضور بالوقت المحدد",
        aiInsightsTitle: "الملخص التكتيكي والتوصيات الإدارية بالذكاء الاصطناعي",
        aiRiskMatrixTitle: "جدول مصفوفة مخاطر انضباط الموظفين والتوصيات",
        thRating: "تقييم الانضباط",
        thWarningCount: "عدد التنبيهات",
        thAiDetails: "تفاصيل التوصية بالذكاء الاصطناعي",
        lblAiTargetEmployee: "التقرير المخصص للموظف:",
        lblAiReportDate: "تاريخ التقرير:",
        optAllEmployees: "👥 جميع الموظفين (All Employees)",
        btnRefreshReport: "تحديث التقرير التنفيذي",
        lblDossierHistory: "إجمالي السجلات المسجلة",
        lblDossierLate15: "حالات التأخير > 15 دقيقة",
        lblDossierLate60: "تأخير شديد يتجاوز 60د",
        lblDossierAbsences: "عدد أيام الغياب المسجلة",
        lblDossierEvaluationTitle: "التصنيف والتوصيات الذكية الخاصة بالموظف"
    }
};

function toggleDatePopover(popoverId) {
    const popover = document.getElementById(popoverId);
    if (!popover) return;
    const isHidden = popover.style.display === 'none' || !popover.style.display;
    
    document.querySelectorAll('#lateness-date-popover, #master-date-popover, #user-date-popover').forEach(p => p.style.display = 'none');
    
    if (isHidden) {
        popover.style.display = 'block';
    }
}

function setQuickDate(inputId, range) {
    const inputEl = document.getElementById(inputId);
    let val = '';
    if (range === 'today') {
        val = new Date().toLocaleDateString('en-CA');
    } else if (range === 'yesterday') {
        const d = new Date();
        d.setDate(d.getDate() - 1);
        val = d.toLocaleDateString('en-CA');
    }
    
    if (inputEl) inputEl.value = val;
    if (inputId === 'lateness-date-filter') {
        const d = document.getElementById('lateness-drawer-date-filter');
        if (d) d.value = val;
        onLatenessDateChange();
    } else if (inputId === 'admin-date-filter') {
        const d = document.getElementById('admin-drawer-date-filter');
        if (d) d.value = val;
        onMasterDateChange();
    } else if (inputId === 'user-drawer-date-filter') {
        onUserDateChange(true);
    }

    // Auto-close popovers after quick selection
    document.querySelectorAll('#lateness-date-popover, #master-date-popover, #user-date-popover').forEach(p => p.style.display = 'none');
}

function onLatenessDateChange(e) {
    const val1 = document.getElementById('lateness-date-filter');
    const val2 = document.getElementById('lateness-drawer-date-filter');
    if (e && e.target) {
        if (e.target === val1 && val2) val2.value = val1.value;
        if (e.target === val2 && val1) val1.value = val2.value;
    }
    latenessCurrentPage = 1;
    renderAdminLatenessTable();
}

function onMasterDateChange(e) {
    const val1 = document.getElementById('admin-date-filter');
    const val2 = document.getElementById('admin-drawer-date-filter');
    if (e && e.target) {
        if (e.target === val1 && val2) val2.value = val1.value;
        if (e.target === val2 && val1) val1.value = val2.value;
    }
    masterCurrentPage = 1;
    filterAdminLogs();
}

function onUserDateChange(shouldClose = false) {
    userLogsCurrentPage = 1;
    loadLogs();

    if (shouldClose) {
        const userPopover = document.getElementById('user-date-popover');
        if (userPopover) {
            userPopover.style.display = 'none';
        }
    }
}

if (typeof document !== 'undefined') {
    document.addEventListener('click', function(e) {
        const latenessPopover = document.getElementById('lateness-date-popover');
        const latenessBtn = document.getElementById('btn-lateness-date-popover');
        if (latenessPopover && latenessBtn && !latenessPopover.contains(e.target) && !latenessBtn.contains(e.target)) {
            latenessPopover.style.display = 'none';
        }
        
        const masterPopover = document.getElementById('master-date-popover');
        const masterBtn = document.getElementById('btn-master-date-popover');
        if (masterPopover && masterBtn && !masterPopover.contains(e.target) && !masterBtn.contains(e.target)) {
            masterPopover.style.display = 'none';
        }

        const userDatePopover = document.getElementById('user-date-popover');
        const userDateBtn = document.getElementById('btn-user-date-popover');
        if (userDatePopover && userDateBtn && !userDatePopover.contains(e.target) && !userDateBtn.contains(e.target)) {
            userDatePopover.style.display = 'none';
        }
    });
}

// State variables
let currentLang = localStorage.getItem('lang') || 'en';
let allAdminRecords = []; // Global cache for admin records
const API_BASE = (typeof window !== 'undefined' && window.location && window.location.port === '8000') ? window.location.origin : 'http://127.0.0.1:8000';

// Function to translate all elements with data-i18n attributes
function updatePageTexts() {
    const t = translations[currentLang];
    if (!t) return;

    // Document Title
    const isDashboard = document.getElementById('logs-body') !== null;
    document.title = isDashboard ? t.pageTitleDashboard : t.pageTitleLogin;
    
    // HTML Lang & Direction
    document.documentElement.lang = currentLang;
    document.documentElement.dir = (currentLang === 'ar') ? 'rtl' : 'ltr';

    // Simple text replacement
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (t[key]) {
            el.innerText = t[key];
        }
    });

    // Rich HTML replacement
    document.querySelectorAll('[data-i18n-html]').forEach(el => {
        const key = el.getAttribute('data-i18n-html');
        if (t[key]) {
            el.innerHTML = t[key];
        }
    });

    // Input placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (t[key]) {
            el.placeholder = t[key];
        }
    });

    // Update switcher UI
    const langSlider = document.getElementById('lang-slider');
    const btnEn = document.getElementById('btn-en');
    const btnAr = document.getElementById('btn-ar');

    if (langSlider && btnEn && btnAr) {
        const isRtl = document.documentElement.dir === 'rtl';
        if (currentLang === 'en') {
            btnEn.classList.add('active');
            btnAr.classList.remove('active');
            // English is physically on the left (0px) in LTR, and on the right (54px) in RTL
            langSlider.style.transform = isRtl ? 'translateX(54px)' : 'translateX(0px)';
        } else {
            btnAr.classList.add('active');
            btnEn.classList.remove('active');
            // Arabic is physically on the right (54px) in LTR, and on the left (0px) in RTL
            langSlider.style.transform = isRtl ? 'translateX(0px)' : 'translateX(54px)';
        }
    }
    
    // Auto-render AI Welcome card in active language if no conversation has started
    const msgBox = document.getElementById('ai-chat-messages');
    const hasActiveMessages = msgBox && msgBox.querySelectorAll('.user-msg, .ai-resp-card').length > 0;
    if (!hasActiveMessages) {
        clearAIChatHistory();
    }

    // Update Greeting and re-render dynamic tables on dashboard if available
    if (isDashboard) {
        const nameDisplay = document.getElementById('user-name-display');
        if (nameDisplay) nameDisplay.textContent = localStorage.getItem('userName') || "NexusLink Employee";
        
        updateDashboardGreeting();
        
        const email = localStorage.getItem('userEmail');
        if (isAdminEmail(email)) {
            if (allAdminRecords && allAdminRecords.length > 0) {
                renderAdminLogsTable(allAdminRecords);
                renderAdminLatenessTable(allAdminRecords);
            }
            loadAdminExcuses();
            loadAIDailySummary();
            const aiReportSection = document.getElementById('ai-report-section');
            const empSel = document.getElementById('ai-report-employee-filter');
            if (empSel) empSel.removeAttribute('data-loaded');
            if (aiReportSection && aiReportSection.style.display !== 'none') {
                loadAiReportData();
            }
        } else {
            loadLogs();
            loadMyExcuses();
        }
        updateAiQuickOptionsUI();
    }
}

// Switch Language handler
function toggleLanguage() {
    currentLang = (currentLang === 'en') ? 'ar' : 'en';
    localStorage.setItem('lang', currentLang);
    updatePageTexts();
    clearAIChatHistory();
}

/* === LOGIN PAGE LOGIC === */

// Field Validations
function validateField(fieldId) {
    const el = document.getElementById(fieldId);
    const errEl = document.getElementById(`error-${fieldId}`);
    if (!el || !errEl) return false;

    let isValid = true;
    if (fieldId === 'email') {
        const val = el.value.trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/i;
        const empIdRegex = /^EMP-\d{5}$/i;
        
        // Supports standard email or EMP-12345
        isValid = emailRegex.test(val) || empIdRegex.test(val);
    } else if (fieldId === 'password') {
        isValid = el.value.trim().length >= 8;
    }

    if (isValid) {
        errEl.style.display = 'none';
        el.classList.remove('input-invalid');
    } else {
        errEl.style.display = 'flex';
        el.classList.add('input-invalid');
    }
    return isValid;
}

// Show/Hide Password
function togglePasswordVisibility() {
    const passwordInput = document.getElementById('password');
    const eyeIcon = document.getElementById('eye-icon');
    if (!passwordInput) return;

    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        if (eyeIcon) {
            eyeIcon.innerHTML = `
                <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                <line x1="1" y1="1" x2="23" y2="23"></line>
            `;
        }
    } else {
        passwordInput.type = 'password';
        if (eyeIcon) {
            eyeIcon.innerHTML = `
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                <circle cx="12" cy="12" r="3"></circle>
            `;
        }
    }
}

// Login Submission
async function handleLogin(event) {
    event.preventDefault();
    
    const emailValid = validateField('email');
    const passwordValid = validateField('password');
    if (!emailValid || !passwordValid) return;

    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const rememberMe = document.getElementById('remember-me').checked;

    // Show loading overlay
    const loadingOverlay = document.getElementById('loading-overlay');
    const errBox = document.getElementById('server-error');
    if (errBox) errBox.style.display = 'none';
    if (loadingOverlay) loadingOverlay.style.display = 'flex';

    try {
        const formData = new FormData();
        formData.append('email', email);
        formData.append('password', password);

        const response = await fetch(`${API_BASE}/api/login`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) throw new Error("Connection failed");

        const result = await response.json();

        if (result.success) {
            // Store credentials
            localStorage.setItem('userEmail', email);
            localStorage.setItem('userName', result.name || "NexusLink Employee");
            localStorage.setItem('userToken', result.token);
            if (rememberMe) {
                localStorage.setItem('rememberUser', 'true');
            } else {
                localStorage.removeItem('rememberUser');
            }

            // Hide loading, show success overlay
            if (loadingOverlay) loadingOverlay.style.display = 'none';
            const successOverlay = document.getElementById('success-overlay');
            if (successOverlay) successOverlay.style.display = 'flex';

            // Wait and redirect to dashboard.html
            setTimeout(() => {
                window.location.href = 'dashboard.html';
            }, 1800);
        } else {
            // Failed check
            if (loadingOverlay) loadingOverlay.style.display = 'none';
            showServerError(translations[currentLang].loginFailed);
        }
    } catch (error) {
        if (loadingOverlay) loadingOverlay.style.display = 'none';
        showServerError(translations[currentLang].loginFailed);
        console.error("Login request error:", error);
    }
}

// Helper to show errors inline
function showServerError(msg) {
    const errBox = document.getElementById('server-error');
    const errText = document.getElementById('server-error-text');
    if (errBox && errText) {
        errText.innerText = msg;
        errBox.style.display = 'flex';
    } else {
        alert(msg);
    }
}

function dismissError() {
    const errBox = document.getElementById('server-error');
    if (errBox) errBox.style.display = 'none';
}

function resetForm() {
    const successOverlay = document.getElementById('success-overlay');
    if (successOverlay) successOverlay.style.display = 'none';
    const form = document.getElementById('login-form');
    if (form) form.reset();
    const rform = document.getElementById('register-form');
    if (rform) rform.reset();
}

let currentFormMode = 'login';

function toggleFormMode(e) {
    if (e) e.preventDefault();
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const ssoDivider = document.querySelector('.sso-divider');
    const ssoBtn = document.querySelector('.sso-btn');
    const cardTitle = document.getElementById('card-title');
    const cardSubtitle = document.getElementById('card-subtitle');
    const toggleLink = document.getElementById('toggle-mode-link');
    const errBox = document.getElementById('server-error');

    if (errBox) errBox.style.display = 'none';

    if (currentFormMode === 'login') {
        currentFormMode = 'register';
        if (loginForm) loginForm.style.display = 'none';
        if (registerForm) registerForm.style.display = 'block';
        if (ssoDivider) ssoDivider.style.display = 'none';
        if (ssoBtn) ssoBtn.style.display = 'none';
        
        if (cardTitle) cardTitle.setAttribute('data-i18n', 'cardTitleRegister');
        if (cardSubtitle) cardSubtitle.setAttribute('data-i18n', 'cardSubtitleRegister');
        if (toggleLink) toggleLink.setAttribute('data-i18n', 'toggleToLogin');
    } else {
        currentFormMode = 'login';
        if (loginForm) loginForm.style.display = 'block';
        if (registerForm) registerForm.style.display = 'none';
        if (ssoDivider) ssoDivider.style.display = 'flex';
        if (ssoBtn) ssoBtn.style.display = 'flex';
        
        if (cardTitle) cardTitle.setAttribute('data-i18n', 'cardTitle');
        if (cardSubtitle) cardSubtitle.setAttribute('data-i18n', 'cardSubtitle');
        if (toggleLink) toggleLink.setAttribute('data-i18n', 'toggleToRegister');
    }
    
    resetForm();
    
    document.querySelectorAll('.error-msg').forEach(el => el.style.display = 'none');
    document.querySelectorAll('.input-field').forEach(el => el.classList.remove('input-invalid'));
    
    updatePageTexts();
}

function validateRegisterField(fieldId) {
    const el = document.getElementById(`register-${fieldId}`);
    const errEl = document.getElementById(`error-register-${fieldId}`);
    if (!el || !errEl) return false;

    let isValid = true;
    if (fieldId === 'name') {
        isValid = el.value.trim().length > 0;
    } else if (fieldId === 'email') {
        const val = el.value.trim();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/i;
        const empIdRegex = /^EMP-\d{5}$/i;
        isValid = emailRegex.test(val) || empIdRegex.test(val);
    } else if (fieldId === 'password') {
        isValid = el.value.trim().length >= 8;
    }

    if (isValid) {
        errEl.style.display = 'none';
        el.classList.remove('input-invalid');
    } else {
        errEl.style.display = 'flex';
        el.classList.add('input-invalid');
    }
    return isValid;
}

function toggleRegisterPasswordVisibility() {
    const passwordInput = document.getElementById('register-password');
    const eyeIcon = document.getElementById('register-eye-icon');
    if (!passwordInput) return;

    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        if (eyeIcon) {
            eyeIcon.innerHTML = `
                <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                <line x1="1" y1="1" x2="23" y2="23"></line>
            `;
        }
    } else {
        passwordInput.type = 'password';
        if (eyeIcon) {
            eyeIcon.innerHTML = `
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                <circle cx="12" cy="12" r="3"></circle>
            `;
        }
    }
}

async function handleRegister(event) {
    event.preventDefault();

    const nameValid = validateRegisterField('name');
    const emailValid = validateRegisterField('email');
    const passwordValid = validateRegisterField('password');
    if (!nameValid || !emailValid || !passwordValid) return;

    const name = document.getElementById('register-name').value.trim();
    const email = document.getElementById('register-email').value.trim();
    const password = document.getElementById('register-password').value.trim();

    const loadingOverlay = document.getElementById('loading-overlay');
    const loadingText = document.getElementById('loading-text');
    const loadingSubtext = document.getElementById('loading-subtext');
    const errBox = document.getElementById('server-error');

    if (errBox) errBox.style.display = 'none';
    
    const origTextKey = loadingText.getAttribute('data-i18n') || 'loadingVerify';
    const origSubtextKey = loadingSubtext.getAttribute('data-i18n') || 'loadingConnect';

    loadingText.innerText = translations[currentLang].loadingRegister || "Creating Account...";
    loadingSubtext.innerText = currentLang === 'ar' ? "الاتصال بقاعدة بيانات SQL..." : "Connecting to SQL Database...";
    
    if (loadingOverlay) loadingOverlay.style.display = 'flex';

    try {
        const formData = new FormData();
        formData.append('name', name);
        formData.append('email', email);
        formData.append('password', password);

        const response = await fetch(`${API_BASE}/api/register`, {
            method: 'POST',
            body: formData
        });

        if (loadingOverlay) loadingOverlay.style.display = 'none';
        
        loadingText.setAttribute('data-i18n', origTextKey);
        loadingSubtext.setAttribute('data-i18n', origSubtextKey);
        updatePageTexts();

        if (!response.ok) {
            let errMsg = translations[currentLang].registerFailed;
            try {
                const errJson = await response.json();
                if (errJson.error === 'email_exists') {
                    errMsg = translations[currentLang].emailExists;
                } else if (errJson.detail) {
                    errMsg = errJson.detail;
                }
            } catch(e) {}
            throw new Error(errMsg);
        }

        const result = await response.json();

        if (result.success) {
            const successOverlay = document.getElementById('success-overlay');
            const successTitle = document.getElementById('success-title');
            const successDesc = document.getElementById('success-desc');
            const successBtn = document.getElementById('success-btn');

            const origSuccessTitleKey = successTitle.getAttribute('data-i18n') || 'successTitle';
            const origSuccessDescKey = successDesc.getAttribute('data-i18n') || 'successDesc';

            successTitle.innerText = translations[currentLang].successTitleRegister || "Account Created";
            successDesc.innerText = translations[currentLang].successDescRegister || "Your account has been created successfully.";
            if (successBtn) successBtn.style.display = 'none';

            if (successOverlay) successOverlay.style.display = 'flex';

            setTimeout(() => {
                if (successOverlay) successOverlay.style.display = 'none';
                
                successTitle.setAttribute('data-i18n', origSuccessTitleKey);
                successDesc.setAttribute('data-i18n', origSuccessDescKey);
                if (successBtn) successBtn.style.display = 'block';
                updatePageTexts();

                toggleFormMode();
            }, 2500);
        } else {
            let errMsg = translations[currentLang].registerFailed;
            if (result.error === 'email_exists') {
                errMsg = translations[currentLang].emailExists;
            } else if (result.error) {
                errMsg = result.error;
            }
            showServerError(errMsg);
        }
    } catch (error) {
        if (loadingOverlay) loadingOverlay.style.display = 'none';
        loadingText.setAttribute('data-i18n', origTextKey);
        loadingSubtext.setAttribute('data-i18n', origSubtextKey);
        updatePageTexts();
        showServerError(error.message || translations[currentLang].registerFailed);
        console.error("Register request error:", error);
    }
}

// Custom alert triggers
function alertForgot(e) {
    e.preventDefault();
    alert(translations[currentLang].alertForgot);
}

// Custom support alert triggers
function alertSupport(e) {
    e.preventDefault();
    alert(translations[currentLang].alertSupport);
}

function triggerSSO() {
    alert(translations[currentLang].alertSSO);
}

/* === PARTICLES BACKGROUND INTERACTIVE RENDERING === */
function initParticles() {
    const canvas = document.getElementById('particle-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    let particlesArray = [];
    const colors = ['rgba(59, 130, 246, 0.4)', 'rgba(16, 185, 129, 0.3)', 'rgba(96, 165, 250, 0.4)'];
    
    function setSize() {
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
    }
    setSize();
    window.addEventListener('resize', setSize);
    
    const mouse = {
        x: null,
        y: null,
        radius: 120
    };
    
    const brandPanel = canvas.parentElement;
    brandPanel.addEventListener('mousemove', (e) => {
        const rect = brandPanel.getBoundingClientRect();
        mouse.x = e.clientX - rect.left;
        mouse.y = e.clientY - rect.top;
    });
    brandPanel.addEventListener('mouseleave', () => {
        mouse.x = null;
        mouse.y = null;
    });
    
    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 2 + 1.5;
            this.speedX = Math.random() * 0.6 - 0.3;
            this.speedY = Math.random() * 0.6 - 0.3;
            this.color = colors[Math.floor(Math.random() * colors.length)];
        }
        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            
            if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
            if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
            
            // Mouse push force
            if (mouse.x !== null && mouse.y !== null) {
                let dx = this.x - mouse.x;
                let dy = this.y - mouse.y;
                let distance = Math.sqrt(dx*dx + dy*dy);
                if (distance < mouse.radius) {
                    const force = (mouse.radius - distance) / mouse.radius;
                    const directionX = dx / distance;
                    const directionY = dy / distance;
                    this.x += directionX * force * 1.5;
                    this.y += directionY * force * 1.5;
                }
            }
        }
        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }
    
    function createParticles() {
        const numberOfParticles = Math.floor((canvas.width * canvas.height) / 10000);
        particlesArray = [];
        for (let i = 0; i < Math.max(numberOfParticles, 25); i++) {
            particlesArray.push(new Particle());
        }
    }
    createParticles();
    
    function connectParticles() {
        let opacityValue = 1;
        for (let a = 0; a < particlesArray.length; a++) {
            for (let b = a; b < particlesArray.length; b++) {
                let dx = particlesArray[a].x - particlesArray[b].x;
                let dy = particlesArray[a].y - particlesArray[b].y;
                let distance = Math.sqrt(dx*dx + dy*dy);
                
                if (distance < 120) {
                    opacityValue = 1 - (distance / 120);
                    ctx.strokeStyle = `rgba(59, 130, 246, ${opacityValue * 0.12})`;
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
                    ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
                    ctx.stroke();
                }
            }
        }
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < particlesArray.length; i++) {
            particlesArray[i].update();
            particlesArray[i].draw();
        }
        connectParticles();
        requestAnimationFrame(animate);
    }
    animate();
    
    window.addEventListener('resize', createParticles);
}


/* === DASHBOARD PAGE LOGIC === */

function isAdminEmail(email) {
    if (!email) return false;
    const e = email.trim().toLowerCase();
    return e === 'admin@nexus.com' || e === 'admin-faisal@gmail.com' || e.startsWith('admin') || e.includes('admin');
}

function setupDashboard() {
    const email = localStorage.getItem('userEmail');
    const token = localStorage.getItem('userToken');
    if (!email || !token) {
        // Redirect to login if user session is not active
        window.location.href = 'index.html';
        return;
    }

    // Set user info
    const nameDisplay = document.getElementById('user-name-display');
    const emailDisplay = document.getElementById('user-email-display');
    
    if (nameDisplay) nameDisplay.textContent = localStorage.getItem('userName') || "NexusLink Employee";
    if (emailDisplay) emailDisplay.textContent = email;

    // Start Clock
    updateClock();
    setInterval(updateClock, 1000);

    // Check if admin user
    const adminSection = document.getElementById('admin-section');
    const userGatewayCard = document.getElementById('user-gateway-card');
    const userExcusesCard = document.getElementById('user-excuses-card');
    const adminSidebarStatus = document.getElementById('admin-sidebar-status');
    const userLogsCard = document.getElementById('user-logs-card');
    const opsDropdownWrapper = document.querySelector('.nav-rail-dropdown-wrapper');
    const liveAuditNavItem = document.querySelector('a[href="#admin-logs-body"]');
    const adminBellWrapper = document.getElementById('admin-notification-bell-wrapper');
    const userBellWrapper = document.getElementById('user-notification-bell-wrapper');
    const aiReportNavItem = document.getElementById('nav-ai-report-item');
    const aiReportSection = document.getElementById('ai-report-section');

    if (isAdminEmail(email)) {
        document.body.classList.add('admin-mode');
        document.body.classList.remove('employee-mode');
        if (adminBellWrapper) adminBellWrapper.style.display = 'block';
        if (userBellWrapper) userBellWrapper.style.display = 'none';
        if (opsDropdownWrapper) opsDropdownWrapper.style.display = 'block';
        if (liveAuditNavItem) liveAuditNavItem.style.display = 'flex';
        if (aiReportNavItem) aiReportNavItem.style.display = 'flex';
        if (userGatewayCard) userGatewayCard.style.display = 'none';
        if (userExcusesCard) userExcusesCard.style.display = 'none';
        if (adminSidebarStatus) adminSidebarStatus.style.display = 'flex';
        if (userLogsCard) userLogsCard.style.display = 'none';
        if (adminSection) {
            adminSection.style.display = 'flex';
            loadAdminLogs();
            loadAdminExcuses();
            loadAiReportData();
        }
    } else {
        document.body.classList.remove('admin-mode');
        document.body.classList.add('employee-mode');
        if (adminBellWrapper) adminBellWrapper.style.display = 'none';
        if (userBellWrapper) userBellWrapper.style.display = 'block';
        if (opsDropdownWrapper) opsDropdownWrapper.style.display = 'none';
        if (liveAuditNavItem) liveAuditNavItem.style.display = 'none';
        if (aiReportNavItem) aiReportNavItem.style.display = 'none';
        if (aiReportSection) aiReportSection.style.display = 'none';
        if (userGatewayCard) userGatewayCard.style.display = 'block';
        if (userExcusesCard) userExcusesCard.style.display = 'none';
        if (adminSidebarStatus) adminSidebarStatus.style.display = 'none';
        if (userLogsCard) userLogsCard.style.display = 'block';
        if (adminSection) adminSection.style.display = 'none';
        loadLogs();
        loadMyExcuses();
    }
}

async function loadAdminLogs() {
    const tbody = document.getElementById('admin-logs-body');
    if (!tbody) return;

    try {
        const token = localStorage.getItem('userToken');
        const response = await fetch(`${API_BASE}/api/attendance/all`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        if (!response.ok) throw new Error("Failed to load admin logs");
        const records = await response.json();
        
        // Cache records globally
        allAdminRecords = records;
        
        // Calculate today's 4 stats accurately per unique employee
        const todayStr = new Date().toLocaleDateString('en-CA');
        const todayUsers = {};

        records.forEach(rec => {
            if (rec.date === todayStr) {
                const em = (rec.email || '').toLowerCase().trim();
                if (!em) return;
                if (!todayUsers[em]) {
                    todayUsers[em] = {
                        checkinTimes: [],
                        checkoutTimes: [],
                        hasAbsent: false
                    };
                }

                const typeLower = rec.type ? rec.type.toLowerCase() : '';
                if (typeLower.includes('دخول') || typeLower.includes('check-in')) {
                    if (rec.time && rec.time !== '--:--:--') {
                        todayUsers[em].checkinTimes.push(rec.time);
                    }
                } else if (typeLower.includes('خروج') || typeLower.includes('check-out')) {
                    if (rec.time && rec.time !== '--:--:--') {
                        todayUsers[em].checkoutTimes.push(rec.time);
                    }
                } else if (typeLower.includes('غياب') || typeLower.includes('absent')) {
                    todayUsers[em].hasAbsent = true;
                }
            }
        });

        let checkinCount = 0;
        let checkoutCount = 0;
        let late15Count = 0;
        let absentCount = 0;

        Object.keys(todayUsers).forEach(em => {
            const u = todayUsers[em];
            if (u.checkinTimes.length > 0) {
                checkinCount++;
                u.checkinTimes.sort();
                const earliestTime = u.checkinTimes[0];
                if (earliestTime > '09:15:00') {
                    late15Count++;
                }
            } else if (u.hasAbsent) {
                absentCount++;
            }
            if (u.checkoutTimes.length > 0) {
                checkoutCount++;
            }
        });

        const checkinEl = document.getElementById('stat-checkin');
        const checkoutEl = document.getElementById('stat-checkout');
        const late15El = document.getElementById('stat-late15');
        const absentEl = document.getElementById('stat-absent');
        const totalUsersEl = document.getElementById('stat-totalusers');

        const uniqueEmails = new Set(records.map(r => (r.email || '').toLowerCase().trim()).filter(Boolean));

        if (checkinEl) checkinEl.textContent = checkinCount;
        if (checkoutEl) checkoutEl.textContent = checkoutCount;
        if (late15El) late15El.textContent = late15Count;
        if (absentEl) absentEl.textContent = absentCount;
        if (totalUsersEl) totalUsersEl.textContent = uniqueEmails.size || 21;
        
        // Render live audit table & dedicated lateness audit table (filtered for target date)
        filterAdminLogs();
        renderAdminLatenessTable(records);

        // Fetch AI Analytics, Daily Summary & Insights
        loadAIAdminAnalytics();
        loadAIDailySummary();
    } catch (err) {
        console.error("Error loading admin logs:", err);
        const errText = currentLang === 'ar' ? 'فشل تحميل سجل المشرف' : 'Failed to load admin logs';
        tbody.innerHTML = `<tr><td colspan="5" style="text-align: center; color: var(--error-color);">${errText}</td></tr>`;
    }
}

async function loadAIDailySummary() {
    const textEl = document.getElementById('ai-daily-summary-text');
    const badgeEl = document.getElementById('ai-health-badge');
    if (!textEl) return;

    try {
        const response = await fetch(`${API_BASE}/api/ai/daily-summary`);
        const data = await response.json();
        if (!data.success) return;

        const isAr = currentLang === 'ar';
        textEl.textContent = isAr ? data.summary_ar : data.summary_en;

        if (badgeEl) {
            if (data.health_status === 'GREEN') {
                badgeEl.style.background = 'rgba(16, 185, 129, 0.2)';
                badgeEl.style.borderColor = 'rgba(16, 185, 129, 0.4)';
                badgeEl.style.color = '#6ee7b7';
                badgeEl.textContent = isAr ? '🟢 حالة الدوام: ممتازة' : '🟢 Health: Optimal';
            } else if (data.health_status === 'YELLOW') {
                badgeEl.style.background = 'rgba(245, 158, 11, 0.2)';
                badgeEl.style.borderColor = 'rgba(245, 158, 11, 0.4)';
                badgeEl.style.color = '#fde68a';
                badgeEl.textContent = isAr ? '🟡 تنبيه: يوجد تأخيرات' : '🟡 Warning: Delays Detected';
            } else {
                badgeEl.style.background = 'rgba(239, 68, 68, 0.2)';
                badgeEl.style.borderColor = 'rgba(239, 68, 68, 0.4)';
                badgeEl.style.color = '#fca5a5';
                badgeEl.textContent = isAr ? '🔴 خطر: تأخير شديد/غياب' : '🔴 Alert: Severe Delays';
            }
        }
    } catch (err) {
        console.error("Error loading AI Daily Summary:", err);
    }
}

function calculateMinutesLateAfter9(timeStr) {
    if (!timeStr) return 0;
    const parts = timeStr.split(':');
    if (parts.length < 2) return 0;
    const hours = parseInt(parts[0], 10);
    const mins = parseInt(parts[1], 10);

    const totalCheckinMins = hours * 60 + mins;
    const workStartMins = 9 * 60; // 09:00 AM

    if (totalCheckinMins <= workStartMins) {
        return 0;
    }
    return totalCheckinMins - workStartMins;
}

function preventScrollOnFocus(e) {
    if (e && e.target) {
        const x = window.scrollX || window.pageXOffset || 0;
        const y = window.scrollY || window.pageYOffset || 0;
        requestAnimationFrame(() => {
            window.scrollTo(x, y);
        });
    }
}

const PAGE_SIZE = 5;
let masterCurrentPage = 1;
let latenessCurrentPage = 1;
let userLogsCurrentPage = 1;
let aiMatrixCurrentPage = 1;
let globalAiUserProfiles = [];

function renderPaginationBar(containerId, currentPage, totalPages, totalItems, onPageChangeFn, pageSize = PAGE_SIZE) {
    const container = document.getElementById(containerId);
    if (!container) return;

    if (!totalItems || totalItems === 0 || totalPages <= 1) {
        container.style.display = 'none';
        return;
    }
    container.style.display = 'flex';

    const isAr = currentLang === 'ar';
    const startItem = (currentPage - 1) * pageSize + 1;
    const endItem = Math.min(currentPage * pageSize, totalItems);

    const infoHtml = isAr
        ? `<span style="font-size: 0.8rem; color: #94a3b8;">عرض <strong>${startItem} - ${endItem}</strong> من أصل <strong>${totalItems}</strong> سجلات</span>`
        : `<span style="font-size: 0.8rem; color: #94a3b8;">Showing <strong>${startItem}-${endItem}</strong> of <strong>${totalItems}</strong> entries</span>`;

    // Dynamic Sliding Window of Max 4 Page Buttons!
    let startPage = Math.max(1, currentPage - 2);
    let endPage = startPage + 3;
    if (endPage > totalPages) {
        endPage = totalPages;
        startPage = Math.max(1, endPage - 3);
    }

    let buttonsHtml = '<div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap;">';

    // Previous Button (<)
    const prevDisabled = currentPage === 1;
    buttonsHtml += `
        <button type="button" onclick="${onPageChangeFn}(${currentPage - 1})" ${prevDisabled ? 'disabled' : ''} 
            style="padding: 6px 12px; border-radius: 8px; border: 1px solid ${prevDisabled ? 'rgba(255,255,255,0.08)' : 'rgba(0,242,254,0.3)'}; background: ${prevDisabled ? 'rgba(255,255,255,0.03)' : 'rgba(0,242,254,0.12)'}; color: ${prevDisabled ? '#475569' : '#38bdf8'}; font-weight: 700; font-size: 0.82rem; cursor: ${prevDisabled ? 'not-allowed' : 'pointer'}; transition: all 0.2s;">
            &lt;
        </button>
    `;

    // Page Numbers (Max 4 buttons rendered)
    for (let i = startPage; i <= endPage; i++) {
        const isActive = i === currentPage;
        buttonsHtml += `
            <button type="button" onclick="${onPageChangeFn}(${i})" 
                style="padding: 6px 12px; border-radius: 8px; border: 1px solid ${isActive ? '#00f2fe' : 'rgba(255,255,255,0.15)'}; background: ${isActive ? 'linear-gradient(135deg, #00f2fe, #3b82f6)' : 'rgba(255,255,255,0.05)'}; color: ${isActive ? '#ffffff' : '#cbd5e1'}; font-weight: 700; font-size: 0.82rem; cursor: pointer; transition: all 0.2s; box-shadow: ${isActive ? '0 0 12px rgba(0,242,254,0.4)' : 'none'};">
                ${i}
            </button>
        `;
    }

    // Next Button (>)
    const nextDisabled = currentPage === totalPages;
    buttonsHtml += `
        <button type="button" onclick="${onPageChangeFn}(${currentPage + 1})" ${nextDisabled ? 'disabled' : ''} 
            style="padding: 6px 12px; border-radius: 8px; border: 1px solid ${nextDisabled ? 'rgba(255,255,255,0.08)' : 'rgba(0,242,254,0.3)'}; background: ${nextDisabled ? 'rgba(255,255,255,0.03)' : 'rgba(0,242,254,0.12)'}; color: ${nextDisabled ? '#475569' : '#38bdf8'}; font-weight: 700; font-size: 0.82rem; cursor: ${nextDisabled ? 'not-allowed' : 'pointer'}; transition: all 0.2s;">
            &gt;
        </button>
    `;

    buttonsHtml += '</div>';
    container.innerHTML = infoHtml + buttonsHtml;
}

function changeMasterPage(page) {
    masterCurrentPage = page;
    filterAdminLogs();
}

function changeLatenessPage(page) {
    latenessCurrentPage = page;
    renderAdminLatenessTable();
}

function changeUserLogsPage(page) {
    userLogsCurrentPage = page;
    loadLogs();
}

function normalizeDateStr(rawDate) {
    if (!rawDate) return '';
    const str = String(rawDate).trim();
    if (!str) return '';
    
    const parts = str.split(/[-/.]/);
    if (parts.length === 3) {
        if (parts[0].length === 4) { // YYYY-MM-DD
            const year = parseInt(parts[0], 10);
            if (year < 2000) return 'INVALID';
            return `${parts[0]}-${parts[1].padStart(2, '0')}-${parts[2].padStart(2, '0')}`;
        } else if (parts[2].length === 4) { // DD/MM/YYYY
            const year = parseInt(parts[2], 10);
            if (year < 2000) return 'INVALID';
            const day = parts[0].padStart(2, '0');
            const month = parts[1].padStart(2, '0');
            return `${year}-${month}-${day}`;
        }
    }
    
    if (/^\d{4}-\d{2}-\d{2}$/.test(str)) {
        const year = parseInt(str.substring(0, 4), 10);
        if (year < 2000) return 'INVALID';
        return str;
    }

    const d = new Date(str);
    if (!isNaN(d.getTime())) {
        if (d.getFullYear() < 2000) return 'INVALID';
        return d.toLocaleDateString('en-CA');
    }
    return str;
}

function renderAdminLatenessTable(recordsToRender) {
    const tbody = document.getElementById('admin-lateness-body');
    if (!tbody) return;

    const records = recordsToRender || allAdminRecords || [];
    const searchVal = (document.getElementById('lateness-search')?.value || '').toLowerCase().trim();
    const filterVal = document.getElementById('lateness-filter')?.value || 'all';

    const latenessDatePick = document.getElementById('lateness-date-filter')?.value || document.getElementById('lateness-drawer-date-filter')?.value || '';
    const targetDate = latenessDatePick ? normalizeDateStr(latenessDatePick) : '';

    tbody.innerHTML = '';

    const rawCheckinRecords = records.filter(r => {
        const typeLower = (r.type || '').toLowerCase();
        return typeLower.includes('دخول') || typeLower.includes('check-in');
    });

    // Deduplicate by (email + date) taking earliest check-in time for accurate daily representation
    const uniqueCheckinsMap = new Map();
    rawCheckinRecords.forEach(r => {
        const key = `${(r.email || '').toLowerCase().trim()}_${r.date}`;
        if (!uniqueCheckinsMap.has(key)) {
            uniqueCheckinsMap.set(key, r);
        } else {
            const existing = uniqueCheckinsMap.get(key);
            if ((r.time || '') < (existing.time || '')) {
                uniqueCheckinsMap.set(key, r);
            }
        }
    });
    const checkinRecords = Array.from(uniqueCheckinsMap.values());

    const filtered = checkinRecords.filter(r => {
        const name = (r.name || '').toLowerCase();
        const email = (r.email || '').toLowerCase();
        const matchesSearch = !searchVal || name.includes(searchVal) || email.includes(searchVal);
        
        let matchesDate = true;
        if (targetDate === 'INVALID') {
            matchesDate = false;
        } else if (targetDate) {
            const rDateNorm = normalizeDateStr(r.date);
            matchesDate = (rDateNorm === targetDate);
        }

        const minsLate = calculateMinutesLateAfter9(r.time);
        let matchesFilter = true;

        if (filterVal === 'grace') {
            matchesFilter = minsLate > 0 && minsLate <= 15;
        } else if (filterVal === 'late') {
            matchesFilter = minsLate > 15 && minsLate <= 60;
        } else if (filterVal === 'deduction') {
            matchesFilter = minsLate > 60;
        }

        return matchesSearch && matchesFilter && matchesDate;
    });

    const isAr = currentLang === 'ar';

    if (filtered.length === 0) {
        const noRecordsText = isAr ? 'لا توجد سجلات تأخير مطابقة معايير البحث والفلترة.' : 'No lateness records matching search criteria.';
        tbody.innerHTML = `<tr><td colspan="5" style="text-align: center; padding: 18px; color: #94a3b8;">${noRecordsText}</td></tr>`;
        renderPaginationBar('lateness-pagination-container', 1, 0, 0, 'changeLatenessPage');
        return;
    }

    filtered.sort((a, b) => (b.date + ' ' + b.time).localeCompare(a.date + ' ' + a.time));

    const totalItems = filtered.length;
    const totalPages = Math.ceil(totalItems / PAGE_SIZE) || 1;
    if (latenessCurrentPage > totalPages) latenessCurrentPage = totalPages;
    if (latenessCurrentPage < 1) latenessCurrentPage = 1;

    const pageRecords = filtered.slice((latenessCurrentPage - 1) * PAGE_SIZE, latenessCurrentPage * PAGE_SIZE);

    pageRecords.forEach(r => {
        const minsLate = calculateMinutesLateAfter9(r.time);
        
        let statusBadge = '';
        let minsText = '';

        if (minsLate === 0) {
            minsText = isAr ? '<span style="color:#34d399; font-weight:700;">0 دقيقة (في الوقت 09:00 ص)</span>' : '<span style="color:#34d399; font-weight:700;">0 mins (On Time 09:00 AM)</span>';
            statusBadge = isAr ? '<span style="display:inline-block; white-space:nowrap; background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.3); color:#6ee7b7; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟢 مبكر / في الوقت المحدد</span>' : '<span style="display:inline-block; white-space:nowrap; background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.3); color:#6ee7b7; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟢 On Time / Early</span>';
        } else if (minsLate <= 15) {
            minsText = isAr ? `<span style="color:#6ee7b7; font-weight:700;">${minsLate} دقيقة بعد 09:00</span>` : `<span style="color:#6ee7b7; font-weight:700;">${minsLate} mins after 09:00</span>`;
            statusBadge = isAr ? '<span style="display:inline-block; white-space:nowrap; background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.3); color:#6ee7b7; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟢 ضمن فترة السماح (15 دقيقة)</span>' : '<span style="display:inline-block; white-space:nowrap; background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.3); color:#6ee7b7; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟢 Grace Period (15 Mins)</span>';
        } else if (minsLate <= 60) {
            const timeDesc = isAr 
                ? `${minsLate} دقيقة (${Math.floor(minsLate/60) > 0 ? Math.floor(minsLate/60) + 'س و ' : ''}${minsLate%60}د)`
                : `${minsLate} mins (${Math.floor(minsLate/60) > 0 ? Math.floor(minsLate/60) + 'h ' : ''}${minsLate%60}m)`;
            minsText = `<span style="color:#fbbf24; font-weight:700;">${timeDesc}</span>`;
            statusBadge = isAr ? '<span style="display:inline-block; white-space:nowrap; background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.3); color:#fde68a; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">⚠️ تأخير بسيط (بدون خصم راتب)</span>' : '<span style="display:inline-block; white-space:nowrap; background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.3); color:#fde68a; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">⚠️ Minor Lateness (No Deduction)</span>';
        } else {
            const hrs = Math.floor(minsLate / 60);
            const remMins = minsLate % 60;
            const timeFormatted = isAr
                ? (hrs > 0 ? `${hrs} ساعة و ${remMins} دقيقة` : `${minsLate} دقيقة`)
                : (hrs > 0 ? `${hrs} hrs and ${remMins} mins` : `${minsLate} mins`);
            minsText = `<span style="color:#f87171; font-weight:800;">${timeFormatted} ${isAr ? 'تأخير' : 'Late'}</span>`;
            statusBadge = isAr ? '<span style="display:inline-block; white-space:nowrap; background:rgba(239,68,68,0.2); border:1px solid rgba(239,68,68,0.4); color:#fca5a5; padding:4px 10px; border-radius:12px; font-weight:800; font-size:0.75rem;">🚨 تأخير شديد (>60د) - خصم نصف يوم</span>' : '<span style="display:inline-block; white-space:nowrap; background:rgba(239,68,68,0.2); border:1px solid rgba(239,68,68,0.4); color:#fca5a5; padding:4px 10px; border-radius:12px; font-weight:800; font-size:0.75rem;">🚨 Severe Lateness (>60m) - Half-Day Deduction</span>';
        }

        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid rgba(255, 255, 255, 0.05)';
        tr.innerHTML = `
            <td style="padding: 10px 14px; font-weight: 700; color: #fff;">👤 ${r.name || (isAr ? 'موظف' : 'Employee')}</td>
            <td style="padding: 10px 14px; color: #94a3b8; font-size: 0.78rem;">📧 ${r.email || ''}</td>
            <td style="padding: 10px 14px; text-align: center; color: #cbd5e1; font-weight: 600; white-space: nowrap;">🕒 ${r.time || '--:--'} <span style="font-size:0.7rem; color:#64748b;">(${r.date || ''})</span></td>
            <td style="padding: 10px 14px; text-align: center;">${minsText}</td>
            <td style="padding: 10px 14px; text-align: center;">${statusBadge}</td>
        `;
        tbody.appendChild(tr);
    });

    renderPaginationBar('lateness-pagination-container', latenessCurrentPage, totalPages, totalItems, 'changeLatenessPage');
}

function renderAdminLogsTable(recordsToRender) {
    const tbody = document.getElementById('admin-logs-body');
    if (!tbody) return;
    
    tbody.innerHTML = '';
    
    if (!recordsToRender || recordsToRender.length === 0) {
        const emptyText = translations[currentLang]?.badgeEmpty || 'لا توجد سجلات';
        tbody.innerHTML = `<tr><td colspan="6" style="text-align: center; color: var(--text-muted); padding: 18px;">${emptyText}</td></tr>`;
        renderPaginationBar('master-pagination-container', 1, 0, 0, 'changeMasterPage');
        return;
    }

    // Group records by email + date to pair Check-In and Check-Out times together
    const groupedMap = new Map();
    
    recordsToRender.forEach(r => {
        const emailKey = (r.email || '').toLowerCase().trim();
        const dateKey = r.date || '';
        const key = `${emailKey}_${dateKey}`;
        
        if (!groupedMap.has(key)) {
            groupedMap.set(key, {
                name: r.name || 'موظف',
                email: r.email || '',
                date: r.date || '',
                checkinTime: '',
                checkoutTime: '',
                isAbsent: false,
                hasMovement: false
            });
        }
        
        const item = groupedMap.get(key);
        const typeLower = (r.type || '').toLowerCase();
        
        if (typeLower === 'تسجيل دخول' || typeLower === 'check-in') {
            item.checkinTime = r.time || '';
            item.hasMovement = true;
        } else if (typeLower === 'تسجيل خروج' || typeLower === 'check-out') {
            item.checkoutTime = r.time || '';
            item.hasMovement = true;
        } else if (typeLower === 'غياب' || typeLower === 'absent') {
            item.isAbsent = true;
        }
    });

    const isAr = currentLang === 'ar';
    const groupedList = Array.from(groupedMap.values());
    groupedList.sort((a, b) => (b.date + ' ' + (b.checkinTime || b.checkoutTime)).localeCompare(a.date + ' ' + (a.checkinTime || a.checkoutTime)));

    const totalItems = groupedList.length;
    const totalPages = Math.ceil(totalItems / PAGE_SIZE) || 1;
    if (masterCurrentPage > totalPages) masterCurrentPage = totalPages;
    if (masterCurrentPage < 1) masterCurrentPage = 1;

    const pageGrouped = groupedList.slice((masterCurrentPage - 1) * PAGE_SIZE, masterCurrentPage * PAGE_SIZE);

    pageGrouped.forEach(item => {
        let checkinDisplay = item.checkinTime 
            ? `<span style="color:#34d399; font-weight:700;">🟢 ${item.checkinTime}</span>` 
            : `<span style="color:#64748b; font-weight:600;">--:--</span>`;
            
        let checkoutDisplay = item.checkoutTime 
            ? `<span style="color:#60a5fa; font-weight:700;">🔴 ${item.checkoutTime}</span>` 
            : `<span style="color:#64748b; font-weight:600;">--:--</span>`;

        let statusBadge = '';
        if (item.isAbsent) {
            statusBadge = isAr
                ? '<span style="display:inline-block; white-space:nowrap; background:rgba(239,68,68,0.15); border:1px solid rgba(239,68,68,0.3); color:#fca5a5; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🔴 غياب مسجّل</span>'
                : '<span style="display:inline-block; white-space:nowrap; background:rgba(239,68,68,0.15); border:1px solid rgba(239,68,68,0.3); color:#fca5a5; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🔴 Absent</span>';
        } else if (item.checkinTime && item.checkoutTime) {
            statusBadge = isAr
                ? '<span style="display:inline-block; white-space:nowrap; background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.3); color:#6ee7b7; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟢 مكتمل (حضور وانصراف)</span>'
                : '<span style="display:inline-block; white-space:nowrap; background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.3); color:#6ee7b7; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟢 Complete (In & Out)</span>';
        } else if (item.checkinTime) {
            statusBadge = isAr
                ? '<span style="display:inline-block; white-space:nowrap; background:rgba(59,130,246,0.15); border:1px solid rgba(59,130,246,0.3); color:#93c5fd; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🔵 متواجد بالعمل (تم الحضور)</span>'
                : '<span style="display:inline-block; white-space:nowrap; background:rgba(59,130,246,0.15); border:1px solid rgba(59,130,246,0.3); color:#93c5fd; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🔵 On Duty (Checked In)</span>';
        } else if (item.checkoutTime) {
            statusBadge = isAr
                ? '<span style="display:inline-block; white-space:nowrap; background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.3); color:#fde68a; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟠 تسجيل خروج فقط</span>'
                : '<span style="display:inline-block; white-space:nowrap; background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.3); color:#fde68a; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟠 Check-Out Only</span>';
        }

        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid rgba(255, 255, 255, 0.05)';
        tr.innerHTML = `
            <td style="padding: 10px 14px; font-weight: 700; color: #fff;">👤 ${item.name}</td>
            <td style="padding: 10px 14px; color: #94a3b8; font-size: 0.78rem;">📧 ${item.email}</td>
            <td style="padding: 10px 14px; text-align: center; color: #cbd5e1; font-weight: 600; white-space: nowrap;">📅 ${item.date}</td>
            <td style="padding: 10px 14px; text-align: center;">${checkinDisplay}</td>
            <td style="padding: 10px 14px; text-align: center;">${checkoutDisplay}</td>
            <td style="padding: 10px 14px; text-align: center;">${statusBadge}</td>
        `;
        tbody.appendChild(tr);
    });

    renderPaginationBar('master-pagination-container', masterCurrentPage, totalPages, totalItems, 'changeMasterPage');
}

function filterAdminLogs() {
    const searchVal = (document.getElementById('admin-search')?.value || "").trim().toLowerCase();
    const selectedDate = document.getElementById('admin-date-filter')?.value || document.getElementById('admin-drawer-date-filter')?.value || "";
    const statusVal = document.getElementById('admin-status-filter')?.value || "all";
    
    const targetDate = selectedDate ? normalizeDateStr(selectedDate) : "";

    const filtered = allAdminRecords.filter(record => {
        // 1. Search term match
        const matchesSearch = !searchVal || 
            (record.name && record.name.toLowerCase().includes(searchVal)) || 
            (record.email && record.email.toLowerCase().includes(searchVal));
            
        // 2. Date match (empty means show all dates)
        let matchesDate = true;
        if (targetDate === 'INVALID') {
            matchesDate = false;
        } else if (targetDate) {
            const rDateNorm = normalizeDateStr(record.date);
            matchesDate = (rDateNorm === targetDate);
        }
        
        // 3. Status match
        let matchesStatus = true;
        if (statusVal !== 'all') {
            const typeLower = (record.type || '').toLowerCase();
            if (statusVal === 'check-in') {
                matchesStatus = typeLower.includes('check-in') || typeLower.includes('دخول');
            } else if (statusVal === 'check-out') {
                matchesStatus = typeLower.includes('check-out') || typeLower.includes('خروج');
            } else if (statusVal === 'absent') {
                matchesStatus = typeLower.includes('absent') || typeLower.includes('غياب');
            }
        }
        
        return matchesSearch && matchesDate && matchesStatus;
    });
    
    renderAdminLogsTable(filtered);
}

function clearAdminFilters() {
    const searchEl = document.getElementById('admin-search');
    const dateEl = document.getElementById('admin-date-filter');
    const statusEl = document.getElementById('admin-status-filter');
    
    if (searchEl) searchEl.value = '';
    if (dateEl) dateEl.value = '';
    if (statusEl) statusEl.value = 'all';
    
    renderAdminLogsTable(allAdminRecords);
}

function toggleMasterFiltersDrawer() {
    const drawer = document.getElementById('master-filters-drawer');
    const arrow = document.getElementById('master-filter-arrow');
    if (!drawer) return;
    
    if (drawer.style.display === 'none' || !drawer.style.display) {
        drawer.style.display = 'block';
        if (arrow) arrow.style.transform = 'rotate(180deg)';
    } else {
        drawer.style.display = 'none';
        if (arrow) arrow.style.transform = 'rotate(0deg)';
    }
}

function toggleLatenessFiltersDrawer() {
    const drawer = document.getElementById('lateness-filters-drawer');
    const arrow = document.getElementById('lateness-filter-arrow');
    if (!drawer) return;
    
    if (drawer.style.display === 'none' || !drawer.style.display) {
        drawer.style.display = 'block';
        if (arrow) arrow.style.transform = 'rotate(180deg)';
    } else {
        drawer.style.display = 'none';
        if (arrow) arrow.style.transform = 'rotate(0deg)';
    }
}

function showAiReportSection() {
    const userEmail = (localStorage.getItem('userEmail') || '').trim().toLowerCase();
    if (!isAdminEmail(userEmail)) return;
    const userGateway = document.getElementById('user-gateway-card');
    const userLogsCard = document.getElementById('user-logs-card');
    const adminSection = document.getElementById('admin-section');
    const aiReportSection = document.getElementById('ai-report-section');
    const chatDrawer = document.getElementById('ai-chat-drawer');
    
    // Hide floating chat window when opening full page report
    if (chatDrawer) chatDrawer.style.display = 'none';

    if (userGateway) userGateway.style.display = 'none';
    if (userLogsCard) userLogsCard.style.display = 'none';
    if (adminSection) adminSection.style.display = 'none';
    
    if (aiReportSection) {
        aiReportSection.style.display = 'block';
        aiReportSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    document.querySelectorAll('.nav-rail-item').forEach(item => item.classList.remove('active'));
    const aiNavItem = document.getElementById('nav-ai-report-item');
    if (aiNavItem) aiNavItem.classList.add('active');

    loadAiReportData();
}

function getAuthToken() {
    return localStorage.getItem('userToken') || localStorage.getItem('token') || sessionStorage.getItem('userToken') || sessionStorage.getItem('token') || '';
}

function formatAiWarningText(w, isAr) {
    if (!w) return '';
    if (isAr) {
        if (w.includes('Late for') && w.includes('consecutive days')) {
            const num = (w.match(/\d+/) || ['3'])[0];
            return `تأخر لـ ${num} أيام متتالية بعد 09:15 ص (يخضع للخصم والإنذار)`;
        }
        if (w.includes('Total recorded absences')) {
            const num = (w.match(/\d+/) || ['1'])[0];
            return `عدد أيام الغياب المسجلة: ${num} يوم`;
        }
        if (w.includes('Severe delay today')) {
            const timeMatch = (w.match(/\(\d{2}:\d{2}:\d{2}\)/) || [''])[0];
            return `تأخير شديد اليوم ${timeMatch}: يتجاوز 60 دقيقة - توصية بخصم نصف يوم حسب السياسة`;
        }
        if (w.includes('Lateness today')) {
            const timeMatch = (w.match(/\(\d{2}:\d{2}:\d{2}\)/) || [''])[0];
            return `تأخير اليوم ${timeMatch}: بعد وقت السماح (09:15 ص)`;
        }
        return w;
    } else {
        if (w.includes('تأخر لـ') || w.includes('أيام متتالية')) {
            const num = (w.match(/\d+/) || ['3'])[0];
            return `Late for ${num} consecutive days after 09:15 AM (Subject to deduction & warning)`;
        }
        if (w.includes('عدد أيام الغياب المسجلة') || w.includes('الغياب المسجلة')) {
            const num = (w.match(/\d+/) || ['1'])[0];
            return `Total recorded absences: ${num} days`;
        }
        if (w.includes('تأخير شديد اليوم')) {
            const timeMatch = (w.match(/\(\d{2}:\d{2}:\d{2}\)/) || [''])[0];
            return `Severe delay today ${timeMatch}: Exceeds 60 mins (Half day deduction recommended per policy)`;
        }
        if (w.includes('تأخير اليوم')) {
            const timeMatch = (w.match(/\(\d{2}:\d{2}:\d{2}\)/) || [''])[0];
            return `Lateness today ${timeMatch}: After 15m grace window (09:15 AM)`;
        }
        return w;
    }
}

function formatAiSummaryText(summary, isAr) {
    if (!summary) return '';
    if (summary.includes('Weekend') || summary.includes('عطلة نهاية الأسبوع') || summary.includes('Official Holiday') || summary.includes('عطلة رسمية')) {
        const dateMatch = summary.match(/\d{4}-\d{2}-\d{2}/)?.[0] || new Date().toISOString().split('T')[0];
        const isWeekendStr = summary.includes('Weekend') || summary.includes('عطلة نهاية الأسبوع');
        if (isWeekendStr) {
            return isAr
                ? `عطلة نهاية الأسبوع (الجمعة/السبت) / لا توجد حركات دوام متوقعة لليوم (${dateMatch}): أيام الدوام الرسمية من الأحد إلى الخميس، وانضباط السجلات مكتمل بنسبة 100%.`
                : `Weekend (Friday/Saturday) / No attendance logs required for (${dateMatch}): Standard working days are Sunday to Thursday. Compliance rate 100%.`;
        }
        return isAr
            ? `عطلة رسمية / لا توجد حركات دوام مسجلة لليوم (${dateMatch}): الكادر في عطلة رسمية وانضباط السجلات مكتمل بنسبة 100%.`
            : `Official Holiday / No attendance logs recorded for (${dateMatch}): All employees off, compliance rate 100%.`;
    }
    if (!isAr && (summary.includes('تحليل الانضباط') || summary.includes('حالة حضور'))) {
        const dateMatch = summary.match(/\d{4}-\d{2}-\d{2}/)?.[0] || new Date().toISOString().split('T')[0];
        const nums = summary.match(/\d+/g) || [];
        // nums will match year, month, day, checkin, absent, late15, graceMins, late60, severeMins
        const checkin = nums[3] || '0';
        const absent = nums[4] || '0';
        const late15 = nums[5] || '0';
        const late60 = nums[7] || '0';
        return `Discipline Analysis for Today (${dateMatch}): Recorded ${checkin} check-ins and ${absent} absences. Found ${late15} employees late after 15m grace window, with ${late60} exceeding 60m delay.`;
    }
    if (isAr && summary.includes('Discipline Analysis for Today')) {
        const dateMatch = summary.match(/\d{4}-\d{2}-\d{2}/)?.[0] || new Date().toISOString().split('T')[0];
        const nums = summary.match(/\d+/g) || [];
        const checkin = nums[3] || '0';
        const absent = nums[4] || '0';
        const late15 = nums[5] || '0';
        const late60 = nums[7] || '0';
        return `تحليل الانضباط لليوم (${dateMatch}): تم تسجيل ${checkin} حالة حضور و ${absent} غياب. يوجد ${late15} موظف متأخر عن مهلة 15 دقيقة، منها ${late60} تأخير يتجاوز 60 دقيقة.`;
    }
    return summary;
}

function isTestAccount(email, name) {
    if (!email) return false;
    const em = email.toLowerCase();
    const nm = (name || '').toLowerCase();
    if (em.includes('test_user') || em.includes('test_') || em.startsWith('test') || em.startsWith('emp_')) return true;
    if (nm.includes('test user') || nm.includes('new test employee') || nm.includes('اختبار') || nm === 'غير معروف') return true;
    return false;
}

function populateAiEmployeeDropdown(usersList) {
    const empSelect = document.getElementById('ai-report-employee-filter');
    if (!empSelect) return;
    
    const isAr = currentLang === 'ar';
    const currentVal = empSelect.value || 'all';
    
    const userMap = new Map();
    
    if (usersList && Array.isArray(usersList)) {
        usersList.forEach(u => {
            const em = (u && u.email) ? u.email.toLowerCase() : '';
            const nm = (u && u.name) ? u.name : '';
            if (em && !isAdminEmail(em) && !isTestAccount(em, nm)) {
                userMap.set(em, nm || em);
            }
        });
    }
    
    if (typeof allAdminRecords !== 'undefined' && Array.isArray(allAdminRecords)) {
        allAdminRecords.forEach(r => {
            const em = r.email ? r.email.toLowerCase() : '';
            const nm = r.name || r.user_name || '';
            if (em && !isAdminEmail(em) && !isTestAccount(em, nm) && !userMap.has(em)) {
                userMap.set(em, nm || em.split('@')[0]);
            }
        });
    }
    
    empSelect.innerHTML = `<option value="all">${isAr ? '👥 جميع الموظفين (All Employees)' : '👥 All Employees'}</option>`;
    
    userMap.forEach((name, email) => {
        const opt = document.createElement('option');
        opt.value = email;
        opt.textContent = `👤 ${name} (${email})`;
        if (email === currentVal) opt.selected = true;
        empSelect.appendChild(opt);
    });
    
    empSelect.setAttribute('data-loaded', 'true');
}

async function loadAiReportData() {
    const isAr = currentLang === 'ar';
    const matrixBody = document.getElementById('ai-risk-matrix-body');
    const insightsBox = document.getElementById('ai-insights-box');
    
    const kpiDiscipline = document.getElementById('ai-kpi-discipline');
    const kpiWarnings = document.getElementById('ai-kpi-warnings');
    const kpiSevere = document.getElementById('ai-kpi-severe');
    const kpiOntime = document.getElementById('ai-kpi-ontime');

    const empSelect = document.getElementById('ai-report-employee-filter');
    const empFilterWrapper = document.getElementById('ai-employee-filter-wrapper');
    const dateInput = document.getElementById('ai-report-date-filter');

    const userEmail = (localStorage.getItem('userEmail') || '').trim().toLowerCase();
    const isAdmin = isAdminEmail(userEmail);

    let selectedEmp = 'all';
    if (!isAdmin) {
        if (empFilterWrapper) empFilterWrapper.style.display = 'none';
        selectedEmp = userEmail;
    } else {
        if (empFilterWrapper) empFilterWrapper.style.display = 'flex';
        selectedEmp = empSelect ? empSelect.value : 'all';
    }

    const todayIso = new Date().toISOString().split('T')[0];
    const selectedDate = dateInput && dateInput.value ? dateInput.value : todayIso;

    if (dateInput && !dateInput.value) {
        dateInput.value = selectedDate;
    }

    try {
        const token = getAuthToken();
        const url = `${API_BASE}/api/ai/analytics?lang=${currentLang}&target_date=${encodeURIComponent(selectedDate)}&target_email=${encodeURIComponent(selectedEmp)}`;
        const resp = await fetch(url, {
            headers: token ? { 'Authorization': `Bearer ${token}` } : {}
        });
        
        let data = null;
        if (resp.ok) {
            data = await resp.json();
        }

        if (data && data.success) {
            populateAiEmployeeDropdown(data.all_users);

            const stats = data.stats || {};
            const isOffDay = (stats.checkin || 0) === 0 && (stats.absent || 0) === 0;

            let ontimeRate = 100;
            let totalWarnings = 0;
            let disciplineScore = 100;

            if (!isOffDay) {
                const ontimeCount = Math.max(0, (stats.checkin || 0) - (stats.late_15 || 0));
                ontimeRate = Math.round((ontimeCount / Math.max(1, stats.checkin || 1)) * 100);
                totalWarnings = (data.user_profiles || []).reduce((acc, p) => acc + (p.warning_count || 0), 0);
                disciplineScore = Math.max(60, 100 - (totalWarnings * 10) - ((stats.late_60 || 0) * 15));
            }

            if (kpiDiscipline) kpiDiscipline.textContent = `${disciplineScore}%`;
            if (kpiWarnings) kpiWarnings.textContent = totalWarnings;
            if (kpiSevere) kpiSevere.textContent = isOffDay ? 0 : (stats.late_60 || 0);
            if (kpiOntime) kpiOntime.textContent = `${ontimeRate}%`;

            const dossierCard = document.getElementById('ai-individual-dossier-card');
            if (selectedEmp !== 'all' && data.user_profiles && data.user_profiles.length > 0) {
                const targetProf = data.user_profiles.find(p => p.email && p.email.toLowerCase() === selectedEmp.toLowerCase()) || data.user_profiles[0];
                if (dossierCard) {
                    dossierCard.style.display = 'block';
                    
                    const avatarEl = document.getElementById('ai-dossier-avatar');
                    const nameEl = document.getElementById('ai-dossier-name');
                    const emailEl = document.getElementById('ai-dossier-email');
                    const badgeEl = document.getElementById('ai-dossier-rating-badge');
                    const logsEl = document.getElementById('ai-dossier-total-logs');
                    const late15El = document.getElementById('ai-dossier-late15');
                    const late60El = document.getElementById('ai-dossier-late60');
                    const absEl = document.getElementById('ai-dossier-absences');
                    const narrativeEl = document.getElementById('ai-dossier-narrative');

                    if (avatarEl) {
                        const parts = (targetProf.name || 'User').split(' ');
                        const initials = parts.length >= 2 ? (parts[0][0] + parts[1][0]).toUpperCase() : parts[0].substring(0, 2).toUpperCase();
                        avatarEl.textContent = initials;
                    }
                    if (nameEl) nameEl.textContent = targetProf.name || selectedEmp;
                    if (emailEl) emailEl.textContent = targetProf.email || selectedEmp;
                    
                    let ratingText = targetProf.rating || '';
                    let ratingColor = '#34d399';
                    if (ratingText.includes('خطر') || ratingText.includes('High Risk')) {
                        ratingColor = '#f87171';
                        ratingText = isAr ? 'خطر انضباط عالي ⚠️' : 'High Discipline Risk ⚠️';
                    } else if (ratingText.includes('تنبيه') || ratingText.includes('Warning')) {
                        ratingColor = '#fbbf24';
                        ratingText = isAr ? 'تنبيه انضباط 🟡' : 'Discipline Warning 🟡';
                    } else {
                        ratingText = isAr ? 'انضباط ممتاز 🟢' : 'Compliant 🟢';
                    }

                    if (badgeEl) {
                        badgeEl.textContent = ratingText;
                        badgeEl.style.color = ratingColor;
                        badgeEl.style.borderColor = ratingColor + '60';
                    }

                    let absentVal = stats.absent || 0;
                    if (absentVal === 0 && targetProf.warnings) {
                        const absWarn = targetProf.warnings.find(w => w.includes('غياب') || w.includes('absences') || w.includes('Absence'));
                        if (absWarn) {
                            const match = absWarn.match(/(\d+)/);
                            if (match) absentVal = parseInt(match[1], 10);
                        }
                    }

                    let late15Val = stats.late_15 || 0;
                    if (late15Val === 0 && targetProf.warnings) {
                        const lateWarn = targetProf.warnings.find(w => w.includes('تأخر') || w.includes('Late') || w.includes('late'));
                        if (lateWarn) {
                            const match = lateWarn.match(/(\d+)/);
                            if (match) late15Val = parseInt(match[1], 10);
                        }
                    }

                    if (logsEl) logsEl.textContent = (stats.checkin && stats.checkin > 0) ? stats.checkin : (late15Val + absentVal);
                    if (late15El) late15El.textContent = late15Val;
                    if (late60El) late60El.textContent = stats.late_60 || 0;
                    if (absEl) absEl.textContent = absentVal;

                    if (narrativeEl) {
                        const formattedSummary = formatAiSummaryText(data.summary, isAr);
                        const warningsList = (targetProf.warnings || []).map(w => `• ${formatAiWarningText(w, isAr)}`).join('<br>');
                        narrativeEl.innerHTML = `📌 <strong>${formattedSummary}</strong><br><br><div style="padding-top:6px; border-top: 1px dashed rgba(255,255,255,0.1);">${warningsList}</div>`;
                    }
                }
            } else {
                if (dossierCard) dossierCard.style.display = 'none';
            }

            if (insightsBox && data.summary) {
                const formattedSummary = formatAiSummaryText(data.summary, isAr);
                insightsBox.innerHTML = `📌 <strong>${isAr ? 'التقرير التنفيذي' : 'Executive Summary'}:</strong> ${formattedSummary}`;
            }

            globalAiUserProfiles = data.user_profiles || [];
            aiMatrixCurrentPage = 1;
            renderAiMatrixTable(aiMatrixCurrentPage);
        } else {
            renderLocalAiReportFallback();
        }
    } catch (err) {
        console.error('Failed to load AI Report data:', err);
        renderLocalAiReportFallback();
    }
}

function changeAiMatrixPage(newPage) {
    aiMatrixCurrentPage = newPage;
    renderAiMatrixTable(aiMatrixCurrentPage);
}

function renderAiMatrixTable(page) {
    const matrixBody = document.getElementById('ai-risk-matrix-body');
    if (!matrixBody) return;
    
    matrixBody.innerHTML = '';
    const isAr = currentLang === 'ar';
    const totalItems = globalAiUserProfiles.length;

    if (!totalItems || totalItems === 0) {
        matrixBody.innerHTML = `<tr><td colspan="5" style="text-align: center; padding: 18px; color: #94a3b8;">${isAr ? 'لا توجد بيانات سجلات أو مخاطر انضباط للموظف الملاحظ لهذا اليوم.' : 'No attendance logs or discipline risks found for target date.'}</td></tr>`;
        renderPaginationBar('ai-matrix-pagination-container', 1, 0, 0, 'changeAiMatrixPage');
        return;
    }

    const totalPages = Math.ceil(totalItems / PAGE_SIZE);
    const currentPage = Math.max(1, Math.min(page, totalPages));
    aiMatrixCurrentPage = currentPage;

    const startIdx = (currentPage - 1) * PAGE_SIZE;
    const pageProfiles = globalAiUserProfiles.slice(startIdx, startIdx + PAGE_SIZE);

    pageProfiles.forEach(p => {
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid rgba(255, 255, 255, 0.05)';
        
        let displayRating = p.rating || '';
        let ratingColor = '#34d399';

        if (displayRating.includes('خطر') || displayRating.includes('High Risk')) {
            ratingColor = '#f87171';
            displayRating = isAr ? 'خطر انضباط عالي ⚠️' : 'High Discipline Risk ⚠️';
        } else if (displayRating.includes('تنبيه') || displayRating.includes('Warning')) {
            ratingColor = '#fbbf24';
            displayRating = isAr ? 'تنبيه انضباط 🟡' : 'Discipline Warning 🟡';
        } else {
            displayRating = isAr ? 'ممتاز 🟢' : 'Compliant 🟢';
        }

        let aiRecommendation = '';
        if (displayRating.includes('خطر') || displayRating.includes('High Risk')) {
            aiRecommendation = isAr
                ? '💡 <strong>توصية HR الذكية:</strong> إصدار إنذار كتابي رسمي وتطبيق سياسة خصم التأخير/الغياب، وتحديد جلسة مراجعة انضباط مع الموارد البشرية.'
                : '💡 <strong>AI HR Recommendation:</strong> Issue formal written warning & apply attendance deduction policy. Schedule mandatory HR review.';
        } else if (displayRating.includes('تنبيه') || displayRating.includes('Warning')) {
            aiRecommendation = isAr
                ? '💡 <strong>توصية HR الذكية:</strong> توجيه إشعار شفهي ودّي وتذكير الموظف بمرونة الالتزام بمواعيد الحضور الرسمية.'
                : '💡 <strong>AI HR Recommendation:</strong> Issue friendly verbal reminder and monitor attendance times over next 14 days.';
        } else {
            aiRecommendation = isAr
                ? '🌟 <strong>توصية HR الذكية:</strong> سجل انضباط مثالي! يُوصى بتقديم إشادة أداء وترشيح الموظف لمكافأة الالتزام.'
                : '🌟 <strong>AI HR Recommendation:</strong> Exemplary punctuality! Recommended for HR Employee Recognition & Loyalty Bonus.';
        }

        let summaryText = '';
        if (p.warning_count > 0) {
            summaryText = isAr
                ? `<div style="font-size:0.75rem; color:#f87171; font-weight:700; margin-bottom:4px;">⚠️ تم رصد ${p.warning_count} حالة انضباط (تأخير/غياب)</div>`
                : `<div style="font-size:0.75rem; color:#f87171; font-weight:700; margin-bottom:4px;">⚠️ Detected ${p.warning_count} discipline incidents (lateness/absences)</div>`;
        } else {
            summaryText = isAr
                ? `<div style="font-size:0.75rem; color:#34d399; font-weight:700; margin-bottom:4px;">✅ التزام تام بمواعيد العمل</div>`
                : `<div style="font-size:0.75rem; color:#34d399; font-weight:700; margin-bottom:4px;">✅ Full compliance with working hours</div>`;
        }

        const warningDetails = `${summaryText}<div style="font-size:0.77rem; color:#cbd5e1; line-height:1.4;">${aiRecommendation}</div>`;

        tr.innerHTML = `
            <td style="padding: 10px 14px; font-weight: 700; color: #fff; white-space: nowrap;">👤 ${p.name}</td>
            <td style="padding: 10px 14px; color: #94a3b8; font-size: 0.78rem;">📧 ${p.email}</td>
            <td style="padding: 10px 14px; text-align: center;"><span style="display:inline-block; padding:4px 10px; border-radius:12px; font-weight:800; font-size:0.75rem; background:rgba(255,255,255,0.05); color:${ratingColor}; border:1px solid ${ratingColor}40;">${displayRating}</span></td>
            <td style="padding: 10px 14px; text-align: center; font-weight: 800; color: ${p.warning_count > 0 ? '#f87171' : '#6ee7b7'};">${p.warning_count}</td>
            <td style="padding: 10px 14px; color: #cbd5e1; font-size: 0.78rem; line-height: 1.4; max-width: 380px;">${warningDetails}</td>
        `;
        matrixBody.appendChild(tr);
    });

    renderPaginationBar('ai-matrix-pagination-container', currentPage, totalPages, totalItems, 'changeAiMatrixPage');
}

function renderLocalAiReportFallback() {
    const isAr = currentLang === 'ar';
    const matrixBody = document.getElementById('ai-risk-matrix-body');
    const insightsBox = document.getElementById('ai-insights-box');
    const dateInput = document.getElementById('ai-report-date-filter');
    const todayIso = new Date().toISOString().split('T')[0];
    const selectedDate = dateInput && dateInput.value ? dateInput.value : todayIso;
    
    const kpiDiscipline = document.getElementById('ai-kpi-discipline');
    const kpiWarnings = document.getElementById('ai-kpi-warnings');
    const kpiSevere = document.getElementById('ai-kpi-severe');
    const kpiOntime = document.getElementById('ai-kpi-ontime');

    const records = (selectedDate && selectedDate !== 'all') 
        ? (allAdminRecords || []).filter(r => r.date === selectedDate || (r.time && r.time.startsWith(selectedDate)))
        : (allAdminRecords || []);

    let checkins = 0;
    let late15 = 0;
    let late60 = 0;
    let absCount = 0;

    records.forEach(r => {
        const typeLower = (r.type || '').toLowerCase();
        if (typeLower.includes('دخول') || typeLower.includes('check-in')) {
            checkins++;
            const mins = calculateMinutesLateAfter9(r.time);
            if (mins > 15) late15++;
            if (mins > 60) late60++;
        } else if (typeLower.includes('غياب') || typeLower.includes('absent')) {
            absCount++;
        }
    });

    const ontime = Math.max(0, checkins - late15);
    const ontimeRate = checkins > 0 ? Math.round((ontime / checkins) * 100) : 100;
    const disciplineScore = Math.max(70, 100 - (late15 * 5) - (late60 * 15));

    if (kpiDiscipline) kpiDiscipline.textContent = `${disciplineScore}%`;
    if (kpiWarnings) kpiWarnings.textContent = late15;
    if (kpiSevere) kpiSevere.textContent = late60;
    if (kpiOntime) kpiOntime.textContent = `${ontimeRate}%`;

    if (insightsBox) {
        insightsBox.innerHTML = isAr
            ? `📌 <strong>التقرير التنفيذي لليوم (${selectedDate}):</strong> إجمالي حركات اليوم (${checkins + absCount})، تم تسجيل ${checkins} حضور و ${absCount} غياب. يوجد ${late15} موظف متأخر عن مهلة 15 دقيقة، منها ${late60} حالة تتجاوز 60 دقيقة وتتطلب اتخاذ إجراءات إدارية حسب سياسة الشركة.`
            : `📌 <strong>Executive Summary (${selectedDate}):</strong> Logged ${checkins} check-ins and ${absCount} absences. Identified ${late15} tardiness occurrences with ${late60} exceeding 60 minutes.`;
    }

    // Aggregate user risk profiles across allAdminRecords or current date records
    const sourceRecords = (allAdminRecords && allAdminRecords.length > 0) ? allAdminRecords : records;
    const userMap = {};

    sourceRecords.forEach(r => {
        const email = (r.email || 'unknown@nexuslink.com').toLowerCase();
        const name = r.name || r.user_name || email.split('@')[0];
        if (isTestAccount(email, name) || isAdminEmail(email)) return;

        if (!userMap[email]) {
            userMap[email] = {
                name: name,
                email: email,
                records: []
            };
        }
        userMap[email].records.push(r);
    });

    const userProfiles = [];
    Object.values(userMap).forEach(u => {
        let userLate15 = 0;
        let userLate60 = 0;
        let userAbsent = 0;
        const warnings = [];

        u.records.forEach(r => {
            const typeLower = (r.type || '').toLowerCase();
            if (typeLower.includes('دخول') || typeLower.includes('check-in')) {
                const mins = calculateMinutesLateAfter9(r.time);
                if (mins > 15) {
                    userLate15++;
                    if (mins > 60) {
                        userLate60++;
                        warnings.push(isAr ? `تأخر بتاريخ ${r.date} بمقدار ${mins} دقيقة` : `Late on ${r.date}: ${mins} mins`);
                    } else {
                        warnings.push(isAr ? `تأخر بتاريخ ${r.date} بمقدار ${mins} دقيقة` : `Late on ${r.date}: ${mins} mins`);
                    }
                }
            } else if (typeLower.includes('غياب') || typeLower.includes('absent')) {
                userAbsent++;
                warnings.push(isAr ? `تسجيل غياب بتاريخ ${r.date}` : `Absent on ${r.date}`);
            }
        });

        let rating = isAr ? 'ممتاز 🟢' : 'Compliant 🟢';
        if (userLate60 > 0 || userAbsent > 0) {
            rating = isAr ? 'خطر انضباط عالي ⚠️' : 'High Discipline Risk ⚠️';
        } else if (userLate15 > 0) {
            rating = isAr ? 'تنبيه انضباط 🟡' : 'Discipline Warning 🟡';
        }

        userProfiles.push({
            name: u.name,
            email: u.email,
            rating: rating,
            warning_count: warnings.length,
            warnings: warnings
        });
    });

    populateAiEmployeeDropdown(userProfiles);

    const empSelect = document.getElementById('ai-report-employee-filter');
    const selectedEmp = empSelect ? empSelect.value : 'all';
    const dossierCard = document.getElementById('ai-individual-dossier-card');

    if (selectedEmp !== 'all' && userProfiles.length > 0) {
        const targetProf = userProfiles.find(p => p.email.toLowerCase() === selectedEmp.toLowerCase()) || userProfiles[0];
        if (dossierCard && targetProf) {
            dossierCard.style.display = 'block';
            
            const avatarEl = document.getElementById('ai-dossier-avatar');
            const nameEl = document.getElementById('ai-dossier-name');
            const emailEl = document.getElementById('ai-dossier-email');
            const badgeEl = document.getElementById('ai-dossier-rating-badge');
            const logsEl = document.getElementById('ai-dossier-total-logs');
            const late15El = document.getElementById('ai-dossier-late15');
            const late60El = document.getElementById('ai-dossier-late60');
            const absEl = document.getElementById('ai-dossier-absences');
            const narrativeEl = document.getElementById('ai-dossier-narrative');

            if (avatarEl) {
                const parts = (targetProf.name || 'User').split(' ');
                const initials = parts.length >= 2 ? (parts[0][0] + parts[1][0]).toUpperCase() : parts[0].substring(0, 2).toUpperCase();
                avatarEl.textContent = initials;
            }
            if (nameEl) nameEl.textContent = targetProf.name;
            if (emailEl) emailEl.textContent = targetProf.email;

            let ratingText = targetProf.rating;
            let ratingColor = '#34d399';
            if (ratingText.includes('خطر') || ratingText.includes('High Risk')) {
                ratingColor = '#f87171';
            } else if (ratingText.includes('تنبيه') || ratingText.includes('Warning')) {
                ratingColor = '#fbbf24';
            }

            if (badgeEl) {
                badgeEl.textContent = ratingText;
                badgeEl.style.color = ratingColor;
                badgeEl.style.borderColor = ratingColor + '60';
            }

            const empRecs = (allAdminRecords || []).filter(r => r.email && r.email.toLowerCase() === targetProf.email.toLowerCase());
            let late15Val = 0, late60Val = 0, absVal = 0;
            empRecs.forEach(r => {
                const typeLower = (r.type || '').toLowerCase();
                if (typeLower.includes('دخول') || typeLower.includes('check-in')) {
                    const mins = calculateMinutesLateAfter9(r.time);
                    if (mins > 15) late15Val++;
                    if (mins > 60) late60Val++;
                } else if (typeLower.includes('غياب') || typeLower.includes('absent')) {
                    absVal++;
                }
            });

            if (logsEl) logsEl.textContent = empRecs.length;
            if (late15El) late15El.textContent = late15Val;
            if (late60El) late60El.textContent = late60Val;
            if (absEl) absEl.textContent = absVal;

            if (narrativeEl) {
                narrativeEl.innerHTML = isAr
                    ? `📌 <strong>التقرير التفصيلي للموظف (${targetProf.name}):</strong> تم رصد ${empRecs.length} حركة دوام مسجلة (${late15Val} حالة تأخير، ${absVal} حالة غياب). التوصية: ${ratingText.includes('خطر') ? 'إصدار إنذار وتطبييق لائحة الخصم مع جلسة تقييم HR.' : 'الحفاظ على الأداء الممتاز وترشيحه لمكافأة الالتزام.'}`
                    : `📌 <strong>Individual Employee Dossier (${targetProf.name}):</strong> Total ${empRecs.length} logs recorded (${late15Val} late, ${absVal} absent). Recommendation: ${ratingText.includes('High Risk') ? 'Enforce HR warning & 1-on-1 review.' : 'Maintain performance and recognize punctuality.'}`;
            }
        }

        globalAiUserProfiles = [targetProf];
    } else {
        if (dossierCard) dossierCard.style.display = 'none';
        globalAiUserProfiles = userProfiles;
    }

    aiMatrixCurrentPage = 1;
    renderAiMatrixTable(aiMatrixCurrentPage);
}

async function generateAiReport() {
    const isAr = currentLang === 'ar';
    const insightsBox = document.getElementById('ai-insights-box');
    if (insightsBox) {
        insightsBox.innerHTML = `⏳ <em>${isAr ? 'جاري تحليل بيانات الدوام وصياغة التقرير التنفيذي بواسطة محرك Gemini AI...' : 'Generating Executive AI Summary via Gemini AI...'}</em>`;
    }

    try {
        const token = localStorage.getItem('token');
        const prompt = isAr
            ? "اعطني ملخص تنفيذي شامل ودقيق للانضباط والحضور اليومي للموظفين وملاحظات الموارد البشرية وتطبيق سياسة الخصومات بناءً على داتا الحضور اليوم."
            : "Provide a detailed executive summary of employee attendance, lateness trends, and HR policy recommendations.";

        const resp = await fetch(`${API_BASE}/api/ai/prompt`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                ...(token ? { 'Authorization': `Bearer ${token}` } : {})
            },
            body: JSON.stringify({ prompt: prompt })
        });

        const data = await resp.json();
        if (data.success && data.response) {
            if (insightsBox) {
                insightsBox.innerHTML = `🚀 <strong>${isAr ? 'تقرير محرك Gemini AI التنفيذي' : 'Gemini AI Executive Narrative'}:</strong><br><br>${data.response}`;
            }
        } else {
            loadAiReportData();
        }
    } catch (err) {
        console.error('Failed to generate AI prompt report:', err);
        loadAiReportData();
    }
}

async function submitAdminAttendance(event) {
    event.preventDefault();
    
    const emailInput = document.getElementById('admin-email');
    const nameInput = document.getElementById('admin-name');
    const typeInput = document.getElementById('admin-type');
    
    if (!emailInput || !typeInput) return;
    
    const email = emailInput.value.trim();
    const name = nameInput ? nameInput.value.trim() : "";
    const type = typeInput.value;
    
    const payload = {
        email: email,
        type: type,
        name: name || "Unknown"
    };

    try {
        const token = localStorage.getItem('userToken');
        const response = await fetch(`${API_BASE}/api/attendance/create`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error("Failed to create attendance record");

        const result = await response.json();
        if (result.success) {
            // Clear form fields
            emailInput.value = '';
            if (nameInput) nameInput.value = '';
            typeInput.selectedIndex = 0;
            
            // Reload logs
            await loadAdminLogs();
            
            // Also reload user own logs just in case they created one for themselves
            if (email.toLowerCase() === localStorage.getItem('userEmail').toLowerCase()) {
                await loadLogs();
            }
            
            alert(currentLang === 'ar' ? 'تم تسجيل الحركة بنجاح!' : 'Attendance record logged successfully!');
        } else {
            throw new Error(result.error || "Unknown error");
        }
    } catch (err) {
        console.error("Error creating admin attendance:", err);
        const errMsg = currentLang === 'ar' ? 'فشل تسجيل الحركة: ' : 'Failed to record attendance: ';
        alert(errMsg + err.message);
    }
}

async function submitAdminCreateUser(event) {
    event.preventDefault();
    const nameInput = document.getElementById('admin-new-name');
    const emailInput = document.getElementById('admin-new-email');
    const passInput = document.getElementById('admin-new-password');
    
    if (!nameInput || !emailInput || !passInput) return;
    
    const name = nameInput.value.trim();
    const email = emailInput.value.trim();
    const password = passInput.value;
    
    if (!name || !email || !password) return;
    
    const formData = new FormData();
    formData.append('name', name);
    formData.append('email', email);
    formData.append('password', password);
    
    try {
        const response = await fetch(`${API_BASE}/api/register`, {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        if (result.success) {
            nameInput.value = '';
            emailInput.value = '';
            passInput.value = '';
            
            await loadAdminLogs();
            alert(currentLang === 'ar' ? 'تم إضافة حساب الموظف في قاعدة البيانات بنجاح!' : 'Employee account created in database successfully!');
        } else {
            const errDetail = result.error === 'email_exists' 
                ? (currentLang === 'ar' ? 'البريد الإلكتروني مسجل بالفعل!' : 'Email is already registered!')
                : (result.error || 'Failed to create user');
            alert(errDetail);
        }
    } catch (err) {
        console.error("Error creating employee account:", err);
        alert((currentLang === 'ar' ? 'فشل إضافة الحساب: ' : 'Failed to create user: ') + err.message);
    }
}

function updateClock() {
    const timeEl = document.getElementById('time');
    const dateEl = document.getElementById('date');
    if (!timeEl || !dateEl) return;

    const now = new Date();
    
    // Always keep digital time format in English ('en-US') as requested for clean appearance
    timeEl.textContent = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true });
    
    const dateLocale = currentLang === 'ar' ? 'ar-EG' : 'en-US';
    dateEl.textContent = now.toLocaleDateString(dateLocale, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
}

function updateDashboardGreeting() {
    const greetingEl = document.getElementById('dashboard-greeting');
    if (!greetingEl) return;

    const now = new Date();
    const hour = now.getHours();
    let greetKey = 'goodMorning';

    if (hour >= 12 && hour < 17) {
        greetKey = 'goodAfternoon';
    } else if (hour >= 17 || hour < 5) {
        greetKey = 'goodEvening';
    }

    const name = localStorage.getItem('userName') || "";
    greetingEl.innerText = `${translations[currentLang][greetKey]}, ${name}`;
}

async function loadLogs() {
    const email = localStorage.getItem('userEmail');
    const tbody = document.getElementById('logs-body');
    if (!email || !tbody) return;

    try {
        const token = localStorage.getItem('userToken');
        const response = await fetch(`${API_BASE}/api/logs?email=${email}`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        if (!response.ok) throw new Error("Failed to load logs");
        const records = await response.json();
        
        tbody.innerHTML = '';
        const isAr = currentLang === 'ar';
        
        const dateInput = document.getElementById('user-drawer-date-filter');
        const selectedDate = dateInput ? dateInput.value.trim() : '';
        const targetDate = selectedDate ? normalizeDateStr(selectedDate) : '';

        let filteredRecords = records;
        if (targetDate === 'INVALID') {
            filteredRecords = [];
        } else if (targetDate) {
            filteredRecords = records.filter(r => normalizeDateStr(r.date) === targetDate);
        }

        const USER_LOGS_PAGE_SIZE = 5;
        if (!filteredRecords || filteredRecords.length === 0) {
            const noRecordsText = isAr ? 'لا توجد سجلات مطابقة لتاريخ الدوام المحدد' : 'No attendance logs matching selected date';
            tbody.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 18px;">${noRecordsText}</td></tr>`;
            renderPaginationBar('user-logs-pagination-container', 1, 0, 0, 'changeUserLogsPage', USER_LOGS_PAGE_SIZE);
            return;
        }

        const totalItems = filteredRecords.length;
        const totalPages = Math.ceil(totalItems / USER_LOGS_PAGE_SIZE) || 1;
        if (userLogsCurrentPage > totalPages) userLogsCurrentPage = totalPages;
        if (userLogsCurrentPage < 1) userLogsCurrentPage = 1;

        const pageRecords = filteredRecords.slice((userLogsCurrentPage - 1) * USER_LOGS_PAGE_SIZE, userLogsCurrentPage * USER_LOGS_PAGE_SIZE);

        pageRecords.forEach(record => {
            let statusBadge = "";
            const isAbsent = record.status === 'absent' || (record.in === '--:--' && record.out === '--:--');
            
            if (isAbsent) {
                statusBadge = isAr
                    ? '<span style="background:rgba(239,68,68,0.15); border:1px solid rgba(239,68,68,0.3); color:#fca5a5; padding:4px 12px; border-radius:12px; font-weight:700; font-size:0.75rem;">🔴 غياب مسجّل</span>'
                    : '<span style="background:rgba(239,68,68,0.15); border:1px solid rgba(239,68,68,0.3); color:#fca5a5; padding:4px 12px; border-radius:12px; font-weight:700; font-size:0.75rem;">🔴 Absent</span>';
            } else if (record.in !== '--:--' && record.out !== '--:--') {
                statusBadge = isAr
                    ? '<span style="background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.3); color:#6ee7b7; padding:4px 12px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟢 مكتمل (حضور وانصراف)</span>'
                    : '<span style="background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.3); color:#6ee7b7; padding:4px 12px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟢 Complete (In & Out)</span>';
            } else if (record.in !== '--:--') {
                statusBadge = isAr
                    ? '<span style="background:rgba(59,130,246,0.15); border:1px solid rgba(59,130,246,0.3); color:#93c5fd; padding:4px 12px; border-radius:12px; font-weight:700; font-size:0.75rem;">🔵 متواجد بالعمل (تم الحضور)</span>'
                    : '<span style="background:rgba(59,130,246,0.15); border:1px solid rgba(59,130,246,0.3); color:#93c5fd; padding:4px 12px; border-radius:12px; font-weight:700; font-size:0.75rem;">🔵 On Duty (Checked In)</span>';
            } else {
                statusBadge = isAr
                    ? '<span style="background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.3); color:#fde68a; padding:4px 12px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟠 انصراف فقط</span>'
                    : '<span style="background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.3); color:#fde68a; padding:4px 12px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟠 Checked Out Only</span>';
            }
            
            const inDisplay = record.in && record.in !== '--:--' 
                ? `<span style="color:#34d399; font-weight:700;">🟢 ${record.in}</span>` 
                : `<span style="color:#64748b; font-weight:600;">--:--</span>`;

            const outDisplay = record.out && record.out !== '--:--' 
                ? `<span style="color:#60a5fa; font-weight:700;">🔴 ${record.out}</span>` 
                : `<span style="color:#64748b; font-weight:600;">--:--</span>`;

            const tr = document.createElement('tr');
            tr.style.borderBottom = '1px solid rgba(255, 255, 255, 0.05)';
            tr.innerHTML = `
                <td style="padding: 8px 12px; text-align: center; color: #cbd5e1; font-weight: 700; white-space: nowrap;">📅 ${record.date}</td>
                <td style="padding: 8px 12px; text-align: center;">${inDisplay}</td>
                <td style="padding: 8px 12px; text-align: center;">${outDisplay}</td>
                <td style="padding: 8px 12px; text-align: center;">${statusBadge}</td>
            `;
            tbody.appendChild(tr);
        });

        renderPaginationBar('user-logs-pagination-container', userLogsCurrentPage, totalPages, totalItems, 'changeUserLogsPage', USER_LOGS_PAGE_SIZE);
    } catch (err) {
        console.error("Error loading logs:", err);
        const errText = currentLang === 'ar' ? 'فشل تحميل سجل العمليات' : 'Failed to load operation logs';
        tbody.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--error-color); padding: 16px;">${errText}</td></tr>`;
        renderPaginationBar('user-logs-pagination-container', 1, 0, 0, 'changeUserLogsPage', USER_LOGS_PAGE_SIZE);
    }
}

async function recordAttendance(type) {
    const email = localStorage.getItem('userEmail');
    const name = localStorage.getItem('userName') || "Unknown";
    if (!email) return;

    try {
        const token = typeof getAuthToken === 'function' ? getAuthToken() : (localStorage.getItem('userToken') || localStorage.getItem('token') || sessionStorage.getItem('userToken') || sessionStorage.getItem('token') || '');
        const headers = { 'Content-Type': 'application/json' };
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        const response = await fetch(`${API_BASE}/api/attendance/create`, { 
            method: 'POST', 
            headers: headers,
            body: JSON.stringify({
                email: email,
                name: name,
                type: type
            })
        });

        if (!response.ok) {
            let errMsg = "Failed to save attendance";
            try {
                const errData = await response.json();
                errMsg = errData.detail || errData.error || errMsg;
            } catch(e) {}
            throw new Error(errMsg);
        }

        // Reload logs in real-time
        await loadLogs();
        if (typeof isAdminEmail === 'function' && isAdminEmail(email)) {
            await loadAdminLogs();
        }
    } catch (err) {
        console.error("Error recording attendance:", err);
        alert(err.message);
    }
}

function logout() {
    localStorage.removeItem('userEmail');
    localStorage.removeItem('userName');
    localStorage.removeItem('userToken');
    window.location.href = 'index.html';
}

function exportAdminLogsToCSV() {
    const searchVal = (document.getElementById('admin-search')?.value || "").trim().toLowerCase();
    const dateVal = document.getElementById('admin-date-filter')?.value || "";
    const statusVal = document.getElementById('admin-status-filter')?.value || "all";
    
    const recordsToExport = allAdminRecords.filter(record => {
        const matchesSearch = !searchVal || 
            (record.name && record.name.toLowerCase().includes(searchVal)) || 
            (record.email && record.email.toLowerCase().includes(searchVal));
        const matchesDate = !dateVal || record.date === dateVal;
        
        let matchesStatus = true;
        if (statusVal !== 'all') {
            const typeLower = record.type.toLowerCase();
            if (statusVal === 'check-in') {
                matchesStatus = typeLower === 'check-in' || typeLower === 'تسجيل دخول';
            } else if (statusVal === 'check-out') {
                matchesStatus = typeLower === 'check-out' || typeLower === 'تسجيل خروج';
            } else if (statusVal === 'absent') {
                matchesStatus = typeLower === 'absent' || typeLower === 'غياب';
            }
        }
        return matchesSearch && matchesDate && matchesStatus;
    });

    // Create CSV content with UTF-8 BOM for Excel Arabic support
    let csvContent = "\uFEFF"; 
    csvContent += "اسم الموظف,البريد الإلكتروني,الحركة,التاريخ,الوقت\n";
    
    recordsToExport.forEach(rec => {
        const row = [
            `"${rec.name || ''}"`,
            `"${rec.email || ''}"`,
            `"${rec.type || ''}"`,
            `"${rec.date || ''}"`,
            `"${rec.time || ''}"`
        ];
        csvContent += row.join(",") + "\n";
    });

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.setAttribute("href", url);
    
    let filename = "attendance_full_logs.csv";
    if (dateVal) {
        filename = `attendance_logs_${dateVal}.csv`;
    }
    
    link.setAttribute("download", filename);
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

let globalUserProfiles = [];

async function loadAIAdminAnalytics() {
    const summaryEl = document.getElementById('ai-summary-text');
    const chipsContainer = document.getElementById('ai-user-chips-container');
    if (!summaryEl || !chipsContainer) return;

    try {
        const token = localStorage.getItem('userToken');
        const res = await fetch(`${API_BASE}/api/ai/analytics`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        if (!res.ok) return;
        const data = await res.json();
        if (data.success) {
            summaryEl.textContent = data.summary;
            globalUserProfiles = data.user_profiles || [];
            
            chipsContainer.innerHTML = '';
            
            if (globalUserProfiles.length === 0) {
                chipsContainer.innerHTML = '<div style="color: var(--text-muted); font-size: 0.8rem;">لا يوجد موظفون مسجلون حالياً.</div>';
                return;
            }

            globalUserProfiles.forEach(u => {
                const badgeColor = u.warning_count > 0 ? 'background: rgba(239, 68, 68, 0.2); border-color: rgba(239, 68, 68, 0.4); color: #fca5a5;' : 'background: rgba(16, 185, 129, 0.12); border-color: rgba(16, 185, 129, 0.3); color: #6ee7b7;';
                const warnBadge = u.warning_count > 0 ? ` <span style="background: #ef4444; color: #fff; padding: 1px 6px; border-radius: 10px; font-size: 0.7rem; font-weight: 800;">⚠️ ${u.warning_count}</span>` : '';
                
                const chipBtn = document.createElement('button');
                chipBtn.type = 'button';
                chipBtn.style.cssText = `padding: 6px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 600; cursor: pointer; transition: all 0.2s ease; border: 1px solid; outline: none; ${badgeColor}`;
                chipBtn.innerHTML = `👤 ${u.name} (${u.email})${warnBadge}`;
                chipBtn.onclick = () => selectAIUserInspection(u.email);
                
                chipsContainer.appendChild(chipBtn);
            });
        }
    } catch(err) {
        console.error("AI Analytics error:", err);
    }
}

function selectAIUserInspection(email) {
    const detailCard = document.getElementById('ai-user-detail-card');
    if (!detailCard) return;

    const user = globalUserProfiles.find(u => u.email.toLowerCase() === email.toLowerCase());
    if (!user) return;

    detailCard.style.display = 'block';
    
    let warningsHTML = '';
    if (user.warnings && user.warnings.length > 0) {
        warningsHTML = user.warnings.map(w => `<li style="margin-bottom: 4px; color: #fca5a5;">⚠️ ${w}</li>`).join('');
    } else {
        warningsHTML = '<li style="color: #4ade80;">✅ لا يوجد أي تحذيرات أو مخالفات مسجلة على هذا الموظف.</li>';
    }

    detailCard.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; flex-wrap: wrap; gap: 8px;">
            <div style="font-weight: 700; color: #c084fc; font-size: 0.9rem;">
                📋 تقرير انضباط الموظف: <span style="color: #fff;">${user.name}</span> (${user.email})
            </div>
            <span style="font-size: 0.78rem; background: rgba(192, 132, 252, 0.2); color: #e9d5ff; padding: 4px 10px; border-radius: 12px; font-weight: 700;">
                التقييم الآلي: ${user.rating}
            </span>
        </div>
        <div style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 6px;">
            إجمالي التحذيرات والمخالفات المكتشفة: <strong style="color: #fff;">${user.warning_count}</strong>
        </div>
        <ul style="margin: 0; padding-inline-start: 20px; font-size: 0.83rem;">
            ${warningsHTML}
        </ul>
    `;
}

function updateAiQuickOptionsUI() {
    const email = localStorage.getItem('userEmail');
    const container = document.getElementById('admin-ai-quick-options');
    const roleBadge = document.getElementById('ai-role-badge');
    if (!container) return;

    const isAdmin = isAdminEmail(email);
    const isAr = currentLang === 'ar';

    if (roleBadge) {
        if (isAdmin) {
            roleBadge.textContent = isAr ? 'المدير العام' : 'EXECUTIVE';
            roleBadge.className = 'ai-role-tag admin-badge';
        } else {
            roleBadge.textContent = isAr ? 'موظف' : 'EMPLOYEE';
            roleBadge.className = 'ai-role-tag employee-badge';
        }
    }

    if (isAdmin) {
        container.innerHTML = `
            <button type="button" class="ai-quick-chip-btn highlight-chip" onclick="selectAdminAiOption('summary')">
                <span>📊</span> <span>${isAr ? 'ملخص دوام اليوم' : "Today's Summary"}</span>
            </button>
            <button type="button" class="ai-quick-chip-btn highlight-chip" onclick="selectAdminAiOption('excuses')">
                <span>📑</span> <span>${isAr ? 'فحص وتدقيق الأعذار' : 'Audit Excuses'}</span>
            </button>
            <button type="button" class="ai-quick-chip-btn" onclick="selectAdminAiOption('lateness')">
                <span>⚠️</span> <span>${isAr ? 'قواعد التأخير والخصم' : 'Lateness Rules'}</span>
            </button>
            <button type="button" class="ai-quick-chip-btn" onclick="selectAdminAiOption('roster')">
                <span>👥</span> <span>${isAr ? 'كادر الموظفين والغيابات' : 'Workforce Roster'}</span>
            </button>
        `;
    } else {
        container.innerHTML = `
            <button type="button" class="ai-quick-chip-btn highlight-cyan" onclick="selectAdminAiOption('mystatus')">
                <span>🕒</span> <span>${isAr ? 'حالة حضوري وتأخيري اليوم' : 'My Status Today'}</span>
            </button>
            <button type="button" class="ai-quick-chip-btn" onclick="selectAdminAiOption('lateness')">
                <span>⚠️</span> <span>${isAr ? 'فترة السماح والخصومات' : 'Grace & Penalties'}</span>
            </button>
            <button type="button" class="ai-quick-chip-btn" onclick="selectAdminAiOption('hours')">
                <span>📅</span> <span>${isAr ? 'ساعات وأيام العمل' : 'Shift Hours'}</span>
            </button>
            <button type="button" class="ai-quick-chip-btn" onclick="selectAdminAiOption('excuse_rules')">
                <span>📝</span> <span>${isAr ? 'شروط ومهلة الأعذار والكروكة' : 'Excuse Rules & Proof'}</span>
            </button>
        `;
    }
}

function toggleAIChatMaximize() {
    const drawer = document.getElementById('ai-chat-drawer');
    const maxBtn = document.getElementById('ai-maximize-btn');
    if (!drawer) return;
    drawer.classList.toggle('maximized');
    if (maxBtn) {
        maxBtn.textContent = drawer.classList.contains('maximized') ? '🗗' : '⛶';
    }
}

function toggleAIChatDrawer() {
    const drawer = document.getElementById('ai-chat-drawer');
    if (!drawer) return;
    if (drawer.style.display === 'none' || !drawer.style.display) {
        updateAiQuickOptionsUI();
        const msgBox = document.getElementById('ai-chat-messages');
        const hasMessages = msgBox && msgBox.querySelectorAll('.user-msg, .ai-resp-card').length > 0;
        if (!hasMessages) {
            clearAIChatHistory();
        }
        drawer.style.display = 'flex';
        const inp = document.getElementById('ai-chat-input');
        if (inp) inp.focus();
    } else {
        drawer.style.display = 'none';
    }
}

function toggleAiDrawer() {
    toggleAIChatDrawer();
}

function copyAiResponse(btn) {
    if (!btn) return;
    const card = btn.closest('.ai-msg.bot-msg') || btn.closest('.ai-resp-card');
    if (!card) return;
    const textToCopy = card.innerText.replace(/📋|نسخ|Copy/g, '').trim();
    navigator.clipboard.writeText(textToCopy).then(() => {
        const orig = btn.innerHTML;
        btn.innerHTML = '✅ <span style="font-size:0.7rem;">تم النسخ</span>';
        setTimeout(() => { btn.innerHTML = orig; }, 2000);
    }).catch(err => {
        console.error("Copy failed", err);
    });
}

function clearAIChatHistory() {
    window._aiChatMemory = [];
    const msgBox = document.getElementById('ai-chat-messages');
    if (!msgBox) return;
    const isAr = currentLang === 'ar';
    const email = localStorage.getItem('userEmail');
    const isAdmin = isAdminEmail(email);

    const welcomeHeader = isAr 
        ? `مرحباً بك في المساعد الذكي لنظام NexusLink`
        : `Welcome to NexusLink AI`;

    const welcomeDesc = isAr
        ? `كيف يمكنني مساعدتك في سياسات وسجلات الدوام اليوم؟`
        : `How can I assist you with your attendance today?`;

    const tilesHTML = isAr ? `
        <div class="welcome-style-a-grid">
            ${isAdmin 
                ? `<div class="style-a-tile status" onclick="selectAdminAiOption('summary')">
                       <div class="style-a-icon">📊</div>
                       <div class="style-a-text">
                           <div class="style-a-title">ملخص اليوم</div>
                           <div class="style-a-sub">الحضور المباشر</div>
                       </div>
                   </div>
                   <div class="style-a-tile lateness" onclick="selectAdminAiOption('excuses')">
                       <div class="style-a-icon">📑</div>
                       <div class="style-a-text">
                           <div class="style-a-title">تدقيق الأعذار</div>
                           <div class="style-a-sub">فحص الطلبات</div>
                       </div>
                   </div>
                   <div class="style-a-tile excuse" onclick="selectAdminAiOption('lateness')">
                       <div class="style-a-icon">⚠️</div>
                       <div class="style-a-text">
                           <div class="style-a-title">قواعد التأخير</div>
                           <div class="style-a-sub">الخصم والإنذارات</div>
                       </div>
                   </div>
                   <div class="style-a-tile leaves" onclick="selectAdminAiOption('roster')">
                       <div class="style-a-icon">👥</div>
                       <div class="style-a-text">
                           <div class="style-a-title">كادر الموظفين</div>
                           <div class="style-a-sub">سجلات الكادر</div>
                       </div>
                   </div>`
                : `<div class="style-a-tile status" onclick="selectAdminAiOption('mystatus')">
                       <div class="style-a-icon">🕒</div>
                       <div class="style-a-text">
                           <div class="style-a-title">حالة حضوري</div>
                           <div class="style-a-sub">فحص الدخول والتأخير</div>
                       </div>
                   </div>
                   <div class="style-a-tile lateness" onclick="selectAdminAiOption('lateness')">
                       <div class="style-a-icon">⚠️</div>
                       <div class="style-a-text">
                           <div class="style-a-title">فترة السماح</div>
                           <div class="style-a-sub">15 دقيقة والخصم</div>
                       </div>
                   </div>
                   <div class="style-a-tile excuse" onclick="selectAdminAiOption('excuse_rules')">
                       <div class="style-a-icon">📝</div>
                       <div class="style-a-text">
                           <div class="style-a-title">الأعذار والإثبات</div>
                           <div class="style-a-sub">الكروكة والتقارير</div>
                       </div>
                   </div>
                   <div class="style-a-tile leaves" onclick="selectAdminAiOption('leaves')">
                       <div class="style-a-icon">🌴</div>
                       <div class="style-a-text">
                           <div class="style-a-title">الإجازات</div>
                           <div class="style-a-sub">رصيد 14 يوم والمرضية</div>
                       </div>
                   </div>`
            }
        </div>
    ` : `
        <div class="welcome-style-a-grid">
            ${isAdmin 
                ? `<div class="style-a-tile status" onclick="selectAdminAiOption('summary')">
                       <div class="style-a-icon">📊</div>
                       <div class="style-a-text">
                           <div class="style-a-title">Today's Summary</div>
                           <div class="style-a-sub">Live stats</div>
                       </div>
                   </div>
                   <div class="style-a-tile lateness" onclick="selectAdminAiOption('excuses')">
                       <div class="style-a-icon">📑</div>
                       <div class="style-a-text">
                           <div class="style-a-title">Excuses Audit</div>
                           <div class="style-a-sub">Review proofs</div>
                       </div>
                   </div>
                   <div class="style-a-tile excuse" onclick="selectAdminAiOption('lateness')">
                       <div class="style-a-icon">⚠️</div>
                       <div class="style-a-text">
                           <div class="style-a-title">Lateness Rules</div>
                           <div class="style-a-sub">Penalties</div>
                       </div>
                   </div>
                   <div class="style-a-tile leaves" onclick="selectAdminAiOption('roster')">
                       <div class="style-a-icon">👥</div>
                       <div class="style-a-text">
                           <div class="style-a-title">Workforce</div>
                           <div class="style-a-sub">Staff profiles</div>
                       </div>
                   </div>`
                : `<div class="style-a-tile status" onclick="selectAdminAiOption('mystatus')">
                       <div class="style-a-icon">🕒</div>
                       <div class="style-a-text">
                           <div class="style-a-title">My Status</div>
                           <div class="style-a-sub">Check-in & delay</div>
                       </div>
                   </div>
                   <div class="style-a-tile lateness" onclick="selectAdminAiOption('lateness')">
                       <div class="style-a-icon">⚠️</div>
                       <div class="style-a-text">
                           <div class="style-a-title">Grace Period</div>
                           <div class="style-a-sub">15m & deductions</div>
                       </div>
                   </div>
                   <div class="style-a-tile excuse" onclick="selectAdminAiOption('excuse_rules')">
                       <div class="style-a-icon">📝</div>
                       <div class="style-a-text">
                           <div class="style-a-title">Excuses</div>
                           <div class="style-a-sub">Medical & proof</div>
                       </div>
                   </div>
                   <div class="style-a-tile leaves" onclick="selectAdminAiOption('leaves')">
                       <div class="style-a-icon">🌴</div>
                       <div class="style-a-text">
                           <div class="style-a-title">Leaves</div>
                           <div class="style-a-sub">14d & sick leave</div>
                       </div>
                   </div>`
            }
        </div>
    `;

    msgBox.innerHTML = `
        <div class="ai-msg bot-msg welcome-bot-card" style="${isAr ? 'direction:rtl; text-align:right;' : 'direction:ltr; text-align:left;'}">
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:10px;">
                <div style="width:34px; height:34px; border-radius:50%; background:linear-gradient(135deg, #a855f7, #6366f1); display:flex; align-items:center; justify-content:center; font-size:16px; box-shadow:0 0 12px rgba(168,85,247,0.5); flex-shrink:0;">✨</div>
                <div>
                    <div style="font-weight:800; color:#fff; font-size:0.96rem;">${welcomeHeader}</div>
                    <div style="font-size:0.78rem; color:#94a3b8;">${welcomeDesc}</div>
                </div>
            </div>
            ${tilesHTML}
        </div>
    `;
}

function selectAdminAiOption(optionKey) {
    const inputEl = document.getElementById('ai-chat-input');
    if (!inputEl) return;
    const isAr = currentLang === 'ar';

    const promptMapAr = {
        'hours': 'أيام وأوقات وساعات العمل الرسمية',
        'lateness': 'قواعد التأخير وفترة السماح والخصومات',
        'logging': 'آلية وقواعد تسجيل الحضور والانصراف',
        'excuse_rules': 'شروط ومهلة تقديم الأعذار والكروكة والتقارير الطبية',
        'leaves': 'ما هي ضوابط الإجازات السنوية والإجازات المرضية؟',
        'summary': 'الملخص الذكي لدوام اليوم',
        'roster': 'قائمة الموظفين في قاعدة البيانات',
        'excuses': 'متابعة وفحص طلبات الأعذار والإثباتات',
        'mystatus': 'هل سجلت الدخول اليوم وهل أنا متأخر؟'
    };

    const promptMapEn = {
        'hours': 'Official working days and hours',
        'lateness': 'Lateness rules, grace period, and deductions',
        'logging': 'Attendance check-in and check-out rules',
        'excuse_rules': 'Excuse submission deadline, Kroka and medical proof rules',
        'leaves': 'Annual and sick leave policy and requirements',
        'summary': "Today's smart attendance summary",
        'roster': 'Registered employee roster',
        'excuses': 'Excuses and proof audit report',
        'mystatus': 'Did I check in today and am I late?'
    };

    const map = isAr ? promptMapAr : promptMapEn;
    inputEl.value = map[optionKey] || optionKey;
    const event = { preventDefault: () => {} };
    sendAIChatMessage(event);
}

function selectEmployeeForDetails(email, name) {
    const inputEl = document.getElementById('ai-chat-input');
    if (!inputEl) return;
    const isAr = currentLang === 'ar';
    inputEl.value = isAr ? `تفاصيل الموظف: ${email}` : `Employee Details: ${email}`;
    const event = { preventDefault: () => {} };
    sendAIChatMessage(event);
}

async function sendAIChatMessage(event) {
    if (event && event.preventDefault) event.preventDefault();
    const inputEl = document.getElementById('ai-chat-input');
    const msgBox = document.getElementById('ai-chat-messages');
    if (!inputEl || !msgBox) return;

    const query = inputEl.value.trim();
    if (!query) return;

    // Append user message
    const userIsAr = /[\u0600-\u06FF]/.test(query);
    const userDir = userIsAr ? 'direction:rtl; text-align:right;' : 'direction:ltr; text-align:left;';
    msgBox.innerHTML += `
        <div class="ai-msg user-msg" style="${userDir}">
            ${query}
        </div>
    `;
    inputEl.value = '';
    msgBox.scrollTop = msgBox.scrollHeight;

    // Add neural reasoning indicator
    const loadingId = 'ai-loading-' + Date.now();
    const isAr = currentLang === 'ar';
    msgBox.innerHTML += `
        <div id="${loadingId}" class="ai-typing-indicator" style="${isAr ? 'direction:rtl;' : 'direction:ltr;'}">
            <span class="ai-typing-dot"></span>
            <span class="ai-typing-dot"></span>
            <span class="ai-typing-dot"></span>
            <span style="font-size: 0.78rem; color: #c084fc; font-weight:700; margin-inline-start: 6px;">${isAr ? '🧠 جاري مراجعة لائحة العمل وتدقيق السجلات...' : '🧠 Reviewing policy guidelines & records...'}</span>
        </div>
    `;
    msgBox.scrollTop = msgBox.scrollHeight;

    try {
        window._aiChatMemory = window._aiChatMemory || [];
        const historySnapshot = window._aiChatMemory.slice(-6);
        window._aiChatMemory.push({ role: 'user', content: query });

        const token = localStorage.getItem('userToken');
        const email = localStorage.getItem('userEmail');
        const res = await fetch(`${API_BASE}/api/ai/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ 
                message: query, 
                history: historySnapshot,
                email: email, 
                lang: currentLang 
            })
        });
        const data = await res.json();
        const loadEl = document.getElementById(loadingId);
        if (loadEl) loadEl.remove();

        const rawReply = data.response || (isAr ? "عذراً، حدث خطأ أثناء الاتصال بالذكاء الاصطناعي." : "Sorry, an error occurred while connecting to AI.");
        window._aiChatMemory.push({ role: 'assistant', content: rawReply });
        if (window._aiChatMemory.length > 12) {
            window._aiChatMemory = window._aiChatMemory.slice(-12);
        }

        const containsArabic = /[\u0600-\u06FF]/.test(rawReply);
        const replyDir = (isAr || containsArabic) ? 'direction:rtl; text-align:right;' : 'direction:ltr; text-align:left;';
        
        msgBox.innerHTML += `
            <div class="ai-msg bot-msg" style="background: rgba(14, 20, 36, 0.85); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 18px; padding: 14px 18px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45); backdrop-filter: blur(16px);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:8px;">
                    <div style="display:flex; align-items:center; gap:8px;">
                        <div style="width:24px; height:24px; border-radius:50%; background:linear-gradient(135deg, #a855f7, #6366f1); display:flex; align-items:center; justify-content:center; font-size:12px; box-shadow:0 0 10px rgba(168, 85, 247, 0.5);">✨</div>
                        <span style="font-weight:800; font-size:0.86rem; color:#f1f5f9; letter-spacing:0.2px;">NexusLink Intelligence</span>
                        <span style="width:6px; height:6px; border-radius:50%; background:#34d399; display:inline-block; box-shadow:0 0 6px #34d399;" title="Online"></span>
                    </div>
                    <button type="button" onclick="copyAiResponse(this)" style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); color:#94a3b8; border-radius:8px; padding:3px 8px; font-size:0.75rem; cursor:pointer; display:flex; align-items:center; gap:4px; transition:all 0.2s;" title="Copy Response" onmouseover="this.style.background='rgba(168,85,247,0.25)'; this.style.color='#fff';" onmouseout="this.style.background='rgba(255,255,255,0.05)'; this.style.color='#94a3b8';">
                        <span>📋</span> <span>${isAr ? 'نسخ' : 'Copy'}</span>
                    </button>
                </div>
                <div class="ai-msg-body" style="color:#f8fafc; font-size:0.92rem; line-height:1.7; ${replyDir}">
                    ${rawReply}
                </div>
            </div>
        `;
        msgBox.scrollTop = msgBox.scrollHeight;
    } catch(err) {
        console.error("AI Chat error:", err);
        const loadEl = document.getElementById(loadingId);
        if (loadEl) loadEl.remove();
        const errMsg = isAr ? "عذراً، يتعذر الاتصال بمساعد الذكاء الاصطناعي حالياً." : "Sorry, unable to connect to AI assistant right now.";
        msgBox.innerHTML += `
            <div class="ai-msg bot-msg" style="background: rgba(239, 68, 68, 0.2); border-color: rgba(239, 68, 68, 0.4); color: #fca5a5;">
                ${errMsg}
            </div>
        `;
        msgBox.scrollTop = msgBox.scrollHeight;
    }
}


// Initialization triggers
document.addEventListener("DOMContentLoaded", () => {
    // Apply texts translations
    updatePageTexts();

    const isDashboard = document.getElementById('logs-body') !== null;
    if (isDashboard) {
        setupDashboard();
    } else {
        // Run login setup
        initParticles();
        
        // Auto fill email if remembered
        if (localStorage.getItem('rememberUser') === 'true') {
            const emailField = document.getElementById('email');
            const savedEmail = localStorage.getItem('userEmail');
            if (emailField && savedEmail) {
                emailField.value = savedEmail;
                // Trigger floating label behavior
                emailField.dispatchEvent(new Event('input'));
            }
        }
    }
});

/* === EXECUTIVE OPS DROPDOWN & CENTERED GLASSMODAL HANDLERS === */
function toggleOpsDropdown(event) {
    if (event) event.stopPropagation();
    const dropdown = document.getElementById('ops-dropdown-menu');
    if (!dropdown) return;
    if (dropdown.style.display === 'none' || !dropdown.style.display) {
        dropdown.style.display = 'flex';
    } else {
        dropdown.style.display = 'none';
    }
}

document.addEventListener('click', function (e) {
    const dropdown = document.getElementById('ops-dropdown-menu');
    const btn = document.getElementById('nav-ops-item');
    if (dropdown && dropdown.style.display !== 'none') {
        if (btn && !btn.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.style.display = 'none';
        }
    }
});

function openExecutiveModal(modalId) {
    const dropdown = document.getElementById('ops-dropdown-menu');
    if (dropdown) dropdown.style.display = 'none';

    const backdrop = document.getElementById('executive-backdrop');
    const modal = document.getElementById(modalId);

    if (backdrop) backdrop.style.display = 'block';
    if (modal) modal.style.display = 'block';
}

function closeExecutiveModals() {
    const backdrop = document.getElementById('executive-backdrop');
    if (backdrop) backdrop.style.display = 'none';

    const modal1 = document.getElementById('modal-add-user');
    const modal2 = document.getElementById('modal-manual-log');

    if (modal1) modal1.style.display = 'none';
    if (modal2) modal2.style.display = 'none';
}

async function submitAdminCreateUserModal(event) {
    event.preventDefault();
    const nameInput = document.getElementById('admin-modal-new-name');
    const emailInput = document.getElementById('admin-modal-new-email');
    const passInput = document.getElementById('admin-modal-new-password');

    if (!nameInput || !emailInput || !passInput) return;

    const origName = document.getElementById('admin-new-name');
    const origEmail = document.getElementById('admin-new-email');
    const origPass = document.getElementById('admin-new-password');

    if (origName) origName.value = nameInput.value;
    if (origEmail) origEmail.value = emailInput.value;
    if (origPass) origPass.value = passInput.value;

    const fakeEvent = { preventDefault: () => { } };
    await submitAdminCreateUser(fakeEvent);

    closeExecutiveModals();
    nameInput.value = '';
    emailInput.value = '';
    passInput.value = '';
}

async function submitAdminManualLogModal(event) {
    event.preventDefault();
    const emailInput = document.getElementById('admin-modal-log-email');
    const nameInput = document.getElementById('admin-modal-log-name');
    const typeInput = document.getElementById('admin-modal-log-type');

    if (!emailInput || !typeInput) return;

    const email = emailInput.value.trim();
    const name = nameInput ? nameInput.value.trim() : "";
    const type = typeInput.value;

    if (!email) {
        alert(currentLang === 'ar' ? 'الرجاء إدخال البريد الإلكتروني للموظف' : 'Please enter employee email');
        return;
    }

    const payload = {
        email: email,
        type: type,
        name: name || "Unknown"
    };

    try {
        const token = localStorage.getItem('userToken');
        const response = await fetch(`${API_BASE}/api/attendance/create`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(payload)
        });

        const result = await response.json();
        if (response.ok && result.success) {
            closeExecutiveModals();
            emailInput.value = '';
            if (nameInput) nameInput.value = '';
            
            await loadAdminLogs();
            alert(currentLang === 'ar' ? 'تم تسجيل الحركة بنجاح!' : 'Attendance record logged successfully!');
        } else {
            const errMsg = result.detail || result.error || (currentLang === 'ar' ? 'فشل تسجيل الحركة' : 'Failed to create attendance record');
            alert("❌ " + errMsg);
        }
    } catch (err) {
        console.error("Error creating admin attendance modal:", err);
        alert((currentLang === 'ar' ? 'فشل تسجيل الحركة: ' : 'Failed to record attendance: ') + err.message);
    }
}

// Close modal on Escape key
document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        closeExecutiveModals();
        closeExcuseModal();
    }
});

/* === LATENESS EXCUSES WORKFLOW LOGIC & PROOF ATTACHMENTS === */

let selectedExcuseProofFile = null;
let activeExcusePreset = null;

const excusePresetTemplates = {
    vehicle: {
        en: "Unexpected vehicle breakdown on the route to work. Currently awaiting mechanical assistance/towing.",
        ar: "عطل طارئ ومفاجئ في المركبة أثناء التوجه إلى العمل وتطلب تدخلاً فورياً للإصلاح."
    },
    medical: {
        en: "Emergency medical condition requiring immediate clinic visit and medical attention.",
        ar: "ظرف صحي طارئ ومفاجئ استدعى مراجعة المركز الصحي / المستشفى بشكل عاجل."
    },
    weather: {
        en: "Severe hazardous weather and road conditions causing extensive unavoidable traffic delays.",
        ar: "أحوال جوية استثنائية وظروف قاهرة أدت إلى عرقلة وصعوبة بالغة في حركة السير على الطرقات."
    },
    family: {
        en: "Critical family bereavement / emergency requiring urgent presence and immediate attention.",
        ar: "ظرف عائلي قاهر / حالة وفاة تطلبت التواجد والمتابعة العاجلة والضرورية."
    }
};

function applyExcusePreset(presetKey) {
    activeExcusePreset = presetKey;
    const isAr = currentLang === 'ar';
    const template = excusePresetTemplates[presetKey];
    const textarea = document.getElementById('excuse-reason-text');
    
    if (template && textarea) {
        textarea.value = isAr ? template.ar : template.en;
        textarea.focus();
    }

    // Highlight active chip
    document.querySelectorAll('.excuse-chip-btn').forEach(btn => btn.classList.remove('active'));
    const clickedBtn = document.querySelector(`.excuse-chip-btn[onclick*="'${presetKey}'"]`);
    if (clickedBtn) {
        clickedBtn.classList.add('active');
    }
}

function openExcuseModal() {
    const modal = document.getElementById('modal-submit-excuse');
    if (modal) {
        modal.style.display = 'flex';
        updatePageTexts();
        initProofDropzone();
    } else {
        window.location.href = 'dashboard.html';
    }
}

function openExcuseModalWithReason(reason) {
    openExcuseModal();
    const textEl = document.getElementById('excuse-reason-text');
    if (textEl && reason) {
        textEl.value = reason;
        textEl.focus();
    }
}

function closeExcuseModal() {
    const modal = document.getElementById('modal-submit-excuse');
    if (modal) modal.style.display = 'none';
    const text = document.getElementById('excuse-reason-text');
    if (text) text.value = '';
    activeExcusePreset = null;
    document.querySelectorAll('.excuse-chip-btn').forEach(btn => btn.classList.remove('active'));
    clearExcuseFile();
}

function handleExcuseFileSelect(event) {
    const file = event.target.files && event.target.files[0];
    if (!file) return;
    processExcuseFile(file);
}

function processExcuseFile(file) {
    if (!file) return;
    selectedExcuseProofFile = file;

    const promptEl = document.getElementById('proof-upload-prompt');
    const previewEl = document.getElementById('proof-upload-preview');
    const fileNameEl = document.getElementById('proof-file-name');
    const fileSizeEl = document.getElementById('proof-file-size');
    const previewImg = document.getElementById('proof-preview-img');
    const docIcon = document.getElementById('proof-preview-doc-icon');

    if (promptEl) promptEl.style.display = 'none';
    if (previewEl) previewEl.style.display = 'flex';
    if (fileNameEl) fileNameEl.textContent = file.name;
    
    const sizeKB = (file.size / 1024).toFixed(1);
    const sizeText = file.size > 1048576 
        ? (file.size / 1048576).toFixed(2) + ' MB' 
        : sizeKB + ' KB';
    if (fileSizeEl) fileSizeEl.textContent = sizeText;

    if (file.type.startsWith('image/') && previewImg) {
        const reader = new FileReader();
        reader.onload = function(e) {
            previewImg.src = e.target.result;
            previewImg.style.display = 'block';
            if (docIcon) docIcon.style.display = 'none';
        };
        reader.readAsDataURL(file);
    } else {
        if (previewImg) {
            previewImg.src = '';
            previewImg.style.display = 'none';
        }
        if (docIcon) {
            docIcon.style.display = 'flex';
            docIcon.textContent = file.type === 'application/pdf' ? '📑 PDF' : '📄';
        }
    }
}

function initProofDropzone() {
    const dropzone = document.getElementById('proof-upload-dropzone');
    if (!dropzone || dropzone.hasAttribute('data-dropzone-bound')) return;
    
    dropzone.setAttribute('data-dropzone-bound', 'true');

    ['dragenter', 'dragover'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.add('dragover');
        }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.remove('dragover');
        }, false);
    });

    dropzone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt && dt.files;
        if (files && files.length > 0) {
            const input = document.getElementById('excuse-attachment-file');
            if (input) {
                input.files = files;
            }
            processExcuseFile(files[0]);
        }
    }, false);
}

function clearExcuseFile(event) {
    if (event) {
        event.stopPropagation();
        event.preventDefault();
    }
    selectedExcuseProofFile = null;
    const fileInput = document.getElementById('excuse-attachment-file');
    if (fileInput) fileInput.value = '';

    const promptEl = document.getElementById('proof-upload-prompt');
    const previewEl = document.getElementById('proof-upload-preview');
    const previewImg = document.getElementById('proof-preview-img');
    const docIcon = document.getElementById('proof-preview-doc-icon');

    if (promptEl) promptEl.style.display = 'flex';
    if (previewEl) previewEl.style.display = 'none';
    if (previewImg) {
        previewImg.src = '';
        previewImg.style.display = 'none';
    }
    if (docIcon) {
        docIcon.style.display = 'none';
    }
}

function openProofLightbox(imageUrl, title) {
    if (!imageUrl) return;
    const modal = document.getElementById('proof-lightbox-modal');
    const img = document.getElementById('proof-lightbox-img');
    const titleEl = document.getElementById('proof-lightbox-title');
    const downloadBtn = document.getElementById('proof-lightbox-download');

    if (img) img.src = imageUrl;
    if (downloadBtn) {
        downloadBtn.href = imageUrl;
        downloadBtn.setAttribute('download', imageUrl.split('/').pop() || 'proof-document');
    }
    if (titleEl && title) {
        titleEl.innerHTML = `<span>🖼️</span> <span>${title}</span>`;
    }
    if (modal) modal.style.display = 'flex';
}

function closeProofLightbox() {
    const modal = document.getElementById('proof-lightbox-modal');
    if (modal) modal.style.display = 'none';
}

async function submitExcuseForm(event) {
    if (event) event.preventDefault();
    const reasonText = document.getElementById('excuse-reason-text')?.value || '';
    if (!reasonText.trim()) {
        alert(currentLang === 'ar' ? 'يرجى كتابة سبب التأخير قبل الإرسال' : 'Please type your excuse reason before submitting');
        return;
    }

    const token = localStorage.getItem('userToken') || localStorage.getItem('token') || sessionStorage.getItem('userToken') || sessionStorage.getItem('token') || '';
    const storedEmail = localStorage.getItem('userEmail') || sessionStorage.getItem('userEmail') || '';

    try {
        const url = `${API_BASE}/api/excuses/submit`;
        let res;

        if (selectedExcuseProofFile) {
            const formData = new FormData();
            formData.append('email', storedEmail);
            formData.append('reason', reasonText.trim());
            formData.append('file', selectedExcuseProofFile);

            res = await fetch(url, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`
                },
                body: formData
            });
        } else {
            res = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    email: storedEmail,
                    reason: reasonText.trim()
                })
            });
        }

        const data = await res.json();
        closeExcuseModal();

        if (res.ok && data.success) {
            alert(data.message || (currentLang === 'ar' ? 'تم تقديم العذر وتقييمه بواسطة الذكاء الاصطناعي بنجاح' : 'Excuse submitted and evaluated by AI successfully'));
            loadLogs();
            loadMyExcuses();
        } else {
            let errStr = data.message || data.error || data.detail;
            if (typeof errStr === 'object') {
                if (Array.isArray(errStr) && errStr.length > 0) {
                    errStr = errStr.map(e => e.msg || e.detail || JSON.stringify(e)).join('\n');
                } else {
                    errStr = JSON.stringify(errStr);
                }
            }
            if (!errStr) {
                errStr = currentLang === 'ar' ? 'حدث خطأ أثناء تقديم العذر' : 'Error submitting excuse';
            }
            alert(errStr);
        }
    } catch (err) {
        console.error('Error submitting excuse:', err);
        alert(currentLang === 'ar' ? 'فشل الاتصال بالسيرفر لتقديم العذر. يرجي تحديث الصفحة (Ctrl + F5)' : 'Failed to connect to server for excuse submission. Please refresh the page (Ctrl + F5)');
    }
}

async function loadMyExcuses() {
    const popoverList = document.getElementById('user-excuse-popover-list');
    const badgeEl = document.getElementById('user-excuse-badge');
    if (!popoverList) return;

    const email = localStorage.getItem('userEmail');
    const token = localStorage.getItem('userToken');

    try {
        const response = await fetch(`${API_BASE}/api/excuses/my?email=${encodeURIComponent(email || '')}`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const data = await response.json();
        if (!data.success) return;

        popoverList.innerHTML = '';
        const excuses = data.excuses || [];
        const pendingCount = excuses.filter(e => e.status === 'pending').length;

        if (badgeEl) {
            if (pendingCount > 0) {
                badgeEl.innerText = pendingCount;
                badgeEl.style.display = 'flex';
            } else {
                badgeEl.style.display = 'none';
            }
        }

        const isAr = currentLang === 'ar';

        if (excuses.length === 0) {
            popoverList.innerHTML = `<div style="text-align: center; color: #64748b; padding: 20px; font-size: 0.85rem;">${isAr ? 'لا توجد طلبات أعذار سابقة.' : 'No delay excuse requests submitted.'}</div>`;
            return;
        }

        excuses.forEach((ex, idx) => {
            let statusBadge = '';
            if (ex.status === 'pending') {
                statusBadge = isAr
                    ? '<span style="background:rgba(245,158,11,0.2); border:1px solid rgba(245,158,11,0.4); color:#fde68a; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">⏳ قيد المراجعة والانتظار</span>'
                    : '<span style="background:rgba(245,158,11,0.2); border:1px solid rgba(245,158,11,0.4); color:#fde68a; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">⏳ Pending Review</span>';
            } else if (ex.status === 'approved') {
                statusBadge = isAr
                    ? '<span style="background:rgba(16,185,129,0.2); border:1px solid rgba(16,185,129,0.4); color:#6ee7b7; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟢 تم القبول (حضور مقبول بعذر)</span>'
                    : '<span style="background:rgba(16,185,129,0.2); border:1px solid rgba(16,185,129,0.4); color:#6ee7b7; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🟢 Accepted (With Excuse)</span>';
            } else {
                statusBadge = isAr
                    ? '<span style="background:rgba(239,68,68,0.2); border:1px solid rgba(239,68,68,0.4); color:#fca5a5; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🔴 تم الرفض (سُجل غياب دغري)</span>'
                    : '<span style="background:rgba(239,68,68,0.2); border:1px solid rgba(239,68,68,0.4); color:#fca5a5; padding:4px 10px; border-radius:12px; font-weight:700; font-size:0.75rem;">🔴 Rejected (Absent Registered)</span>';
            }

            let proofBtnHtml = '';
            if (ex.attachment) {
                const viewProofText = isAr ? '🖼️ معاينة الإثبات المرفق (الكروكة/التقرير)' : '🖼️ View Attached Proof Document';
                proofBtnHtml = `
                    <div style="margin-top: 6px;">
                        <button type="button" onclick="openProofLightbox('${ex.attachment}', '${isAr ? 'إثبات عذر' : 'Proof for'} ${ex.date}')" style="padding: 5px 12px; background: rgba(56, 189, 248, 0.2); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; border-radius: 8px; font-size: 0.76rem; font-weight: 700; cursor: pointer; transition: all 0.2s;">
                            ${viewProofText}
                        </button>
                    </div>
                `;
            }

            const card = document.createElement('div');
            card.style.cssText = 'background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 12px; display: flex; flex-direction: column; gap: 8px; backdrop-filter: blur(10px);';
            card.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px;">
                    <span style="font-weight: 800; color: #38bdf8; font-size: 0.85rem;">${idx + 1}. ${ex.date} <span style="font-size:0.72rem; color:#94a3b8;">(${ex.checkin_time || ''})</span></span>
                    ${statusBadge}
                </div>
                <div style="font-size: 0.82rem; color: #e2e8f0; margin-top: 2px;">
                    <strong style="color: #94a3b8;">${isAr ? 'سبب العذر:' : 'Reason:'}</strong> ${ex.reason}
                </div>
                ${proofBtnHtml}
            `;
            popoverList.appendChild(card);
        });
    } catch (err) {
        console.error("Error loading my excuses:", err);
    }
}

function toggleAdminExcuseNotificationDrawer(event) {
    if (event) event.stopPropagation();
    const popover = document.getElementById('admin-excuse-popover');
    if (!popover) return;
    if (popover.style.display === 'none' || !popover.style.display) {
        popover.style.display = 'block';
        loadAdminExcuses();
    } else {
        popover.style.display = 'none';
    }
}

function toggleUserExcuseNotificationDrawer(event) {
    if (event) event.stopPropagation();
    const popover = document.getElementById('user-excuse-popover');
    if (!popover) return;
    if (popover.style.display === 'none' || !popover.style.display) {
        popover.style.display = 'block';
        loadMyExcuses();
    } else {
        popover.style.display = 'none';
    }
}

document.addEventListener('click', function (e) {
    const adminPopover = document.getElementById('admin-excuse-popover');
    const adminBellWrapper = document.getElementById('admin-notification-bell-wrapper');
    if (adminPopover && adminPopover.style.display === 'block') {
        if (!adminPopover.contains(e.target) && (!adminBellWrapper || !adminBellWrapper.contains(e.target))) {
            adminPopover.style.display = 'none';
        }
    }

    const userPopover = document.getElementById('user-excuse-popover');
    const userBellWrapper = document.getElementById('user-notification-bell-wrapper');
    if (userPopover && userPopover.style.display === 'block') {
        if (!userPopover.contains(e.target) && (!userBellWrapper || !userBellWrapper.contains(e.target))) {
            userPopover.style.display = 'none';
        }
    }
});

async function loadAdminExcuses() {
    const popoverList = document.getElementById('admin-excuse-popover-list');
    const badgeEl = document.getElementById('admin-excuse-badge');
    const token = localStorage.getItem('userToken');

    try {
        const response = await fetch(`${API_BASE}/api/excuses/all`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        const data = await response.json();
        if (!data.success) return;

        const excuses = data.excuses || [];
        const pendingCount = excuses.filter(e => e.status === 'pending').length;

        const cardBadgeEl = document.getElementById('lateness-card-excuse-badge');

        [badgeEl, cardBadgeEl].forEach(b => {
            if (b) {
                if (pendingCount > 0) {
                    b.textContent = pendingCount;
                    b.style.display = 'inline-block';
                } else {
                    b.style.display = 'none';
                }
            }
        });

        if (!popoverList) return;
        popoverList.innerHTML = '';

        const emptyText = currentLang === 'ar' ? 'لا توجد طلبات أعذار قيد المراجعة حالياً.' : 'No pending excuse requests at the moment.';
        if (excuses.length === 0) {
            popoverList.innerHTML = `<div style="text-align: center; color: #94a3b8; padding: 18px 10px; font-size: 0.8rem;">${emptyText}</div>`;
            return;
        }

        excuses.forEach((ex, idx) => {
            const isPending = ex.status === 'pending';
            const isApproved = ex.status === 'approved';

            const isAr = currentLang === 'ar';
            const reqTitle = isAr ? 'طلب عذر تأخير' : 'Lateness Excuse Request';
            const approveText = isAr ? 'قبول العذر' : 'Approve';
            const rejectText = isAr ? 'رفض العذر' : 'Reject';

            let statusBadge = '';
            let actionButtons = '';

            if (isPending) {
                statusBadge = isAr 
                    ? '<span style="background:rgba(245,158,11,0.2); border:1px solid rgba(245,158,11,0.4); color:#fde68a; padding:3px 10px; border-radius:10px; font-size:0.72rem; font-weight:700;">⏳ قيد المراجعة</span>'
                    : '<span style="background:rgba(245,158,11,0.2); border:1px solid rgba(245,158,11,0.4); color:#fde68a; padding:3px 10px; border-radius:10px; font-size:0.72rem; font-weight:700;">⏳ Pending</span>';
                
                actionButtons = `
                    <div style="display:flex; gap:8px; margin-top:10px;">
                        <button type="button" onclick="actionExcuse(${ex.id}, 'approve')" style="flex:1; padding:8px 14px; background:linear-gradient(135deg, #10b981, #059669); border:none; border-radius:10px; color:#fff; font-weight:800; font-size:0.82rem; cursor:pointer; box-shadow:0 4px 14px rgba(16,185,129,0.35); transition:transform 0.2s;">${approveText}</button>
                        <button type="button" onclick="actionExcuse(${ex.id}, 'reject')" style="flex:1; padding:8px 14px; background:linear-gradient(135deg, #ef4444, #b91c1c); border:none; border-radius:10px; color:#fff; font-weight:800; font-size:0.82rem; cursor:pointer; box-shadow:0 4px 14px rgba(239,68,68,0.35); transition:transform 0.2s;">${rejectText}</button>
                    </div>
                `;
            } else if (isApproved) {
                statusBadge = isAr 
                    ? '<span style="background:rgba(16,185,129,0.2); border:1px solid rgba(16,185,129,0.4); color:#6ee7b7; padding:3px 10px; border-radius:10px; font-size:0.72rem; font-weight:700;">🟢 مقبول</span>'
                    : '<span style="background:rgba(16,185,129,0.2); border:1px solid rgba(16,185,129,0.4); color:#6ee7b7; padding:3px 10px; border-radius:10px; font-size:0.72rem; font-weight:700;">🟢 Approved</span>';
            } else {
                statusBadge = isAr 
                    ? '<span style="background:rgba(239,68,68,0.2); border:1px solid rgba(239,68,68,0.4); color:#fca5a5; padding:3px 10px; border-radius:10px; font-size:0.72rem; font-weight:700;">🔴 مرفوض</span>'
                    : '<span style="background:rgba(239,68,68,0.2); border:1px solid rgba(239,68,68,0.4); color:#fca5a5; padding:3px 10px; border-radius:10px; font-size:0.72rem; font-weight:700;">🔴 Rejected</span>';
            }

            let aiBadgeHtml = '';
            if (ex.ai_recommendation) {
                try {
                    const aiObj = typeof ex.ai_recommendation === 'string' ? JSON.parse(ex.ai_recommendation) : ex.ai_recommendation;
                    const badgeText = isAr ? (aiObj.badge_ar || '🤖 التقييم الذكي') : (aiObj.badge_en || '🤖 AI Recommendation');
                    const expText = isAr ? (aiObj.explanation_ar || '') : (aiObj.explanation_en || '');
                    
                    let borderCol = 'rgba(168, 85, 247, 0.4)';
                    let bgCol = 'rgba(168, 85, 247, 0.15)';
                    if (aiObj.recommendation === 'APPROVE') {
                        borderCol = 'rgba(16, 185, 129, 0.4)';
                        bgCol = 'rgba(16, 185, 129, 0.15)';
                    } else if (aiObj.recommendation === 'REJECT') {
                        borderCol = 'rgba(239, 68, 68, 0.4)';
                        bgCol = 'rgba(239, 68, 68, 0.15)';
                    }

                    aiBadgeHtml = `
                        <div style="background: ${bgCol}; border: 1px solid ${borderCol}; border-radius: 10px; padding: 8px 12px; margin-bottom: 8px; font-size: 0.78rem;">
                            <div style="font-weight: 800; color: #fff; margin-bottom: 2px;">${badgeText}</div>
                            ${expText ? `<div style="color: #cbd5e1; font-size: 0.74rem;">${expText}</div>` : ''}
                        </div>
                    `;
                } catch(e) { console.error("Error parsing AI recommendation", e); }
            }

            let proofAttachmentBtn = '';
            if (ex.attachment) {
                const proofLabel = isAr ? '🖼️ معاينة الإثبات المرفق (الكروكة/التقرير)' : '🖼️ View Attached Proof';
                proofAttachmentBtn = `
                    <div style="margin-bottom: 8px;">
                        <button type="button" onclick="openProofLightbox('${ex.attachment}', '${isAr ? 'إثبات الموظف:' : 'Proof:'} ${ex.name || ''}')" style="width: 100%; padding: 7px 12px; background: rgba(56, 189, 248, 0.18); border: 1px solid rgba(56, 189, 248, 0.45); border-radius: 8px; color: #38bdf8; font-weight: 700; font-size: 0.78rem; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; gap: 6px;">
                            ${proofLabel}
                        </button>
                    </div>
                `;
            }

            const item = document.createElement('div');
            item.style.cssText = 'background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 16px; padding: 14px; backdrop-filter: blur(14px); box-shadow: 0 8px 30px rgba(0,0,0,0.4); transition: transform 0.2s;';
            item.innerHTML = `
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <div style="font-weight:800; color:#fff; font-size:0.9rem; display:flex; align-items:center; gap:6px;">
                        <span style="color:#c084fc; font-weight:900;">${idx + 1}.</span> ${reqTitle}
                    </div>
                    ${statusBadge}
                </div>
                <div style="font-size:0.83rem; color:#f8fafc; font-weight:700; margin-bottom:2px;">👤 ${ex.name || 'Employee'}</div>
                <div style="font-size:0.76rem; color:#94a3b8; margin-bottom:8px;">📧 ${ex.email || ''} | 📅 ${ex.date || ''} ${ex.checkin_time ? `(${ex.checkin_time})` : ''}</div>
                
                <!-- Dedicated Highlighted Excuse Reason Box -->
                <div style="background: rgba(30, 41, 59, 0.85); border-right: 3px solid #38bdf8; border-radius: 10px; padding: 10px 12px; margin-bottom: 8px;">
                    <div style="font-size: 0.72rem; color: #38bdf8; font-weight: 700; margin-bottom: 4px; display: flex; align-items: center; gap: 4px;">
                        <span>💬</span> ${isAr ? 'نص العذر المقدم:' : 'Submitted Excuse Text:'}
                    </div>
                    <div style="font-size: 0.85rem; color: #ffffff; font-weight: 600; line-height: 1.4; word-break: break-word;">
                        "${ex.reason || (isAr ? 'لم يتم كتابة تفاصيل عذر' : 'No details provided')}"
                    </div>
                </div>

                ${proofAttachmentBtn}
                ${aiBadgeHtml}
                ${actionButtons}
            `;
            popoverList.appendChild(item);
        });
    } catch (err) {
        console.error("Error loading admin excuses for notification bell:", err);
    }
}

async function actionExcuse(excuseId, actionType) {
    const token = localStorage.getItem('userToken');
    const isAr = currentLang === 'ar';
    const actionName = isAr 
        ? (actionType === 'approve' ? 'قبول العذر واحتساب حضور' : 'رفض العذر وتنزيل غياب')
        : (actionType === 'approve' ? 'Approve Excuse & Mark Present' : 'Reject Excuse & Mark Absent');

    const confirmMsg = isAr 
        ? `هل أنت تأكد من قرار: [${actionName}] لهذا الموظف؟`
        : `Are you sure you want to perform action: [${actionName}] for this employee?`;

    if (!confirm(confirmMsg)) return;

    try {
        const response = await fetch(`${API_BASE}/api/excuses/action`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
                excuse_id: excuseId,
                action: actionType
            })
        });

        const data = await response.json();
        if (data.success) {
            alert("✅ " + (data.message || (isAr ? "تم إنجاز التعديل بنجاح" : "Action executed successfully")));
            loadAdminExcuses();
            loadAdminLogs(); // refresh audit logs & lateness table
        } else {
            const errTitle = isAr ? "❌ خطأ: " : "❌ Error: ";
            alert(errTitle + (data.error || (isAr ? "فشل تنفيذ القرار" : "Action failed")));
        }
    } catch (err) {
        console.error("Error taking excuse action:", err);
        alert(isAr ? "❌ حدث خطأ في الاتصال بالسيرفر" : "❌ Server connection error");
    }
}