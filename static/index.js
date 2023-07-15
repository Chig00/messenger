window.setInterval(
    () => {
        if (
            document.getElementById("message").value === ""
            && document.getElementById("message") !== document.activeElement
            && document.getElementById("name") !== document.activeElement
        ) {
            document.getElementById("form").submit();
        }
    },
    1000
);