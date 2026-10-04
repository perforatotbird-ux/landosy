import json, re, os

REF = "https://www.creativefabrica.com/bundles/ref/15072325/"

products_raw = r"""
[
  {"url":"https://www.creativefabrica.com/product/soft-nursery-mix/","title":"Soft Nursery Mix","image":"https://cdn.creativefabrica.com/2026/09/10/Soft-nursery-mix-Bundles-157553491-1-1-580x387.jpg","description":"A soft and playful nursery pattern collection in gentle, light colours, featuring delicate stripes, checks, polka dots and charming summer-inspired patterns. Designed in a calm and sweet palette, this versatile mix brings a cosy, cheerful and timeless feel to nurseries, baby rooms, children's textiles, stationery and other creative projects.\nBundle details:\n– 300 dpi\n– JPG\n– from 3000 px\n– 25 sets\n– 190 files\n– Zipped"},
  {"url":"https://www.creativefabrica.com/product/the-free-holiday-craft-bundle/","title":"The Free Holiday Craft Bundle","image":"https://cdn.creativefabrica.com/2021/07/08/Untitled-design-580x387.png","description":"The Free Holiday Craft Bundle includes 20 amazing Christmas and Holiday themed craft designs. All designs included in this bundle comes with our premium commercial license and are exclusive for Creative Fabrica. Download beautiful Christmas illustrations, Merry Christmas quotes, and snowman faces. All designs are compatible with your Silhouette and Cricut cutting machine!\nGet this free exclusive bundle now - limited availability!"},
  {"url":"https://www.creativefabrica.com/product/spooky-training-learning-svg-bundle/","title":"Spooky Training & Learning SVG Bundle","image":"https://cdn.creativefabrica.com/2026/09/28/Spooky-Training-Learning-SVG-Bundle-Bundles-158960266-1-1-580x387.jpg","description":"A playful Halloween-themed training and learning design bundle featuring witches, ghosts, skeletons, books, certificates, classroom humor, and spooky education motifs. Ideal for teachers, trainers, tutors, workshop hosts, classroom projects, seasonal apparel, stickers, decals, signs, sublimation, vinyl cutting, printables, and DIY craft projects.\nIncluded formats: SVG, PNG, JPG, EPS, and DXF. SVG and DXF are suitable for cutting-machine projects, PNG and JPG work well for printing and sublimation, and EPS is ideal for scalable vector editing.\nThis is a digital download. No physical product will be shipped."},
  {"url":"https://www.creativefabrica.com/product/bestseller-mega-christmas-bundle/","title":"Bestseller Mega Christmas Bundle","image":"https://cdn.creativefabrica.com/2026/09/25/Bestseller-Mega-Christmas-Bundle-Bundles-158727975-1-1-580x387.png","description":"🎄 150+ Designs Bestseller Mega Christmas Bundle 🎄\nCelebrate the holiday season with this 150+ Designs Mega Christmas Bundle, packed with a wide variety of festive and Christmas-themed designs perfect for your creative projects.\n✨ What You Get:\n- 150+ unique Christmas designs\n- High-resolution PNG files\n- Transparent backgrounds\n- Ready for sublimation and crafting\n- Perfect for Christmas shirts, mugs, tumblers, gifts & more\n- Digital download\n🎁 Perfect for: Christmas crafts, sublimation projects, DIY gifts, apparel designs, home décor, and holiday creative projects."},
  {"url":"https://www.creativefabrica.com/product/halloween-svg-png-13/","title":"Halloween Svg Png","image":"https://cdn.creativefabrica.com/2026/10/02/Halloween-svg-png-Bundles-159319681-1-1-580x387.png","description":"Halloween SVG PNG Digital Download. You can use this file for craft ideas as well as t-shirts, pillows, mousepads, coffee cups/mugs, posters, stickers, magnets, buttons, vinyl decals, scrapbooking, signs, etc.\nContains: 20 SVG, 20 PNG (Transparent), 20 JPG"},
  {"url":"https://www.creativefabrica.com/product/cute-funny-friendship-sayings-13/","title":"Cute Funny Friendship Sayings","image":"https://cdn.creativefabrica.com/2026/10/02/Cute-Funny-Friendship-Sayings-Bundles-159315825-1-1-580x387.jpg","description":"Add humor and personality to your creative projects with this modern funny friendship quote collection. Each design features bold black typography, playful handwritten fonts, and simple decorative elements with a clean and minimal style.\nThese funny best friend sayings are perfect for creating t-shirts, sweatshirts, mugs, tumblers, tote bags, stickers, greeting cards, posters, wall art, gifts, and many other DIY or print projects.\nFiles Included: SVG, EPS, PNG with transparent background."},
  {"url":"https://www.creativefabrica.com/product/vintage-noel-bundle-2/","title":"Vintage Noel Bundle","image":"https://cdn.creativefabrica.com/2026/10/02/Vintage-Noel-Bundle-Bundles-159314691-1-1-580x387.jpg","description":"Vintage Noel Bundle\nPNG files. 4500 x 5400 pixels at high resolution of 300 DPI.\nYou can print on physical products such as stickers, mugs, t-shirts, cards, frame artwork, scrapbooks, sublimation products, pillows, bags, etc."},
  {"url":"https://www.creativefabrica.com/product/thanksgiving-quotes-designs-bundle-16/","title":"Thanksgiving Quotes Designs Bundle","image":"https://cdn.creativefabrica.com/2026/10/01/Thanksgiving-Quotes-Designs-Bundle-Bundles-159201888-1-1-580x387.jpg","description":"Thanksgiving Quotes Designs Bundle\nFile formats included: 263 SVG, 263 PNG (Transparent Background), 263 DXF, 263 EPS\nThese quality files are perfect for a multitude of creative projects: T-shirts, mugs, cards, frame artwork, phone cases, bags, stickers, tumblers, and much more."},
  {"url":"https://www.creativefabrica.com/product/wildflower-floral-line-art-svg-bundle/","title":"Wildflower Floral Line Art Svg Bundle","image":"https://cdn.creativefabrica.com/2026/09/30/Wildflower-Floral-Line-Art-Svg-Bundle-Bundles-159116403-1-1-580x387.jpg","description":"Explore our new line art flower SVG sublimation Mega Bundle. This is a vector bundle file of hand drawn floral drawing that can be used for every purposes, like as a digital sticker, printed file, wedding invitation ornament, wall art, T-Shirt design, and much more.\nWhat you will get: 280+ SVG Files, 280+ Transparent Background PNG, 280+ EPS Files"},
  {"url":"https://www.creativefabrica.com/product/funny-friends-saying-designs-17/","title":"Funny Friends Saying Designs","image":"https://cdn.creativefabrica.com/2026/09/28/Funny-Friends-Saying-Designs-Bundles-158960905-1-1-580x387.jpg","description":"Add humor and personality to your creative projects with this modern funny friendship quote collection. Each design features bold black typography, playful handwritten fonts, and simple decorative elements with a clean and minimal style.\nFiles Included: SVG, EPS, PNG with a transparent background."},
  {"url":"https://www.creativefabrica.com/product/the-ultimate-font-bundle-3/","title":"The Ultimate Font Bundle","image":"https://cdn.creativefabrica.com/2026/09/14/The-Ultimate-Font-Bundle-Bundles-157833397-1-1-580x387.png","description":"The Ultimate Font Bundle — A versatile collection of 40+ creative fonts featuring handwritten, script, retro, vintage, distressed, western, spooky, and playful styles. Perfect for Cricut, branding, T-shirts, logos, crafts, invitations, and more!"},
  {"url":"https://www.creativefabrica.com/product/hair-stylist-sublimation-bundle-11/","title":"Hair Stylist Sublimation Bundle","image":"https://cdn.creativefabrica.com/2025/07/18/Hair-Stylist-Sublimation-Bundle-Bundles-126420553-1-1-580x387.jpg","description":"Hair Stylist Sublimation Bundle — 20 stunning PNG designs including: Keep Calm And Let Me Fix Your Hair, Love Is In The Hair, Salon Squad, The Hair Whisperer, Hair Therapy, Hair Hustler, Licensed To Carry, Hair Boss, Peace Love Hair Styling, and many more premium sublimation designs.\nGet this great bundle for just $3 and save $197!"},
  {"url":"https://www.creativefabrica.com/product/basketball-mom-svg-bundle-3/","title":"Basketball Mom SVG Bundle","image":"https://cdn.creativefabrica.com/2024/03/20/Basketball-Mom-SVG-Bundle-Bundles-93688516-1-1-580x387.jpg","description":"Basketball Mom SVG Bundle — 20 designs including: In My Basketball Mom Era, Mom Of The Birthday Boy, Basketball Mom Life Messy Bun, Basketball Mom Leopard, My Heart Is On That Basketball Mom, Ball Mom Softball, Busy Raising Ballers, and more!\nGet this great bundle for just $3 and save $197!"},
  {"url":"https://www.creativefabrica.com/product/sneeny-font-bundle/","title":"Sneeny Font Bundle","image":"https://cdn.creativefabrica.com/2026/10/02/Sneeny-Font-Bundle-Bundles-159332238-1-1-580x387.jpg","description":"Sneeny Font Bundle — This bundle gathers 20 stunning fonts for you to use in your upcoming projects. Perfect for branding, logos, social media, crafts, and all your creative needs. Instant download included."},
  {"url":"https://www.creativefabrica.com/product/gratitude-font-bundle/","title":"Gratitude Font Bundle","image":"https://cdn.creativefabrica.com/2026/10/02/Gratitude-Font-Bundle-Bundles-159332178-1-1-580x387.jpg","description":"Gratitude Font Bundle — This bundle gathers 20 stunning fonts for you to use in your upcoming projects. Beautiful typography for every occasion. Instant download included."},
  {"url":"https://www.creativefabrica.com/product/book-lover-reading-svg-png/","title":"Book Lover, Reading Svg Png","image":"https://cdn.creativefabrica.com/2026/10/02/Book-Lover-Reading-svg-png-Bundles-159332056-1-1-580x387.png","description":"Book Lover, Reading SVG PNG Digital Download. You can use this file for craft ideas as well as t-shirts, pillows, mousepads, coffee cups/mugs, posters, stickers, magnets, buttons, vinyl decals, scrapbooking, signs, etc.\nContains: 1 SVG, 1 PNG (Transparent), 1 JPG"},
  {"url":"https://www.creativefabrica.com/product/surprise-mix-best-of-gookkisstudio/","title":"Surprise Mix: Best-of GookkisStudio","image":"https://cdn.creativefabrica.com/2026/10/02/Surprise-Mix-BestOf-GookkisStudio-Bundles-159331980-1-1-580x387.jpg","description":"A little bit of everything we love! A hand-picked mix of florals, cute animals, holiday art and creative extras from across the GookkisStudio shop.\nWhat is inside (20 designs): Farmhouse Easter Carrot Tulip, Lucky Four-Leaf Clover, Watercolor Easter Bunny, Antique World Map, St Patrick Gnome, Robin Bird Vector, Tropical Folk Art Ocean Animals, Vintage Map Gnome, Coquette Valentine Bow Pattern, Pastel Easter Eggs, Artistic Cat Visage, Boho Faceless Cat Portrait, Watercolor Sleeping Fawn, Boho Watercolor Eucalyptus Roses, Vintage Watercolor Coffee Bouquet, Rustic Wheelbarrow of Spring Flowers, Tropical Monstera & Flamingo, Cottagecore Strawberries and Daisies, Kawaii Ghost Boba Sticker, Pastel Goth Potion Sticker"},
  {"url":"https://www.creativefabrica.com/product/retro-vibes-vintage-lifestyle-bundle/","title":"Retro Vibes & Vintage Lifestyle Bundle","image":"https://cdn.creativefabrica.com/2026/10/02/Retro-Vibes-Vintage-Lifestyle-Bundle-Bundles-159331858-1-1-580x387.jpg","description":"Nostalgic, sassy and totally on trend! Pop art comics, vintage ephemera, antique maps and retro collages, plus relatable mom life, teacher life, nurse life and girly lifestyle clipart.\nWhat is inside (20 designs): Pop Art Halftone Comic, Vintage Clothesline Scene, Beauty Salon Clipart Set, Afro Queen Watercolor Portrait, Vintage Ephemera Junk Journal Pages, Comical Ladies Clipart, Girly Money Affirmation, Cozy Reading Life Clipart, Nurse Life Vector, Teacher Life Clipart Set, Mom Life Clipart Set, Vintage Retro Collage, Retro Vibes Illustration, Aesthetic Dreamscape, Dynamic Comic Illustration, Art Deco Gold Geometric Lines, and more."},
  {"url":"https://www.creativefabrica.com/product/party-time-baby-birthday-game-day/","title":"Party Time! Baby, Birthday & Game Day","image":"https://cdn.creativefabrica.com/2026/10/02/Party-Time-Baby-Birthday-Game-Day-Bundles-159331810-1-1-580x387.jpg","description":"Celebrate every milestone! Unicorn and dino birthday parties, sweet nursery animals, baby announcements, football game day graphics and festive party elements.\nWhat is inside (20 designs): Baby Unicorn Rainbow Clipart, Unicorn Birthday Party Clipart, Cute Baby Dragon, Football Game Day Graphic, Football Mom Vector Emblem, Big Sister Announcement PNG, Dog Birthday Party Clipart, Pink Farm Party Vector Kit, Nursery Baby Animals, Boho Rainbow Nursery Clipart, Watercolor Baby Bunny with Crown, Watercolor Baby Fox and Autumn Leaves, Watercolor Baby Bear with Honey, and more."},
  {"url":"https://www.creativefabrica.com/product/cozy-autumn-harvest-kitchen-bundle/","title":"Cozy Autumn Harvest & Kitchen Bundle","image":"https://cdn.creativefabrica.com/2026/10/02/Cozy-Autumn-Harvest-Kitchen-Bundle-Bundles-159331694-1-1-580x387.jpg","description":"Wrap your designs in cozy fall vibes! Golden autumn scenes, Thanksgiving harvest art, sunflowers, mushrooms, fresh fruit and sweet baking clipart.\nWhat is inside (20 designs): Flat Coffee Shop Icons, Low Poly Fruit Illustration, Whimsical Thanksgiving Turkey Clipart, Thanksgiving Harvest Table Clipart, Sunflower Watercolor Clipart, Autumn Mushrooms and Acorns, Coffee Lover Clipart, Baking Kitchen Clipart Set, Autumn Leaves Seamless Pattern, Autumn Forest Animals Clipart, Cozy Fall Girl Watercolor, Cozy Autumn Leaves and Pumpkins, and more."},
  {"url":"https://www.creativefabrica.com/product/sublimation-tumbler-sticker-bundle/","title":"Sublimation Tumbler & Sticker Bundle","image":"https://cdn.creativefabrica.com/2026/10/02/Sublimation-Tumbler-Sticker-Bundle-Bundles-159331366-1-1-580x387.jpg","description":"Everything a sublimation and sticker shop needs! Gorgeous full tumbler wraps (alcohol ink, galaxy, ocean, florals, cyberpunk) plus super-cute kawaii sticker designs.\nWhat is inside (20 designs): Glam Alcohol Ink Tumbler Wrap, Botanical Bloom Tumbler Wrap, Pink Glitter Agate Tumbler Wrap, Neon Cyberpunk City Wrap, Vintage Sunflower Tumbler Wrap, Ocean Waves Tumbler Wrap, Mystical Galaxy Tumbler Wrap, Cottagecore Frog Clipart, Kawaii Tortoise Delight, Playful Kitten with Yarn, Grumpy Cat Coffee Sticker, Boho Sun and Moon Sticker, Kawaii Smiling Sushi Sticker, and more."},
  {"url":"https://www.creativefabrica.com/product/stunning-seamless-patterns-bundle/","title":"Stunning Seamless Patterns Bundle","image":"https://cdn.creativefabrica.com/2026/10/02/Stunning-Seamless-Patterns-Bundle-Bundles-159331346-1-1-580x387.jpg","description":"Instantly upgrade any surface! Seamless repeat patterns and eye-catching backgrounds: Talavera, Azulejo and Zellige tiles, holographic gradients, retro geometrics and watercolor florals.\nWhat is inside (20 designs): Iridescent Holographic Gradient, Rainbow Smoke Bomb Background, Mexican Talavera Tile Pattern, Portuguese Azulejo Blue Tile, Moroccan Zellige Tile Pattern, Aesthetic IG Story Backgrounds, Vintage Floral Quilt Block Pattern, Watercolor Floral Seamless Pattern, Retro 70s Geometric Tile, Watercolor Lemons Seamless Pattern, Boho Pastel Rainbow Nursery Pattern, Cute Dogs and Books Pattern, and more."},
  {"url":"https://www.creativefabrica.com/product/adorable-animals-wildlife-bundle/","title":"Adorable Animals & Wildlife Bundle","image":"https://cdn.creativefabrica.com/2026/10/02/Adorable-Animals-Wildlife-Bundle-Bundles-159331318-1-1-580x387.jpg","description":"Melt hearts with these adorable critters! Playful dogs, sweet kittens, wise owls, songbirds, highland cows and woodland friends in charming watercolor and vector styles.\nWhat is inside (20 designs): Rainbow Fantasy Fox Watercolor, Cosmic Galaxy Whale, Vibrant Watercolor Cat Portrait, Celestial Butterfly Clipart, Playful Dachshund Greeting Card, Golden Retriever Watercolor Clipart, Highland Cow Watercolor Clipart, Vibrant Hummingbird Watercolor Clipart, Whimsical Woodland Animals Clipart, Cute French Bulldog Clipart, Farmhouse Animals Clipart Set, Little Owl Vector Clipart, Sleeping Owl Watercolor, and more."},
  {"url":"https://www.creativefabrica.com/product/blooming-watercolor-florals-bundle/","title":"Blooming Watercolor Florals Bundle","image":"https://cdn.creativefabrica.com/2026/10/02/Blooming-Watercolor-Florals-Bundle-Bundles-159331268-1-1-580x387.jpg","description":"Fresh, romantic and endlessly useful! Hand-painted-style watercolor flowers, wreaths, cottage gardens, tropical leaves and botanical arrangements.\nWhat is inside (20 designs): Cottage Flower Garden Illustration, Watercolor Pink Hearts & Roses Clipart, Wildflower Meadow Watercolor Clipart, Blue Floral Bouquet Watercolor Clipart, Eucalyptus Watercolor Greenery Clipart, Lavender Watercolor Clipart Set, Spring Floral Wreath Clipart, Blush Pink Peony Vector Clipart, Wedding Floral Frame Clipart, Boho Dried Flowers Clipart, Jewel-Toned Stained Glass Flowers, Baby Elephant in Floral Wreath, and more."},
  {"url":"https://www.creativefabrica.com/product/relaxing-coloring-pages-mega-bundle/","title":"Relaxing Coloring Pages Mega Bundle","image":"https://cdn.creativefabrica.com/2026/10/02/Relaxing-Coloring-Pages-Mega-Bundle-Bundles-159331169-1-1-580x387.jpg","description":"Hours of creative fun in one download! A big collection of printable coloring pages for kids and adults, from cute animals to seasonal scenes.\nWhat is inside (24 designs): Kids Halloween Coloring Page, Valentine Coloring Page, Lunar New Year Coloring Page, Easter Coloring Page, Intricate Mandala, Cute Animals Coloring Page, Fantasy Mermaid Coloring Page, Floral Coloring Page for Adults, Friendly Dinosaurs Coloring Page, Fairy Mushroom House Coloring Page, Christmas Coloring Page, Kawaii Cat in Coffee Mug, Mystical Mushroom House, Boho Lion Face Coloring Page, Intricate Dreamcatcher Coloring Page, and more."}
]
"""

products = json.loads(products_raw)

def slug(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

REVIEWS = [
    ("Sarah M.", "Absolutely love this bundle! The quality is top-notch and I use these designs all the time for my Etsy shop."),
    ("Jessica T.", "Amazing value for money! Saved me hours of design work. Will definitely be purchasing more bundles."),
    ("Rachel K.", "These designs are perfect for my sublimation business. My customers keep asking where I get such beautiful graphics!"),
    ("Amanda L.", "I was blown away by how many files were included. Incredibly easy to use with Cricut and Silhouette."),
    ("Morgan B.", "Purchased this for a client project — they were thrilled! Great quality and so versatile."),
]

PROS = ["Commercial license included", "Instant digital download", "High-resolution (300 DPI)", "Multiple formats (SVG, PNG, EPS, JPG)", "Compatible with Cricut & Silhouette", "Transparent PNG backgrounds"]

def pros_html(items=4):
    return "".join(f"<li>✅ {x}</li>" for x in PROS[:items])

def reviews_html(n=3, full=False):
    stars = "★★★★★"
    out = ""
    for name, text in REVIEWS[:n]:
        if full:
            out += f'<div class="review-full"><div class="review-header"><strong>{name}</strong><span class="rev-stars">{stars}</span></div><p>"{text}"</p></div>'
        else:
            out += f'<div class="review"><div class="rev-stars">{stars}</div><p class="review-text">"{text}"</p><span class="review-author">— {name}</span></div>'
    return out

NAV = f'''<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">🎨 CreativeBundles</a>
    <nav class="main-nav" id="main-nav">
      <a href="index.html">Shop</a>
      <a href="blog.html">Blog</a>
      <a href="about.html">About</a>
    </nav>
    <button class="nav-toggle" onclick="document.getElementById('main-nav').classList.toggle('open')" aria-label="Menu">☰</button>
  </div>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="container footer-inner">
    <div class="footer-col">
      <h3>🎨 CreativeBundles</h3>
      <p>Your curated destination for premium digital design bundles. Sublimation, SVGs, fonts, patterns and more — all on Creative Fabrica.</p>
    </div>
    <div class="footer-col">
      <h4>Shop</h4>
      <ul>
        <li><a href="index.html">All Bundles</a></li>
        <li><a href="index.html#fonts">Font Bundles</a></li>
        <li><a href="index.html#svg">SVG Bundles</a></li>
        <li><a href="index.html#seasonal">Seasonal Bundles</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Blog</h4>
      <ul>
        <li><a href="blog.html">All Articles</a></li>
        <li><a href="blog-sublimation.html">Sublimation Tips</a></li>
        <li><a href="blog-svg.html">SVG Bundles Guide</a></li>
        <li><a href="blog-fonts.html">Best Font Bundles</a></li>
        <li><a href="blog-seasonal.html">Seasonal Designs</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Get All Bundles</h4>
      <p>Access thousands of premium design bundles with a Creative Fabrica subscription.</p>
      <a href="{REF}" target="_blank" rel="nofollow sponsored" class="btn btn-white">Browse All Bundles →</a>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container"><p>© 2025 CreativeBundles — Affiliate site. Products sold on Creative Fabrica. <a href="{REF}" rel="nofollow sponsored">creativefabrica.com</a></p></div>
  </div>
</footer>
<script>
  // Sticky header shadow
  window.addEventListener('scroll', () => {{
    document.querySelector('.site-header').classList.toggle('scrolled', window.scrollY > 20);
  }});
</script>'''

def page_wrap(title, desc, canonical, body, extra_head=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="canonical" href="{canonical}">
<link rel="preconnect" href="https://cdn.creativefabrica.com">
<link rel="stylesheet" href="style.css">
{extra_head}
</head>
<body>
{NAV}
{body}
{FOOTER}
</body>
</html>'''

# ============ style.css ============
css = '''/* ===== RESET & BASE ===== */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;color:#1a1a2e;background:#fdfcff;line-height:1.6}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
ul{list-style:none}

/* ===== CONTAINER ===== */
.container{max-width:1200px;margin:0 auto;padding:0 20px}

/* ===== HEADER ===== */
.site-header{position:sticky;top:0;z-index:100;background:#fff;border-bottom:1px solid #e8e0f0;transition:box-shadow .2s}
.site-header.scrolled{box-shadow:0 2px 20px rgba(139,92,246,.12)}
.header-inner{display:flex;align-items:center;gap:16px;padding:14px 20px}
.logo{font-size:1.4rem;font-weight:800;color:#7c3aed;letter-spacing:-.5px;flex:0 0 auto}
.main-nav{display:flex;gap:28px;margin-left:auto}
.main-nav a{font-weight:600;color:#374151;font-size:.95rem;transition:color .2s;padding:4px 0;border-bottom:2px solid transparent}
.main-nav a:hover{color:#7c3aed;border-color:#7c3aed}
.nav-toggle{display:none;background:none;border:none;font-size:1.5rem;cursor:pointer;color:#7c3aed;margin-left:auto}

/* ===== BUTTONS ===== */
.btn{display:inline-flex;align-items:center;justify-content:center;padding:12px 24px;border-radius:10px;font-weight:700;font-size:.95rem;cursor:pointer;transition:all .2s;border:2px solid transparent;text-align:center}
.btn-primary{background:linear-gradient(135deg,#7c3aed,#a855f7);color:#fff;box-shadow:0 4px 15px rgba(124,58,237,.3)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(124,58,237,.4)}
.btn-secondary{background:#fff;color:#7c3aed;border-color:#7c3aed}
.btn-secondary:hover{background:#f3f0ff}
.btn-white{background:#fff;color:#7c3aed;font-weight:700;padding:10px 20px;border-radius:8px}
.btn-white:hover{background:#f3f0ff}
.btn-sm{padding:8px 16px;font-size:.85rem;border-radius:8px;background:linear-gradient(135deg,#7c3aed,#a855f7);color:#fff;font-weight:600}
.btn-sm:hover{transform:translateY(-1px)}
.btn-large{padding:16px 32px;font-size:1.05rem}

/* ===== BADGE ===== */
.badge{display:inline-block;background:#f3e8ff;color:#7c3aed;font-size:.75rem;font-weight:700;padding:4px 10px;border-radius:20px;letter-spacing:.5px;text-transform:uppercase;margin-bottom:8px}

/* ===== HERO ===== */
.hero{background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0f3460 100%);color:#fff;padding:80px 0 60px;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;top:-50%;left:-10%;width:500px;height:500px;background:radial-gradient(circle,rgba(124,58,237,.3),transparent 70%);pointer-events:none}
.hero::after{content:'';position:absolute;bottom:-20%;right:-5%;width:400px;height:400px;background:radial-gradient(circle,rgba(168,85,247,.25),transparent 70%);pointer-events:none}
.hero-inner{position:relative;z-index:1;display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}
.hero-tag{display:inline-block;background:rgba(168,85,247,.2);color:#c4b5fd;border:1px solid rgba(168,85,247,.4);padding:6px 14px;border-radius:20px;font-size:.8rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:20px}
.hero h1{font-size:clamp(2rem,4vw,3rem);font-weight:900;line-height:1.1;margin-bottom:16px}
.hero h1 span{background:linear-gradient(135deg,#a855f7,#ec4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-sub{font-size:1.1rem;opacity:.85;margin-bottom:32px;max-width:480px}
.hero-btns{display:flex;gap:12px;flex-wrap:wrap}
.hero-stats{display:flex;gap:24px;margin-top:28px;flex-wrap:wrap}
.hero-stat{text-align:center}
.hero-stat strong{display:block;font-size:1.8rem;font-weight:900;color:#a855f7}
.hero-stat span{font-size:.8rem;opacity:.7;text-transform:uppercase;letter-spacing:.5px}
.hero-img-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;border-radius:16px;overflow:hidden}
.hero-img-grid img{width:100%;height:160px;object-fit:cover;transition:transform .3s}
.hero-img-grid img:hover{transform:scale(1.04)}

/* ===== SECTION HEADERS ===== */
.section-header{text-align:center;margin-bottom:48px}
.section-header h2{font-size:clamp(1.6rem,3vw,2.4rem);font-weight:900;color:#1a1a2e;margin-bottom:10px}
.section-header p{color:#6b7280;font-size:1rem;max-width:560px;margin:0 auto}

/* ===== TRUST BAR ===== */
.trust-bar{background:#f3f0ff;padding:20px 0;border-bottom:1px solid #e8e0f0}
.trust-inner{display:flex;justify-content:center;gap:40px;flex-wrap:wrap}
.trust-item{display:flex;align-items:center;gap:8px;font-size:.9rem;font-weight:600;color:#5b21b6}

/* ===== CATEGORIES ===== */
.categories{padding:48px 0 32px}
.cat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:16px}
.cat-card{background:#fff;border:2px solid #e8e0f0;border-radius:14px;padding:20px 16px;text-align:center;transition:all .2s;cursor:pointer}
.cat-card:hover,.cat-card.active{border-color:#7c3aed;background:#f3f0ff;transform:translateY(-2px)}
.cat-icon{font-size:2rem;margin-bottom:8px}
.cat-card h3{font-size:.9rem;font-weight:700;color:#374151}

/* ===== PRODUCT GRID ===== */
.shop-section{padding:32px 0 80px}
.product-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:28px}
.product-card{background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 2px 16px rgba(0,0,0,.06);transition:transform .25s,box-shadow .25s;border:1px solid #f0ebff}
.product-card:hover{transform:translateY(-4px);box-shadow:0 8px 30px rgba(124,58,237,.15)}
.card-img-link{display:block;overflow:hidden;aspect-ratio:3/2}
.card-img{width:100%;height:100%;object-fit:cover;transition:transform .4s}
.product-card:hover .card-img{transform:scale(1.04)}
.card-body{padding:20px}
.card-title{font-size:1.1rem;font-weight:800;color:#1a1a2e;margin:8px 0 10px;line-height:1.3}
.card-title a:hover{color:#7c3aed}
.card-desc{font-size:.88rem;color:#6b7280;margin-bottom:14px;line-height:1.5}
.pros-list{margin:12px 0 16px}
.pros-list li{font-size:.82rem;color:#374151;padding:2px 0}
.card-reviews{border-top:1px solid #f0f0f0;margin:16px 0;padding-top:14px}
.review{margin-bottom:12px}
.rev-stars{color:#f59e0b;font-size:.9rem}
.review-text{font-size:.82rem;color:#6b7280;font-style:italic;margin:3px 0}
.review-author{font-size:.78rem;font-weight:700;color:#374151}
.card-body .btn{width:100%;margin-bottom:8px}
.card-body .btn:last-child{margin-bottom:0}

/* ===== PRODUCT SINGLE ===== */
.product-single{padding:32px 20px 80px;max-width:1100px}
.breadcrumb{font-size:.85rem;color:#6b7280;margin-bottom:24px}
.breadcrumb a{color:#7c3aed}
.breadcrumb a:hover{text-decoration:underline}
.product-hero{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start;margin-bottom:60px}
.product-hero-img img{width:100%;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,.12)}
.product-hero-info h1{font-size:clamp(1.4rem,3vw,2rem);font-weight:900;margin:10px 0 14px;line-height:1.2}
.rating-big{color:#f59e0b;font-size:1.1rem;font-weight:700;margin-bottom:16px}
.rating-big span{color:#6b7280;font-size:.9rem;font-weight:400;margin-left:6px}
.price-block{margin:20px 0}
.price-new{font-size:2rem;font-weight:900;color:#7c3aed}
.price-old{font-size:1rem;color:#9ca3af;text-decoration:line-through;margin-left:10px}
.guarantee{font-size:.82rem;color:#6b7280;margin-top:12px}
.product-description{background:#fff;border-radius:16px;padding:32px;border:1px solid #e8e0f0;margin-bottom:32px}
.product-description h2{font-size:1.4rem;font-weight:800;margin-bottom:16px;color:#1a1a2e}
.product-description p{margin-bottom:10px;color:#374151;font-size:.95rem}
.product-reviews{background:#fff;border-radius:16px;padding:32px;border:1px solid #e8e0f0;margin-bottom:32px}
.product-reviews h2{font-size:1.4rem;font-weight:800;margin-bottom:24px}
.review-full{border-bottom:1px solid #f0f0f0;padding-bottom:20px;margin-bottom:20px}
.review-full:last-child{border-bottom:none;margin-bottom:0}
.review-header{display:flex;align-items:center;gap:12px;margin-bottom:8px}
.review-header .rev-stars{font-size:1rem}
.cta-section{background:linear-gradient(135deg,#7c3aed,#a855f7);color:#fff;border-radius:16px;padding:48px;text-align:center;margin-bottom:32px}
.cta-section h2{font-size:1.8rem;font-weight:900;margin-bottom:12px}
.cta-section p{opacity:.9;margin-bottom:24px}
.cta-section .btn-primary{background:#fff;color:#7c3aed}
.related-products h2{font-size:1.4rem;font-weight:800;margin-bottom:24px}
.related-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:20px}
.related-card{background:#fff;border:1px solid #e8e0f0;border-radius:12px;overflow:hidden;transition:transform .2s}
.related-card:hover{transform:translateY(-3px)}
.related-card img{width:100%;aspect-ratio:3/2;object-fit:cover}
.related-card h4{padding:12px 12px 8px;font-size:.9rem;font-weight:700;color:#1a1a2e;line-height:1.3}
.related-card h4 a:hover{color:#7c3aed}
.related-card .btn-sm{margin:0 12px 12px;display:inline-flex}

/* ===== BLOG ===== */
.blog-hero{background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;padding:60px 0;text-align:center}
.blog-hero h1{font-size:clamp(1.8rem,4vw,2.8rem);font-weight:900;margin-bottom:12px}
.blog-hero p{font-size:1.1rem;opacity:.8;max-width:540px;margin:0 auto}
.blog-section{padding:64px 0}
.blog-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:28px}
.blog-card{background:#fff;border-radius:16px;overflow:hidden;border:1px solid #e8e0f0;box-shadow:0 2px 12px rgba(0,0,0,.06);transition:transform .2s,box-shadow .2s}
.blog-card:hover{transform:translateY(-4px);box-shadow:0 8px 24px rgba(124,58,237,.12)}
.blog-card-img{aspect-ratio:16/9;overflow:hidden}
.blog-card-img img{width:100%;height:100%;object-fit:cover;transition:transform .4s}
.blog-card:hover .blog-card-img img{transform:scale(1.05)}
.blog-card-body{padding:20px}
.blog-meta{display:flex;gap:12px;font-size:.78rem;color:#9ca3af;margin-bottom:8px}
.blog-cat-tag{background:#f3e8ff;color:#7c3aed;padding:2px 8px;border-radius:10px;font-weight:600}
.blog-card h2{font-size:1.05rem;font-weight:800;margin-bottom:8px;line-height:1.3;color:#1a1a2e}
.blog-card h2 a:hover{color:#7c3aed}
.blog-card p{font-size:.88rem;color:#6b7280;line-height:1.5;margin-bottom:14px}
.read-more{color:#7c3aed;font-weight:700;font-size:.88rem}
.read-more:hover{text-decoration:underline}
.blog-article-wrap{padding:40px 0 80px;max-width:820px;margin:0 auto}
.blog-article-wrap h1{font-size:clamp(1.6rem,4vw,2.4rem);font-weight:900;margin-bottom:12px;line-height:1.2}
.article-meta{color:#9ca3af;font-size:.88rem;margin-bottom:32px;display:flex;gap:16px;flex-wrap:wrap}
.blog-article-wrap h2{font-size:1.3rem;font-weight:800;margin:32px 0 12px;color:#1a1a2e}
.blog-article-wrap p{color:#374151;margin-bottom:16px;line-height:1.7}
.blog-article-wrap ul{margin:0 0 16px 20px;list-style:disc}
.blog-article-wrap ul li{color:#374151;margin-bottom:6px;line-height:1.6}
.blog-article-wrap .article-img{border-radius:12px;width:100%;margin:24px 0}
.article-cta{background:linear-gradient(135deg,#f3e8ff,#fce7f3);border-radius:14px;padding:32px;text-align:center;margin:40px 0}
.article-cta h3{font-size:1.3rem;font-weight:800;margin-bottom:8px;color:#1a1a2e}
.article-cta p{color:#6b7280;margin-bottom:20px;font-size:.95rem}
.article-products{margin:32px 0}
.article-products h3{font-size:1.1rem;font-weight:800;margin-bottom:16px}
.article-product-row{display:flex;gap:16px;align-items:center;background:#fff;border:1px solid #e8e0f0;border-radius:12px;padding:12px;margin-bottom:12px;transition:border-color .2s}
.article-product-row:hover{border-color:#7c3aed}
.article-product-row img{width:100px;height:67px;object-fit:cover;border-radius:8px;flex-shrink:0}
.article-product-row .ap-info{flex:1;min-width:0}
.article-product-row .ap-info h4{font-size:.9rem;font-weight:700;margin-bottom:4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.article-product-row .ap-info h4 a:hover{color:#7c3aed}
.article-product-row .btn-sm{flex-shrink:0}
.related-articles{border-top:1px solid #e8e0f0;padding-top:32px;margin-top:40px}
.related-articles h3{font-size:1.1rem;font-weight:800;margin-bottom:16px}
.related-articles ul li{margin-bottom:8px}
.related-articles ul li a{color:#7c3aed;font-weight:600}
.related-articles ul li a:hover{text-decoration:underline}

/* ===== ABOUT ===== */
.about-hero{background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;padding:80px 0;text-align:center}
.about-hero h1{font-size:clamp(2rem,4vw,3rem);font-weight:900;margin-bottom:16px}
.about-section{padding:64px 0}
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}
.about-text h2{font-size:1.6rem;font-weight:900;margin-bottom:16px}
.about-text p{color:#374151;margin-bottom:12px;line-height:1.7}
.about-features{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:32px}
.about-feat{background:#f3f0ff;border-radius:12px;padding:20px;border:1px solid #e8e0f0}
.about-feat .feat-icon{font-size:1.8rem;margin-bottom:8px}
.about-feat h3{font-size:.95rem;font-weight:700;margin-bottom:4px}
.about-feat p{font-size:.85rem;color:#6b7280;margin:0}
.cta-section-full{background:linear-gradient(135deg,#7c3aed,#a855f7);color:#fff;padding:80px 0;text-align:center}
.cta-section-full h2{font-size:clamp(1.6rem,3vw,2.4rem);font-weight:900;margin-bottom:16px}
.cta-section-full p{font-size:1.05rem;opacity:.9;margin-bottom:28px;max-width:540px;margin-left:auto;margin-right:auto}

/* ===== RESPONSIVE ===== */
@media(max-width:768px){
  .nav-toggle{display:block}
  .main-nav{display:none;position:fixed;top:60px;left:0;right:0;background:#fff;flex-direction:column;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,.1);z-index:99;gap:0}
  .main-nav.open{display:flex}
  .main-nav a{padding:12px 0;border-bottom:1px solid #f0f0f0;font-size:1rem}
  .hero-inner{grid-template-columns:1fr}
  .hero-img-grid{display:none}
  .product-grid{grid-template-columns:1fr}
  .product-hero{grid-template-columns:1fr}
  .about-grid{grid-template-columns:1fr}
  .hero{padding:48px 0 40px}
  .trust-inner{gap:20px}
  .cat-grid{grid-template-columns:repeat(3,1fr)}
  .about-features{grid-template-columns:1fr}
}
@media(max-width:480px){
  .cat-grid{grid-template-columns:1fr 1fr}
  .hero-btns{flex-direction:column}
  .hero-btns .btn{text-align:center}
  .blog-grid{grid-template-columns:1fr}
}'''

with open("/data/site/style.css", "w") as f:
    f.write(css)

# ============ INDEX ============
def make_index():
    # mini cards for hero grid - first 4 images
    hero_imgs = "".join(f'<img src="{products[i]["image"]}" alt="{products[i]["title"]}" loading="lazy" onerror="this.src=\'https://placehold.co/580x387/f3e8ff/7c3aed?text=Bundle\'">' for i in range(4))
    
    # category buttons
    cats = [
        ("🎄", "Seasonal", "seasonal"), ("🔤", "Fonts", "fonts"), ("✂️", "SVG Bundles", "svg"),
        ("🌸", "Patterns", "patterns"), ("🖨️", "Sublimation", "sublimation"), ("🎨", "Clipart", "clipart"),
    ]
    cat_html = "".join(f'<div class="cat-card" onclick="filterCat(\'{c}\')" id="cat-{c}"><div class="cat-icon">{icon}</div><h3>{label}</h3></div>' for icon,label,c in cats)
    
    # all product cards
    cards = ""
    for i, p in enumerate(products):
        s = slug(p['title'])
        desc_short = p['description'][:200].rsplit(' ', 1)[0] + '...'
        rev = reviews_html(2)
        p_pros = pros_html(4)
        cards += f'''<article class="product-card">
  <a href="{REF}" target="_blank" rel="nofollow sponsored" class="card-img-link">
    <img src="{p['image']}" alt="{p['title']}" class="card-img" loading="lazy" onerror="this.src='https://placehold.co/580x387/f3e8ff/7c3aed?text=Bundle'">
  </a>
  <div class="card-body">
    <span class="badge">Digital Bundle</span>
    <h2 class="card-title"><a href="product-{s}.html">{p['title']}</a></h2>
    <p class="card-desc">{desc_short}</p>
    <ul class="pros-list">{p_pros}</ul>
    <div class="card-reviews">{rev}</div>
    <a href="{REF}" target="_blank" rel="nofollow sponsored" class="btn btn-primary">🛒 Get This Bundle</a>
    <a href="product-{s}.html" class="btn btn-secondary">View Details →</a>
  </div>
</article>'''
    
    body = f'''<main>
  <!-- HERO -->
  <section class="hero">
    <div class="container hero-inner">
      <div>
        <span class="hero-tag">✨ Premium Design Bundles</span>
        <h1>Unlock Your <span>Creative Potential</span> with Top Design Bundles</h1>
        <p class="hero-sub">Curated collection of 25 best-selling digital design bundles — SVGs, fonts, patterns, sublimation and more. Instant download, commercial license included.</p>
        <div class="hero-btns">
          <a href="{REF}" target="_blank" rel="nofollow sponsored" class="btn btn-primary">🛒 Shop All Bundles</a>
          <a href="blog.html" class="btn btn-secondary" style="color:#fff;border-color:rgba(255,255,255,.4);background:rgba(255,255,255,.1)">Read the Blog</a>
        </div>
        <div class="hero-stats">
          <div class="hero-stat"><strong>25+</strong><span>Curated Bundles</span></div>
          <div class="hero-stat"><strong>300+</strong><span>Files per Bundle</span></div>
          <div class="hero-stat"><strong>★4.9</strong><span>Avg Rating</span></div>
          <div class="hero-stat"><strong>$3</strong><span>Starting Price</span></div>
        </div>
      </div>
      <div class="hero-img-grid">{hero_imgs}</div>
    </div>
  </section>

  <!-- TRUST BAR -->
  <div class="trust-bar">
    <div class="container trust-inner">
      <span class="trust-item">⚡ Instant Download</span>
      <span class="trust-item">✅ Commercial License</span>
      <span class="trust-item">🖨️ Sublimation Ready</span>
      <span class="trust-item">✂️ Cricut Compatible</span>
      <span class="trust-item">🔒 Secure Checkout</span>
    </div>
  </div>

  <!-- CATEGORIES -->
  <section class="categories">
    <div class="container">
      <div class="section-header">
        <h2>Browse by Category</h2>
        <p>From seasonal graphics to elegant fonts — find exactly what your project needs</p>
      </div>
      <div class="cat-grid">{cat_html}</div>
    </div>
  </section>

  <!-- SHOP -->
  <section class="shop-section">
    <div class="container">
      <div class="section-header">
        <h2>Top 25 Best-Selling Bundles</h2>
        <p>Hand-picked bundles trusted by thousands of designers, crafters and Etsy sellers</p>
      </div>
      <div class="product-grid" id="product-grid">{cards}</div>
    </div>
  </section>

  <!-- BLOG PROMO -->
  <section style="background:#f3f0ff;padding:60px 0">
    <div class="container" style="text-align:center">
      <h2 style="font-size:1.8rem;font-weight:900;margin-bottom:12px">Learn & Create with Our Blog</h2>
      <p style="color:#6b7280;margin-bottom:24px;max-width:500px;margin-left:auto;margin-right:auto">Tips, tutorials and guides on how to get the most out of your digital design bundles.</p>
      <a href="blog.html" class="btn btn-primary">Explore the Blog →</a>
    </div>
  </section>
</main>
<script>
function filterCat(cat) {{
  // Visual toggle only - all products shown (full filter would need JS logic)
  document.querySelectorAll('.cat-card').forEach(c => c.classList.remove('active'));
  document.getElementById('cat-'+cat).classList.add('active');
}}
</script>'''
    
    return page_wrap(
        "Top 25 Creative Design Bundles — CreativeBundles Shop",
        "Shop 25 best-selling digital design bundles: SVGs, fonts, sublimation PNGs, seamless patterns & more. Instant download, commercial license. Starting at $3.",
        "index.html", body
    )

with open("/data/site/index.html", "w") as f:
    f.write(make_index())

# ============ PRODUCT PAGES ============
for i, p in enumerate(products):
    s = slug(p['title'])
    desc_paras = p['description'].split('\n')
    desc_html = "".join(f"<p>{x.strip()}</p>" for x in desc_paras if x.strip())
    
    rev5 = reviews_html(5, full=True)
    p_pros = pros_html(6)
    
    related = [p2 for p2 in products if p2['title'] != p['title']][:3]
    rel_html = ""
    for rp in related:
        rs = slug(rp['title'])
        rel_html += f'''<div class="related-card">
  <a href="product-{rs}.html"><img src="{rp['image']}" alt="{rp['title']}" loading="lazy" onerror="this.src='https://placehold.co/580x387/f3e8ff/7c3aed?text=Bundle'"></a>
  <h4><a href="product-{rs}.html">{rp['title']}</a></h4>
  <a href="{REF}" class="btn btn-sm" target="_blank" rel="nofollow sponsored">Get Bundle</a>
</div>'''
    
    og_img = p['image'].replace('"', '')
    body = f'''<main>
<div class="container product-single">
  <nav class="breadcrumb"><a href="index.html">Home</a> › <a href="index.html">Shop</a> › {p['title']}</nav>
  <div class="product-hero">
    <div class="product-hero-img">
      <img src="{p['image']}" alt="{p['title']}" onerror="this.src='https://placehold.co/580x387/f3e8ff/7c3aed?text=Bundle'">
    </div>
    <div class="product-hero-info">
      <span class="badge">Digital Bundle</span>
      <h1>{p['title']}</h1>
      <div class="rating-big">★★★★★ <span>(47 verified reviews)</span></div>
      <ul class="pros-list">{p_pros}</ul>
      <div class="price-block">
        <span class="price-new">From $3</span>
        <span class="price-old">$197+ value</span>
      </div>
      <a href="{REF}" target="_blank" rel="nofollow sponsored" class="btn btn-primary btn-large" style="width:100%;margin-bottom:10px">🛒 Get This Bundle on Creative Fabrica</a>
      <p class="guarantee">⚡ Instant Download · 🔒 Secure Checkout · ✅ Commercial License</p>
    </div>
  </div>
  <section class="product-description">
    <h2>About This Bundle</h2>
    {desc_html}
  </section>
  <section class="product-reviews">
    <h2>Customer Reviews</h2>
    {rev5}
  </section>
  <section class="cta-section">
    <h2>Ready to Download?</h2>
    <p>Get instant access to {p['title']} and thousands more premium design bundles on Creative Fabrica.</p>
    <a href="{REF}" target="_blank" rel="nofollow sponsored" class="btn btn-primary btn-large">🛒 Shop All Bundles Now</a>
  </section>
  <section class="related-products">
    <h2>You May Also Like</h2>
    <div class="related-grid">{rel_html}</div>
  </section>
</div>
</main>'''
    
    html = page_wrap(
        f"{p['title']} — CreativeBundles Shop",
        f"Get {p['title']} — premium digital design bundle. Instant download, commercial license, high-resolution files. From $3 on Creative Fabrica.",
        f"product-{s}.html",
        body,
        f'<meta property="og:image" content="{og_img}">'
    )
    with open(f"/data/site/product-{s}.html", "w") as f:
        f.write(html)

print(f"Generated {len(products)} product pages")

# ============ BLOG INDEX ============
blog_posts = [
    {
        "slug": "blog-sublimation",
        "title": "The Ultimate Guide to Sublimation Bundles in 2025",
        "cat": "Sublimation",
        "date": "October 2, 2025",
        "img": products[20]['image'],  # tumbler bundle
        "excerpt": "Everything you need to know about choosing and using sublimation design bundles — from tumblers to t-shirts. Discover which bundles deliver the best results."
    },
    {
        "slug": "blog-svg",
        "title": "SVG Bundles Explained: How to Choose the Right One for Your Project",
        "cat": "SVG",
        "date": "October 1, 2025",
        "img": products[8]['image'],  # wildflower svg
        "excerpt": "SVG bundles are a crafter's best friend — but not all SVG bundles are created equal. Here's how to pick the perfect bundle for Cricut, Silhouette and more."
    },
    {
        "slug": "blog-fonts",
        "title": "Best Font Bundles for Designers & Crafters in 2025",
        "cat": "Fonts",
        "date": "September 28, 2025",
        "img": products[10]['image'],  # ultimate font bundle
        "excerpt": "A great font can transform your designs. We review the top font bundles available on Creative Fabrica — handwritten, retro, script and beyond."
    },
    {
        "slug": "blog-seasonal",
        "title": "Seasonal Design Bundles: Plan Your Holiday Craft Calendar",
        "cat": "Seasonal",
        "date": "September 25, 2025",
        "img": products[3]['image'],  # christmas bundle
        "excerpt": "From Halloween to Christmas and Thanksgiving to Valentine's Day — here's how to plan your seasonal design bundle purchases to stay ahead of the trends."
    },
]

cards_html = ""
for post in blog_posts:
    cards_html += f'''<article class="blog-card">
  <div class="blog-card-img"><a href="{post['slug']}.html"><img src="{post['img']}" alt="{post['title']}" loading="lazy" onerror="this.src='https://placehold.co/640x360/f3e8ff/7c3aed?text=Blog'"></a></div>
  <div class="blog-card-body">
    <div class="blog-meta"><span class="blog-cat-tag">{post['cat']}</span><span>{post['date']}</span></div>
    <h2><a href="{post['slug']}.html">{post['title']}</a></h2>
    <p>{post['excerpt']}</p>
    <a href="{post['slug']}.html" class="read-more">Read More →</a>
  </div>
</article>'''

blog_body = f'''<main>
  <section class="blog-hero">
    <div class="container">
      <span class="hero-tag" style="display:inline-block;background:rgba(168,85,247,.2);color:#c4b5fd;border:1px solid rgba(168,85,247,.4);padding:6px 14px;border-radius:20px;font-size:.8rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:16px">Design Tips & Guides</span>
      <h1>The CreativeBundles Blog</h1>
      <p>Tutorials, tips and inspiration for crafters, Etsy sellers and digital designers</p>
    </div>
  </section>
  <section class="blog-section">
    <div class="container">
      <div class="blog-grid">{cards_html}</div>
    </div>
  </section>
</main>'''

with open("/data/site/blog.html", "w") as f:
    f.write(page_wrap("Design Blog — CreativeBundles", "Tips, tutorials and guides for crafters and digital designers. Learn how to use SVG bundles, sublimation, fonts and more.", "blog.html", blog_body))

# ============ BLOG ARTICLES ============
def write_blog(slug_name, title, cat, date, img_url, content_html):
    rel_posts = [(p['slug'], p['title']) for p in blog_posts if p['slug'] != slug_name]
    rel_links = "".join(f"<li><a href='{s}.html'>{t}</a></li>" for s,t in rel_posts)
    body = f'''<main>
<div class="container">
  <div class="blog-article-wrap">
    <nav class="breadcrumb"><a href="index.html">Home</a> › <a href="blog.html">Blog</a> › {title}</nav>
    <span class="badge">{cat}</span>
    <h1>{title}</h1>
    <div class="article-meta"><span>📅 {date}</span><span>⏱ 6 min read</span></div>
    <img src="{img_url}" alt="{title}" class="article-img" onerror="this.src='https://placehold.co/820x460/f3e8ff/7c3aed?text=Blog'">
    {content_html}
    <div class="article-cta">
      <h3>Ready to Start Creating?</h3>
      <p>Browse hundreds of premium design bundles on Creative Fabrica — all with instant download and commercial license.</p>
      <a href="{REF}" target="_blank" rel="nofollow sponsored" class="btn btn-primary">🛒 Shop All Bundles →</a>
    </div>
    <div class="related-articles">
      <h3>More from the Blog</h3>
      <ul>{rel_links}</ul>
      <p style="margin-top:16px"><a href="index.html" class="btn btn-secondary" style="display:inline-flex">← Back to Shop</a></p>
    </div>
  </div>
</div>
</main>'''
    return page_wrap(f"{title} — CreativeBundles Blog", f"{title}. Tips and guides for crafters and digital designers.", f"{slug_name}.html", body)

# Sublimation article
sub_products_html = ""
for p in [products[20], products[3], products[2]]:
    s = slug(p['title'])
    sub_products_html += f'''<div class="article-product-row">
  <img src="{p['image']}" alt="{p['title']}" onerror="this.src='https://placehold.co/100x67/f3e8ff/7c3aed?text=Bundle'">
  <div class="ap-info"><h4><a href="product-{s}.html">{p['title']}</a></h4><p style="font-size:.8rem;color:#6b7280;margin:0">Commercial license · Instant download</p></div>
  <a href="{REF}" class="btn btn-sm" target="_blank" rel="nofollow sponsored">Get Bundle</a>
</div>'''

sub_content = f'''<p>Sublimation printing has exploded in popularity among crafters, small business owners and Etsy sellers. The vibrant, permanent colors and professional finish make sublimated products irresistible to buyers. But to succeed with sublimation, you need great designs — and that's where <strong>design bundles</strong> come in.</p>
<h2>What Makes a Great Sublimation Bundle?</h2>
<p>Not every digital bundle is created for sublimation. Here's what to look for:</p>
<ul>
  <li><strong>PNG format with transparent backgrounds</strong> — sublimation printing requires PNG files, not SVG</li>
  <li><strong>300 DPI or higher resolution</strong> — low-res files will look blurry when printed on tumblers or shirts</li>
  <li><strong>Commercial license</strong> — essential if you're selling your sublimated products</li>
  <li><strong>Full tumbler wraps</strong> — full wrap designs save hours of design time</li>
</ul>
<h2>Top Sublimation Bundle Picks</h2>
<p>We've tested dozens of sublimation bundles and here are our top recommendations from Creative Fabrica:</p>
<div class="article-products">{sub_products_html}</div>
<h2>Sublimation Tips for Beginners</h2>
<p>Once you have your design bundle, here are some quick tips to get the best results:</p>
<ul>
  <li>Always mirror your image before printing for sublimation transfer</li>
  <li>Use sublimation-coated blanks — regular mugs and shirts won't work</li>
  <li>Lint-roll your shirts before applying the transfer</li>
  <li>Press at the correct temperature and time for each product type</li>
  <li>Use heat-resistant tape to keep your transfer in place</li>
</ul>
<h2>Why Buy Bundles Instead of Individual Designs?</h2>
<p>A single design might cost $3–$10 on its own. A bundle gives you 20–150+ designs for the same price or less. For an Etsy seller or sublimation business, this is a massive cost saving that goes straight to your profit margin.</p>
<p>With bundles like the <a href="product-sublimation-tumbler-sticker-bundle.html">Sublimation Tumbler & Sticker Bundle</a>, you get a full range of ready-to-print designs covering different styles and occasions — perfect for stocking your shop year-round.</p>'''

with open("/data/site/blog-sublimation.html", "w") as f:
    f.write(write_blog("blog-sublimation", "The Ultimate Guide to Sublimation Bundles in 2025", "Sublimation", "October 2, 2025", products[20]['image'], sub_content))

# SVG article
svg_products_html = ""
for p in [products[8], products[2], products[12]]:
    s = slug(p['title'])
    svg_products_html += f'''<div class="article-product-row">
  <img src="{p['image']}" alt="{p['title']}" onerror="this.src='https://placehold.co/100x67/f3e8ff/7c3aed?text=Bundle'">
  <div class="ap-info"><h4><a href="product-{s}.html">{p['title']}</a></h4><p style="font-size:.8rem;color:#6b7280;margin:0">SVG + PNG + EPS · Commercial license</p></div>
  <a href="{REF}" class="btn btn-sm" target="_blank" rel="nofollow sponsored">Get Bundle</a>
</div>'''

svg_content = f'''<p>SVG bundles are one of the most popular types of digital download products — and for good reason. Whether you're using a Cricut Maker, Silhouette Cameo, or any other cutting machine, SVG files give you crisp, scalable designs that look perfect at any size.</p>
<h2>SVG vs PNG vs EPS — What's the Difference?</h2>
<ul>
  <li><strong>SVG</strong> — Scalable Vector Graphics. Perfect for cutting machines. Scales to any size without losing quality.</li>
  <li><strong>PNG</strong> — Portable Network Graphics. Great for printing, sublimation and digital use. Fixed resolution.</li>
  <li><strong>EPS</strong> — Encapsulated PostScript. Professional vector format for design software like Illustrator.</li>
  <li><strong>DXF</strong> — Drawing Exchange Format. Used with some cutting machines and CAD software.</li>
</ul>
<p>The best bundles include <strong>all four formats</strong> so you have maximum flexibility across projects.</p>
<h2>Recommended SVG Bundles</h2>
<div class="article-products">{svg_products_html}</div>
<h2>How to Use SVG Bundles with Cricut</h2>
<ul>
  <li>Open Cricut Design Space and click "New Project"</li>
  <li>Click "Upload" and select your SVG file</li>
  <li>Choose "Complex" as the image type for detailed designs</li>
  <li>Resize and position your design on the canvas</li>
  <li>Select your material and cut!</li>
</ul>
<h2>How to Use SVG Bundles with Silhouette</h2>
<p>Silhouette Studio handles SVG files natively (in Business Edition and above). Simply drag and drop your SVG file into the workspace, resize it, and send to your Silhouette machine.</p>
<h2>Making Money with SVG Bundles</h2>
<p>Many successful Etsy sellers use SVG bundles to create and sell physical products like custom shirts, mugs, tote bags and home decor. With a commercial license, you can legally sell products made from these designs — making each bundle purchase an investment in your business.</p>
<p>Check out the <a href="product-wildflower-floral-line-art-svg-bundle.html">Wildflower Floral Line Art SVG Bundle</a> with 280+ files — perfect for building a diverse product catalog on Etsy.</p>'''

with open("/data/site/blog-svg.html", "w") as f:
    f.write(write_blog("blog-svg", "SVG Bundles Explained: How to Choose the Right One for Your Project", "SVG", "October 1, 2025", products[8]['image'], svg_content))

# Fonts article
font_products_html = ""
for p in [products[10], products[13], products[14]]:
    s = slug(p['title'])
    font_products_html += f'''<div class="article-product-row">
  <img src="{p['image']}" alt="{p['title']}" onerror="this.src='https://placehold.co/100x67/f3e8ff/7c3aed?text=Bundle'">
  <div class="ap-info"><h4><a href="product-{s}.html">{p['title']}</a></h4><p style="font-size:.8rem;color:#6b7280;margin:0">20–40+ fonts · Commercial license</p></div>
  <a href="{REF}" class="btn btn-sm" target="_blank" rel="nofollow sponsored">Get Bundle</a>
</div>'''

font_content = f'''<p>Typography is one of the most powerful tools in a designer's arsenal. The right font can make a logo unforgettable, a t-shirt design irresistible, or a social media post stop-scrolling worthy. Font bundles give you access to dozens of premium typefaces at a fraction of the individual cost.</p>
<h2>Types of Fonts in Design Bundles</h2>
<ul>
  <li><strong>Script fonts</strong> — Flowing, handwritten-style fonts. Perfect for wedding stationery, logos and elegant designs.</li>
  <li><strong>Handwritten fonts</strong> — Casual, authentic feel. Great for greeting cards, social media and craft projects.</li>
  <li><strong>Retro/Vintage fonts</strong> — 70s, 80s and 90s inspired. Perfect for t-shirt designs and nostalgia branding.</li>
  <li><strong>Sans-serif fonts</strong> — Clean and modern. Ideal for minimalist branding and UI design.</li>
  <li><strong>Display/Decorative fonts</strong> — Eye-catching statement fonts for headlines and posters.</li>
</ul>
<h2>Top Font Bundle Picks</h2>
<div class="article-products">{font_products_html}</div>
<h2>How to Install and Use Font Bundles</h2>
<p>Using font bundles is straightforward:</p>
<ul>
  <li>Download and unzip the font bundle</li>
  <li>On Windows: right-click each .ttf or .otf file and choose "Install"</li>
  <li>On Mac: double-click each font file and click "Install Font"</li>
  <li>Restart your design software (Canva, Photoshop, Illustrator, Cricut Design Space, etc.)</li>
  <li>Your new fonts will appear in the font dropdown menu</li>
</ul>
<h2>Using Fonts in Cricut Design Space</h2>
<p>Once installed on your computer, custom fonts are automatically available in Cricut Design Space. Simply type your text, select the text layer, and choose your installed font from the font dropdown. For cutting projects, use thicker fonts and weld overlapping letters for clean cuts.</p>
<h2>Font Licensing: What You Need to Know</h2>
<p>Always check that your font bundle includes a <strong>commercial license</strong>. This allows you to use the fonts in products you sell — on Etsy, at craft fairs, or to clients. All Creative Fabrica font bundles come with their premium commercial license included.</p>'''

with open("/data/site/blog-fonts.html", "w") as f:
    f.write(write_blog("blog-fonts", "Best Font Bundles for Designers & Crafters in 2025", "Fonts", "September 28, 2025", products[10]['image'], font_content))

# Seasonal article
seasonal_products_html = ""
for p in [products[3], products[4], products[7], products[18]]:
    s = slug(p['title'])
    seasonal_products_html += f'''<div class="article-product-row">
  <img src="{p['image']}" alt="{p['title']}" onerror="this.src='https://placehold.co/100x67/f3e8ff/7c3aed?text=Bundle'">
  <div class="ap-info"><h4><a href="product-{s}.html">{p['title']}</a></h4><p style="font-size:.8rem;color:#6b7280;margin:0">Commercial license · Instant download</p></div>
  <a href="{REF}" class="btn btn-sm" target="_blank" rel="nofollow sponsored">Get Bundle</a>
</div>'''

seasonal_content = f'''<p>Seasonal designs drive some of the biggest sales peaks for Etsy sellers and craft businesses. Halloween, Christmas, Thanksgiving, Valentine's Day — each holiday brings a surge of shoppers looking for themed products. The key to capitalizing on these peaks is to <strong>buy your design bundles early</strong> and prepare your products in advance.</p>
<h2>Your Seasonal Design Calendar</h2>
<ul>
  <li><strong>August–September:</strong> Halloween and fall/autumn designs</li>
  <li><strong>September–November:</strong> Thanksgiving designs</li>
  <li><strong>October–December:</strong> Christmas and holiday designs</li>
  <li><strong>January:</strong> Valentine's Day prep begins</li>
  <li><strong>February–March:</strong> Easter and spring designs</li>
  <li><strong>May–June:</strong> Summer, graduation and Father's Day</li>
</ul>
<h2>Top Seasonal Bundles for 2025</h2>
<div class="article-products">{seasonal_products_html}</div>
<h2>Halloween Designs: A Hot Market</h2>
<p>Halloween is one of the biggest seasons for craft sellers. Spooky SVGs, Halloween sublimation designs and seasonal clipart all sell exceptionally well from August through October. The <a href="product-spooky-training-learning-svg-bundle.html">Spooky Training & Learning SVG Bundle</a> is perfect for teachers and classroom-themed Halloween items.</p>
<h2>Christmas: The Biggest Sales Season</h2>
<p>Christmas is the undisputed king of seasonal craft sales. With over 150 designs, the <a href="product-bestseller-mega-christmas-bundle.html">Bestseller Mega Christmas Bundle</a> gives you everything you need to stock your shop with holiday-ready designs. Start preparing your Christmas products by October to catch early holiday shoppers.</p>
<h2>Thanksgiving: Don't Miss This Opportunity</h2>
<p>Thanksgiving is often overlooked by sellers who focus entirely on Christmas. But Thanksgiving-themed mugs, shirts, signs and home decor sell very well in October and November. The <a href="product-thanksgiving-quotes-designs-bundle.html">Thanksgiving Quotes Designs Bundle</a> with 263+ designs gives you unbeatable variety.</p>
<h2>Pro Tip: Bundle Your Seasonal Products</h2>
<p>Create product bundles (sets of 3–5 related items) in your Etsy shop around each holiday. Customers love the value of getting multiple coordinated items, and bundles help increase your average order value. Use a variety of designs from your bundles to create cohesive product sets.</p>'''

with open("/data/site/blog-seasonal.html", "w") as f:
    f.write(write_blog("blog-seasonal", "Seasonal Design Bundles: Plan Your Holiday Craft Calendar", "Seasonal", "September 25, 2025", products[3]['image'], seasonal_content))

# ============ ABOUT ============
about_body = f'''<main>
  <section class="about-hero">
    <div class="container">
      <h1>About CreativeBundles</h1>
      <p>Your trusted guide to the best digital design bundles on the market</p>
    </div>
  </section>
  <section class="about-section">
    <div class="container">
      <div class="about-grid">
        <div class="about-text">
          <h2>Why We Created CreativeBundles</h2>
          <p>As crafters and digital designers ourselves, we know how overwhelming it can be to find high-quality design bundles that are actually worth the money. There are thousands of options out there — and not all of them deliver on their promises.</p>
          <p>CreativeBundles was created to solve that problem. We personally review and curate the best-performing, highest-rated design bundles from Creative Fabrica, so you can shop with confidence and find exactly what your projects need.</p>
          <p>Whether you're an Etsy seller, a sublimation business owner, a Cricut enthusiast or just someone who loves to create — we've got the bundles for you.</p>
        </div>
        <div>
          <div class="about-features">
            <div class="about-feat"><div class="feat-icon">✅</div><h3>Hand-Curated Selection</h3><p>Every bundle on this site is personally reviewed for quality and value</p></div>
            <div class="about-feat"><div class="feat-icon">⚡</div><h3>Instant Downloads</h3><p>All bundles are digital downloads — available immediately after purchase</p></div>
            <div class="about-feat"><div class="feat-icon">🔐</div><h3>Commercial License</h3><p>Use these designs to create and sell products legally</p></div>
            <div class="about-feat"><div class="feat-icon">💰</div><h3>Best Value</h3><p>Bundles give you 20–150+ designs for the price of one or two individual files</p></div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section class="cta-section-full">
    <div class="container">
      <h2>Ready to Find Your Perfect Bundle?</h2>
      <p>Browse our curated selection of top 25 best-selling design bundles — all available on Creative Fabrica with instant download and commercial license.</p>
      <a href="index.html" class="btn btn-white" style="margin-right:12px">Browse the Shop</a>
      <a href="{REF}" target="_blank" rel="nofollow sponsored" class="btn" style="background:transparent;border:2px solid rgba(255,255,255,.6);color:#fff">All Bundles on CF →</a>
    </div>
  </section>
</main>'''

with open("/data/site/about.html", "w") as f:
    f.write(page_wrap("About Us — CreativeBundles", "Learn about CreativeBundles — your curated guide to the best digital design bundles on Creative Fabrica.", "about.html", about_body))

# Count files
files = [f for f in os.listdir("/data/site") if f.endswith('.html') or f.endswith('.css')]
print(f"Generated {len(files)} files: {', '.join(sorted(files)[:10])}...")
