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

Optimizations:

1. Can use [any()] for cleaner and faster short-circuiting.
2. Convert to set (only if exact matching).
3. Precompile patterns (Best for many domains).
4. Avoid unnecessary function calls (micro-optimization).
5. Early filtering (if URLs are structured).
