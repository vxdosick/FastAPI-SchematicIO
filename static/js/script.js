// Load Example Text
function loadExample() {
  const exampleText = `Artificial intelligence is transforming the world. Modern large language models can understand context and generate text almost like humans. However, they have limitations—they don't possess true understanding and may hallucinate. Knowledge graphs help solve this problem. Knowledge Graphs allow AI to work with structured relationships and make more reliable inferences.`;
  const textarea = document.getElementById('input-text');
  if(textarea){
    textarea.value = exampleText;
  }
}

// Empty Field Warning
function showWarning(message){
  // Create warning
  const warning = document.createElement('div');
  warning.innerText = message;
  warning.className = "fixed top-5 left-1/2 transform -translate-x-1/2 bg-[#1A0033] text-white px-6 py-3 rounded-xl shadow-lg opacity-0 z-50 transition-all duration-500 ease-out";
  
  document.body.appendChild(warning);
  
  setTimeout(()=>{ warning.style.opacity = '1'; warning.style.transform = 'translateX(-50%) translateY(0)'; }, 50);
  
  setTimeout(()=>{
    warning.style.opacity = '0';
    warning.style.transform = 'translateX(-50%) translateY(-20px)';
    setTimeout(()=>{ warning.remove(); }, 500);
  }, 3000);
}

// Form Validation
window.addEventListener('DOMContentLoaded', ()=>{
  const form = document.getElementById('graph-form');
  const exampleBtn = document.querySelector('button[onclick="loadExample()"]');

  // Example button
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

// Load Example Text and Scroll
function loadExample() {
  const exampleText = `Artificial intelligence is transforming the world. Modern large language models can understand context and generate text almost like humans. However, they have limitations—they don't possess true understanding and may hallucinate. Knowledge graphs help solve this problem. Knowledge Graphs allow AI to work with structured relationships and make more reliable inferences.`;
  
  const textarea = document.getElementById('input-text');
  if(textarea){
    textarea.value = exampleText;
  }

  // Smooth scroll to Try It Yourself
  const demoSection = document.getElementById('demo');
  if(demoSection){
    demoSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Copy Text function
async function copyText(button) {
    const container = button.closest('.copy-container');
    
    const textElement = container.querySelector('.text-to-copy');
    
    const content = textElement.getAttribute('data-copy-value') || textElement.innerText;

    try {
        await navigator.clipboard.writeText(content);
        
        const originalText = button.innerHTML;
        button.innerHTML = "✓";
        button.classList.add('copied');
        
        setTimeout(() => {
            button.innerHTML = originalText;
            button.classList.remove('copied');
        }, 2000);
    } catch (err) {
        console.error('Failed to copy:', err);
    }
}