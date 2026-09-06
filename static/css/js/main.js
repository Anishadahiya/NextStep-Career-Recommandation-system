/* ==========================================================
   NEXTSTEP - FINAL JAVASCRIPT
   ========================================================== */

document.addEventListener("DOMContentLoaded", function () {

    /* ======================================================
       1. PAGE LOAD ANIMATION
       ====================================================== */

    document.body.classList.add("page-loaded");


    /* ======================================================
       2. CARD ANIMATION
       ====================================================== */

    const animatedCards = document.querySelectorAll(
        ".card, " +
        ".feature-card, " +
        ".question-card, " +
        ".recommendation-card, " +
        ".resource-card, " +
        ".game-card, " +
        ".achievement-badge"
    );

    animatedCards.forEach(function (card, index) {

        card.style.opacity = "0";
        card.style.transform = "translateY(15px)";

        setTimeout(function () {

            card.style.transition =
                "opacity 0.5s ease, transform 0.5s ease";

            card.style.opacity = "1";
            card.style.transform = "translateY(0)";

        }, Math.min(index * 45, 500));

    });


    /* ======================================================
       3. PROGRESS BAR ANIMATION
       ====================================================== */

    const progressBars = document.querySelectorAll(
        ".score-bar-fill, " +
        ".modern-progress-bar, " +
        ".skill-fill"
    );

    progressBars.forEach(function (bar) {

        let finalWidth = bar.style.width;

        /*
         * Arcade progress uses:
         * data-progress="45"
         */

        if (bar.dataset.progress) {

            finalWidth =
                bar.dataset.progress + "%";

        }

        /*
         * Some bars may get their value from
         * a CSS width attribute.
         */

        if (!finalWidth) {

            finalWidth = "0%";

        }

        bar.style.width = "0%";

        setTimeout(function () {

            bar.style.width = finalWidth;

        }, 350);

    });


    /* ======================================================
       4. NUMBER COUNTERS
       ====================================================== */

    const counters = document.querySelectorAll(
        "[data-counter]"
    );

    counters.forEach(function (counter) {

        const target = parseInt(
            counter.dataset.counter,
            10
        );

        if (isNaN(target)) {

            return;

        }

        /*
         * Don't animate zero.
         */

        if (target === 0) {

            counter.textContent = "0";

            return;

        }

        let current = 0;

        const increment =
            Math.max(
                1,
                Math.ceil(target / 35)
            );

        const timer = setInterval(
            function () {

                current += increment;

                if (current >= target) {

                    current = target;

                    clearInterval(timer);

                }

                counter.textContent =
                    current;

            },
            25
        );

    });


    /* ======================================================
       5. BUTTON PRESS EFFECT
       ====================================================== */

    const buttons = document.querySelectorAll(
        ".btn, " +
        "button, " +
        ".game-play-button, " +
        ".resource-button"
    );

    buttons.forEach(function (button) {

        button.addEventListener(
            "mousedown",
            function () {

                button.style.transform =
                    "scale(0.97)";

            }
        );

        button.addEventListener(
            "mouseup",
            function () {

                button.style.transform =
                    "";

            }
        );

        button.addEventListener(
            "mouseleave",
            function () {

                button.style.transform =
                    "";

            }
        );

    });


    /* ======================================================
       6. QUIZ RADIO SELECTION
       ====================================================== */

    const quizInputs =
        document.querySelectorAll(
            'input[type="radio"]'
        );

    quizInputs.forEach(function (input) {

        input.addEventListener(
            "change",
            function () {

                const groupInputs =
                    document.querySelectorAll(
                        'input[name="' +
                        input.name +
                        '"]'
                    );

                groupInputs.forEach(
                    function (otherInput) {

                        const parent =
                            otherInput.closest(
                                ".quiz-option"
                            );

                        if (parent) {

                            parent.classList.remove(
                                "selected"
                            );

                        }

                    }
                );


                const selectedParent =
                    input.closest(
                        ".quiz-option"
                    );

                if (selectedParent) {

                    selectedParent.classList.add(
                        "selected"
                    );

                }

            }
        );

    });


    /* ======================================================
       7. ASSESSMENT PROGRESS
       ====================================================== */

    const assessmentForm =
        document.querySelector(
            'form[action*="assessment"]'
        );

    if (assessmentForm) {

        const assessmentInputs =
            assessmentForm.querySelectorAll(
                'input[type="radio"]'
            );

        const questionGroups =
            new Set();

        assessmentInputs.forEach(
            function (input) {

                if (input.name) {

                    questionGroups.add(
                        input.name
                    );

                }

            }
        );

        const totalQuestions =
            questionGroups.size;


        function updateAssessmentProgress() {

            let answered =
                0;


            questionGroups.forEach(
                function (groupName) {

                    const checked =
                        assessmentForm.querySelector(
                            'input[name="' +
                            groupName +
                            '"]:checked'
                        );

                    if (checked) {

                        answered++;

                    }

                }
            );


            const percentage =
                totalQuestions > 0
                    ? Math.round(
                        (answered /
                        totalQuestions) * 100
                    )
                    : 0;


            const progressText =
                document.getElementById(
                    "assessment-progress-text"
                );


            const progressBar =
                document.getElementById(
                    "assessment-progress-bar"
                );


            if (progressText) {

                progressText.textContent =
                    answered +
                    " / " +
                    totalQuestions +
                    " answered";

            }


            if (progressBar) {

                progressBar.style.width =
                    percentage + "%";

            }

        }


        assessmentInputs.forEach(
            function (input) {

                input.addEventListener(
                    "change",
                    updateAssessmentProgress
                );

            }
        );


        updateAssessmentProgress();

    }


    /* ======================================================
       8. RESOURCE TOAST
       ====================================================== */

    const resourceLinks =
        document.querySelectorAll(
            ".resource-button"
        );

    resourceLinks.forEach(function (link) {

        link.addEventListener(
            "click",
            function () {

                showToast(
                    "📚 Learning resource opened!"
                );

            }
        );

    });


    /* ======================================================
       9. XP ANIMATION
       ====================================================== */

    const xpElements =
        document.querySelectorAll(
            ".xp-number"
        );

    xpElements.forEach(function (element) {

        const text =
            element.textContent.trim();


        /*
         * Looks for:
         * +50 XP
         * +100 XP
         */

        if (
            /\+\d+\s*XP/i.test(text)
        ) {

            element.classList.add(
                "xp-pulse"
            );

        }

    });


    /* ======================================================
       10. BADGE ANIMATION
       ====================================================== */

    const badges =
        document.querySelectorAll(
            ".achievement-badge"
        );

    badges.forEach(function (badge) {

        const text =
            badge.textContent.toUpperCase();


        if (
            text.includes("UNLOCKED")
        ) {

            badge.classList.add(
                "badge-unlocked"
            );

        }

    });


    /* ======================================================
       11. MOBILE NAVIGATION SUPPORT
       ====================================================== */

    const navLinks =
        document.querySelector(
            ".nav-links"
        );

    if (navLinks) {

        /*
         * Allows the navigation to scroll
         * horizontally on very small screens.
         */

        if (
            navLinks.scrollWidth >
            navLinks.clientWidth
        ) {

            navLinks.style.overflowX =
                "auto";

            navLinks.style.whiteSpace =
                "nowrap";

        }

    }


    /* ======================================================
       12. CURRENT YEAR
       ====================================================== */

    const yearElements =
        document.querySelectorAll(
            "[data-current-year]"
        );

    yearElements.forEach(
        function (element) {

            element.textContent =
                new Date().getFullYear();

        }
    );


    /* ======================================================
       13. CAREER SPRINT TIMER
       ====================================================== */

    const sprintForm =
        document.getElementById(
            "sprint-form"
        );

    const sprintTimer =
        document.getElementById(
            "timer"
        );

    const sprintTimerBar =
        document.getElementById(
            "timer-bar"
        );


    /*
     * Only start the timer when the
     * Career Sprint page exists.
     */

    if (
        sprintForm &&
        sprintTimer
    ) {

        let timeLeft = 30;

        const totalTime = 30;


        const countdown =
            setInterval(
                function () {

                    timeLeft--;


                    sprintTimer.textContent =
                        timeLeft;


                    if (sprintTimerBar) {

                        const percentage =
                            (
                                timeLeft /
                                totalTime
                            ) * 100;


                        sprintTimerBar.style.width =
                            percentage + "%";

                    }


                    /*
                     * Warning when 10 seconds
                     * remain.
                     */

                    if (
                        timeLeft <= 10
                    ) {

                        sprintTimer.style.color =
                            "#d63031";

                        sprintTimer.style.transform =
                            "scale(1.05)";

                    }


                    /*
                     * Time finished.
                     */

                    if (
                        timeLeft <= 0
                    ) {

                        clearInterval(
                            countdown
                        );


                        sprintTimer.textContent =
                            "0";


                        sprintForm.submit();

                    }

                },
                1000
            );


        /*
         * Stop the timer when form
         * is manually submitted.
         */

        sprintForm.addEventListener(
            "submit",
            function () {

                clearInterval(
                    countdown
                );

            }
        );

    }


    /* ======================================================
       14. CHECK FOR ACHIEVEMENT RESULT
       ====================================================== */

    const resultPage =
        document.querySelector(
            ".xp-card"
        );

    if (resultPage) {

        const resultText =
            resultPage.textContent;


        if (
            /\+\d+\s*XP/i.test(
                resultText
            )
        ) {

            /*
             * Small delay so the result
             * page loads first.
             */

            setTimeout(
                function () {

                    showToast(
                        "⭐ XP earned! Keep going!"
                    );

                },
                700
            );

        }

    }

});


/* ==========================================================
   TOAST MESSAGE
   ========================================================== */

function showToast(message) {

    let toast =
        document.getElementById(
            "nextstep-toast"
        );


    /*
     * Create toast if it doesn't exist.
     */

    if (!toast) {

        toast =
            document.createElement(
                "div"
            );


        toast.id =
            "nextstep-toast";


        toast.style.position =
            "fixed";


        toast.style.right =
            "20px";


        toast.style.bottom =
            "20px";


        toast.style.zIndex =
            "99999";


        toast.style.padding =
            "13px 17px";


        toast.style.borderRadius =
            "12px";


        toast.style.background =
            "#172033";


        toast.style.color =
            "#ffffff";


        toast.style.fontSize =
            "0.85rem";


        toast.style.fontWeight =
            "700";


        toast.style.boxShadow =
            "0 12px 30px rgba(0,0,0,0.18)";


        toast.style.opacity =
            "0";


        toast.style.transform =
            "translateY(10px)";


        toast.style.transition =
            "all 0.25s ease";


        document.body.appendChild(
            toast
        );

    }


    toast.textContent =
        message;


    /*
     * Show toast
     */

    requestAnimationFrame(
        function () {

            toast.style.opacity =
                "1";

            toast.style.transform =
                "translateY(0)";

        }
    );


    /*
     * Hide after 2.2 seconds
     */

    setTimeout(
        function () {

            toast.style.opacity =
                "0";

            toast.style.transform =
                "translateY(10px)";

        },
        2200
    );

}


/* ==========================================================
   CONFETTI
   ========================================================== */

function launchConfetti() {

    const totalPieces = 45;


    for (
        let i = 0;
        i < totalPieces;
        i++
    ) {

        const piece =
            document.createElement(
                "div"
            );


        piece.style.position =
            "fixed";


        piece.style.left =
            Math.random() * 100 +
            "vw";


        piece.style.top =
            "-15px";


        piece.style.width =
            "8px";


        piece.style.height =
            "14px";


        piece.style.borderRadius =
            "3px";


        piece.style.zIndex =
            "100000";


        piece.style.background =
            [
                "#6c5ce7",
                "#0984e3",
                "#00b894",
                "#fdcb6e",
                "#e17055"
            ][
                Math.floor(
                    Math.random() * 5
                )
            ];


        document.body.appendChild(
            piece
        );


        const duration =
            1200 +
            Math.random() * 1200;


        const animation =
            piece.animate(
                [
                    {
                        transform:
                            "translateY(0) rotate(0deg)",
                        opacity: 1
                    },
                    {
                        transform:
                            "translateY(105vh) rotate(720deg)",
                        opacity: 0
                    }
                ],
                {
                    duration:
                        duration,
                    easing:
                        "cubic-bezier(.2,.7,.3,1)"
                }
            );


        animation.onfinish =
            function () {

                piece.remove();

            };

    }

}


/* ==========================================================
   GLOBAL XP CELEBRATION
   ========================================================== */

function celebrateAchievement() {

    showToast(
        "🏆 Achievement unlocked!"
    );

    launchConfetti();

}