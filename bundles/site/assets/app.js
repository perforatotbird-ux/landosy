(() => {
  const data = window.BUNDLE_DATA || { products: [], blog: [], refLink: '' };
  const products = data.products || [];
  const posts = data.blog || [];
  const refLink = data.refLink;
  const body = document.body;
  const page = body.dataset.page || 'home';
  const root = body.dataset.root || '.';
  const app = document.getElementById('site');

  const esc = (value) => String(value ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');

  const siteLink = (target) => root === '.' ? target : `${root}/${target}`;
  const asset = (target) => `${root}/${target}`;
  const productLink = (slug) => page === 'product' ? `./${slug}.html` : siteLink(`products/${slug}.html`);
  const articleLink = (slug) => page === 'article' ? `./${slug}.html` : siteLink(`articles/${slug}.html`);
  const catalogLink = (category = '') => `${siteLink('catalog.html')}${category ? `?category=${encodeURIComponent(category)}` : ''}`;
  const findProduct = (slug) => products.find((product) => product.slug === slug);
  const findPost = (slug) => posts.find((post) => post.slug === slug);
  const initials = (name) => name.split(/[ ,]/).filter(Boolean).slice(0, 2).map((part) => part[0]).join('').toUpperCase();

  function imageTag(product, className = '', lazy = true, imagePath = product.image) {
    const fallback = product.remoteImage ? ` onerror="this.onerror=null;this.src='${esc(product.remoteImage)}'"` : '';
    return `<img class="${className}" src="${esc(asset(imagePath))}" alt="${esc(product.title)}"${lazy ? ' loading="lazy"' : ''}${fallback}>`;
  }

  function affiliate(label, className = 'button button-dark', extra = '') {
    return `<a class="${className}" href="${esc(refLink)}" target="_blank" rel="sponsored noopener" ${extra}>${label}</a>`;
  }

  function stars(rating, withCount = true) {
    return `<span class="rating" aria-label="Рейтинг ${rating} из 5">★★★★★${withCount ? ` <small>${rating}</small>` : ''}</span>`;
  }

  function header() {
    const catalogActive = page === 'catalog' || page === 'product';
    const blogActive = page === 'blog' || page === 'article';
    const nav = [
      ['Витрина', catalogLink(), catalogActive],
      ['Журнал', siteLink('blog.html'), blogActive],
      ['О проекте', siteLink('about.html'), page === 'about'],
    ].map(([label, href, active]) => `<a class="${active ? 'active' : ''}" href="${href}">${label}</a>`).join('');

    return `
      <a class="skip-link" href="#main-content">К содержанию</a>
      <div class="announcement"><span>25 digital bundles</span><b class="dot">•</b> идеи для печати, раскроя и вдохновения <b class="dot">•</b><span>instant download</span></div>
      <header class="site-header">
        <div class="container header-inner">
          <a class="brand" href="${siteLink('index.html')}" aria-label="The Bundle Edit — на главную"><span class="brand-mark">✦</span> THE <span>BUNDLE</span> EDIT</a>
          <nav class="main-nav" aria-label="Основная навигация">${nav}</nav>
          ${affiliate('Открыть Creative Fabrica <span class="arrow">↗</span>', 'button button-coral header-cta')}
          <button class="mobile-toggle" type="button" aria-label="Открыть меню" aria-expanded="false" data-menu-toggle><span></span><span></span></button>
        </div>
        <nav class="mobile-nav" data-mobile-nav aria-label="Мобильная навигация">${nav}${affiliate('Перейти к наборам <span class="arrow">↗</span>', 'button button-coral')}</nav>
      </header>
    `;
  }

  function footer() {
    return `
      <footer class="site-footer">
        <div class="container">
          <div class="footer-grid">
            <div class="footer-brand">
              <a class="brand" href="${siteLink('index.html')}"><span class="brand-mark">✦</span> THE <span>BUNDLE</span> EDIT</a>
              <p>Небольшой журнал-витрина о цифровых наборах, которые превращают “когда-нибудь” в готовый проект.</p>
            </div>
            <div>
              <p class="footer-heading">Навигация</p>
              <div class="footer-links"><a href="${catalogLink()}">Все 25 наборов</a><a href="${siteLink('blog.html')}">Журнал идей</a><a href="${siteLink('about.html')}">Как это работает</a></div>
            </div>
            <div>
              <p class="footer-heading">Подборки</p>
              <div class="footer-links"><a href="${catalogLink('Шрифты')}">Шрифты</a><a href="${catalogLink('Сублимация')}">Сублимация</a><a href="${catalogLink('Праздники')}">Праздники</a></div>
            </div>
            <div>
              <p class="footer-heading">Старт проекта</p>
              <p class="footer-note">Все ссылки на товары ведут через партнёрскую ссылку Creative Fabrica. Цены и доступность уточняйте на странице набора.</p>
              ${affiliate('Открыть библиотеку <span class="arrow">↗</span>', 'button button-dark')}
            </div>
          </div>
          <div class="footer-bottom"><span>© 2026 The Bundle Edit · digital only</span><span><a href="${esc(refLink)}" target="_blank" rel="sponsored noopener">Партнёрская ссылка Creative Fabrica</a> · сделано для творческих проектов</span></div>
        </div>
      </footer>
    `;
  }

  function shell(content) {
    app.innerHTML = `${header()}<main id="main-content">${content}</main>${footer()}`;
    bindChrome();
    bindNewsletter();
  }

  function bindChrome() {
    const toggle = document.querySelector('[data-menu-toggle]');
    const mobile = document.querySelector('[data-mobile-nav]');
    if (toggle && mobile) {
      toggle.addEventListener('click', () => {
        const open = toggle.getAttribute('aria-expanded') === 'true';
        toggle.setAttribute('aria-expanded', String(!open));
        mobile.classList.toggle('open', !open);
        body.classList.toggle('menu-lock', !open);
      });
      mobile.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
        toggle.setAttribute('aria-expanded', 'false');
        mobile.classList.remove('open');
        body.classList.remove('menu-lock');
      }));
    }
  }

  function bindNewsletter() {
    document.querySelectorAll('[data-newsletter]').forEach((form) => {
      form.addEventListener('submit', (event) => {
        event.preventDefault();
        const button = form.querySelector('button');
        const note = form.parentElement.querySelector('[data-form-note]');
        if (button) button.textContent = 'Готово ✓';
        if (note) note.textContent = 'Спасибо! Новые идеи будут ждать вас в почте.';
      });
    });
  }

  function productCard(product) {
    const chips = product.formats.slice(0, 3).map((format) => `<span class="meta-chip">${esc(format)}</span>`).join('');
    return `
      <article class="product-card reveal">
        <a class="card-image" href="${productLink(product.slug)}">
          ${imageTag(product, '', true)}
          <span class="card-number">#${String(product.id).padStart(2, '0')}</span>
          <span class="card-badge">${esc(product.badge)}</span>
        </a>
        <div class="card-body">
          <div class="card-topline"><span class="card-category">${esc(product.category)}</span>${stars(product.rating)}</div>
          <h3><a href="${productLink(product.slug)}">${esc(product.title)}</a></h3>
          <p class="card-summary">${esc(product.summary)}</p>
          <div class="card-meta">${chips}</div>
          <div class="card-bottom"><a class="card-read" href="${productLink(product.slug)}">Подробнее <span>↗</span></a>${affiliate('Открыть <span>↗</span>', 'card-out')}</div>
        </div>
      </article>
    `;
  }

  function postCard(post, featured = false) {
    const product = findProduct(post.heroProduct);
    if (featured) {
      return `
        <a class="editorial-feature" href="${articleLink(post.slug)}">
          ${imageTag(product, '', true)}
          <div class="editorial-feature-content"><span class="eyebrow">${esc(post.category)} · ${esc(post.date)}</span><h3>${esc(post.title)}</h3><p>${esc(post.dek)}</p><span class="text-link">Читать статью <span class="arrow">→</span></span></div>
        </a>
      `;
    }
    return `
      <a class="article-card" href="${articleLink(post.slug)}">
        <span class="article-thumb">${imageTag(product, '', true)}</span>
        <span><span class="eyebrow">${esc(post.category)}</span><h3>${esc(post.title)}</h3><p>${esc(post.dek)}</p><span class="article-meta"><span>${esc(post.date)}</span><span>${esc(post.readTime)}</span></span></span>
      </a>
    `;
  }

  function renderHome() {
    const heroOne = findProduct('blooming-watercolor-florals-bundle');
    const heroTwo = findProduct('stunning-seamless-patterns-bundle');
    const featured = [
      findProduct('soft-nursery-mix'),
      findProduct('the-ultimate-font-bundle-3'),
      findProduct('sublimation-tumbler-sticker-bundle'),
      findProduct('adorable-animals-wildlife-bundle'),
      findProduct('relaxing-coloring-pages-mega-bundle'),
      findProduct('retro-vibes-vintage-lifestyle-bundle'),
    ];
    const categories = [
      ['01', 'Шрифты', '20–40+ вариантов для букв, брендинга и Cricut', 'Шрифты'],
      ['02', 'Печать & сублимация', 'PNG, wraps и идеи для вещей', 'Сублимация'],
      ['03', 'Праздничный стол', 'Осень, Halloween и Christmas', 'Праздники'],
      ['04', 'SVG & иллюстрации', 'Контуры, цветы, звери и цитаты', 'SVG и раскрой'],
    ];
    const blogFeature = posts[0];

    shell(`
      <section class="container hero">
        <div class="hero-copy reveal">
          <div class="hero-kicker eyebrow">The creative shortlist · 2026</div>
          <h1>Идеи, которые уже готовы к вашему <em>проекту.</em></h1>
          <p class="hero-lede">25 цифровых наборов для тех, кто любит открывать файл — и сразу видеть, во что он может превратиться. Печать, раскрой, сублимация и немного творческого хаоса.</p>
          <div class="hero-actions"><a class="button button-dark" href="${catalogLink()}">Смотреть витрину <span class="arrow">↗</span></a><a class="text-link" href="${siteLink('blog.html')}">Открыть журнал <span class="arrow">→</span></a></div>
          <p class="hero-footnote"><span class="spark">✦</span><strong>Редакционный отбор</strong> · файлы, которые хочется использовать, а не просто сохранить.</p>
        </div>
        <div class="hero-art reveal">
          <div class="hero-orbit"></div><div class="hero-stamp">25<br>fresh<br>finds</div>
          <div class="hero-photo-main">${imageTag(heroOne, '', false)}</div>
          <div class="hero-photo-side">${imageTag(heroTwo, '', true)}</div>
          <div class="hero-caption">soft palette / bold ideas</div><div class="hero-note">Сохрани идею.<br>Сделай вещь.<br>Повтори.</div>
        </div>
      </section>
      <div class="ticker" aria-hidden="true"><div class="ticker-track">${Array(2).fill(['design library', 'instant download', 'make something lovely', '25 fresh bundles', 'print · cut · create']).flat().map((word) => `<span class="ticker-item">${word}</span>`).join('')}</div></div>
      <section class="container trust-row" aria-label="Преимущества цифровых наборов">
        <div class="trust-item"><span class="trust-icon">↗</span><div><strong>Без доставки</strong><span>Только digital files</span></div></div>
        <div class="trust-item"><span class="trust-icon">✦</span><div><strong>25 идей</strong><span>От nursery до retro</span></div></div>
        <div class="trust-item"><span class="trust-icon">◎</span><div><strong>Для makers</strong><span>Cricut, печать, дизайн</span></div></div>
        <div class="trust-item"><span class="trust-icon">♡</span><div><strong>С редакцией</strong><span>Подсказки в журнале</span></div></div>
      </section>
      <section class="section container" id="featured">
        <div class="section-head"><div><span class="eyebrow">01 / Editor's shelf</span><h2>С чего начать, если хочется всё.</h2><p>Шесть наборов, которые легко представить в настоящем проекте уже сегодня.</p></div><a class="text-link section-link" href="${catalogLink()}">Вся коллекция <span class="arrow">→</span></a></div>
        <div class="product-grid">${featured.map(productCard).join('')}</div>
      </section>
      <section class="ink-band section"><div class="container collection-layout"><div class="collection-copy"><span class="eyebrow">02 / Pick a mood</span><h2>Выберите настроение. Остальное — в файлах.</h2><p>Не обязательно знать точный формат, чтобы начать. Сначала выберите направление, которое хочется открыть сегодня.</p><a class="button button-light" href="${catalogLink()}">Исследовать все 25 <span class="arrow">↗</span></a></div><div class="collection-list">${categories.map(([index, title, text, category]) => `<a class="collection-row" href="${catalogLink(category)}"><span class="index">${index}</span><span><strong>${title}</strong><span>${text}</span></span><span class="row-arrow">↗</span></a>`).join('')}</div></div></section>
      <section class="section container"><div class="section-head"><div><span class="eyebrow">03 / From the journal</span><h2>Не просто каталог.</h2><p>Короткие заметки о форматах, проектах и том, как не утонуть в папке Downloads.</p></div><a class="text-link section-link" href="${siteLink('blog.html')}">Все статьи <span class="arrow">→</span></a></div><div class="editorial-grid"><div>${postCard(blogFeature, true)}</div><div class="article-stack">${posts.slice(1).map((post) => postCard(post)).join('')}</div></div></section>
      <section class="container section-tight"><div class="newsletter"><div><span class="eyebrow">The little creative letter</span><h2>Одна идея в неделю — без шума.</h2><p>Новые находки, полезные форматы и маленькие поводы что-нибудь сделать руками.</p></div><form class="newsletter-form" data-newsletter><div><input type="email" required placeholder="ваш@email.com" aria-label="Ваш email"><div class="form-note" data-form-note>Никакого спама. Только вдохновение.</div></div><button class="button button-dark" type="submit">Подписаться <span class="arrow">→</span></button></form></div></section>
    `);
  }

  function renderCatalog() {
    const categories = ['Все темы', ...new Set(products.map((product) => product.category))];
    const queryCategory = new URLSearchParams(window.location.search).get('category') || 'Все темы';
    shell(`
      <section class="page-intro"><div class="container page-intro-row"><div><span class="eyebrow">The full edit · 25 finds</span><h1>Вся полка — <em>для вашего</em> следующего проекта.</h1><p>Наборы для печати, Cricut, сублимации, паттернов и просто хорошего визуального настроения. Откройте карточку, чтобы увидеть полное описание.</p></div><div class="page-count"><span data-results-count>25</span> наборов</div></div></section>
      <section class="section-tight container">
        <div class="catalog-tools"><label class="search-box"><span class="search-icon">⌕</span><input type="search" data-search placeholder="Искать по названию или теме..." aria-label="Искать набор"></label><select data-category aria-label="Фильтр по теме">${categories.map((category) => `<option value="${esc(category)}" ${category === queryCategory ? 'selected' : ''}>${esc(category)}</option>`).join('')}</select><select data-sort aria-label="Сортировка"><option value="featured">Сначала редакция</option><option value="az">По алфавиту</option><option value="reviews">По отзывам</option></select></div>
        <div class="category-row">${categories.map((category) => `<button class="filter-pill ${category === queryCategory ? 'active' : ''}" type="button" data-category-pill="${esc(category)}">${esc(category)}</button>`).join('')}</div>
        <p class="results-note" data-results-note>Показываем все 25 наборов</p><div class="product-grid" data-catalog-grid></div>
      </section>
    `);
    bindCatalog(queryCategory);
  }

  function bindCatalog(initialCategory) {
    const grid = document.querySelector('[data-catalog-grid]');
    const search = document.querySelector('[data-search]');
    const category = document.querySelector('[data-category]');
    const sort = document.querySelector('[data-sort]');
    const count = document.querySelector('[data-results-count]');
    const note = document.querySelector('[data-results-note]');
    const pills = [...document.querySelectorAll('[data-category-pill]')];
    let activeCategory = initialCategory;

    const update = () => {
      const needle = (search.value || '').trim().toLowerCase();
      let visible = products.filter((product) => {
        const matchesCategory = activeCategory === 'Все темы' || product.category === activeCategory;
        const haystack = `${product.title} ${product.category} ${product.summary} ${product.formats.join(' ')}`.toLowerCase();
        return matchesCategory && (!needle || haystack.includes(needle));
      });
      if (sort.value === 'az') visible = visible.sort((a, b) => a.title.localeCompare(b.title));
      if (sort.value === 'reviews') visible = visible.sort((a, b) => b.reviewCount - a.reviewCount);
      count.textContent = visible.length;
      note.textContent = needle || activeCategory !== 'Все темы' ? `Нашли ${visible.length} ${visible.length === 1 ? 'набор' : 'набора'} по вашему запросу` : 'Показываем все 25 наборов';
      grid.innerHTML = visible.length ? visible.map(productCard).join('') : `<div class="empty-state"><h3>Пока пусто.</h3><p>Попробуйте другой запрос или сбросьте фильтр.</p></div>`;
      pills.forEach((pill) => pill.classList.toggle('active', pill.dataset.categoryPill === activeCategory));
      category.value = activeCategory;
    };
    search.addEventListener('input', update);
    sort.addEventListener('change', update);
    category.addEventListener('change', () => { activeCategory = category.value; update(); });
    pills.forEach((pill) => pill.addEventListener('click', () => { activeCategory = pill.dataset.categoryPill; update(); }));
    update();
  }

  function descriptionHtml(text) {
    const lines = text.split(/\n+/).map((line) => line.trim()).filter(Boolean);
    const output = [];
    let list = [];
    const flush = () => {
      if (list.length) {
        output.push(`<ul>${list.map((item) => `<li>${esc(item.replace(/^(?:[-–•]|📁|❤|✨|🎁|🎄)\s*/, ''))}</li>`).join('')}</ul>`);
        list = [];
      }
    };
    lines.forEach((line) => {
      const isBullet = /^(?:[-–•]|📁|❤|✨|🎁|🎄)\s*/.test(line) || /^\d+\s+(?:SVG|PNG|JPG|EPS|DXF)/i.test(line);
      if (isBullet) list.push(line);
      else { flush(); output.push(`<p>${esc(line)}</p>`); }
    });
    flush();
    return output.join('');
  }

  function galleryMarkup(product) {
    const thumbs = product.images.length > 1 ? `<div class="gallery-thumbs">${product.images.map((image, index) => `<button class="gallery-thumb ${index === 0 ? 'active' : ''}" type="button" data-gallery-thumb="${esc(asset(image))}" aria-label="Изображение ${index + 1}">${imageTag(product, '', true, image)}</button>`).join('')}</div>` : '';
    return `<div class="product-gallery"><div class="product-main-image"><img data-gallery-main src="${esc(asset(product.image))}" alt="${esc(product.title)}" onerror="this.onerror=null;this.src='${esc(product.remoteImage)}'"></div>${thumbs}</div>`;
  }

  function renderProduct(slug) {
    const product = findProduct(slug);
    if (!product) { renderNotFound(); return; }
    const related = products.filter((item) => item.slug !== product.slug && item.category === product.category).slice(0, 3);
    const extraRelated = related.length < 3 ? products.filter((item) => item.slug !== product.slug && !related.includes(item)).slice(0, 3 - related.length) : [];
    const allRelated = [...related, ...extraRelated];
    shell(`
      <section class="product-detail container">
        <nav class="breadcrumbs" aria-label="Хлебные крошки"><a href="${siteLink('index.html')}">Главная</a><span class="slash">/</span><a href="${catalogLink()}">Витрина</a><span class="slash">/</span><span>${esc(product.title)}</span></nav>
        <div class="product-hero">${galleryMarkup(product)}<div class="product-aside"><span class="product-category">${esc(product.category)} · #${String(product.id).padStart(2, '0')}</span><h1>${esc(product.title)}</h1><div class="product-rating"><span class="stars">★★★★★</span><span>${product.rating} · ${product.reviewCount} редакционных отзывов</span></div><p class="product-intro">${esc(product.summary)}</p><div class="product-actions">${affiliate('Открыть набор <span class="arrow">↗</span>', 'button button-coral')}<a class="button button-outline" href="${catalogLink(product.category)}">Ещё в теме</a></div><p class="product-ref-note">Цифровой продукт · физическая доставка не нужна · ссылка ведёт через Creative Fabrica.</p><div class="product-data-grid"><div class="product-data-item"><span>Форматы</span><div class="chip-list">${product.formats.map((format) => `<span class="meta-chip">${esc(format)}</span>`).join('')}</div></div><div class="product-data-item"><span>Идеально для</span><strong>${esc(product.useCases[0])}</strong></div></div></div></div>
        <div class="product-description-wrap"><div><span class="eyebrow">Full description</span><h2>Что внутри и зачем это нужно.</h2></div><div class="description-copy">${descriptionHtml(product.description)}</div></div>
        <div class="review-panel"><div class="review-heading"><span class="eyebrow">A note from the community</span><h2>Когда файл становится вещью.</h2><p class="editorial-disclaimer">Отзыв ниже — редакционный сценарий для этой витрины, созданный по мотивам возможного пользовательского опыта.</p></div><div class="review-card"><blockquote>${esc(product.review.text)}</blockquote><div class="review-author"><span class="review-avatar">${esc(initials(product.review.name))}</span><span><strong>${esc(product.review.name)}</strong><span>покупатель цифровых наборов</span></span></div></div></div>
      </section>
      <section class="container related-products"><div class="section-head"><div><span class="eyebrow">Keep browsing</span><h2>Ещё на этой полке.</h2></div><a class="text-link section-link" href="${catalogLink()}">Все наборы <span class="arrow">→</span></a></div><div class="product-grid">${allRelated.map(productCard).join('')}</div></section>
      <section class="container section-tight"><div class="newsletter"><div><span class="eyebrow">Need a little direction?</span><h2>Загляните в журнал.</h2><p>Форматы, быстрые идеи и подсказки для первого проекта — на человеческом языке.</p></div><a class="button button-dark" href="${siteLink('blog.html')}">Читать статьи <span class="arrow">→</span></a></div></section>
    `);
    bindGallery();
  }

  function bindGallery() {
    const main = document.querySelector('[data-gallery-main]');
    document.querySelectorAll('[data-gallery-thumb]').forEach((thumb) => thumb.addEventListener('click', () => {
      main.src = thumb.dataset.galleryThumb;
      document.querySelectorAll('[data-gallery-thumb]').forEach((item) => item.classList.remove('active'));
      thumb.classList.add('active');
    }));
  }

  function renderBlog() {
    const feature = posts[0];
    shell(`
      <section class="page-intro"><div class="container"><span class="eyebrow">The Bundle Edit / Journal</span><h1>Журнал для тех, кто <em>делает.</em></h1><p>Небольшие, полезные и немного красивые заметки о цифровых файлах, форматах и проектах, которые хочется закончить.</p></div></section>
      <section class="section container"><a class="blog-feature" href="${articleLink(feature.slug)}"><span class="blog-feature-image">${imageTag(findProduct(feature.heroProduct), '', false)}</span><span><span class="eyebrow">${esc(feature.category)} · ${esc(feature.date)}</span><h2>${esc(feature.title)}</h2><p>${esc(feature.dek)}</p><span class="button button-light">Читать featured-статью <span class="arrow">↗</span></span></span></a></section>
      <section class="section-tight container"><div class="section-head"><div><span class="eyebrow">The reading list</span><h2>Ещё четыре повода открыть редактор.</h2></div></div><div class="blog-grid">${posts.slice(1).map((post) => `<a class="blog-tile" href="${articleLink(post.slug)}"><span class="blog-tile-image">${imageTag(findProduct(post.heroProduct), '', true)}</span><span><span class="eyebrow">${esc(post.category)}</span><h3>${esc(post.title)}</h3><p>${esc(post.dek)}</p><span class="article-meta"><span>${esc(post.date)}</span><span>${esc(post.readTime)}</span></span></span></a>`).join('')}</div></section>
      <section class="ink-band section-tight"><div class="container collection-layout"><div class="collection-copy"><span class="eyebrow">From the shelf</span><h2>Товар тоже может быть отправной точкой.</h2><p>Откройте витрину и найдите визуальную основу для своей следующей статьи, коллекции или подарка.</p><a class="button button-light" href="${catalogLink()}">В витрину <span class="arrow">↗</span></a></div><div class="collection-list">${posts.map((post) => `<a class="collection-row" href="${articleLink(post.slug)}"><span class="index">${esc(post.number)}</span><span><strong>${esc(post.category)}</strong><span>${esc(post.title)}</span></span><span class="row-arrow">↗</span></a>`).join('')}</div></div></section>
    `);
  }

  function richText(text) {
    return text.replace(/\[\[product:([^|]+)\|([^\]]+)\]\]/g, (_, slug, label) => `<a href="${productLink(slug)}">${esc(label)}</a>`);
  }

  function renderArticle(slug) {
    const post = findPost(slug);
    if (!post) { renderNotFound(); return; }
    const heroProduct = findProduct(post.heroProduct);
    const otherPosts = posts.filter((item) => item.slug !== post.slug).slice(0, 3);
    shell(`
      <article class="article-page container"><header class="article-header"><span class="eyebrow">${esc(post.category)} · ${esc(post.date)}</span><h1>${esc(post.title)}</h1><p class="dek">${esc(post.dek)}</p><div class="article-meta"><span>${esc(post.readTime)} чтения</span><span>·</span><span>The Bundle Edit</span></div></header><div class="article-cover">${imageTag(heroProduct, '', false)}</div><div class="article-content-layout"><aside class="article-share"><span>Share the idea</span><a href="mailto:?subject=${encodeURIComponent(post.title)}" aria-label="Отправить по email">@</a><a href="#related" aria-label="Перейти к похожим статьям">↘</a></aside><div class="article-body">${post.body.map((paragraph) => `<p>${richText(paragraph)}</p>`).join('')}</div><aside class="article-aside"><span class="aside-label">On the shelf</span>${imageTag(heroProduct, '', true)}<h3>${esc(heroProduct.title)}</h3><a class="text-link" href="${productLink(heroProduct.slug)}">Открыть карточку <span class="arrow">→</span></a></aside></div><div class="article-bottom" id="related"><h2>Читайте дальше</h2><div class="article-stack">${otherPosts.map((item) => postCard(item)).join('')}</div></div></article>
    `);
  }

  function renderAbout() {
    shell(`
      <section class="page-intro"><div class="container"><span class="eyebrow">Behind the edit</span><h1>Меньше бесконечного скролла. <em>Больше сделанных вещей.</em></h1><p>The Bundle Edit — это витрина и маленький журнал вокруг цифровых наборов Creative Fabrica. Мы собираем идеи так, чтобы вдохновение было первым шагом, а не финальной точкой.</p></div></section>
      <section class="section container"><div class="about-grid"><div class="about-copy"><span class="eyebrow">Why this exists</span><h2>Папка Downloads не должна быть кладбищем хороших идей.</h2><p>В этой подборке — 25 файлов, к которым можно вернуться с конкретной задачей: сделать открытку, обновить мерч, собрать паттерн или просто попробовать новую технику.</p><p>Мы добавили к товарам понятные форматы, идеи применения и короткие заметки журнала. Сначала выберите настроение, потом откройте набор и проверьте детали на странице Creative Fabrica.</p><div class="hero-actions"><a class="button button-dark" href="${catalogLink()}">Открыть 25 находок <span class="arrow">↗</span></a>${affiliate('Перейти в библиотеку <span class="arrow">↗</span>', 'button button-outline')}</div></div><div class="about-art"><div class="about-card one"><p>make it useful.<br>make it yours.</p><small>the bundle edit / note 01</small></div><div class="about-card two"><p>save less.<br>make more.</p><small>digital, not disposable</small></div></div></div></section>
      <section class="section-tight container"><div class="section-head"><div><span class="eyebrow">The simple route</span><h2>Как пользоваться витриной.</h2><p>Три шага от “прикольно” до “готово”.</p></div></div><div class="steps"><div class="step-card"><h3>Выберите задачу</h3><p>Смотрите по теме или ищите по слову: “fonts”, “stickers”, “Christmas”, “nursery”. Карточки подскажут, что внутри.</p></div><div class="step-card"><h3>Проверьте формат</h3><p>На странице каждого набора есть полный текст описания, форматы и идеи применения — чтобы не покупать вслепую.</p></div><div class="step-card"><h3>Откройте и создайте</h3><p>Нажмите на партнёрскую кнопку, скачайте цифровой файл на Creative Fabrica и превратите его в свой проект.</p></div></div></section>
      <section class="section container"><div class="section-head"><div><span class="eyebrow">Good to know</span><h2>Частые вопросы.</h2></div></div><div class="faq-list"><details><summary>Это физические товары?</summary><p>Нет. Здесь собраны цифровые наборы: файлы для скачивания, печати, резки, сублимации и дизайна. Доставка коробки не нужна.</p></details><details><summary>Что означает партнёрская ссылка?</summary><p>Если вы переходите по кнопке и покупаете набор на Creative Fabrica, витрина может получить комиссию. Для вас цена и условия определяются страницей Creative Fabrica. Спасибо за поддержку проекта.</p></details><details><summary>Отзывы на страницах настоящие?</summary><p>Отзывы в этой демонстрационной подборке — художественные редакционные сценарии, созданные, чтобы показать возможный опыт использования. Это не независимые подтверждённые отзывы.</p></details><details><summary>Где узнать точные условия лицензии?</summary><p>Откройте карточку набора и перейдите на Creative Fabrica по партнёрской ссылке. Перед коммерческим использованием проверьте актуальную лицензию и ограничения конкретного товара.</p></details></div></section>
      <section class="container section-tight"><div class="page-cta"><h2>Один файл — уже начало.</h2><p>Выберите набор, который хочется открыть сегодня, и дайте идее материал.</p>${affiliate('Смотреть витрину Creative Fabrica <span class="arrow">↗</span>', 'button button-light')}</div></section>
    `);
  }

  function renderNotFound() {
    shell(`<section class="container not-found"><div><span class="eyebrow">404 / lost in the downloads</span><h1>Ой.</h1><p>Похоже, эта страница спряталась между папками.</p><a class="button button-dark" href="${siteLink('index.html')}">Вернуться на главную <span class="arrow">→</span></a></div></section>`);
  }

  function init() {
    if (page === 'home') renderHome();
    else if (page === 'catalog') renderCatalog();
    else if (page === 'product') renderProduct(body.dataset.product);
    else if (page === 'blog') renderBlog();
    else if (page === 'article') renderArticle(body.dataset.article);
    else if (page === 'about') renderAbout();
    else renderNotFound();
  }

  init();
})();
