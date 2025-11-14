const imgInput = document.getElementById('imgInput');
const step1Img = document.getElementById('step1');
const workflowSection = document.getElementById('workflow');

// Show a preview in the "Original" box on file selection
imgInput.addEventListener('change', function() {
  document.getElementById('detectBtn').disabled = false;
  document.getElementById('status').textContent = '';

  // Show the workflow box now that we have an image
  workflowSection.hidden = false;

  // Show preview in original image box
  const file = imgInput.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function(e) {
      step1Img.src = e.target.result;
      step1Img.style.display = 'block'; // show's the image if it was hidden by default
      // Hide the detected image until detection is run
      document.getElementById('step2').style.display = 'none';
    };
    reader.readAsDataURL(file);
  }
});

// On detection, set original and detected images as before
document.getElementById('detectBtn').addEventListener('click', async () => {
  const input = document.getElementById('imgInput');
  if (!input.files.length) {
    alert('Please select an image.');
    return;
  }

  document.getElementById('status').textContent = 'Processing...';

  const data = new FormData();
  data.append('file', input.files[0]);

  try {
    const resp = await fetch('/upload', { method: 'POST', body: data });
    if (!resp.ok) throw new Error('Upload failed');
    const json = await resp.json();

    // Now show processed overlay in original box and detected image in the detected box
    step1Img.src = json.original_image;
    document.getElementById('step2').src = json.annotated_image;
    document.getElementById('step2').style.display = 'block';

    // Show details etc. as before
    document.getElementById('diseaseInfo').hidden = false;
    document.getElementById('diseaseName').textContent = json.disease_name;
    document.getElementById('description').textContent = json.description || '';
    document.getElementById('cause').textContent = json.cause || '';
    document.getElementById('precautions').textContent = json.precautions;

    document.getElementById('status').textContent = 'Done!';
  } catch (err) {
    document.getElementById('status').textContent = `Error: ${err.message}`;
  }
});
