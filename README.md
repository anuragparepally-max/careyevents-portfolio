# Carey International Event Portfolio Website

A sophisticated, high-end event portfolio website showcasing Carey International's global logistics expertise across music tours, sports events, fashion shows, corporate summits, and more.

## 📁 Project Structure

```
careyevents-portfolio/
├── index.html                          # Main portfolio homepage
├── assets/
│   └── images/
│       └── carey-logo.png             # Carey International logo (PLACE YOUR LOGO HERE)
├── events/                             # Individual event detail pages
│   ├── beyonce-european-tour.html     # ✅ COMPLETED
│   ├── madonna-european-tour.html     # ✅ COMPLETED
│   ├── super-bowl.html                # ✅ COMPLETED
│   ├── louis-vuitton-miami.html       # ✅ COMPLETED
│   └── [25 more pages to create]      # See list below
└── README.md                           # This file
```

## 🎨 Design Features

- **Carey Blue Branding**: Official Carey International color scheme (#003B5C navy blue and white)
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Interactive Elements**:
  - Animated counter metrics on scroll
  - Filterable event cards by category
  - Smooth scrolling navigation
  - Hover effects and transitions
- **Visual Gallery**: High-quality Unsplash imagery for each event category

## 🚀 How to Use

### 1. Add Your Logo

**IMPORTANT**: Place your Carey International logo in the following location:
```
assets/images/carey-logo.png
```

The logo you provided has been saved locally - you need to copy it to this location.

### 2. View the Website

Simply open `index.html` in your web browser. The main portfolio page includes:
- Hero section with Carey branding
- Animated impact metrics (50,000+ VIPs, 5,000+ vehicles, etc.)
- Filterable event cards across 6 industries
- Client testimonials
- All 29 events with clickable links

### 3. Create Remaining Event Pages

**Completed Pages** (4/29):
- ✅ Beyoncé European Tour
- ✅ Madonna European Tour
- ✅ Super Bowl
- ✅ Louis Vuitton Men's PF Show (Miami)

**Pages to Create** (25 remaining):

**Music & Entertainment:**
- kylie-minogue-european-tour.html
- foo-fighters-european-tour.html
- global-citizens-concert.html

**Sports:**
- nba-all-stars.html
- nfl-honors.html
- pga-golf.html

**Fashion & Lifestyle:**
- louis-vuitton-cruise.html
- gucci-new-york.html

**Corporate:**
- bcg-summit.html
- vanguard-conference.html
- blackrock-summit.html
- jpmorgan-healthcare.html

**Technology & Media:**
- nvidia-conference.html
- oracle-openworld.html
- ibm-think.html
- nbc-events.html
- toshiba-corporate.html

**Healthcare:**
- abbott-conference.html
- cigna-summit.html
- boston-scientific.html
- eli-lilly-summit.html

## 📋 Event Page Template

Use the completed pages (`madonna-european-tour.html`, `super-bowl.html`, `louis-vuitton-miami.html`, `beyonce-european-tour.html`) as templates. Each page includes:

### Required Sections:

1. **Hero Section** - Event name and category
2. **Stats Cards** - 4 key metrics (vehicles, people served, duration, performance)
3. **Overview** - 2-3 paragraphs describing the event and Carey's role
4. **Image Gallery** - 6 high-quality images from Unsplash
5. **Fleet Details** - 3 cards describing vehicle types and specifications
6. **Operational Highlights** - 4 boxes highlighting key achievements
7. **Testimonials** - 2-3 realistic client quotes with names and titles

### Customization Steps:

1. Copy one of the completed HTML files
2. Update the `<title>` tag
3. Change the hero background image URL
4. Modify stats numbers based on event data
5. Rewrite overview text for the specific event
6. Replace image gallery URLs with relevant Unsplash images
7. Customize fleet composition details
8. Create unique testimonials that fit the event context

### Finding Images

Use Unsplash for high-quality, royalty-free images:
- Music Events: https://unsplash.com/s/photos/concert
- Sports: https://unsplash.com/s/photos/stadium
- Fashion: https://unsplash.com/s/photos/fashion-show
- Corporate: https://unsplash.com/s/photos/business-meeting
- Technology: https://unsplash.com/s/photos/tech-conference
- Healthcare: https://unsplash.com/s/photos/medical-conference

## 🎯 Key Metrics by Event Category

### Music & Entertainment
- **Beyoncé**: 800 vehicles, 2,500 people, SUV/Sprinter/Mini Bus
- **Madonna**: 700 vehicles, 2,300 people
- **Kylie Minogue**: 600 vehicles, 1,900 people
- **Foo Fighters**: 500 vehicles, 1,800 people
- **Global Citizens**: Main stage talent transportation

### Sports
- **Super Bowl**: 1,200 vehicles, 5,000 people, full VIP/sponsor deployment
- **NBA All-Stars**: 500 vehicles, 3,000 people
- **NFL Honors**: Official partner since 2011
- **PGA Golf**: Premium transportation services

### Fashion & Lifestyle
- **LV Miami**: 400 SUVs (20 talent-specific), 5 days
- **LV Cruise Shows**: NY (2019), San Diego (2023), Palm Springs
- **Gucci NY**: White-glove exclusive events

### Corporate
- **BCG, Vanguard, BlackRock, JP Morgan**: 150+ executive sedans each
- **Service**: Secure, discreet C-suite transportation

### Technology & Media
- **Nvidia, Oracle, IBM, NBC, Toshiba**: 300+ attendees transported per conference

### Healthcare
- **Abbott, Cigna, Boston Scientific, Eli Lilly**: Premium executive transportation

## 🎨 Color Palette

```css
--carey-blue: #003B5C       /* Primary brand color */
--carey-light-blue: #0A5279 /* Accent blue */
--white: #FFFFFF            /* Background */
--light-gray: #F5F5F5       /* Secondary background */
--dark-gray: #4A4A4A        /* Text color */
```

## 📱 Responsive Breakpoints

- Desktop: 1400px max-width containers
- Tablet: Grid adapts at 768px
- Mobile: Single column layout below 768px

## 🔗 Navigation

- Main page: `index.html`
- Event pages: `events/[event-name].html`
- Back button on each event page returns to main portfolio

## 📄 Browser Compatibility

- Chrome, Firefox, Safari, Edge (latest versions)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🚀 Deployment

### Option 1: GitHub Pages
1. Ensure logo is in `assets/images/carey-logo.png`
2. Commit all changes to your repository
3. Go to repository Settings → Pages
4. Select "main" branch as source
5. Site will be live at: `https://anuragparepally-max.github.io/careyevents-portfolio/`

### Option 2: Custom Hosting
Upload all files to your web server, maintaining the folder structure.

## 📝 Notes

- All event cards on the main page are clickable and link to detail pages
- Smooth scrolling is enabled throughout
- Filter buttons allow viewing events by category
- Animated counters trigger when scrolled into view
- All pages use the same consistent Carey blue branding

## 🎯 Next Steps

1. **Add your logo** to `assets/images/carey-logo.png`
2. **Create remaining 25 event pages** using the templates provided
3. **Test all links** to ensure navigation works properly
4. **Review content** for accuracy and brand consistency
5. **Deploy** to GitHub Pages or your preferred hosting platform

---

**Built with:** HTML5, CSS3, Vanilla JavaScript
**Color Scheme:** Carey International Brand Colors (Navy Blue #003B5C + White)
**Images:** Unsplash (royalty-free)
**Responsive:** Mobile, Tablet, Desktop optimized
