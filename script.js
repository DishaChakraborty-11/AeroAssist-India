const missions = [
  {
    id: 'MED-104',
    type: 'medical',
    title: 'Cardiac support request',
    location: 'Jaipur, Rajasthan',
    description: 'Patient vitals show low oxygen and high heart rate. Dispatch AED and oxygen payload.',
    eta: '9 min',
  },
  {
    id: 'SAR-221',
    type: 'rescue',
    title: 'Monsoon flood search grid',
    location: 'Silchar, Assam',
    description: 'Thermal scan needed for a two-square-kilometre low-visibility riverbank zone.',
    eta: '14 min',
  },
  {
    id: 'SUP-078',
    type: 'supply',
    title: 'Rural clinic resupply',
    location: 'Wayanad, Kerala',
    description: 'Deliver antibiotics, IV fluids, and satellite beacon to the hill clinic landing point.',
    eta: '22 min',
  },
  {
    id: 'MED-119',
    type: 'medical',
    title: 'High-fever triage',
    location: 'Nagpur, Maharashtra',
    description: 'Rapid transport of cooling packs and remote consultation kit requested by responders.',
    eta: '12 min',
  },
  {
    id: 'SAR-242',
    type: 'rescue',
    title: 'Forest trail missing person',
    location: 'Dehradun, Uttarakhand',
    description: 'Autonomous sweep planned with loudspeaker beacon and high-resolution image capture.',
    eta: '18 min',
  },
  {
    id: 'SUP-096',
    type: 'supply',
    title: 'Blood sample transfer',
    location: 'Bhopal, Madhya Pradesh',
    description: 'Temperature-controlled capsule transfer between district hospital and diagnostic lab.',
    eta: '16 min',
  },
];

const missionList = document.querySelector('#missionList');
const filterButtons = document.querySelectorAll('.filter-button');
const dispatchForm = document.querySelector('#dispatchForm');
const dispatchResult = document.querySelector('#dispatchResult');

function renderMissions(filter = 'all') {
  const filteredMissions = filter === 'all'
    ? missions
    : missions.filter((mission) => mission.type === filter);

  missionList.innerHTML = filteredMissions
    .map((mission) => `
      <article class="mission-card">
        <span class="badge ${mission.type}">${mission.type.toUpperCase()}</span>
        <h3>${mission.title}</h3>
        <p>${mission.description}</p>
        <p><strong>${mission.location}</strong> • ETA ${mission.eta}</p>
      </article>
    `)
    .join('');
}

filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    filterButtons.forEach((item) => item.classList.remove('active'));
    button.classList.add('active');
    renderMissions(button.dataset.filter);
  });
});

dispatchForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const missionType = document.querySelector('#missionType').value;
  const location = document.querySelector('#location').value.trim();
  const priority = document.querySelector('#priority').value;
  const payload = document.querySelector('#payload').value.trim();
  const launchWindow = priority === 'Critical' ? 'within 5 minutes' : 'within 15 minutes';

  dispatchResult.innerHTML = `
    <strong>${priority} ${missionType}</strong> assigned to ${location}.<br />
    Recommended payload: ${payload}. Launch window: ${launchWindow}.
  `;
});

renderMissions();
