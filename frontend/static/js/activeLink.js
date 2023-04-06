let links = document.querySelectorAll('.nav a');
    links.forEach(link => {
        const currentLink = document.URL;
        if (link.href === currentLink) {
            link.classList.add('bg-[#012210c4]');
            link.classList.add('dark:bg-[#011b0d]');
        }

    });