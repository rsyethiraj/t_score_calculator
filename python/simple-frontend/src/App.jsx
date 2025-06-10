import { useState } from 'react';
import './App.css';

function App() {
  const [weights, setWeights] = useState('');
  const [speeds, setSpeeds] = useState('');
  const [names, setNames] = useState('');
  const [inLbs, setInLbs] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setResult(null);

    try {
      const response = await fetch('http://localhost:5001/t-score', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          weights: weights.split(',').map(s => s.trim()),
          speeds: speeds.split(',').map(s => s.trim()),
          names: names ? names.split(',').map(s => s.trim()) : null,
          in_lbs: inLbs
        })

      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const data = await response.json();
      setResult(data.t_scores);
    } catch (err) {
      setError('Error fetching T-scores: ' + err.message);
    }
  };

  return (
    <div className='center-container'>
    <div className='App'>
      <h1>T-Score Calculator</h1>
      <form onSubmit={handleSubmit}>
        <div className='input-group'>
          <label>Weight(s) (comma-separated):</label>
          <input type='text' value={weights} onChange={e => setWeights(e.target.value)} required />
        </div>
        <div className='input-group'>
          <label>Split(s) (comma-separated, both splits and watts accepted):</label>
          <input type='text' value={speeds} onChange={e => setSpeeds(e.target.value)} required />
        </div>
        <div className='input-group'>
          <label>Names (optional, comma-separated):</label>
          <input type='text' value={names} onChange={e => setNames(e.target.value)} />
        </div>
        <div className='checkbox-group'>
          <label>
            <input type='checkbox' checked={inLbs} onChange={() => setInLbs(!inLbs)} />
            Check here to interpret weights as pounds, default is kilograms.
          </label>
        </div>
        <button type='submit'>Calculate</button>
      </form>

      {error && <p style={{ color: 'red' }}>{error}</p>}
      {result && (
        <div>
          <h2>Results</h2>
          <ul>
            {result.map((score, idx) => (
              <li key={idx}>{score}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
    </div>
  );
}

export default App;
