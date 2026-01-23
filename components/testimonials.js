/* CANONICAL TESTIMONIALS COMPONENT - SINGLE SOURCE OF TRUTH */
/* DO NOT duplicate this logic in any page-level JavaScript */

(function() {
    'use strict';

    /**
     * Renders testimonials from JSON data
     * @param {Array} testimonials - Array of testimonial objects
     * @returns {string} HTML string for testimonials grid
     */
    function renderTestimonials(testimonials) {
        if (!testimonials || !testimonials.length) {
            return '';
        }

        const cards = testimonials.map(testimonial => {
            const initials = testimonial.author
                .split(' ')
                .map(name => name[0])
                .join('');

            return `
                <div class="tst-card">
                    <div class="tst-rating">
                        <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
                    </div>
                    <p class="tst-text">${testimonial.text}</p>
                    <div class="tst-footer">
                        <div class="tst-avatar">${initials}</div>
                        <div class="tst-info">
                            <div class="tst-author">${testimonial.author}</div>
                            <div class="tst-role">${testimonial.role}</div>
                        </div>
                    </div>
                </div>
            `;
        }).join('');

        return `
            <section class="tst-section">
                <div class="tst-container">
                    <h2 class="tst-title">Client Testimonials</h2>
                    <div class="tst-grid">
                        ${cards}
                    </div>
                </div>
            </section>
        `;
    }

    /**
     * Adds "Read more" functionality to testimonials that overflow
     */
    function initializeReadMore() {
        const cards = document.querySelectorAll('.tst-card');

        cards.forEach(card => {
            const textElement = card.querySelector('.tst-text');
            const footer = card.querySelector('.tst-footer');

            if (!textElement || !footer) return;

            // Check if text is overflowing
            if (textElement.scrollHeight > textElement.clientHeight + 5) {
                // Create read more button
                const readMoreBtn = document.createElement('button');
                readMoreBtn.className = 'tst-read-more-btn';
                readMoreBtn.innerHTML = 'Read more →';
                readMoreBtn.setAttribute('aria-expanded', 'false');

                // Insert before footer
                footer.parentNode.insertBefore(readMoreBtn, footer);

                // Add click handler
                readMoreBtn.addEventListener('click', function() {
                    const isExpanded = textElement.classList.contains('expanded');

                    if (isExpanded) {
                        textElement.classList.remove('expanded');
                        readMoreBtn.innerHTML = 'Read more →';
                        readMoreBtn.setAttribute('aria-expanded', 'false');
                    } else {
                        textElement.classList.add('expanded');
                        readMoreBtn.innerHTML = '← Show less';
                        readMoreBtn.setAttribute('aria-expanded', 'true');
                    }
                });
            }
        });
    }

    /**
     * Initializes testimonials component
     */
    function initTestimonials() {
        const root = document.getElementById('testimonials-root');
        if (!root) return;

        try {
            // Get testimonials data from data attribute
            const testimonialsData = root.getAttribute('data-testimonials');
            if (!testimonialsData) {
                console.error('No testimonials data found');
                return;
            }

            const testimonials = JSON.parse(testimonialsData);

            // Render testimonials
            const html = renderTestimonials(testimonials);
            root.innerHTML = html;

            // Initialize read more functionality
            initializeReadMore();
        } catch (error) {
            console.error('Error initializing testimonials:', error);
        }
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTestimonials);
    } else {
        initTestimonials();
    }
})();
