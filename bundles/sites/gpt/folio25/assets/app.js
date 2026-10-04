
const q=(s,c=document)=>c.querySelector(s),qa=(s,c=document)=>[...c.querySelectorAll(s)];
const bar=q('.progress');addEventListener('scroll',()=>{if(bar){let d=document.documentElement;bar.style.width=((d.scrollTop/(d.scrollHeight-d.clientHeight))*100)+'%'}});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target)}}),{threshold:.08});qa('.reveal').forEach(x=>io.observe(x));
qa('.faq-q').forEach(b=>b.addEventListener('click',()=>{let item=b.closest('.faq-item'),open=item.classList.toggle('open');b.setAttribute('aria-expanded',open)}));
const mb=q('.menu-btn'),nl=q('.nav-links');if(mb)mb.addEventListener('click',()=>{nl.classList.toggle('open');mb.setAttribute('aria-expanded',nl.classList.contains('open'))});
if(matchMedia('(pointer:fine)').matches){qa('[data-parallax]').forEach((el,i)=>addEventListener('mousemove',e=>{let x=(e.clientX/innerWidth-.5)*(i?10:16),y=(e.clientY/innerHeight-.5)*(i?8:12);el.style.translate=x+'px '+y+'px'}))}
