// ===========================
// Floating background shapes
// ===========================
const canvas = document.getElementById('background-canvas');
const ctx = canvas ? canvas.getContext('2d') : null;
let shapes = [];

function resizeCanvas() {
  if(!canvas) return;
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

function initShapes() {
  shapes = [];
  for(let i=0;i<20;i++){
    shapes.push({
      x: Math.random()*canvas.width,
      y: Math.random()*canvas.height,
      vx: (Math.random()-0.5)*0.3,
      vy: (Math.random()-0.5)*0.3,
      size: 20+Math.random()*30
    });
  }
}
initShapes();

function animateShapes() {
  if(!ctx) return;
  ctx.clearRect(0,0,canvas.width,canvas.height);
  shapes.forEach(s=>{
    s.x+=s.vx;
    s.y+=s.vy;
    if(s.x<0||s.x>canvas.width) s.vx*=-1;
    if(s.y<0||s.y>canvas.height) s.vy*=-1;
    ctx.strokeStyle='rgba(255,255,255,0.05)';
    ctx.lineWidth=1;
    ctx.beginPath();
    ctx.moveTo(s.x,s.y);
    ctx.lineTo(s.x+s.size,s.y+s.size);
    ctx.moveTo(s.x+s.size,s.y);
    ctx.lineTo(s.x,s.y+s.size);
    ctx.stroke();
  });
  requestAnimationFrame(animateShapes);
}
animateShapes();

// ===========================
// Load Example Text (только вставка)
// ===========================
function loadExample() {
  const exampleText = `Artificial intelligence is transforming the world. Modern large language models can understand context and generate text almost like humans. However, they have limitations—they don't possess true understanding and may hallucinate. Knowledge graphs help solve this problem. Knowledge Graphs allow AI to work with structured relationships and make more reliable inferences.`;
  const textarea = document.getElementById('input-text');
  if(textarea){
    textarea.value = exampleText;
  }
}

// ===========================
// Empty Field Warning
// ===========================
function showWarning(message){
  // Создаём блок
  const warning = document.createElement('div');
  warning.innerText = message;
  warning.className = "fixed top-5 left-1/2 transform -translate-x-1/2 bg-[#1A0033] text-white px-6 py-3 rounded-xl shadow-lg opacity-0 z-50 transition-all duration-500 ease-out";
  
  document.body.appendChild(warning);
  
  // Анимация появления
  setTimeout(()=>{ warning.style.opacity = '1'; warning.style.transform = 'translateX(-50%) translateY(0)'; }, 50);
  
  // Автоудаление через 3 секунды с анимацией
  setTimeout(()=>{
    warning.style.opacity = '0';
    warning.style.transform = 'translateX(-50%) translateY(-20px)';
    setTimeout(()=>{ warning.remove(); }, 500);
  }, 3000);
}

// ===========================
// Form Validation
// ===========================
window.addEventListener('DOMContentLoaded', ()=>{
  const form = document.getElementById('graph-form');
  const exampleBtn = document.querySelector('button[onclick="loadExample()"]');

  // Example button просто вставляет текст
  if(exampleBtn){
    exampleBtn.addEventListener('click', loadExample);
  }

  if(form){
    form.addEventListener('submit', (e)=>{
      const textarea = document.getElementById('input-text');
      if(!textarea.value.trim()){
        e.preventDefault();
        showWarning("Please enter some text!");
        return false;
      }
    });
  }
});

// ===========================
// Load Example Text and Scroll
// ===========================
function loadExample() {
  const exampleText = `Artificial intelligence is transforming the world. Modern large language models can understand context and generate text almost like humans. However, they have limitations—they don't possess true understanding and may hallucinate. Knowledge graphs help solve this problem. Knowledge Graphs allow AI to work with structured relationships and make more reliable inferences.`;
  
  const textarea = document.getElementById('input-text');
  if(textarea){
    textarea.value = exampleText;
  }

  // Плавно скроллим к секции Try It Yourself
  const demoSection = document.getElementById('demo');
  if(demoSection){
    demoSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}