Network request blocking:
Stop requests to known ad servers.
Example rule (like EasyList)

Hide ad elements using CSS:

.ad-banner,
.sponsored,
#ads {
    display: none !important;
}

Prevent tracking scripts:

if (script.src.includes("ads")) {
    blockScript();
}

